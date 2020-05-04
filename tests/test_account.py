from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User


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
        # Nominal account creation
        response = self.client.post(reverse('account:creation'),
                                    {'username': 'roberto',
                                     'email': 'robertc@madrid.com',
                                    'password': 'allez'})
        self.assertEqual(response.status_code, 200)
        # Email already used
        response2 = self.client.post(reverse('account:creation'),
                                    {'username': 'robertoto',
                                     'email': 'robertc@madrid.com',
                                     'password': 'allez'})
        self.assertEqual(response2.status_code, 200)
        # Username already used
        response3 = self.client.post(reverse('account:creation'),
                                     {'username': 'roberto',
                                      'email': 'robertco@madrid.com',
                                      'password': 'allez'})
        self.assertEqual(response3.status_code, 200)
