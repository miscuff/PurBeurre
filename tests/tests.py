from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone

from products.models import Category, Product, Substitute


# HomePage
class HomePageTestCase(TestCase):
    # test that home page returns 200
    def test_home_page(self):
        response = self.client.get(reverse('home:home'))
        self.assertEqual(response.status_code, 200)


# Account app
class AccountPageTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='john',
                                             email='jlennon@beatles.com',
                                             password='glass onion')

    # test connexion
    def test_connexion(self):
        u1 = User.objects.get(username='john')
        response = self.client.post(reverse('account:connexion'),
                                    {'user_id': u1.id})
        self.assertEqual(response.status_code, 200)

    # test account_page
    def test_account_page(self):
        self.client.login(username="john", password="glass onion")
        response = self.client.get(reverse('account:account'))
        self.assertEqual(response.status_code, 200)

    # test deconnexion
    def test_deconnexion(self):
        self.client.login(username="john", password="glass onion")
        self.client.logout()
        response = self.client.get(reverse('account:deconnexion'))
        self.assertEqual(response.status_code, 200)

    # test account_creation
    def test_account_creation(self):
        response = self.client.post(reverse('account:creation'),
                                    {'username': 'roberto',
                                     'email': 'robertc@madrid.com',
                                    'password': 'allez'})
        self.assertEqual(response.status_code, 200)


# Products app
class ProductsPageTestCase(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='petit-dejeuners')
        self.c1 = Category.objects.get(name='petit-dejeuners')
        self.product = Product.objects.create(product_name='nutella',
                                              nutriscore_grade='d',
                                              url_picture='http://url_picture.fr',
                                              url_product='http://url_product.fr',
                                              category=self.category)
        self.p1 = Product.objects.get(product_name='nutella')
        self.user = User.objects.create_user(username='john',
                                 email='jlennon@beatles.com',
                                 password='glass onion')
        self.u1 = User.objects.get(username='john')


    # test the list of products
    def test_display_product(self):
        product_name = self.p1.product_name
        response = self.client.post(reverse('products:search'),
                                    {'search_products': product_name})
        self.assertEqual(response.status_code, 200)

    # test details page
    def test_details(self):
        product_id = self.p1.id
        response = self.client.get(reverse('products:detail',
                                            args=(product_id,)))
        self.assertEqual(response.status_code, 200)

    # test the list of substitutes
    def test_display_substitutes(self):
        product_id = self.p1.id
        response = self.client.get(reverse('products:substitute',
                                            args=(product_id,)))
        self.assertEqual(response.status_code, 200)

    # test the sub is saved it will add one row to database
    def test_save_substitutes(self):
        old_sub = Substitute.objects.count()  # count bookings before a request
        self.substitute = Substitute.objects.create(id=self.p1.id,
                                                    created_at=timezone.now(),
                                                    user_id=self.u1.id)
        self.s1 = Substitute.objects.get(user_id=self.u1)
        response = self.client.get(reverse('products:save', args=(self.s1,)))
        new_sub = Substitute.objects.count()  # count bookings after
        self.assertEqual(new_sub, old_sub + 1)  # make sure 1 booking was added

    # test the list of favorites
    def test_display_favorites(self):
        response = self.client.get(reverse('products:show_favorites'))
        self.assertEqual(response.status_code, 302)
