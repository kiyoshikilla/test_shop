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
    category_id= request.GET.getlist('category')
    
    if category_id:
        products= Product.objects.filter(category__id__in=category_id)
    else:
        products= Product.objects.all()

    return render(request, 'products/shop.html', {"categories" : categories, "products" : products, 'selected_categories' : category_id,})