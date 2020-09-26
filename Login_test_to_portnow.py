import unittest
from time import sleep

from selenium import webdriver

class MyTestCase(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Chrome(r"C:\Users\Oleg\PycharmProjects\Selenium_Ellie\Tests\chromedriver\chromedriver_win32\chromedriver.exe")
        self.driver = webdriver.Chrome("C:\\Users\\Oleg\\PycharmProjects\\Selenium_Ellie\\Tests\\chromedriver\\chromedriver_win32\\chromedriver.exe")   # On windows we need "//" for path.
        self.driver.get("http://hrm-online.portnov.com/")

    def test_valid_login(self):
        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id('btnLogin').click()

        sleep(2)
        welcome_text = driver.find_element_by_id('welcome').text

        # Expected value vs Actual value
        self.assertEqual('Welcome Admin', welcome_text)

    def test_invalid_password(self):
        pass

    def test_empty_password(self):
        pass





if __name__ == '__main__':
    unittest.main()
