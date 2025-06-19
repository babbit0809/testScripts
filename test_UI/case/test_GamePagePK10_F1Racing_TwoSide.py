import unittest
from config.SetUIConfig import Driver
from test_UI.common.GamePageCommon import GamePageCommon
from test_UI.page.LoginPage import LoginPage
from test_UI.page.HomePage import HomePage
from test_UI.page.GamePage import GamePage
from test_UI.page.GamePagePK10 import GamePagePK10
from utils import Assertion, Localization


class F1Racing_TwoSide(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver
        login_page = LoginPage(cls.driver)
        login_page.execute_login()

        home_page = HomePage(cls.driver)
        home_page.switch_category("game")

        game_page = GamePage(cls.driver)
        cls.game_name = game_page.switch_game("PK10", "f1racing")
        cls.OrderInfoTrace_No = Localization.get_loc("GamePage_Common", 'OrderInfoTrace_No')

    def test_10_F1Racing_twoSide_twoface(self):
        page_pk10 = GamePagePK10(self.driver)
        page_pk10.switch_twoSide_game("twoface")
        page_pk10.bet_twoSide_all("twoface")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_twoSide_bet_setting("2")

        bet_flow.click_payment("twoSide")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "100.00", self.OrderInfoTrace_No, "1", "50"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_11_F1Racing_twoSide_combination1and2(self):
        page_pk10 = GamePagePK10(self.driver)
        page_pk10.switch_twoSide_game("combination1and2")
        page_pk10.bet_twoSide_all("combination1and2")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_twoSide_bet_setting("2")

        bet_flow.click_payment("twoSide")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "90.00", self.OrderInfoTrace_No, "1", "45"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_12_F1Racing_twoSide_sum1and2(self):
        page_pk10 = GamePagePK10(self.driver)
        page_pk10.switch_twoSide_game("sum1and2")
        page_pk10.bet_twoSide_all("sum1and2")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_twoSide_bet_setting("2")

        bet_flow.click_payment("twoSide")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "42.00", self.OrderInfoTrace_No, "1", "21"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_13_F1Racing_twoSide_firsttotenth(self):
        page_pk10 = GamePagePK10(self.driver)
        page_pk10.switch_twoSide_game("firsttotenth")
        page_pk10.bet_twoSide_all("firsttotenth")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_twoSide_bet_setting("2")

        bet_flow.click_payment("twoSide")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "200.00", self.OrderInfoTrace_No, "1", "100"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    @classmethod
    def tearDownClass(cls):
        cls.driver = Driver
        bet_flow = GamePageCommon(cls.driver)
        bet_flow.back_to_homepage()
        bet_flow.check_homepage_showing()


if __name__ == '__main__':
    unittest.main()
