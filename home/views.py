from django.shortcuts import render


def home(request):
    """
    :param request: None
    :return: HomePage
    """
    return render(request, 'home/accueil.html', locals())
