import unittest
from config.SetUIConfig import Driver
from test_UI.common.GamePageCommon import GamePageCommon
from test_UI.page.LoginPage import LoginPage
from test_UI.page.HomePage import HomePage
from test_UI.page.GamePage import GamePage
from test_UI.page.GamePage11x5 import GamePage11x5
from utils import Assertion, Localization


class SK11x5_TwoSide(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver
        login_page = LoginPage(cls.driver)
        login_page.execute_login()

        home_page = HomePage(cls.driver)
        home_page.switch_category("game")

        game_page = GamePage(cls.driver)
        cls.game_name = game_page.switch_game("11x5", "sk11x5")
        cls.OrderInfoTrace_No = Localization.get_loc("GamePage_Common", 'OrderInfoTrace_No')

    def test_43_SK11x5_twoSide_firstBall(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_twoSide_game("firstBall")
        page_11x5.bet_twoSide_all("firstBall")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_twoSide_bet_setting("2")

        bet_flow.click_payment("twoSide")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "30.00", self.OrderInfoTrace_No, "1", "15"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_44_SK11x5_twoSide_secondBall(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_twoSide_game("secondBall")
        page_11x5.bet_twoSide_all("secondBall")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_twoSide_bet_setting("2")

        bet_flow.click_payment("twoSide")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "30.00", self.OrderInfoTrace_No, "1", "15"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_45_SK11x5_twoSide_thirdBall(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_twoSide_game("thirdBall")
        page_11x5.bet_twoSide_all("thirdBall")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_twoSide_bet_setting("2")

        bet_flow.click_payment("twoSide")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "30.00", self.OrderInfoTrace_No, "1", "15"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_46_SK11x5_twoSide_fourthBall(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_twoSide_game("fourthBall")
        page_11x5.bet_twoSide_all("fourthBall")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_twoSide_bet_setting("2")

        bet_flow.click_payment("twoSide")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "30.00", self.OrderInfoTrace_No, "1", "15"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_47_SK11x5_twoSide_fifthBall(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_twoSide_game("fifthBall")
        page_11x5.bet_twoSide_all("fifthBall")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_twoSide_bet_setting("2")

        bet_flow.click_payment("twoSide")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "30.00", self.OrderInfoTrace_No, "1", "15"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_48_SK11x5_twoSide_total(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_twoSide_game("total")
        page_11x5.bet_twoSide_all("total")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_twoSide_bet_setting("2")

        bet_flow.click_payment("twoSide")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "12.00", self.OrderInfoTrace_No, "1", "6"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_49_SK11x5_twoSide_dragon(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_twoSide_game("dragon")
        page_11x5.bet_twoSide_all("dragon")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_twoSide_bet_setting("2")

        bet_flow.click_payment("twoSide")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "20.00", self.OrderInfoTrace_No, "1", "10"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_50_SK11x5_twoSide_tiger(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_twoSide_game("tiger")
        page_11x5.bet_twoSide_all("tiger")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_twoSide_bet_setting("2")

        bet_flow.click_payment("twoSide")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "20.00", self.OrderInfoTrace_No, "1", "10"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    @classmethod
    def tearDownClass(cls):
        cls.driver = Driver
        bet_flow = GamePageCommon(cls.driver)
        bet_flow.back_to_homepage()
        bet_flow.check_homepage_showing()


if __name__ == '__main__':
    unittest.main()
