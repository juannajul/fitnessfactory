"""Product categories views."""

# Django rest framework
from rest_framework import mixins, viewsets
from rest_framework.response import Response

# Serializers
from ecommerce.serializers.categories import CategoryModelSerializer

# Models 
from ecommerce.models.categories import Category

# Pagination

class CategoryViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):
    """Categories view set"""

    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    #pagination_class = SizePagination

