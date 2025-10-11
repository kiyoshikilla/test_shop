from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.core.paginator import Paginator

from .models import ProductCategory, Product, Size, Cart
from users.models import User

from django.core.cache import cache



# Create your views here.

def index(request):
    context = {
        'title' : 'Store',
        'products' : Product.objects.all(),
        'categories' : ProductCategory.objects.all()
    }
    return render(request, 'products/index.html', context)


def shop(request, page_number=1):
    products = Product.objects.all().order_by('id')


    categories = ProductCategory.objects.all()
    size = Size.objects.all()

    selected_categories= request.GET.getlist('category')
    selected_sizes= request.GET.getlist('size')

    cache_key = f"shop_list_page_{page_number}"   

    if selected_categories:
        cache_key += f"_cat_{'_'.join(selected_categories)}"
    if selected_sizes:
        cache_key += f"_size_{'_'.join(selected_sizes)}"
    
    context = cache.get(cache_key,)

    if context is None:
        products = Product.objects.all()
        categories = ProductCategory.objects.all()
        size = Size.objects.all()

    if selected_categories:
        products= products.filter(category__id__in=selected_categories)
    if selected_sizes:
        products= products.filter(size__id__in=selected_sizes)
  
    per_page = 3
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page_number)   

    context = {"categories" : categories,
                "products" : products_paginator,
                'selected_categories' : selected_categories,
                'sizes' : size,
                'selected_sizes' : selected_sizes,}

    cache.set(cache_key, context, 60 * 15)

    return render(request, 'products/shop.html', context)



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
