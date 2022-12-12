"""Category model."""

from django.db import models

class Category(models.Model):
    """Category model."""
    name = models.CharField(max_length=255, unique=True, verbose_name="Category name")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Category slug")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        """Return brand name"""
        return self.name

    class Meta:
        verbose_name_plural = "Categories"