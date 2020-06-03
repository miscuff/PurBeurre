from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

from .forms import LoginForm, CreationForm, ParagraphErrorList


@csrf_exempt
def connexion(request):
    """
    :param request: None
    :return: Return connexion page if the form is valid
    """
    error = False
    form = LoginForm(request.POST or None, error_class=ParagraphErrorList)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'account/account.html', locals())
        else:
            error = True
            return render(request, 'account/connexion.html', locals())
    else:
        return render(request, 'account/connexion.html', locals())


# Voir comment utiliser plus proprement
def deconnexion(request):
    """
    :param request: Click the button logout
    :return: homepage
    """
    logout(request)
    return render(request, 'home/accueil.html', locals())


def account_creation(request):
    """
    :param request: Creation button
    :return: Connexion page is the form is valid
    """
    form = CreationForm(request.POST or None, error_class=ParagraphErrorList)
    if form.is_valid():
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = User.objects.create_user(username, email, password)
        user.save()
        form = LoginForm(None)
        envoi = True
        return render(request, 'account/connexion.html', locals())
    else:
        return render(request, 'account/creation.html', locals())


def account_page(request):
    """
    :param request: user is login
    :return: account page
    """
    user_id = request.user.id
    user = User.objects.filter(pk=user_id).first()
    context = {
        'username': user.username,
        'email': user.email,
        'password': user.password
    }
    return render(request, 'account/account.html', context)
