
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

class IntegrationTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super(IntegrationTests, cls).setUpClass()
        cls.selenium = WebDriver()


    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(IntegrationTests, cls).tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('Test11')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('Test11')
        self.selenium.find_element_by_xpath('//input[@value="Login"]').click()