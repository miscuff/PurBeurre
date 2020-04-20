from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User

from account.forms import LoginForm, CreationForm
from products.models import Category, Product, Substitute


# HomePage
class HomePageTestCase(TestCase):
    # test that home page returns 200
    def test_home_page(self):
        response = self.client.get(reverse('home:home'))
        self.assertEqual(response.status_code, 200)

"""
# Account app
class AccountPageTestCase(TestCase):

    def setUp(self):
        self.create_user = CreationForm('Alex', 'alexandre@gmail.com', 'toto')
        self.user = User.objects.get(email='alexandre@gmail.com')

    # test connexion
    def test_connexion(self):
        pass

    # test deconnexion
    def test_deconnexion(self):
        pass

    # test ccount_page
    def test_account_page(self):
        username = self.user.username
        response = self.client.get(reverse('account:account', args=(username,)))
        self.assertEqual(response.status_code, 200)

    # test account_creation
    def test_account_creation(self):
        pass
    
"""
# Products app
class ProductsPageTestCase(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='petit-dejeuners')
        self.c1 = Category.objects.get(name='petit-dejeuners')
        self.product = Product.objects.create(name='nutella',
                                              nutriscore_grade='b',
                                              url_picture='http://url_picture.fr',
                                              url_product='http://url_product.fr',
                                              category=self.c1.pk)
        self.p1 = Product.objects.get(name='nutella')

    # test the list of products
    def test_display_product(self):
        response = self.client.get(reverse('products:search'))
        self.assertEqual(response.status_code, 200)

    """
    # test details page
    def test_details(self):
        pass

    # test the list of substitutes
    def test_display_substitutes(self):
        pass

    # test the sub is saved
    def test_save_substitutes(self):
        pass

    # test the list of favorites
    def test_display_favorites(self):
        pass

"""