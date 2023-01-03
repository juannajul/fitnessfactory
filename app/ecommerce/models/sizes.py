"""Sizes model."""

from django.db import models
from ecommerce.models.products import Product

class Size(models.Model):
    """Sizes model."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE ,related_name="product_sizes")
    size = models.CharField(max_length=20, unique=True, verbose_name="Size")
    qty = models.IntegerField(default=0)

    def __str__(self):
        """Return size name"""
        return self.size

    class Meta:
        verbose_name = "Sizes"
        verbose_name_plural = "Sizes"