from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('connexion/', views.connexion, name='connexion'),
    path('new_user/', views.account_creation, name='creation'),
    ]
