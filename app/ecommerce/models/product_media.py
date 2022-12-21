"""Product media model."""

from django.db import models
from ecommerce.models.products import Product
from django.dispatch import receiver

class ProductMedia(models.Model):
    """Product media model."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE ,related_name="product_media")
    image = image = models.ImageField(blank=True, upload_to="media/products/", verbose_name="product image")

    def __str__(self):
        """Return size name"""
        return self.image

    class Meta:
        verbose_name = "Product images"
        verbose_name_plural = "Product Images"

@receiver(models.signals.post_delete, sender=ProductMedia)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `Document` object is deleted.
    """
    if instance.image:
        instance.image.delete(False)
