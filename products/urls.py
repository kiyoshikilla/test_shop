from django.urls import path
from products.views import shop, detail, cart

app_name= 'products'

urlpatterns = [
    path('', shop, name='shop'),
    path('details/<int:pk>/', detail, name='detail'),
    path('cart/', cart, name="cart")
]

