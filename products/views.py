from django.shortcuts import render
from .models import ProductCategory, Product
# Create your views here.

def index(request):
    context = {
        'title' : 'Store',
        'products' : Product.objects.all(),
        'categories' : ProductCategory.objects.all()
    }
    return render(request, 'products/index.html', context)

def shop(request):
    categories = ProductCategory.objects.all()
    selected_categories= request.GET.getlist('category')

    
    if selected_categories:
        products= Product.objects.filter(category__id__in=selected_categories)
    else:
        products= Product.objects.all()

    return render(request, 'products/shop.html', {"categories" : categories, "products" : products, 'selected_categories' : selected_categories,})