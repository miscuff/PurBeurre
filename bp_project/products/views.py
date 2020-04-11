from django.shortcuts import render


def search(request):
    search_products = request.POST.get('search_products')
    context = {
        'products': search_products
    }
    return render(request, 'products/aliments.html', context)
