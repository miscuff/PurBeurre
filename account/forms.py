from django.forms import ModelForm, TextInput, EmailInput, \
    PasswordInput, ValidationError
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django import forms
import re


# Manage Error in account page
class ParagraphErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return ''
        return '<div class="errorlist">%s</div>' % ''.join(
            ['<p class="small error">%s</p>' % e for e in self])


# Create LoginForm
class LoginForm(forms.Form):
    username = forms.CharField(label="Votre nom d'utilisateur")
    password = forms.CharField(label="Votre mot de passe")


# Create CreationForm
class CreationForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        widget = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'password': PasswordInput(attrs={'class': 'form-control'})
        }
        help_texts = {
            'username': None,
        }

    # Check if email is not used
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Cette email est déjà utilisé")
        return email

    # Check if username is not used
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Ce nom d'utilisateur est déjà "
                                        "utilisé")
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        special_characters = ['@', '-', '/', '%', '$', '*', '&', '#']
        if len(password) < 8:
            raise ValidationError("Le mot de passe doit comporter"
                                            " au moins 8 caracteres")
        if not any(c in special_characters for c in password):
            raise ValidationError(
                "Le mote de passe doit comporter au moins 1 "
                "caractere special : @ - / % $ * & #")
        if re.search('[a-z]', password) is None:
            raise ValidationError(
                "Le mot de passe doit comporter au moins 1 minuscule")
        if re.search('[A-Z]', password) is None:
            raise ValidationError(
                "Le mot de passe doit comporter au moins 1 majuscule")
        if re.search('[0-9]', password) is None:
            raise ValidationError(
                "Le mot de passe doit comporter au moins 1 chiffre")
        return password
