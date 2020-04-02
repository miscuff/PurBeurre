from django import forms
from django.contrib.auth.models import User


class ConnexionForm(forms.Form):
    username = forms.CharField(label="Votre nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Votre mot de passe", max_length=10,
                               widget=forms.PasswordInput)


class CreationForm(forms.Form):
    username = forms.CharField(label="Votre nom d'utilisateur", max_length=30)
    email = forms.EmailField(label="Votre adresse e-mail")
    password = forms.CharField(label="Votre mot de passe", max_length=10,
                               widget=forms.PasswordInput)


def clean_email(self):
    email = cleaned_data.get('email')
    if User.objects.filter(email=self.email).exists():
        raise forms.ValidationError("Cette email est déjà utilisé")
