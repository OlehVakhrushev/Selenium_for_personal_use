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
        driver.find_element_by_id('password').send_keys('sdfdfgdfg')
        driver.find_element_by_id('submit').click()

        sleep(1)

        driver.find_element_by_xpath("//a[@data-target='Navbar-accountDropdown']").click()




#        # мы сохраняем текст #1445 variable actual
        actual = driver.find_element_by_xpath("//div[text()='#1445']").text
        expected = "#1445"

        # expected vs actual
        self.assertEqual(expected, actual)

        driver.find_element_by_xpath("//a[@data-name='games']").click()
        driver.find_element_by_xpath("//div[text()=' 2']").click()         # Goes to the Overwatch 2
        driver.back()

        driver.find_element_by_xpath("//a[@data-name='games']").click()
        driver.find_element_by_xpath("//img[@src='https://blznav.akamaized.net/img/games/logo-ow-4be5755bc0a4cbaf.png']").click() # Goes to Overwatch 1
        driver.back()

        driver.find_element_by_xpath("//a[@data-name='games']").click()
        driver.find_element_by_xpath("//div[text()='World of Warcraft']").click() # goes to Warcraft
        driver.back()

        driver.find_element_by_xpath("//a[@data-name='games']").click()
        driver.find_element_by_xpath("//div[text()='Hearthstone']").click() # goes to Heatstone
        driver.back()

        driver.find_element_by_xpath("//a[@data-name='games']").click()
        driver.find_element_by_xpath("//div[text()='Heroes of the Storm™']").click() # goes to HotS
        driver.back()

        driver.find_element_by_xpath("//a[@data-name='games']").click()
        driver.find_element_by_xpath("//div[text()=' III: Reforged™']").click()  # goes to W2 Reforged
        driver.back()

        driver.find_element_by_xpath("//a[@data-name='games']").click()
        driver.find_element_by_xpath("//div[text()=' IV']").click()  # goes to Diablo 4
        driver.back()




        sleep(1)


if __name__ == '__main__':
    unittest.main()