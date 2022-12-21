"""Colors model."""

from django.db import models

class Color(models.Model):
    """Colors model."""
    color = models.CharField(max_length=255, unique=True, verbose_name="Color")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Color slug")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        """Return color name"""
        return self.color

    class Meta:
        verbose_name_plural = "Colors"