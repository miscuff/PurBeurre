from django.shortcuts import render
import django.contrib.postgres

from .models import Category, Product, Substitute


def search(request):
    search_products = request.POST.get('search_products').lower()
    products_db = Product.objects.filter(product_name__istartswith=search_products).values()
    context = {
        'products': products_db
    }
    return render(request, 'products/aliments.html', context)


def detail(request, product_id):
    pass
