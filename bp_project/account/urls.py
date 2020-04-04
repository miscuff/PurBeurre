from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('connexion/', views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('new_user/', views.account_creation, name='creation'),
    path('account/', views.account_page, name='account'),
    ]
