from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone

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


def substitute(request, product_id):
    substitute_chosen = Product.objects.get(pk=product_id)
    stores = substitute_chosen.store
    if stores == "[]":
        store = ""
    else:
        store = stores.split(',')
        store = store[0]
        store = store.replace("['", "")
        store = store.replace("']", "")
    context = {
        'substitute': substitute_chosen,
        'store': store
    }
    return render(request, 'products/informations.html', context)


@login_required
def save(request, sub_id):
    fav = Product.objects.get(pk=sub_id)
    user = request.user.id
    try:
        if Substitute.objects.filter(pk=fav.id):
            print("Cet aliment est déjà dans vos favoris")
        else:
            add_favorite = Substitute(id=fav.id, created_at=timezone.now(),
                                      user_id=user)
            add_favorite.save()
    except KeyError as e:
        print(e)
    sub = Substitute.objects.filter(user_id=user)
    context = {
        'favorites': sub,
    }
    return render(request, 'products/favorites.html', context)


@login_required
def show_favorites(request):
    user_id = request.user.id
    sub = Substitute.objects.filter(user_id=user_id).values('id')
    get_all_subs = []
    for i in sub:
        get_all_subs.append(i['id'])
    favorites = [favorite for favorite in Product.objects.all().values() if
                 favorite['id'] in get_all_subs]
    print(favorites)
    context = {
        'favorites': favorites,
    }
    return render(request, 'products/favorites.html', context)
