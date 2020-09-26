import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait



class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("/Users/igor/PycharmProjects/HRM_Spr/browser_drivers/chromedriver") # show the path where web.driver with //
        self.wait = WebDriverWait(self.driver, 25)
        self.driver.get("https://www.") # link for website witch we will test


    def tearDown(self):
        self.driver.quit() #
        self.driver.close() #

    def test_something(self):

        driver = self.driver

        #Locators and names for locators
        driver.find_element_by_id()
        driver.find_element_by_xpath()
        driver.find_element_by_css_selector()
        driver.find_element_by_tag_name()
        driver.find_element_by_class_name()
        driver.find_element_by_name()
        driver.find_element_by_link_text()

        driver.find_elements()
        driver.find_elements_by_xpath()

        #Actions what we can do with locators
        driver.find_element_by_id().click()
        driver.find_element_by_id().clear()
        driver.find_element_by_id().send_keys('Hello')
        driver.find_element_by_id().get_attribute()
        driver.find_element_by_id().text

        #Select from menu
        Select(driver.find_element_by_id()).select_by_visible_text()
        Select(driver.find_element_by_id()).select_by_index()
        Select(driver.find_element_by_id()).select_by_value()
        Select(driver.find_element_by_id()).deselect_all()


        #wait
        sleep(2)
        #ImplicitWait - set for the entire duration of the webdriver object
        # Will help only for new page be loaded
        driver.manage.timeouts.implicit_wait = 5
        #ExplicitWait - wait particular element
        # wait for element be loaded
        WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located((By.XPATH, 'welcome')))
        id = 123
        username = 'jb' + str(id)
        self.wait.until(expected_conditions.visibility_of_element_located((By.ID, 'id'))).send_keys('jb' + id)
        self.wait.until(expected_conditions.alert_is_present)

        #Scroll
        driver.execute_script("window.scrollTo(0, 250)")

        #Asserts
        self.assertEqual('Billing', '')
        self.assertTrue()
        self.assertFalse()
        self.assertNotEquals
        self.assertGreater()
        self.assertLess()

        # xpath
        # absolute xpath starts from the body html - starts with /
        # html/body/div[5]/div[2]/div/div[2]/div[2]/h2[1]

        # relative xpath starts from any point of html tree - starts with //
        # // *[ @ id = 'answers']

        # Search in console - $x("//a[@class='a-link-normal fsdLink fsdDeptLink'][contains(text(), 'Children')]")

        "//a[@class='nav-a' and text()=\"Today's Deals\"]"
        "//*[contains(@class, 'small') and text()='#{x}']"
        '//p[starts-with(@me,"you")]'
        "//span[@title='All Listings' and text()='All Listings']"
        "//*[contains(@class,'small') and text()='All Listings']"
        "//div[@class='september']/div[@class='irritating']/ul/li"
        "//div[@class='a-fixed-left-grid-inner']//span[@class='a-icon-alt'][contains(text(), '4.9') or contains(text(), '4.8') or contains(text(), '4.7')]"
        "//div[@class='a-fixed-left-grid-inner']//span[@class='a-icon-alt'][contains(text(), '4.')]"


        # close and quit
        # close - closes the current window, for example pop up window
        # quit - quits the browser session

        # switch
        # switch_to - swith from current document to another window or frame
        # switch_to_alert -


if __name__ == '__main__':
    unittest.main()