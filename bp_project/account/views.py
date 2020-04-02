from django.shortcuts import render

from .forms import ConnexionForm


def connexion(request):
    form = ConnexionForm(request.POST or None)
    if form.is_valid():
        # Ici nous pouvons traiter les données du formulaire
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        envoi = True
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'account/connexion.html', locals())


def account_creation(request):
    return render(request, 'account/creation.html', locals())
