
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
import time
class IntegrationTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super(IntegrationTests, cls).setUpClass()
        cls.selenium = WebDriver()


    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(IntegrationTests, cls).tearDownClass()

    def test_register(self):
        self.selenium.get('%s%s' % (self.live_server_url,'/register/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('test11')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('test11')
        email_input = self.selenium.find_element_by_name("email")
        email_input.send_keys('test@test.com')

        self.selenium.find_element_by_xpath('//input[@value="Register"]').click()
        time.sleep(5)
        
    def test_login(self):
        
        self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('test11')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('test11')
        self.selenium.find_element_by_xpath('//input[@value="Login"]').click()
        time.sleep(5)

    
        


        

