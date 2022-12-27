"""Product media views."""

# Django rest framework
from rest_framework import mixins, viewsets
from rest_framework.response import Response

# Serializers
from ecommerce.serializers.product_media import ProductMediaModelSerializer

# Models 
from ecommerce.models.product_media import ProductMedia

# Pagination

class ProductMediaViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):
    """Product media view set."""

    queryset = ProductMedia.objects.all()
    serializer_class = ProductMediaModelSerializer
    #pagination_class = SizePagination

