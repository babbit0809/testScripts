import unittest
from config.SetUIConfig import Driver, Target
from test_UI.page.HomePage import HomePage
from test_UI.page.UserPage import UserPage


class TestFinished(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver
        print(cls.driver, "\nStart tearDown.")

    @staticmethod
    def test_finished():
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver = Driver
        if Target == 'app':
            print("Logout app.")
            home_page = HomePage(cls.driver)
            home_page.switch_category("user")
            page_user = UserPage(cls.driver)
            page_user.click_logout()
        elif Target == 'h5':
            print("Close mobile browser.")
            cls.driver.close_app()
        elif Target in ['web', 'admintool']:
            print("Close PC browser.")
            cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
