from django.contrib import admin

from ecommerce.models.products import Product
from ecommerce.models.sizes import Size
from ecommerce.models.product_media import ProductMedia

@admin.register(Size)
class SizesAdmin(admin.ModelAdmin):
    list_display = ('product', 'size')

class SizeInline(admin.StackedInline):
    model = Size
    can_delete = False
    verbose_name_plural = 'sizes'

@admin.register(ProductMedia)
class ProductMediaAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')

class ProductMediaInline(admin.StackedInline):
    model = ProductMedia
    can_delete = True
    verbose_name_plural = 'Product images'

class CustomProductAdmin(admin.ModelAdmin):
    inlines = (SizeInline, ProductMediaInline)
    list_display = ('id', 'name', 'sku', 'stock', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('name', 'sku')
    list_display_links = ('name',)
    #actions = ['update_products_stock']
"""
    def update_products_stock(self, request, queryset):
        products_id = queryset.values_list('id', flat=True)
        for product_id in products_id:
            sizes_qty = 0
            product = Product.objects.get(pk=product_id)
            product_sizes = ProductSizes.objects.filter(item_product_sizes=product_id)
            for size in product_sizes:
                qty_size = size.qty
                sizes_qty += qty_size
                product.stock = sizes_qty
                product.save()
    update_products_stock.short_dedscription = 'Update Products sizes stock.' """

admin.site.register(Product, CustomProductAdmin)



