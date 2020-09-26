import unittest
import time

from selenium import webdriver

class MyTestCase(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(r"C:\Users\Oleg\PycharmProjects\Selenium_Ellie\Tests\chromedriver\chromedriver_win32\chromedriver.exe")
        self.driver = webdriver.Chrome("C:\\Users\\Oleg\\PycharmProjects\\Selenium_Ellie\\Tests\\chromedriver\\chromedriver_win32\\chromedriver.exe")
        self.driver.get('http://hrm-online.portnov.com/symfony/web/index.php/auth/login') # Отвечает за сайт, куда мы посылаем запрос

    def test_valid_login(self):
        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id('btnLogin').click()

        time.sleep(2)
        welcome_text = driver.find_element_by_id('welcome').text
        self.assertEqual('Welcome Admin', welcome_text)

        # CLICK THE ADD BUTTON
        driver.find_element_by_id('btnAdd').click()

        # Enter First and Last name
        driver.find_element_by_id('firstName').send_keys("James")
        driver.find_element_by_id('lastName').send_keys('Bond')

        # Enter and remember the empId
        driver.find_element_by_id('employeeId').clear()
        driver.find_element_by_id('employeeId').send_keys('101112')

        # Save the Employee
        driver.find_element_by_id('btnSave').click()

        # go to the PIM page
        driver.find_element_by_id('menu_pim_viewPimModule').click()

        # Search by EmpId
        driver.find_element_by_id('empsearch_id').send_keys('101112')
        driver.find_element_by_id('searchBtn').click()


        # Expexted: i record back


        # Expected Correct Full Name
        firstName = driver.find_element_by_xpath('//td[3]/a').text
        lastName = driver.find_element_by_xpath('//td[4]/a').text

        self.assertEqual('James', firstName)
        self.assertEqual('Bond', lastName)

if __name__ == '__main__':
    unittest.main()

