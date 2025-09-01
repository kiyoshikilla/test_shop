from django.urls import path
from products.views import shop, detail

app_name= 'products'

urlpatterns = [
    path('', shop, name='shop'),
    path('details/<int:pk>/', detail, name='detail'),
    
]

