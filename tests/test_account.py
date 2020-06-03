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

    # test form with invalid mail
    def test_form_invalid(self):
        data = {
            'username': 'alex',
            'email': 'alex',
            'password': 'toto',
        }
        form = CreationForm(data)
        self.assertFalse(form.is_valid())

    # test password nominal
    def test_password_nominal(self):
        data = {
            'username': 'alex',
            'email': 'alex@gmail.com',
            'password': 'Alexandre1@',
        }
        form = CreationForm(data)
        self.assertTrue(form.is_valid())

    # test password length
    def test_password_length(self):
        data = {
            'username': 'alex',
            'email': 'alex@gmail.com',
            'password': 'Ale1@',
        }
        form = CreationForm(data)
        self.assertEqual(
            form.errors['password'],
            ["Le mot de passe doit comporter au moins 8 caracteres"]
        )
        self.assertIn('class="errorlist"', form.as_p())

    # test password uppercase
    def test_password_upper(self):
        data = {
            'username': 'alex',
            'email': 'alex@gmail.com',
            'password': 'aleeeeee1@',
        }
        form = CreationForm(data)
        self.assertEqual(
            form.errors['password'],
            ["Le mot de passe doit comporter au moins 1 majuscule"]
        )
        self.assertIn('class="errorlist"', form.as_p())

    # test password lowercase
    def test_password_lower(self):
        data = {
            'username': 'alex',
            'email': 'alex@gmail.com',
            'password': 'ALEEEEEEE1@',
        }
        form = CreationForm(data)
        self.assertEqual(
            form.errors['password'],
            ["Le mot de passe doit comporter au moins 1 minuscule"]
        )
        self.assertIn('class="errorlist"', form.as_p())

    # test password special character
    def test_password_spe(self):
        data = {
            'username': 'alex',
            'email': 'alex@gmail.com',
            'password': 'Alexandreee1',
        }
        form = CreationForm(data)
        self.assertEqual(
            form.errors['password'],
            ["Le mote de passe doit comporter au moins 1 "
             "caractere special : @ - / % $ * & #"]
        )
        self.assertIn('class="errorlist"', form.as_p())

    # test password number
    def test_password_number(self):
        data = {
            'username': 'alex',
            'email': 'alex@gmail.com',
            'password': 'Alexandreee@',
        }
        form = CreationForm(data)
        self.assertEqual(
            form.errors['password'],
            ["Le mot de passe doit comporter au moins 1 chiffre"]
        )
        self.assertIn('class="errorlist"', form.as_p())
