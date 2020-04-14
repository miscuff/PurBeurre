from django.shortcuts import render
import django.contrib.postgres

from .models import Category, Product, Substitute


def search(request):
    search_products = request.POST.get('search_products').lower()
    products_db = Product.objects.filter(product_name__istartswith=search_products).values()
    context = {
        'products': products_db,
        'search_products': search_products
    }
    return render(request, 'products/aliments.html', context)


def detail(request, product_id):
    product_chosen = Product.objects.get(pk=product_id)
    category = product_chosen.category_id
    products = Product.objects.filter(category_id=category).values()
    substitutes = [product for product in products if product['nutriscore_grade'] < product_chosen.nutriscore_grade]
    context = {
        'product': product_chosen,
        'substitutes': substitutes,
    }
    return render(request, 'products/resultats.html', context)
