import unittest
from config.SetUIConfig import Driver
from test_UI.common.GamePageCommon import GamePageCommon
from test_UI.page.LoginPage import LoginPage
from test_UI.page.HomePage import HomePage
from test_UI.page.GamePage import GamePage
from test_UI.page.GamePageQuick3 import GamePageQuick3
from utils import Assertion, Localization


class Quick3_TwoSide(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver
        login_page = LoginPage(cls.driver)
        login_page.execute_login()

        home_page = HomePage(cls.driver)
        home_page.switch_category("game")

        game_page = GamePage(cls.driver)
        cls.game_name = game_page.switch_game("Quick3", "quick3")
        cls.OrderInfoTrace_No = Localization.get_loc("GamePage_Common", 'OrderInfoTrace_No')

    def test_08_Quick3_twoSide_army3(self):
        page_quick3 = GamePageQuick3(self.driver)
        page_quick3.switch_twoSide_game("army3")
        page_quick3.bet_twoSide_all("army3")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_twoSide_bet_setting("2")

        bet_flow.click_payment("twoSide")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "12.00", self.OrderInfoTrace_No, "1", "6"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_09_Quick3_twoSide_fast3Sum(self):
        page_quick3 = GamePageQuick3(self.driver)
        page_quick3.switch_twoSide_game("fast3Sum")
        page_quick3.bet_twoSide_all("fast3Sum")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_twoSide_bet_setting("2")

        bet_flow.click_payment("twoSide")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "8.00", self.OrderInfoTrace_No, "1", "4"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_10_Quick3_twoSide_point(self):
        page_quick3 = GamePageQuick3(self.driver)
        page_quick3.switch_twoSide_game("point")
        page_quick3.bet_twoSide_all("point")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_twoSide_bet_setting("2")

        bet_flow.click_payment("twoSide")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "28.00", self.OrderInfoTrace_No, "1", "14"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_11_Quick3_twoSide_triple(self):
        page_quick3 = GamePageQuick3(self.driver)
        page_quick3.switch_twoSide_game("triple")
        page_quick3.bet_twoSide_all("triple")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_twoSide_bet_setting("2")

        bet_flow.click_payment("twoSide")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "14.00", self.OrderInfoTrace_No, "1", "7"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_12_Quick3_twoSide_long(self):
        page_quick3 = GamePageQuick3(self.driver)
        page_quick3.switch_twoSide_game("long")
        page_quick3.bet_twoSide_all("long")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_twoSide_bet_setting("2")

        bet_flow.click_payment("twoSide")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "30.00", self.OrderInfoTrace_No, "1", "15"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_13_Quick3_twoSide_short(self):
        page_quick3 = GamePageQuick3(self.driver)
        page_quick3.switch_twoSide_game("short")
        page_quick3.bet_twoSide_all("short")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_twoSide_bet_setting("2")

        bet_flow.click_payment("twoSide")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "12.00", self.OrderInfoTrace_No, "1", "6"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_14_Quick3_twoSide_fishShrimpCrab(self):
        page_quick3 = GamePageQuick3(self.driver)
        page_quick3.switch_twoSide_game("fishShrimpCrab")
        page_quick3.bet_twoSide_all("fishShrimpCrab")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_twoSide_bet_setting("2")

        bet_flow.click_payment("twoSide")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "12.00", self.OrderInfoTrace_No, "1", "6"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    @classmethod
    def tearDownClass(cls):
        cls.driver = Driver
        bet_flow = GamePageCommon(cls.driver)
        bet_flow.back_to_homepage()
        bet_flow.check_homepage_showing()


if __name__ == '__main__':
    unittest.main()
