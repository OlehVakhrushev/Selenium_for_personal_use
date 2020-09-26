import unittest
from time import sleep


from selenium import webdriver

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\Oleg\\PycharmProjects\\Selenium_Ellie\\Tests\\chromedriver\\chromedriver_win32\\chromedriver.exe")
        self.driver.get("https://www.blizzard.com/en-us/")

    def test_blizzard(self):
        driver = self.driver
        driver.find_element_by_xpath("//div[text()='My Account']").click()
        driver.find_element_by_xpath("//a[text()='Log In']").click()
        driver.find_element_by_id('accountName').send_keys("akradabaska@gmail.com")
        driver.find_element_by_id('password').send_keys('X0500536667x')
        driver.find_element_by_id('submit').click()



sleep(1)






if __name__ == '__main__':
    unittest.main()