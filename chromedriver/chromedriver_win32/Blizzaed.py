import unittest


from selenium import webdriver

class MyTestCase(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(r"C:\Users\Oleg\PycharmProjects\Selenium_Ellie\Tests\chromedriver\chromedriver_win32\chromedriver.exe")
        self.driver = webdriver.Chrome("C:\\Users\\Oleg\\PycharmProjects\\Selenium_Ellie\\Tests\\chromedriver\\chromedriver_win32\\chromedriver.exe")
        self.driver.get('https://us.battle.net/login/en/?ref=https://us.shop.battle.net/en-us&app=shop') # Отвечает за сайт, куда мы посылаем запрос

    def test_valid_login(self):
        driver = self.driver
        driver.find_element_by_id('accountName').send_keys('Akradabaska@gmail.com')
        driver.find_element_by_id('password').send_keys('Z0500536667Z')
        driver.find_element_by_id('submit').click()






if __name__ == '__main__':
    unittest.main()