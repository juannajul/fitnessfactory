"""Courses categories views."""

# Django rest framework
from rest_framework import mixins, viewsets
from rest_framework.response import Response

# Serializers
from courses.serializers.categories import CategoryModelSerializer

# Models 
from courses.models.categories import Category

# Pagination

class CategoryViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):
    """Courses categories view set"""

    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    lookup_field = 'slug'

