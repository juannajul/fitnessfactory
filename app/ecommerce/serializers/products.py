"""Products serializer."""

# Django rest framework
from rest_framework import serializers

# Django
from django.utils.text import slugify
import uuid

# Models
from ecommerce.models.categories import Category
from ecommerce.models.product_media import ProductMedia
from ecommerce.models.sizes import Size
from ecommerce.models.products import Product

# Serializers
from ecommerce.serializers.categories import CategoryModelSerializer
from ecommerce.serializers.product_media import ProductMediaModelSerializer
from ecommerce.serializers.sizes import SizeModelSerializer, CreateSizeSerializer

class ProductModelSerializer(serializers.ModelSerializer):
    """Product model serializer."""
    category = CategoryModelSerializer(many=True)
    sizes = SizeModelSerializer(many=True)
    product_media = ProductMediaModelSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'


class CreateProductSerializer(serializers.ModelSerializer):
    # Create product serializer.
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    gender = serializers.ChoiceField(allow_blank=True,choices=[
        ("CA", "Caballeros"),
        ("DA", "Damas"),
        ("UN", "Unisex"),
    ])
    description = serializers.CharField(allow_blank=True)
    color = serializers.CharField(allow_blank=True)
    store_price = serializers.DecimalField(default=0, max_digits=6, decimal_places=2)
    sale_price = serializers.DecimalField(default=0, max_digits=6, decimal_places=2)
    
    class Meta:
        model = Product
        fields = '__all__'
    
    def validate(self, data):
        """Validate if de slug already exists. If exists modificate."""

        slug_name = data['slug']
        if Product.objects.filter(slug=slug_name).exists():
            id = str(uuid.uuid4())
            new_slug_name = slugify("{}-{}".format(
                data["name"], id[:8]
            ))
            data['slug'] = new_slug_name
        return data

    def create(self, data):
        """Create single product.""" 
        product = Product.objects.create(name=data['name'], sku=data['sku'], 
        slug=data['slug'], description=data['description'], gender=data['gender'],
        color=data['color'], brand=data['brand'], store_price=data['store_price'],
        sale_price=data['sale_price'], user=data['user'])
        product.save()
        categories = data['categories']
        for category in categories:
            product.categories.add(category)
        product.save()
        return product

        #('name', 'sku', 'slug', 'description', 'gender', 'color', 'brand', 'store_price', 'sale_price', 'user')