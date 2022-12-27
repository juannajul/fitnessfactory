"""Product media serializers."""

# Django rest framework
from rest_framework import serializers

# Models
from  ecommerce.models.product_media import ProductMedia

class ProductMediaModelSerializer(serializers.ModelSerializer):
    """Product media model serializer."""

    class Meta:
        model = ProductMedia
        fields = '__all__'
        

class CreateProductMediaSerializer(serializers.ModelSerializer):
    """Create Product media serializer."""

    class Meta:
        model = ProductMedia
        fields = '__all__'
        