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
    products = product_chosen.objects.filter.select_related('category')
    substitutes = [product for product in products if products['nutriscore_grade'] < product_chosen['nutriscore_grade']]
    context = {
        'product': product_chosen,
        'substitutes': substitutes,
    }
    return render(request, 'store/resultats.html', context)
