"""Product sizes views."""

# Django rest framework
from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination

# Serializers
from ecommerce.serializers.sizes import SizeModelSerializer, SizeInStockModelSerializer

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

    serializer_class = SizeModelSerializer
    #pagination_class = SizePagination

    def get_queryset(self): 
        if self.action == 'sizes_in_stock':
            return Size.objects.filter(qty__gt=0)
        return Size.objects.all()

    @action(detail=False, methods=["get"])
    def sizes_in_stock(self, request, *args, **kwargs):
        """List products by category."""
        paginator = PageNumberPagination()
        paginator.page_size = 12
        products = self.filter_queryset(self.get_queryset())
        result_page = paginator.paginate_queryset(products, request)
        serializer = SizeModelSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)