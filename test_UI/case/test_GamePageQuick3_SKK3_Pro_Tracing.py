import unittest
from config.SetUIConfig import Driver, Target
from test_UI.common.GamePageCommon import GamePageCommon
from test_UI.page.LoginPage import LoginPage
from test_UI.page.HomePage import HomePage
from test_UI.page.GamePage import GamePage
from test_UI.page.GamePageQuick3 import GamePageQuick3
from utils import Assertion


@unittest.skipUnless(Target == 'web', '此測項為web使用')
class SKK3_Pro_Tracing(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver
        login_page = LoginPage(cls.driver)
        login_page.execute_login()

        home_page = HomePage(cls.driver)
        home_page.switch_category("game")

        game_page = GamePage(cls.driver)
        cls.game_name = game_page.switch_game("Quick3", "skk3")

    def test_01_SKK3_pro_normal_continuous3_double_tracking(self):
        page_quick3 = GamePageQuick3(self.driver)
        page_quick3.switch_pro_game("normal", "continuous3")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        page_quick3.click_random_button()

        bet_flow.click_tracing_category("double_tracking", "4")
        OrderInfoTrace_Yes = bet_flow.OrderInfoTrace_Yes("4")
        default_tracking_data_of_current = bet_flow.default_tracking_data_of_current()
        default_tracking_data_of_expect = bet_flow.default_tracking_data_of_expect('double_tracking')
        bet_flow.input_multiples_of_tracing_value()
        expect_tracking_data_of_current = bet_flow.expect_tracking_data_of_current()
        expect_tracking_data = bet_flow.expect_tracking_data('double_tracking')

        bet_flow.click_payment("tracing_bet")
        order_info_confirm = bet_flow.check_order_info()
        bet_flow.click_tracking_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_tracing_order_done()

        expect_data = [self.game_name, "", "0.30", OrderInfoTrace_Yes, "1", "1"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)
        self.assertEqual([default_tracking_data_of_expect, expect_tracking_data],
                         [default_tracking_data_of_current, expect_tracking_data_of_current])

    def test_02_SKK3_pro_normal_continuous3_smart_tracking(self):
        page_quick3 = GamePageQuick3(self.driver)
        page_quick3.switch_pro_game("normal", "continuous3")
        # page_quick3.bet_pro_all("continuous3")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        page_quick3.click_random_button()

        bet_flow.click_tracing_category("smart_tracking", "4")
        OrderInfoTrace_Yes = bet_flow.OrderInfoTrace_Yes("4")
        default_tracking_data_of_current = bet_flow.default_tracking_data_of_current()
        default_tracking_data_of_expect = bet_flow.default_tracking_data_of_expect('smart_tracking')
        bet_flow.input_multiples_of_tracing_value()
        expect_tracking_data_of_current = bet_flow.expect_tracking_data_of_current()
        expect_tracking_data = bet_flow.expect_tracking_data('smart_tracking')

        bet_flow.click_payment("tracing_bet")
        order_info_confirm = bet_flow.check_order_info()
        bet_flow.click_tracking_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_tracing_order_done()

        expect_data = [self.game_name, "", "0.30", OrderInfoTrace_Yes, "1", "1"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)
        self.assertEqual([default_tracking_data_of_expect, expect_tracking_data],
                         [default_tracking_data_of_current, expect_tracking_data_of_current])

    def test_03_SKK3_pro_normal_same3_double_tracking(self):
        page_quick3 = GamePageQuick3(self.driver)
        page_quick3.switch_pro_game("normal", "same3")
        # page_quick3.bet_pro_all("same3")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        page_quick3.click_random_button()

        bet_flow.click_tracing_category("double_tracking", "4")
        OrderInfoTrace_Yes = bet_flow.OrderInfoTrace_Yes("4")
        default_tracking_data_of_current = bet_flow.default_tracking_data_of_current()
        default_tracking_data_of_expect = bet_flow.default_tracking_data_of_expect('double_tracking')
        bet_flow.input_multiples_of_tracing_value()
        expect_tracking_data_of_current = bet_flow.expect_tracking_data_of_current()
        expect_tracking_data = bet_flow.expect_tracking_data('double_tracking')

        bet_flow.click_payment("tracing_bet")
        order_info_confirm = bet_flow.check_order_info()
        bet_flow.click_tracking_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_tracing_order_done()

        expect_data = [self.game_name, "", "0.30", OrderInfoTrace_Yes, "1", "1"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)
        self.assertEqual([default_tracking_data_of_expect, expect_tracking_data],
                         [default_tracking_data_of_current, expect_tracking_data_of_current])

    def test_04_SKK3_pro_normal_same3_smart_tracking(self):
        page_quick3 = GamePageQuick3(self.driver)
        page_quick3.switch_pro_game("normal", "same3")
        # page_quick3.bet_pro_all("same3")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        page_quick3.click_random_button()

        bet_flow.click_tracing_category("smart_tracking", "4")
        OrderInfoTrace_Yes = bet_flow.OrderInfoTrace_Yes("4")
        default_tracking_data_of_current = bet_flow.default_tracking_data_of_current()
        default_tracking_data_of_expect = bet_flow.default_tracking_data_of_expect('smart_tracking')
        bet_flow.input_multiples_of_tracing_value()
        expect_tracking_data_of_current = bet_flow.expect_tracking_data_of_current()
        expect_tracking_data = bet_flow.expect_tracking_data('smart_tracking')

        bet_flow.click_payment("tracing_bet")
        order_info_confirm = bet_flow.check_order_info()
        bet_flow.click_tracking_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_tracing_order_done()

        expect_data = [self.game_name, "", "0.30", OrderInfoTrace_Yes, "1", "1"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)
        self.assertEqual([default_tracking_data_of_expect, expect_tracking_data],
                         [default_tracking_data_of_current, expect_tracking_data_of_current])

    def test_05_SKK3_pro_normal_differ3_double_tracking(self):
        page_quick3 = GamePageQuick3(self.driver)
        page_quick3.switch_pro_game("normal", "differ3")
        # page_quick3.bet_pro_all("differ3")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        page_quick3.click_random_button()

        bet_flow.click_tracing_category("double_tracking", "4")
        OrderInfoTrace_Yes = bet_flow.OrderInfoTrace_Yes("4")
        default_tracking_data_of_current = bet_flow.default_tracking_data_of_current()
        default_tracking_data_of_expect = bet_flow.default_tracking_data_of_expect('double_tracking')
        bet_flow.input_multiples_of_tracing_value()
        expect_tracking_data_of_current = bet_flow.expect_tracking_data_of_current()
        expect_tracking_data = bet_flow.expect_tracking_data('double_tracking')

        bet_flow.click_payment("tracing_bet")
        order_info_confirm = bet_flow.check_order_info()
        bet_flow.click_tracking_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_tracing_order_done()

        expect_data = [self.game_name, "", "0.30", OrderInfoTrace_Yes, "1", "1"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)
        self.assertEqual([default_tracking_data_of_expect, expect_tracking_data],
                         [default_tracking_data_of_current, expect_tracking_data_of_current])

    # def test_06_SKK3_pro_normal_differ3_smart_tracking(self):
    #     page_quick3 = GamePageQuick3(self.driver)
    #     page_quick3.switch_pro_game("normal", "differ3")
    #     # page_quick3.bet_pro_all("differ3")
    #
    #     bet_flow = GamePageCommon(self.driver)
    #     bet_flow.set_pro_bet_setting("cent")
    #     page_quick3.click_random_button()
    #
    #     bet_flow.click_tracing_category("smart_tracking", "4")
    #     OrderInfoTrace_Yes = bet_flow.OrderInfoTrace_Yes("4")
    #     default_tracking_data_of_current = bet_flow.default_tracking_data_of_current()
    #     default_tracking_data_of_expect = bet_flow.default_tracking_data_of_expect('smart_tracking')
    #     bet_flow.input_multiples_of_tracing_value()
    #     expect_tracking_data_of_current = bet_flow.expect_tracking_data_of_current()
    #     expect_tracking_data = bet_flow.expect_tracking_data('smart_tracking')
    #
    #     bet_flow.click_payment("tracing_bet")
    #     order_info_confirm = bet_flow.check_order_info()
    #     bet_flow.click_tracking_order_confirm()
    #     order_info_done = bet_flow.check_order_info()
    #     bet_flow.click_tracing_order_done()
    #
    #     expect_data = [self.game_name, "", "0.30", OrderInfoTrace_Yes, "1", "1"]
    #     Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)
    #     self.assertEqual([default_tracking_data_of_expect, expect_tracking_data],
    #                      [default_tracking_data_of_current, expect_tracking_data_of_current])

    def test_07_SKK3_pro_normal_same2_singleChoice_double_tracking(self):
        page_quick3 = GamePageQuick3(self.driver)
        page_quick3.switch_pro_game("normal", "same2", "singleChoice")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        page_quick3.click_random_button()

        bet_flow.click_tracing_category("double_tracking", "4")
        OrderInfoTrace_Yes = bet_flow.OrderInfoTrace_Yes("4")
        default_tracking_data_of_current = bet_flow.default_tracking_data_of_current()
        default_tracking_data_of_expect = bet_flow.default_tracking_data_of_expect('double_tracking')
        bet_flow.input_multiples_of_tracing_value()
        expect_tracking_data_of_current = bet_flow.expect_tracking_data_of_current()
        expect_tracking_data = bet_flow.expect_tracking_data('double_tracking')

        bet_flow.click_payment("tracing_bet")
        order_info_confirm = bet_flow.check_order_info()
        bet_flow.click_tracking_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_tracing_order_done()

        expect_data = [self.game_name, "", "0.30", OrderInfoTrace_Yes, "1", "1"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)
        self.assertEqual([default_tracking_data_of_expect, expect_tracking_data],
                         [default_tracking_data_of_current, expect_tracking_data_of_current])

    # def test_08_SKK3_pro_normal_same2_singleChoice_smart_tracking(self):
    #     page_quick3 = GamePageQuick3(self.driver)
    #     page_quick3.switch_pro_game("normal", "same2", "singleChoice")
    #
    #     bet_flow = GamePageCommon(self.driver)
    #     bet_flow.set_pro_bet_setting("cent")
    #     page_quick3.click_random_button()
    #
    #     bet_flow.click_tracing_category("smart_tracking", "4")
    #     OrderInfoTrace_Yes = bet_flow.OrderInfoTrace_Yes("4")
    #     default_tracking_data_of_current = bet_flow.default_tracking_data_of_current()
    #     default_tracking_data_of_expect = bet_flow.default_tracking_data_of_expect('smart_tracking')
    #     bet_flow.input_multiples_of_tracing_value()
    #     expect_tracking_data_of_current = bet_flow.expect_tracking_data_of_current()
    #     expect_tracking_data = bet_flow.expect_tracking_data('smart_tracking')
    #
    #     bet_flow.click_payment("tracing_bet")
    #     order_info_confirm = bet_flow.check_order_info()
    #     bet_flow.click_tracking_order_confirm()
    #     order_info_done = bet_flow.check_order_info()
    #     bet_flow.click_tracing_order_done()
    #
    #     expect_data = [self.game_name, "", "0.30", OrderInfoTrace_Yes, "1", "1"]
    #     Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)
    #     self.assertEqual([default_tracking_data_of_expect, expect_tracking_data],
    #                      [default_tracking_data_of_current, expect_tracking_data_of_current])

    def test_09_SKK3_pro_normal_differ2_double_tracking(self):
        page_quick3 = GamePageQuick3(self.driver)
        page_quick3.switch_pro_game("normal", "differ2")
        # page_quick3.bet_pro_all("differ2")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        page_quick3.click_random_button()

        bet_flow.click_tracing_category("double_tracking", "4")
        OrderInfoTrace_Yes = bet_flow.OrderInfoTrace_Yes("4")
        default_tracking_data_of_current = bet_flow.default_tracking_data_of_current()
        default_tracking_data_of_expect = bet_flow.default_tracking_data_of_expect('double_tracking')
        bet_flow.input_multiples_of_tracing_value()
        expect_tracking_data_of_current = bet_flow.expect_tracking_data_of_current()
        expect_tracking_data = bet_flow.expect_tracking_data('double_tracking')

        bet_flow.click_payment("tracing_bet")
        order_info_confirm = bet_flow.check_order_info()
        bet_flow.click_tracking_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_tracing_order_done()

        expect_data = [self.game_name, "", "0.30", OrderInfoTrace_Yes, "1", "1"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)
        self.assertEqual([default_tracking_data_of_expect, expect_tracking_data],
                         [default_tracking_data_of_current, expect_tracking_data_of_current])

    def test_10_SKK3_pro_normal_differ2_smart_tracking(self):
        page_quick3 = GamePageQuick3(self.driver)
        page_quick3.switch_pro_game("normal", "differ2")
        # page_quick3.bet_pro_all("differ2")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        page_quick3.click_random_button()

        bet_flow.click_tracing_category("smart_tracking", "4")
        OrderInfoTrace_Yes = bet_flow.OrderInfoTrace_Yes("4")
        default_tracking_data_of_current = bet_flow.default_tracking_data_of_current()
        default_tracking_data_of_expect = bet_flow.default_tracking_data_of_expect('smart_tracking')
        bet_flow.input_multiples_of_tracing_value()
        expect_tracking_data_of_current = bet_flow.expect_tracking_data_of_current()
        expect_tracking_data = bet_flow.expect_tracking_data('smart_tracking')

        bet_flow.click_payment("tracing_bet")
        order_info_confirm = bet_flow.check_order_info()
        bet_flow.click_tracking_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_tracing_order_done()

        expect_data = [self.game_name, "", "0.30", OrderInfoTrace_Yes, "1", "1"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)
        self.assertEqual([default_tracking_data_of_expect, expect_tracking_data],
                         [default_tracking_data_of_current, expect_tracking_data_of_current])

    @classmethod
    def tearDownClass(cls):
        cls.driver = Driver
        bet_flow = GamePageCommon(cls.driver)
        bet_flow.back_to_homepage()
        bet_flow.check_homepage_showing()


if __name__ == '__main__':
    unittest.main()
