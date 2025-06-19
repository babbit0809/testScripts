import unittest
from config.SetUIConfig import Driver
from test_UI.common.GamePageCommon import GamePageCommon
from test_UI.page.LoginPage import LoginPage
from test_UI.page.HomePage import HomePage
from test_UI.page.GamePage import GamePage
from test_UI.page.GamePage11x5 import GamePage11x5
from utils import Assertion, Localization


class TW11x5_Pro(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver
        login_page = LoginPage(cls.driver)
        login_page.execute_login()

        home_page = HomePage(cls.driver)
        home_page.switch_category("game")

        game_page = GamePage(cls.driver)
        cls.game_name = game_page.switch_game("11x5", "tw11x5")
        cls.OrderInfoTrace_No = Localization.get_loc("GamePage_Common", 'OrderInfoTrace_No')

    def test_01_TW11x5_pro_normal_r2_standard(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "r2", "standard")
        page_11x5.bet_pro_all("r2", "standard")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "1.10", self.OrderInfoTrace_No, "1", "55"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_02_TW11x5_pro_normal_r2_order(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "r2", "order")
        page_11x5.bet_pro_all("r2", "order", bet_number="0102,0103;0104*0105")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.08", self.OrderInfoTrace_No, "1", "4"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_03_TW11x5_pro_normal_r3_standard(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "r3", "standard")
        page_11x5.bet_pro_all("r3", "standard")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "3.30", self.OrderInfoTrace_No, "1", "165"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_04_TW11x5_pro_normal_r3_order(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "r3", "order")
        page_11x5.bet_pro_all("r3", "order", bet_number="010203,010204;010205*010206")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.08", self.OrderInfoTrace_No, "1", "4"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_05_TW11x5_pro_normal_r4_standard(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "r4", "standard")
        page_11x5.bet_pro_all("r4", "standard")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "6.60", self.OrderInfoTrace_No, "1", "330"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_06_TW11x5_pro_normal_r4_order(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "r4", "order")
        page_11x5.bet_pro_all("r4", "order", bet_number="01020304,01020305;01020306*01020307")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.08", self.OrderInfoTrace_No, "1", "4"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_07_TW11x5_pro_normal_r5_standard(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "r5", "standard")
        page_11x5.bet_pro_all("r5", "standard")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "9.24", self.OrderInfoTrace_No, "1", "462"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_08_TW11x5_pro_normal_r5_order(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "r5", "order")
        page_11x5.bet_pro_all("r5", "order", bet_number="0102030405,0102030406;0102030407*0102030408")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.08", self.OrderInfoTrace_No, "1", "4"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_09_TW11x5_pro_normal_r6_standard(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "r6", "standard")
        page_11x5.bet_pro_all("r6", "standard")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "9.24", self.OrderInfoTrace_No, "1", "462"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_10_TW11x5_pro_normal_r6_order(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "r6", "order")
        page_11x5.bet_pro_all("r6", "order", bet_number="010203040506,010203040507;010203040508*010203040509")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.08", self.OrderInfoTrace_No, "1", "4"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_11_TW11x5_pro_normal_r7_standard(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "r7", "standard")
        page_11x5.bet_pro_all("r7", "standard")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "6.60", self.OrderInfoTrace_No, "1", "330"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_12_TW11x5_pro_normal_r7_order(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "r7", "order")
        page_11x5.bet_pro_all("r7", "order", bet_number="01020304050607,01020304050608;01020304050609*01020304050610")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.08", self.OrderInfoTrace_No, "1", "4"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_13_TW11x5_pro_normal_r8_standard(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "r8", "standard")
        page_11x5.bet_pro_all("r8", "standard")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "3.30", self.OrderInfoTrace_No, "1", "165"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_14_TW11x5_pro_normal_r8_order(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "r8", "order")
        page_11x5.bet_pro_all("r8", "order", bet_number="0102030405060708,0102030405060709;0102030405060710*0102030405060711")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.08", self.OrderInfoTrace_No, "1", "4"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_15_TW11x5_pro_normal_front1_directStandard(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "front1", "directStandard")
        page_11x5.bet_pro_all("front1", "directStandard")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.22", self.OrderInfoTrace_No, "1", "11"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_16_TW11x5_pro_normal_front1_directOrder(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "front1", "directOrder")
        page_11x5.bet_pro_all("front1", "directOrder", bet_number="01,02;03*04")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.08", self.OrderInfoTrace_No, "1", "4"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_17_TW11x5_pro_normal_front2_directStandard(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "front2", "directStandard")
        page_11x5.bet_pro_all("front2", "directStandard")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "2.20", self.OrderInfoTrace_No, "1", "110"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_18_TW11x5_pro_normal_front2_groupSelect(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "front2", "groupSelect")
        page_11x5.bet_pro_all("front2", "groupSelect")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "1.10", self.OrderInfoTrace_No, "1", "55"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_19_TW11x5_pro_normal_front2_directOrder(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "front2", "front2_directOrder")
        page_11x5.bet_pro_all("front2", "directOrder", bet_number="0102,0103;0104*0105")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.08", self.OrderInfoTrace_No, "1", "4"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_20_TW11x5_pro_normal_front3_directStandard(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "front3", "directStandard")
        page_11x5.bet_pro_all("front3", "directStandard")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "19.80", self.OrderInfoTrace_No, "1", "990"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_21_TW11x5_pro_normal_front3_groupSelect(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "front3", "groupSelect")
        page_11x5.bet_pro_all("front3", "groupSelect")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "3.30", self.OrderInfoTrace_No, "1", "165"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_22_TW11x5_pro_normal_front3_directOrder(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("normal", "front3", "front3_directOrder")
        page_11x5.bet_pro_all("front3", "directOrder", bet_number="010203,010204;010205*010206")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.08", self.OrderInfoTrace_No, "1", "4"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_23_TW11x5_pro_fun_sum_front3(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("fun", "sum", "front3")
        page_11x5.bet_pro_all("sum", "front3")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.58", self.OrderInfoTrace_No, "29", "29"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_24_TW11x5_pro_fun_sum_middle3(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("fun", "sum", "middle3")
        page_11x5.bet_pro_all("sum", "middle3")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.58", self.OrderInfoTrace_No, "29", "29"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_25_TW11x5_pro_fun_sum_back3(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("fun", "sum", "back3")
        page_11x5.bet_pro_all("sum", "back3")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.58", self.OrderInfoTrace_No, "29", "29"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_26_TW11x5_pro_fun_sum_front2(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("fun", "sum", "front2")
        page_11x5.bet_pro_all("sum", "front2")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.46", self.OrderInfoTrace_No, "23", "23"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_27_TW11x5_pro_fun_sum_back2(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("fun", "sum", "back2")
        page_11x5.bet_pro_all("sum", "back2")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.46", self.OrderInfoTrace_No, "23", "23"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_28_TW11x5_pro_fun_crossDegree_all5(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("fun", "crossDegree", "all5")
        page_11x5.bet_pro_all("crossDegree", "all5")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.22", self.OrderInfoTrace_No, "11", "11"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_29_TW11x5_pro_fun_crossDegree_front3(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("fun", "crossDegree", "crossDegree_front3")
        page_11x5.bet_pro_all("crossDegree", "front3")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.26", self.OrderInfoTrace_No, "13", "13"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_30_TW11x5_pro_fun_crossDegree_middle3(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("fun", "crossDegree", "crossDegree_middle3")
        page_11x5.bet_pro_all("crossDegree", "middle3")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.26", self.OrderInfoTrace_No, "13", "13"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_31_TW11x5_pro_fun_crossDegree_back3(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("fun", "crossDegree", "crossDegree_back3")
        page_11x5.bet_pro_all("crossDegree", "back3")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.26", self.OrderInfoTrace_No, "13", "13"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_32_TW11x5_pro_fun_cowcow(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("fun", "cowcow")
        page_11x5.bet_pro_all("cowcow")

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

    def test_33_TW11x5_pro_fun_cardPoint_front3(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("fun", "cardPoint", "front3")
        page_11x5.bet_pro_all("cardPoint", "front3")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.28", self.OrderInfoTrace_No, "14", "14"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_34_TW11x5_pro_fun_cardPoint_middle3(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("fun", "cardPoint", "middle3")
        page_11x5.bet_pro_all("cardPoint", "middle3")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.28", self.OrderInfoTrace_No, "14", "14"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_35_TW11x5_pro_fun_cardPoint_back3(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("fun", "cardPoint", "back3")
        page_11x5.bet_pro_all("cardPoint", "back3")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.28", self.OrderInfoTrace_No, "14", "14"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_36_TW11x5_pro_fun_dragonTiger_all5(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("fun", "dragonTiger", "all5")
        page_11x5.bet_pro_all("dragonTiger", "all5")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.04", self.OrderInfoTrace_No, "1", "2"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_37_TW11x5_pro_fun_dragonTiger_front3(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("fun", "dragonTiger", "dragonTiger_front3")
        page_11x5.bet_pro_all("dragonTiger", "front3")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.04", self.OrderInfoTrace_No, "1", "2"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_38_TW11x5_pro_fun_dragonTiger_middle3(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("fun", "dragonTiger", "dragonTiger_middle3")
        page_11x5.bet_pro_all("dragonTiger", "middle3")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.04", self.OrderInfoTrace_No, "1", "2"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_39_TW11x5_pro_fun_dragonTiger_back3(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("fun", "dragonTiger", "dragonTiger_back3")
        page_11x5.bet_pro_all("dragonTiger", "back3")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.04", self.OrderInfoTrace_No, "1", "2"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_40_TW11x5_pro_fun_dragonTiger_front2(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("fun", "dragonTiger", "dragonTiger_front2")
        page_11x5.bet_pro_all("dragonTiger", "front2")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.04", self.OrderInfoTrace_No, "1", "2"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_41_TW11x5_pro_fun_dragonTiger_back2(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("fun", "dragonTiger", "dragonTiger_back2")
        page_11x5.bet_pro_all("dragonTiger", "back2")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.04", self.OrderInfoTrace_No, "1", "2"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_42_TW11x5_pro_fun_alwaysGuess(self):
        page_11x5 = GamePage11x5(self.driver)
        page_11x5.switch_pro_game("fun", "alwaysGuess")
        page_11x5.bet_pro_all("alwaysGuess")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.22", self.OrderInfoTrace_No, "1", "11"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    @classmethod
    def tearDownClass(cls):
        cls.driver = Driver
        bet_flow = GamePageCommon(cls.driver)
        bet_flow.back_to_homepage()
        bet_flow.check_homepage_showing()


if __name__ == '__main__':
    unittest.main()
