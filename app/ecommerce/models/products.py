"""Inventory models."""

from distutils.command.upload import upload
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver

# Models
from users.models.users import User
from ecommerce.models.categories import Category
from ecommerce.models.colors import Color

class Product(models.Model):
    """Product model."""
    name = models.CharField(max_length=255, verbose_name="Product name")
    sku = models.CharField(max_length=20, unique=True, verbose_name= "Product sku")
    slug = models.SlugField(max_length=255, unique=False, verbose_name="Product slug")
    description = models.TextField(max_length=455, blank=True, verbose_name="Product description")
    category = models.ManyToManyField(Category, blank=True, related_name="product_categories")
    colors = models.ManyToManyField(Color, related_name="item_product_colors", null=True)
    stock = models.PositiveIntegerField(default=0)
    brand = models.CharField(max_length=255, verbose_name="brand")
    store_price = models.DecimalField(max_digits=6, decimal_places=2)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, default=0)
    is_sale_price_active = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        """Return product name"""
        return self.name
    
            
    