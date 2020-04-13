from django.urls import path, include
from . import views

app_name = 'products'

urlpatterns = [
    path('search', views.search, name='search'),
    path('<product_id>', views.detail, name='detail'),
]
