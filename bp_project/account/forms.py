from django import forms


class ConnexionForm(forms.Form):
    username = forms.CharField(label="Votre nom d'utilisateur", max_length=30)
    email = forms.EmailField(label="Votre adresse e-mail")

"""
class CreationForm(forms.Form)
    password = forms.CharField(label="Votre mot de passe", max_length=10,
                               widget=forms.PasswordInput)
"""