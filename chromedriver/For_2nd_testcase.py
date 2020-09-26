import unittest
from time import sleep


from selenium import webdriver

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\Oleg\\PycharmProjects\\Selenium_Ellie\\Tests\\chromedriver\\chromedriver_win32\\chromedriver.exe")
        self.driver.get("https://www.blizzard.com/en-us/")

    def test_blizzard(self):
        driver = self.driver
        driver.find_element_by_xpath("//a[@data-target='Navbar-esportsDropdown']").click()
        driver.find_element_by_xpath("//img[@src='https://blznav.akamaized.net/img/esports/esports-overwatch-36d8f7f486d363c1.png']").click()
        driver.back()

        driver.find_element_by_xpath("//a[@data-target='Navbar-esportsDropdown']").click()
        driver.find_element_by_xpath("//img[@src='https://blznav.akamaized.net/img/esports/esports-overwatch-world-cup-43d00c39399a70b8.png']").click()
        driver.back()




        driver.close()





if __name__ == '__main__':
    unittest.main()