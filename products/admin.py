from django.contrib import admin
from products.models import *


# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    pass
