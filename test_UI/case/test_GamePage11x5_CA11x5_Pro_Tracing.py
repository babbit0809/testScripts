import unittest
from config.SetUIConfig import Driver, Target
from test_UI.common.GamePageCommon import GamePageCommon
from test_UI.page.LoginPage import LoginPage
from test_UI.page.HomePage import HomePage
from test_UI.page.GamePage import GamePage
from test_UI.page.GamePage11x5 import GamePage11x5
from utils import Assertion


@unittest.skipUnless(Target == 'web', '此測項為web使用')
class CA11x5_Pro_Tracing(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver
        login_page = LoginPage(cls.driver)
        login_page.execute_login()

        home_page = HomePage(cls.driver)
        home_page.switch_category("game")

        game_page = GamePage(cls.driver)
        cls.game_name = game_page.switch_game("11x5", "ca11x5")

    def test_01_CA11x5_pro_normal_r2_standard_double_tracking(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "r2", "standard")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        page_11x5.click_random_button()

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

    def test_02_CA11x5_pro_normal_r2_standard_smart_tracking(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "r2", "standard")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        page_11x5.click_random_button()

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

    def test_03_CA11x5_pro_normal_r3_standard_double_tracking(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "r3", "standard")
        page_11x5.bet_pro_all("r3", "standard")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        page_11x5.click_random_button()

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

    def test_04_CA11x5_pro_normal_r3_standard_smart_tracking(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "r3", "standard")
        page_11x5.bet_pro_all("r3", "standard")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        page_11x5.click_random_button()

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

    def test_05_CA11x5_pro_normal_r4_standard_double_tracking(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "r4", "standard")
        page_11x5.bet_pro_all("r4", "standard")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        page_11x5.click_random_button()

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

    def test_06_CA11x5_pro_normal_r4_standard_smart_tracking(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "r4", "standard")
        page_11x5.bet_pro_all("r4", "standard")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        page_11x5.click_random_button()

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

    def test_07_CA11x5_pro_normal_r5_standard_double_tracking(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "r5", "standard")
        page_11x5.bet_pro_all("r5", "standard")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        page_11x5.click_random_button()

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

    def test_08_CA11x5_pro_normal_r5_standard_smart_tracking(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "r5", "standard")
        page_11x5.bet_pro_all("r5", "standard")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        page_11x5.click_random_button()

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

    def test_09_CA11x5_pro_normal_r6_standard_double_tracking(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "r6", "standard")
        page_11x5.bet_pro_all("r6", "standard")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        page_11x5.click_random_button()

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

    def test_10_CA11x5_pro_normal_r6_standard_smart_tracking(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "r6", "standard")
        page_11x5.bet_pro_all("r6", "standard")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        page_11x5.click_random_button()

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

    def test_11_CA11x5_pro_normal_r7_standard_double_tracking(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "r7", "standard")
        page_11x5.bet_pro_all("r7", "standard")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        page_11x5.click_random_button()

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

    def test_12_CA11x5_pro_normal_r7_standard_smart_tracking(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "r7", "standard")
        page_11x5.bet_pro_all("r7", "standard")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        page_11x5.click_random_button()

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

    def test_13_CA11x5_pro_normal_r8_standard_double_tracking(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "r8", "standard")
        page_11x5.bet_pro_all("r8", "standard")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        page_11x5.click_random_button()

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

    def test_14_CA11x5_pro_normal_r8_standard_smart_tracking(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "r8", "standard")
        page_11x5.bet_pro_all("r8", "standard")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        page_11x5.click_random_button()

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

    def test_15_CA11x5_pro_normal_front1_directStandard_double_tracking(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "front1", "directStandard")
        page_11x5.bet_pro_all("front1", "directStandard")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        page_11x5.click_random_button()

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

    def test_16_CA11x5_pro_normal_front1_directStandard_smart_tracking(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "front1", "directStandard")
        page_11x5.bet_pro_all("front1", "directStandard")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        page_11x5.click_random_button()

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

    def test_17_CA11x5_pro_normal_front2_directStandard_double_tracking(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "front2", "directStandard")
        page_11x5.bet_pro_all("front2", "directStandard")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        page_11x5.click_random_button()

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

    def test_18_CA11x5_pro_normal_front2_directStandard_smart_tracking(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "front2", "directStandard")
        page_11x5.bet_pro_all("front2", "directStandard")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        page_11x5.click_random_button()

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

    def test_19_CA11x5_pro_normal_front3_directStandard_double_tracking(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "front3", "directStandard")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        page_11x5.click_random_button()

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

    def test_20_CA11x5_pro_normal_front3_directStandard_smart_tracking(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "front3", "directStandard")
        page_11x5.bet_pro_all("front3", "directStandard")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        page_11x5.click_random_button()

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
