import unittest
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


from selenium import webdriver

class MyTestCase(unittest.TestCase):



    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\Oleg\\PycharmProjects\\Selenium_Ellie\\Tests\\chromedriver\\chromedriver_win32\\chromedriver.exe")
        self.driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")


    def test_LinkenIn(self):
        driver = self.driver
        driver.maximize_window()
#        driver.find_element_by_xpath("(//data-tracking-will-navigate[text()='Sign in'])[0]").click()
        driver.find_element_by_id('username').send_keys("oleh.vakhrushev@gmail.com")
        driver.find_element_by_id('password').send_keys("Z4055966z")
        driver.find_element_by_xpath("(//button[text()='Sign in'])").click()
        sleep(2)
        driver.find_element_by_id("mynetwork-tab-icon").click()
        sleep(4)
        element = driver.find_element_by_xpath("//span[text()='Connect']")

        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        for i in range(0, 15):
            for i in range(0, 4):
                driver.find_elements_by_xpath("//span[text()='Connect']")[i].click()
            driver.find_element_by_id("mynetwork-tab-icon").click()
            sleep(4)
            element = driver.find_element_by_xpath("//span[text()='Connect']")

            actions = ActionChains(driver)
            actions.move_to_element(element).perform()



        sleep(2)


    def tearDown(self):
        self.driver.quit()










if __name__ == '__main__':
        unittest.main()