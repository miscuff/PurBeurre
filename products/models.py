from django.db import models
from django.contrib.auth.models import User


# Create a Category on DB
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)


# Create a Product on DB
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    nutriscore_grade = models.CharField(max_length=1, null=True)
    store = models.TextField(null=True)
    url_picture = models.URLField()
    url_picture_small = models.URLField(null=True)
    url_product = models.URLField()
    description = models.TextField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


# Create a Substitute on DB
class Substitute(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, related_name='substitutes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
