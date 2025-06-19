import unittest
from config.SetUIConfig import Driver
from test_UI.common.GamePageCommon import GamePageCommon
from test_UI.page.LoginPage import LoginPage
from test_UI.page.HomePage import HomePage
from test_UI.page.GamePage import GamePage
from test_UI.page.GamePagePK10 import GamePagePK10
from utils import Assertion, Localization


class CARacing_Pro(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver
        login_page = LoginPage(cls.driver)
        login_page.execute_login()

        home_page = HomePage(cls.driver)
        home_page.switch_category("game")

        game_page = GamePage(cls.driver)
        cls.game_name = game_page.switch_game("PK10", "caracing")
        cls.OrderInfoTrace_No = Localization.get_loc("GamePage_Common", 'OrderInfoTrace_No')

    def test_01_CARacing_pro_normal_guess1(self):
        page_pk10 = GamePagePK10(self.driver)
        page_pk10.switch_pro_game("normal", "guess1")
        page_pk10.bet_pro_all("guess1")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.20", self.OrderInfoTrace_No, "1", "10"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_02_CARacing_pro_normal_guess12(self):
        page_pk10 = GamePagePK10(self.driver)
        page_pk10.switch_pro_game("normal", "guess12")
        page_pk10.bet_pro_all("guess12")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "1.80", self.OrderInfoTrace_No, "1", "90"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_03_CARacing_pro_normal_guess123(self):
        page_pk10 = GamePagePK10(self.driver)
        page_pk10.switch_pro_game("normal", "guess123")
        page_pk10.bet_pro_all("guess123")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "14.40", self.OrderInfoTrace_No, "1", "720"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_04_CARacing_pro_normal_firstToTenth(self):
        page_pk10 = GamePagePK10(self.driver)
        page_pk10.switch_pro_game("normal", "firstToTenth")
        page_pk10.bet_pro_all("firstToTenth")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "2.00", self.OrderInfoTrace_No, "10", "100"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_05_CARacing_pro_fun_eat1(self):
        page_pk10 = GamePagePK10(self.driver)
        page_pk10.switch_pro_game("fun", "eat1")
        page_pk10.bet_pro_all("eat1")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.20", self.OrderInfoTrace_No, "1", "10"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_06_CARacing_pro_fun_bet3(self):
        page_pk10 = GamePagePK10(self.driver)
        page_pk10.switch_pro_game("fun", "bet3")
        page_pk10.bet_pro_all("bet3")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.20", self.OrderInfoTrace_No, "1", "10"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_07_CARacing_pro_fun_eat3(self):
        page_pk10 = GamePagePK10(self.driver)
        page_pk10.switch_pro_game("fun", "eat3")
        page_pk10.bet_pro_all("eat3")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.20", self.OrderInfoTrace_No, "1", "10"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_08_CARacing_pro_fun_positionQ(self):
        page_pk10 = GamePagePK10(self.driver)
        page_pk10.switch_pro_game("fun", "positionQ")
        page_pk10.bet_pro_all("positionQ")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.90", self.OrderInfoTrace_No, "1", "45"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_09_CARacing_pro_fun_winningStreak(self):
        page_pk10 = GamePagePK10(self.driver)
        page_pk10.switch_pro_game("fun", "winningStreak")
        page_pk10.bet_pro_all("winningStreak")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.90", self.OrderInfoTrace_No, "1", "45"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    @classmethod
    def tearDownClass(cls):
        cls.driver = Driver
        bet_flow = GamePageCommon(cls.driver)
        bet_flow.back_to_homepage()
        bet_flow.check_homepage_showing()


if __name__ == '__main__':
    unittest.main()
