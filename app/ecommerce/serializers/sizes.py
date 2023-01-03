"""Sizes serializers."""

# Django rest framework
from rest_framework import serializers

# Models
from  ecommerce.models.sizes import Size

class SizeModelSerializer(serializers.ModelSerializer):
    """Size model serializer."""

    class Meta:
        model = Size
        fields = '__all__'

class SizeInStockModelSerializer(serializers.ModelSerializer):
    """Sizes in stock model serializer."""

    class Meta:
        model = Size
        fields = '__all__'
    
    def get_sizes_in_stock(self, instance):
        sizes_in_stock = Size.objects.filter(qty__gt=0)
        print(sizes_in_stock)
        return SizeModelSerializer(sizes_in_stock, many=True).data

        

class CreateSizeSerializer(serializers.ModelSerializer):
    """Create size serializer."""

    class Meta:
        model = Size
        fields = '__all__'
        