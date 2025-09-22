from django.urls import path
from products.views import shop, detail, cart, cart_add

app_name= 'products'

urlpatterns = [
    path('', shop, name='shop'),
    path('details/<int:pk>/', detail, name='detail'),
    path('cart/', cart, name="cart"),
    path('cart/add/<int:product_id>/', cart_add, name="cart_add"),
]

