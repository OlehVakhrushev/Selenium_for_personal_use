import unittest

from selenium import webdriver


class AddEmployee(unittest.TestCase):

    def set(self):
        self.driver = webdriver.Chrome(
            executable_path= r'C:\Users\Oleg\PycharmProjects\Selenium_Ellie\Tests\chromedriver\chromedriver_win32\chromedriver.exe')
        self.driver.get('http://hrm-online.portnov.com/symfony/web/index.php/auth/login')

    def tearDown(self):
        self.driver.quit()

    def test_something(self):
        # login
        # click the button
        # enter First and Last name
        # enter anf remember the empId
        # Save the Employee
        # go to PIM page
        # search by EmpId
        # expected: I record back
        # expected Correct Name and EmpId



        self.assertEqual(True, False)


if __name__=="__main__":
    unittest.main()