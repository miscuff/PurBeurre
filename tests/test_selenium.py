from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


class MySeleniumTests(StaticLiveServerTestCase):

    def test_connexion_account(self):
        baseurl = "http://167.71.166.235/account/connexion"
        username = "alexandre"
        password = "toto"

        xpaths = {'loginBox': "//input[@name='username']",
                  'passwordBox': "//input[@name='password']",
                  'submitButton': "//input[@type='submit']"
                  }

        browser = webdriver.Firefox()
        browser.get(baseurl)
        browser.maximize_window()

        # Clear Username TextBox if already allowed "Remember Me"
        browser.find_element_by_xpath(xpaths['loginBox']).clear()

        # Write Username in Username TextBox
        browser.find_element_by_xpath(xpaths['loginBox']).send_keys(username)

        # Clear Password TextBox if already allowed "Remember Me"
        browser.find_element_by_xpath(xpaths['passwordBox']).clear()

        # Write Password in password TextBox
        browser.find_element_by_xpath(xpaths['passwordBox']).send_keys(
            password)

        # Click Login button
        browser.find_element_by_xpath(xpaths['submitButton']).click()

        assert "Bonjour" in browser.page_source
        browser.quit()
