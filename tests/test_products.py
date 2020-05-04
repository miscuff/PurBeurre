from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
import debug_toolbar

from products.models import Category, Product, Substitute


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
    def test_count_substitutes(self):
        old_sub = Substitute.objects.count()  # count bookings before a request
        self.substitute = Substitute.objects.create(id=self.p1.id,
                                                    created_at=timezone.now(),
                                                    user_id=self.u1.id)
        self.s1 = Substitute.objects.get(user_id=self.u1)
        self.client.get(reverse('products:save', args=(self.s1,)))
        new_sub = Substitute.objects.count()  # count bookings after
        self.assertEqual(new_sub, old_sub + 1)  # make sure 1 booking was added


# Products Models
class ProductsModelsTestCase(TestCase):

    def setUp(self):
        self.cat = Category.objects.create(name='soupe')
        self.product = Product.objects.create(product_name='sirop de menthe',
                                              nutriscore_grade='d',
                                              store='naturalia',
                                              url_picture='http://url_picture.fr',
                                              url_picture_small='http://url_picture_small.fr',
                                              url_product='http://url_product.fr',
                                              description='une super boisson',
                                              category=self.cat)
        self.user = User.objects.create_user(username='john',
                                             email='jlennon@beatles.com',
                                             password='glass onion')
        self.time = timezone.now()
        self.substitute = Substitute.objects.create(id=self.product.id,
                                                    created_at=self.time,
                                                    user_id=self.user.id)

    # Test category on DB
    def test_category(self):
        cat1 = Category.objects.get(name='soupe')
        self.assertEqual(self.cat, cat1)

    # Test product on DB
    def test_product(self):
        p1 = self.product
        self.assertEqual(p1.product_name, 'sirop de menthe')
        self.assertEqual(p1.nutriscore_grade, 'd')
        self.assertEqual(p1.store, 'naturalia')
        self.assertEqual(p1.url_picture, 'http://url_picture.fr')
        self.assertEqual(p1.url_picture_small, 'http://url_picture_small.fr')
        self.assertEqual(p1.url_product, 'http://url_product.fr')
        self.assertEqual(p1.description, 'une super boisson')
        self.assertEqual(p1.category, self.cat)

    # Test substitute on DB
    def test_substitute(self):
        s1 = self.substitute
        self.assertEqual(s1.id, self.product.id)
        self.assertEqual(s1.user_id, self.user.id)
