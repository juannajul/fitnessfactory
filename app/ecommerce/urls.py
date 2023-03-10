"""Ecommerce Urls."""

# Django rest framework
from rest_framework.routers import DefaultRouter

#Django
from django.urls import path, include

# Views
from .views import categories as category_views
from .views import sizes as sizes_views
from .views import products as products_views
from .views import product_media as product_media_views

router = DefaultRouter()
router.register(r'categories', category_views.CategoryViewSet, basename="category")
router.register(r'sizes', sizes_views.SizesViewSet, basename="sizes")
router.register(r'products', products_views.ProductViewSet, basename="product")
router.register(r'product_media', product_media_views.ProductMediaViewSet, basename="product_media")

urlpatterns = [
    path('', include(router.urls))
]