from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.forms import ValidationError

from .forms import ConnexionForm, CreationForm


def connexion(request):
    form = ConnexionForm(request.POST or None)
    if form.is_valid():
        # Ici nous pouvons traiter les données du formulaire
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        envoi = True
        """
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
        else:
            # Return an 'invalid login' error message.         
             """
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'account/connexion.html', locals())


def account_creation(request):
    form = CreationForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        User.objects.create_user(username, email, password)
        envoi = True
    return render(request, 'account/creation.html', locals())


