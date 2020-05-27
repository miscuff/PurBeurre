from django.urls import reverse
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.contrib.auth.models import User
from django.db import IntegrityError

from account.forms import CreationForm


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

    # test account_creation with email
    def test_account_creation_email(self):
        # Nominal case
        User.objects.create_user(username='roberto',
                                         email='roberto@beatles.com',
                                         password='glass onion')

        # Email already used
        try:
            user2 = User.objects.create_user(username='roberto2',
                                             email='roberto@beatles.com',
                                             password='glass onion')
            user2.full_clean()
        except ValidationError as e:
            self.assertTrue('email' in e.message_dict)

    # test account_creation with username
    def test_account_creation_username(self):
        # Nominal case
        User.objects.create_user(username='roberto',
                                 email='roberto@beatles.com',
                                 password='glass onion')
        # Username already used
        with self.assertRaises(IntegrityError):
            User.objects.create_user(username='roberto',
                                     email='roberto3@beatles.com',
                                     password='glass onion')

    # test form is valid
    def test_form_valid(self):
        data = {
            'username': 'alex',
            'email': 'alex@gmail.com',
            'password': 'toto',
        }
        form = CreationForm(data)
        self.assertTrue(form.is_valid())

    # test form is not valid
    def test_form_invalid(self):
        data = {
            'username': 'alex',
            'password': 'toto',
        }
        form = CreationForm(data)
        self.assertFalse(form.is_valid())
