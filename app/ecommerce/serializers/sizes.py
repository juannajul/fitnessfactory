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


class SizeInStockModelSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        if instance.qty > 0:
            return {
                'product': instance.product.pk,
                'size': instance.size,
                'qty': instance.qty
            }     

class CreateSizeSerializer(serializers.ModelSerializer):
    """Create size serializer."""

    class Meta:
        model = Size
        fields = '__all__'
        