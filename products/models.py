from django.db import models
from django.utils.text import slugify

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    value = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='categories_images', blank=True, null=True)

    def __str__(self):
        return self.name
    

class Size(models.Model):
    name = models.CharField(max_length= 4, unique = True)
    order = models.PositiveIntegerField(default= 0)

    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.name



     
class Product(models.Model):
    name = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    rating = models.FloatField(default= 0)
    image = models.ImageField(upload_to='products_images')
    size = models.ForeignKey(Size, on_delete = models.SET_NULL, null= True, blank= True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=256, blank=True, null=True)

    def __str__(self):
        return f'Продукт: {self.name} | Категорія: {self.category.name}'
    
    def get_price_with_currency(self):
        return f"{self.price} UAH"
    
