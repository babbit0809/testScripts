import unittest
from config.SetUIConfig import Driver
from test_UI.common.GamePageCommon import GamePageCommon
from test_UI.page.LoginPage import LoginPage
from test_UI.page.HomePage import HomePage
from test_UI.page.GamePage import GamePage
from test_UI.page.GamePageQuick3 import GamePageQuick3
from utils import Assertion, Localization


class HuBK3_Pro(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver
        login_page = LoginPage(cls.driver)
        login_page.execute_login()

        home_page = HomePage(cls.driver)
        home_page.switch_category("game")

        game_page = GamePage(cls.driver)
        cls.game_name = game_page.switch_game("Quick3", "hubk3")
        cls.OrderInfoTrace_No = Localization.get_loc("GamePage_Common", 'OrderInfoTrace_No')

    def test_01_HuBK3_pro_normal_sum(self):
        page_quick3 = GamePageQuick3(self.driver)
        page_quick3.switch_pro_game("normal", "sum")
        page_quick3.bet_pro_all("sum")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.40", self.OrderInfoTrace_No, "20", "20"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_02_HuBK3_pro_normal_continuous3(self):
        page_quick3 = GamePageQuick3(self.driver)
        page_quick3.switch_pro_game("normal", "continuous3")
        page_quick3.bet_pro_all("continuous3")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.10", self.OrderInfoTrace_No, "2", "5"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_03_HuBK3_pro_normal_same3(self):
        page_quick3 = GamePageQuick3(self.driver)
        page_quick3.switch_pro_game("normal", "same3")
        page_quick3.bet_pro_all("same3")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.14", self.OrderInfoTrace_No, "2", "7"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_04_HuBK3_pro_normal_differ3(self):
        page_quick3 = GamePageQuick3(self.driver)
        page_quick3.switch_pro_game("normal", "differ3")
        page_quick3.bet_pro_all("differ3")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.42", self.OrderInfoTrace_No, "2", "21"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_05_HuBK3_pro_normal_same2_singleChoice(self):
        bet_case = (
            # A tuple of (params_value, subTest_description)
            ("same2case1", "同號: 1 + 二同號通選 + 不同號: 2-6"),
            ("same2case2", "同號: 2-6 + 二同號通選 + 不同號: 1")
        )

        for params_value, subTest_description in bet_case:

            with self.subTest(subTest_description):
                page_quick3 = GamePageQuick3(self.driver)
                page_quick3.switch_pro_game("normal", "same2", "singleChoice")
                page_quick3.bet_pro_all("same2", "singleChoice", params_value)

                bet_flow = GamePageCommon(self.driver)
                bet_flow.set_pro_bet_setting("cent")
                bet_flow.click_bet_basket()

                bet_flow.click_payment("pro")
                order_info_confirm = bet_flow.check_order_info()

                bet_flow.click_order_confirm()
                order_info_done = bet_flow.check_order_info()
                bet_flow.click_order_done()

                expect_data = [self.game_name, "", "0.12", self.OrderInfoTrace_No, "2", "6"]
                Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_06_HuBK3_pro_normal_same2_multiChoices(self):
        page_quick3 = GamePageQuick3(self.driver)
        page_quick3.switch_pro_game("normal", "same2", "multiChoices")
        page_quick3.bet_pro_all("same2", "multiChoices")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.12", self.OrderInfoTrace_No, "1", "6"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_07_HuBK3_pro_normal_differ2(self):
        page_quick3 = GamePageQuick3(self.driver)
        page_quick3.switch_pro_game("normal", "differ2")
        page_quick3.bet_pro_all("differ2")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.30", self.OrderInfoTrace_No, "15", "15"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    @classmethod
    def tearDownClass(cls):
        cls.driver = Driver
        bet_flow = GamePageCommon(cls.driver)
        bet_flow.back_to_homepage()
        bet_flow.check_homepage_showing()


if __name__ == '__main__':
    unittest.main()
