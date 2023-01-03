"""Product sizes views."""

# Django rest framework
from rest_framework import mixins, viewsets
from rest_framework.response import Response

# Serializers
from ecommerce.serializers.sizes import SizeModelSerializer

# Models 
from ecommerce.models.sizes import Size

# Pagination
#from ecommerce.custom_pagination import SizePagination

class SizesViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):
    """Sizes view set"""

    queryset = Size.objects.all()
    serializer_class = SizeModelSerializer
    #pagination_class = SizePagination

    #def get_queryset(self): 
    #    return Size.objects.filter(qty__gt=0)