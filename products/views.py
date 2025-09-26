from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import ProductCategory, Product, Size, Cart
from users.models import User
from django.core.paginator import Paginator


# Create your views here.

def index(request):
    context = {
        'title' : 'Store',
        'products' : Product.objects.all(),
        'categories' : ProductCategory.objects.all()
    }
    return render(request, 'products/index.html', context)

def shop(request, page_number=1):
    products = Product.objects.all()
    

    categories = ProductCategory.objects.all()
    size = Size.objects.all()

    selected_categories= request.GET.getlist('category')
    selected_sizes= request.GET.getlist('size')

    
    if selected_categories:
        products= products.filter(category__id__in=selected_categories)
    if selected_sizes:
        products= products.filter(size__id__in=selected_sizes)
  
    per_page = 3
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page_number)   


    return render(request, 'products/shop.html', {"categories" : categories, "products" : products_paginator, 'selected_categories' : selected_categories, 'sizes' : size, 'selected_sizes' : selected_sizes,})


def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/detail.html', {'product' : product})

def cart(request):
    carts = Cart.objects.filter(user=request.user)
    has_items = carts.exists()
    return render(request, "products/basket.html", {"carts" : carts, "has_items" : has_items})

def cart_add(request, product_id):
    product = Product.objects.get(id=product_id)
    carts = Cart.objects.filter(user=request.user, product=product)

    if not carts.exists():
        Cart.objects.create(user=request.user, product=product, quantity=1)
    else:
        carts = carts.first()
        carts.quantity += 1
        carts.save()
    
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
