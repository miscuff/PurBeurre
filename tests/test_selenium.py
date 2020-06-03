from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class MySeleniumTests(StaticLiveServerTestCase):

    def setUp(self):
        self.username = 'Alexandre15'
        self.email = 'alexandre15@wanadoo.fr'
        self.password = 'P@ssword123'
        # To Launch with Chrome
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.browser = webdriver.Chrome(ChromeDriverManager().install(),
                                        chrome_options=chrome_options)

        # To Launch with Firefox
        """ options = Options()
        options.headless = True
        self.browser = webdriver.Firefox(options=options)"""

    def test_a_creation(self):
        base_url = "http://127.0.0.1:8000/account/new_user"

        xpaths = {'loginBox': "//input[@name='username']",
                  'emailBox': "//input[@name='email']",
                  'passwordBox': "//input[@name='password']",
                  'submitButton': "//input[@type='submit']"
                  }

        self.browser.get(base_url)
        self.browser.maximize_window()

        # Clear Username TextBox if already allowed "Remember Me"
        self.browser.find_element_by_xpath(xpaths['loginBox']).clear()

        # Write Username in Username TextBox
        self.browser.find_element_by_xpath(xpaths['loginBox']).send_keys(
            self.username)

        # Clear Username TextBox if already allowed "Remember Me"
        self.browser.find_element_by_xpath(xpaths['emailBox']).clear()

        # Write Username in Username TextBox
        self.browser.find_element_by_xpath(xpaths['emailBox']).send_keys(
            self.email)

        # Clear Password TextBox if already allowed "Remember Me"
        self.browser.find_element_by_xpath(xpaths['passwordBox']).clear()

        # Write Password in password TextBox
        self.browser.find_element_by_xpath(xpaths['passwordBox']).send_keys(
            self.password)

        # Click Login button
        self.browser.find_element_by_xpath(xpaths['submitButton']).click()

        assert "Connectez-vous" in self.browser.page_source

        self.browser.quit()

    def test_b_login(self):
        base_url = "http://127.0.0.1:8000/account/connexion"

        xpaths = {'loginBox': "//input[@name='username']",
                  'passwordBox': "//input[@name='password']",
                  'submitButton': "//input[@type='submit']"
                  }

        self.browser.get(base_url)
        self.browser.maximize_window()

        # Clear Username TextBox if already allowed "Remember Me"
        self.browser.find_element_by_xpath(xpaths['loginBox']).clear()

        # Write Username in Username TextBox
        self.browser.find_element_by_xpath(xpaths['loginBox']).send_keys(
            self.username)

        # Clear Password TextBox if already allowed "Remember Me"
        self.browser.find_element_by_xpath(xpaths['passwordBox']).clear()

        # Write Password in password TextBox
        self.browser.find_element_by_xpath(xpaths['passwordBox']).send_keys(
            self.password)

        # Click Login button
        self.browser.find_element_by_xpath(xpaths['submitButton']).click()

        assert "Bonjour" in self.browser.page_source

        self.browser.quit()
