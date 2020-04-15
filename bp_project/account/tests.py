from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User

from .forms import LoginForm, CreationForm


class AccountPageTestCase(TestCase):

    def setUp(self):
        CreationForm('Alex', 'alexandre@gmail.com', 'toto')
        self.user = User.objects.filter(email='alexandre@gmail.com').first()

    # connexion
    def test_connexion(self):
        pass

    # deconnexion
    def test_deconnexion(self):
        pass

    # account_page
    def test_account_page(self):
        pass

    # account_creation
    def test_account_creation(self):
        user = self.user
        response = self.client.get(reverse('account:creation', args=(user,)))
        self.assertEqual(response.statut_code, 200)

