from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import time


class MySeleniumTests(StaticLiveServerTestCase):

    def test_login(self):
        browser = webdriver.Firefox()
        time.sleep(10)
        browser.get('https://purdebeurre.herokuapp.com/')

        assert 'Pur' in browser.title
        elem = browser.find_element_by_id('page-top')
        assert (elem is not None)

        browser.quit()

    def test_connexion_account(self):
        browser = webdriver.Firefox()
        time.sleep(10)
        browser.get('https://purdebeurre.herokuapp.com/')

