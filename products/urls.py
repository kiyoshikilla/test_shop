from django.urls import path
from products.views import shop

app_name= 'products'

urlpatterns = [
    path('', shop, name='shop'),
    
]

