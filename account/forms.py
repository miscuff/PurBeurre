from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label="Votre nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Votre mot de passe", max_length=10,
                               widget=forms.PasswordInput)


class CreationForm(forms.Form):
    username = forms.CharField(label="Votre nom d'utilisateur", max_length=30)
    email = forms.EmailField(label="Votre adresse e-mail")
    password = forms.CharField(label="Votre mot de passe", max_length=10,
                               widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Cette email est déjà utilisé")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Ce nom d'utilisateur est déjà "
                                        "utilisé")
        return username
