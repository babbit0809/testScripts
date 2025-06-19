import unittest
from config.SetUIConfig import Driver
from test_UI.common.GamePageCommon import GamePageCommon
from test_UI.page.LoginPage import LoginPage
from test_UI.page.HomePage import HomePage
from test_UI.page.GamePage import GamePage
from test_UI.page.GamePageSSC import GamePageSSC
from utils import Assertion, Localization


class BTCFFC_TwoSide(unittest.TestCase):  # 比特幣分分彩 QAT/STG環境任選主玩法為關閉

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver
        login_page = LoginPage(cls.driver)
        login_page.execute_login()

        home_page = HomePage(cls.driver)
        home_page.switch_category("game")

        game_page = GamePage(cls.driver)
        cls.game_name = game_page.switch_game("SSC", "btcffc")
        cls.OrderInfoTrace_No = Localization.get_loc("GamePage_Common", 'OrderInfoTrace_No')

    def test_44_BTCFFC_twoSide_firstBall(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_twoSide_game("firstBall")
        page_ssc.bet_twoSide_all("firstBall")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_twoSide_bet_setting("2")

        bet_flow.click_payment("twoSide")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "28.00", self.OrderInfoTrace_No, "1", "14"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_45_BTCFFC_twoSide_secondBall(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_twoSide_game("secondBall")
        page_ssc.bet_twoSide_all("secondBall")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_twoSide_bet_setting("2")

        bet_flow.click_payment("twoSide")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "28.00", self.OrderInfoTrace_No, "1", "14"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_46_BTCFFC_twoSide_thirdBall(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_twoSide_game("thirdBall")
        page_ssc.bet_twoSide_all("thirdBall")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_twoSide_bet_setting("2")

        bet_flow.click_payment("twoSide")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "28.00", self.OrderInfoTrace_No, "1", "14"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_47_BTCFFC_twoSide_fourthBall(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_twoSide_game("fourthBall")
        page_ssc.bet_twoSide_all("fourthBall")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_twoSide_bet_setting("2")

        bet_flow.click_payment("twoSide")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "28.00", self.OrderInfoTrace_No, "1", "14"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_48_BTCFFC_twoSide_fifthBall(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_twoSide_game("fifthBall")
        page_ssc.bet_twoSide_all("fifthBall")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_twoSide_bet_setting("2")

        bet_flow.click_payment("twoSide")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "28.00", self.OrderInfoTrace_No, "1", "14"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_49_BTCFFC_twoSide_total(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_twoSide_game("total")
        page_ssc.bet_twoSide_all("total")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_twoSide_bet_setting("2")

        bet_flow.click_payment("twoSide")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "8.00", self.OrderInfoTrace_No, "1", "4"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_50_BTCFFC_twoSide_front3(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_twoSide_game("front3")
        page_ssc.bet_twoSide_all("front3")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_twoSide_bet_setting("2")

        bet_flow.click_payment("twoSide")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "10.00", self.OrderInfoTrace_No, "1", "5"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_51_BTCFFC_twoSide_middle3(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_twoSide_game("middle3")
        page_ssc.bet_twoSide_all("middle3")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_twoSide_bet_setting("2")

        bet_flow.click_payment("twoSide")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "10.00", self.OrderInfoTrace_No, "1", "5"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_52_BTCFFC_twoSide_back3(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_twoSide_game("back3")
        page_ssc.bet_twoSide_all("back3")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_twoSide_bet_setting("2")

        bet_flow.click_payment("twoSide")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "10.00", self.OrderInfoTrace_No, "1", "5"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_53_BTCFFC_twoSide_dragon(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_twoSide_game("dragon")
        page_ssc.bet_twoSide_all("dragon")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_twoSide_bet_setting("2")

        bet_flow.click_payment("twoSide")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "20.00", self.OrderInfoTrace_No, "1", "10"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_54_BTCFFC_twoSide_tiger(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_twoSide_game("tiger")
        page_ssc.bet_twoSide_all("tiger")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_twoSide_bet_setting("2")

        bet_flow.click_payment("twoSide")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "20.00", self.OrderInfoTrace_No, "1", "10"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_55_BTCFFC_twoSide_equal(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_twoSide_game("equal")
        page_ssc.bet_twoSide_all("equal")

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
