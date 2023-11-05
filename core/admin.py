from django.contrib import admin
from core.models.product import Product, ProductImages, Category, Size, CartProduct
from core.models.order import Order


class ProductImagesInline(admin.StackedInline):
    model = ProductImages


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'added_on']
    list_filter = ['name', 'added_on']
    # list_editable = ['price', 'stock', 'available']
    # prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImagesInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Size)
admin.site.register(CartProduct)
admin.site.register(Order)
