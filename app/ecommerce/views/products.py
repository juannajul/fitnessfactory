"""Product view set."""

# Django rest framework
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

# Serializers
from ecommerce.serializers.products import ProductModelSerializer, CreateProductSerializer

# Models 
from ecommerce.models.products import Product
from ecommerce.models.categories import Category
from ecommerce.models.sizes import Size
from ecommerce.models.product_media import ProductMedia

# Permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework.pagination import PageNumberPagination

# Basket
from ecommerce.basket.basket import Basket



class ProductViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):
    """Product view set"""

    #queryset = Product.objects.all()
    lookup_field = 'slug'


    def get_serializer_class(self):
        """Return serializer based on actions"""
        if self.action == 'create':
            return CreateProductSerializer
        return ProductModelSerializer

    
    """def get_permissions(self):
        permissions = [IsAuthenticatedOrReadOnly]
        #if self.action in ['update', 'partial_update', 'destroy']:
        #    permissions.append(IsBrandOwner)
        return [p() for p in permissions]"""
        

    def get_queryset(self): 
        if self.action == 'products_in_stock':
            #product_sizes = Size.objects.filter(qty__gt=0)
            #print(product_sizes)
            return Product.objects.filter(product_sizes__qty__gt=0, is_active=True) 
        if self.action == 'product_by_category':
            print(self.kwargs['slug'])
            print(self.args)
            if self.kwargs['slug'] == 'ofertas':
                return Product.objects.filter(is_active=True, is_sale_price_active=True)
            else:
                category = Category.objects.get(slug=self.kwargs['slug'])
                return Product.objects.filter(category=category, is_active=True)
        if self.action == 'list_random_products':
            return Product.objects.order_by('?')
        if self.action == 'add_product_basket':
            product = Product.objects.get(slug=self.kwargs['slug'], is_active=True)
            return product
        if self.action == 'delete_product_basket':
            product = Product.objects.get(slug=self.kwargs['slug'], is_active=True)
            return product
        if self.action == 'update_basket':
            product = Product.objects.get(slug=self.kwargs['slug'], is_active=True)
            return product
        return Product.objects.all()

    @action(detail=True, methods=["get"])
    def product_by_category(self, request, *args, **kwargs):
        """List products by category."""
        paginator = PageNumberPagination()
        paginator.page_size = 12
        products = self.filter_queryset(self.get_queryset())
        result_page = paginator.paginate_queryset(products, request)
        serializer = ProductModelSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
        
    @action(detail=False, methods=["get"])
    def products_in_stock(self, request, *args, **kwargs):
        """List products by category."""
        paginator = PageNumberPagination()
        paginator.page_size = 12
        products = self.filter_queryset(self.get_queryset())
        result_page = paginator.paginate_queryset(products, request)
        serializer = ProductModelSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
        
        
        """ 
        products = self.filter_queryset(self.get_queryset())
        serializer = ProductModelSerializer(products, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
        """
    
    @action(detail=False, methods=['get'])
    def list_random_products(self, request, *args, **kwargs):
        paginator = PageNumberPagination()
        paginator.page_size = 15
        products = self.filter_queryset(self.get_queryset())
        result_page = paginator.paginate_queryset(products, request)
        serializer = ProductModelSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    @action(detail=True, methods=["post"])
    def add_product_basket(self, request, *args, **kwargs):
        # Add products to the bag.
        basket = Basket(request)
        product = self.filter_queryset(self.get_queryset())
        product_size_id = self.request.data['product_size_id']
        serializer = ProductModelSerializer(product).data
        basket.add(serializer, product_size_id)
        basket_qty = basket.__len__()
        basket_total = basket.get_total_price()
        user = str(request.user)
        auth = str(request.auth)
        response = {basket_qty, basket_total, user, auth}
        return Response(response, status=status.HTTP_200_OK)
    
    
    @action(detail=True, methods=["post"])
    def delete_product_basket(self, request, *args, **kwargs):
        # Delete products to the bag.
        basket = Basket(request)
        product = self.filter_queryset(self.get_queryset())
        product_slug = product.slug
        product_size_id = self.request.data['product_size_id']
        basket.delete(product=product_slug, product_size_id=product_size_id)
        basket_qty = basket.__len__()
        basket_total = basket.get_total_price()
        response = {basket_qty, basket_total}
        return Response(response, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=["post"])
    def update_basket(self, request, *args, **kwargs):
        # Update products qty in the bag.
        basket = Basket(request)
        product = self.filter_queryset(self.get_queryset())
        product_slug = product.slug
        product_size_id = self.request.data['product_size_id']
        qty = self.request.data['qty']
        basket.update(product_slug, product_size_id, qty)
        basket_qty = basket.__len__()
        basket_total = basket.get_total_price()
        response = {basket_qty,  basket_total}
        return Response(response, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"])
    def refresh_basket(self, request, *args, **kwargs):
        # Update products in the bag.
        basket = Basket(request)
        basket.refresh_basket()
        basket_qty = basket.__len__()
        basket_total = basket.get_total_price()
        response = {basket_qty, f"total:${basket_total}"}
        return Response(response, status=status.HTTP_200_OK)
    
