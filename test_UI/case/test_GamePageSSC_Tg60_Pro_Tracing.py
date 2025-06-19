import unittest
from config.SetUIConfig import Driver, Target
from test_UI.common.GamePageCommon import GamePageCommon
from test_UI.page.LoginPage import LoginPage
from test_UI.page.HomePage import HomePage
from test_UI.page.GamePage import GamePage
from test_UI.page.GamePageSSC import GamePageSSC
from utils import Assertion


@unittest.skipUnless(Target == 'web', '此測項為web使用')
class Tg60_Pro_Tracing(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver
        login_page = LoginPage(cls.driver)
        login_page.execute_login()

        home_page = HomePage(cls.driver)
        home_page.switch_category("game")

        game_page = GamePage(cls.driver)
        cls.game_name = game_page.switch_game("SSC", "tg60")

    def test_01_Tg60_pro_normal_fiveStar_fiveStarDirectSelection_double_tracking(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "fiveStar", "fiveStarDirectSelection")
        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.bet_tracing()

        bet_flow.click_tracing_category("double_tracking", "4")
        OrderInfoTrace_Yes = bet_flow.OrderInfoTrace_Yes("4")
        default_tracking_data_of_current = bet_flow.default_tracking_data_of_current()
        default_tracking_data_of_expect = bet_flow.default_tracking_data_of_expect('double_tracking')
        bet_flow.input_multiples_of_tracing_value()
        expect_tracking_data_of_current = bet_flow.expect_tracking_data_of_current()
        expect_tracking_data = bet_flow.expect_tracking_data('double_tracking')

        bet_flow.click_payment("tracing_bet")
        order_info_confirm = bet_flow.check_order_info()
        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_tracing_order_done()

        expect_data = [self.game_name, "", "0.30", OrderInfoTrace_Yes, "1", "1"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)
        self.assertEqual([default_tracking_data_of_expect, expect_tracking_data],
                         [default_tracking_data_of_current, expect_tracking_data_of_current])

    # def test_02_Tg60_pro_normal_fiveStar_fiveStarDirectSelection_smart_tracking(self):
    #     page_ssc = GamePageSSC(self.driver)
    #     page_ssc.switch_pro_game("normal", "fiveStar", "fiveStarDirectSelection")
    #     bet_flow = GamePageCommon(self.driver)
    #     bet_flow.set_pro_bet_setting("cent")
    #     bet_flow.bet_tracing()
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
    #     bet_flow.click_order_confirm()
    #     order_info_done = bet_flow.check_order_info()
    #     bet_flow.click_tracing_order_done()
    #
    #     expect_data = [self.game_name, "", "0.30", OrderInfoTrace_Yes, "1", "1"]
    #     Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)
    #     self.assertEqual([default_tracking_data_of_expect, expect_tracking_data],
    #                      [default_tracking_data_of_current, expect_tracking_data_of_current])

    def test_03_Tg60_pro_normal_threeStar_front3Choice_double_tracking(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "threeStar", "front3Choice")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.bet_tracing()

        bet_flow.click_tracing_category("double_tracking", "4")
        OrderInfoTrace_Yes = bet_flow.OrderInfoTrace_Yes("4")
        default_tracking_data_of_current = bet_flow.default_tracking_data_of_current()
        default_tracking_data_of_expect = bet_flow.default_tracking_data_of_expect('double_tracking')
        bet_flow.input_multiples_of_tracing_value()
        expect_tracking_data_of_current = bet_flow.expect_tracking_data_of_current()
        expect_tracking_data = bet_flow.expect_tracking_data('double_tracking')

        bet_flow.click_payment("tracing_bet")
        order_info_confirm = bet_flow.check_order_info()
        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_tracing_order_done()

        expect_data = [self.game_name, "", "0.30", OrderInfoTrace_Yes, "1", "1"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)
        self.assertEqual([default_tracking_data_of_expect, expect_tracking_data],
                         [default_tracking_data_of_current, expect_tracking_data_of_current])

    def test_04_Tg60_pro_normal_threeStar_front3Choice_smart_tracking(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "threeStar", "front3Choice")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.bet_tracing()

        bet_flow.click_tracing_category("smart_tracking", "4")
        OrderInfoTrace_Yes = bet_flow.OrderInfoTrace_Yes("4")
        default_tracking_data_of_current = bet_flow.default_tracking_data_of_current()
        default_tracking_data_of_expect = bet_flow.default_tracking_data_of_expect('smart_tracking')
        bet_flow.input_multiples_of_tracing_value()
        expect_tracking_data_of_current = bet_flow.expect_tracking_data_of_current()
        expect_tracking_data = bet_flow.expect_tracking_data('smart_tracking')

        bet_flow.click_payment("tracing_bet")
        order_info_confirm = bet_flow.check_order_info()
        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_tracing_order_done()

        expect_data = [self.game_name, "", "0.30", OrderInfoTrace_Yes, "1", "1"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)
        self.assertEqual([default_tracking_data_of_expect, expect_tracking_data],
                         [default_tracking_data_of_current, expect_tracking_data_of_current])

    def test_05_Tg60_pro_normal_twoStar_frontDirect_double_tracking(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "twoStar", "frontDirect")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.bet_tracing()

        bet_flow.click_tracing_category("double_tracking", "4")
        OrderInfoTrace_Yes = bet_flow.OrderInfoTrace_Yes("4")
        default_tracking_data_of_current = bet_flow.default_tracking_data_of_current()
        default_tracking_data_of_expect = bet_flow.default_tracking_data_of_expect('double_tracking')
        bet_flow.input_multiples_of_tracing_value()
        expect_tracking_data_of_current = bet_flow.expect_tracking_data_of_current()
        expect_tracking_data = bet_flow.expect_tracking_data('double_tracking')

        bet_flow.click_payment("tracing_bet")
        order_info_confirm = bet_flow.check_order_info()
        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_tracing_order_done()

        expect_data = [self.game_name, "", "0.30", OrderInfoTrace_Yes, "1", "1"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)
        self.assertEqual([default_tracking_data_of_expect, expect_tracking_data],
                         [default_tracking_data_of_current, expect_tracking_data_of_current])

    def test_06_Tg60_pro_normal_twoStar_frontDirect_smart_tracking(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "twoStar", "frontDirect")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.bet_tracing()

        bet_flow.click_tracing_category("smart_tracking", "4")
        OrderInfoTrace_Yes = bet_flow.OrderInfoTrace_Yes("4")
        default_tracking_data_of_current = bet_flow.default_tracking_data_of_current()
        default_tracking_data_of_expect = bet_flow.default_tracking_data_of_expect('smart_tracking')
        bet_flow.input_multiples_of_tracing_value()
        expect_tracking_data_of_current = bet_flow.expect_tracking_data_of_current()
        expect_tracking_data = bet_flow.expect_tracking_data('smart_tracking')

        bet_flow.click_payment("tracing_bet")
        order_info_confirm = bet_flow.check_order_info()
        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_tracing_order_done()

        expect_data = [self.game_name, "", "0.30", OrderInfoTrace_Yes, "1", "1"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)
        self.assertEqual([default_tracking_data_of_expect, expect_tracking_data],
                         [default_tracking_data_of_current, expect_tracking_data_of_current])

    def test_07_Tg60_pro_normal_dingweidan_double_tracking(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "dingweidan")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.bet_tracing()

        bet_flow.click_tracing_category("double_tracking", "4")
        OrderInfoTrace_Yes = bet_flow.OrderInfoTrace_Yes("4")
        default_tracking_data_of_current = bet_flow.default_tracking_data_of_current()
        default_tracking_data_of_expect = bet_flow.default_tracking_data_of_expect('double_tracking')
        bet_flow.input_multiples_of_tracing_value()
        expect_tracking_data_of_current = bet_flow.expect_tracking_data_of_current()
        expect_tracking_data = bet_flow.expect_tracking_data('double_tracking')

        bet_flow.click_payment("tracing_bet")
        order_info_confirm = bet_flow.check_order_info()
        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_tracing_order_done()

        expect_data = [self.game_name, "", "0.30", OrderInfoTrace_Yes, "1", "1"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)
        self.assertEqual([default_tracking_data_of_expect, expect_tracking_data],
                         [default_tracking_data_of_current, expect_tracking_data_of_current])

    def test_08_Tg60_pro_normal_dingweidan_smart_tracking(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "dingweidan")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.bet_tracing()

        bet_flow.click_tracing_category("smart_tracking", "4")
        OrderInfoTrace_Yes = bet_flow.OrderInfoTrace_Yes("4")
        default_tracking_data_of_current = bet_flow.default_tracking_data_of_current()
        default_tracking_data_of_expect = bet_flow.default_tracking_data_of_expect('smart_tracking')
        bet_flow.input_multiples_of_tracing_value()
        expect_tracking_data_of_current = bet_flow.expect_tracking_data_of_current()
        expect_tracking_data = bet_flow.expect_tracking_data('smart_tracking')

        bet_flow.click_payment("tracing_bet")
        order_info_confirm = bet_flow.check_order_info()
        bet_flow.click_order_confirm()
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
