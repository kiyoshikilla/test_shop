from django.contrib import admin
from products.models import *


# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display =  ('name', 'price', 'category')
    fields = ('name', 'price', 'rating', 'image', 'size', 'category')
    search_fields = ('name',)

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    pass

class CartAdmin(admin.TabularInline):
    model = Cart
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0   
