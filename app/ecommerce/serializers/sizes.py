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
        

class CreateSizeSerializer(serializers.ModelSerializer):
    """Create size serializer."""

    class Meta:
        model = Size
        fields = '__all__'
        