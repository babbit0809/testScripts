import unittest
from config.SetUIConfig import Driver
from test_UI.common.GamePageCommon import GamePageCommon
from test_UI.page.LoginPage import LoginPage
from test_UI.page.HomePage import HomePage
from test_UI.page.GamePage import GamePage
from test_UI.page.GamePageSSC import GamePageSSC
from utils import Assertion, Localization


class CAJC_Pro(unittest.TestCase):  # 台灣時時彩 QAT/STG環境任選主玩法為關閉

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver
        login_page = LoginPage(cls.driver)
        login_page.execute_login()

        home_page = HomePage(cls.driver)
        home_page.switch_category("game")

        game_page = GamePage(cls.driver)
        cls.game_name = game_page.switch_game("SSC", "cajc")
        cls.OrderInfoTrace_No = Localization.get_loc("GamePage_Common", 'OrderInfoTrace_No')

    def test_01_CAJC_pro_normal_fiveStar_fiveStarDirectSelection(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "fiveStar", "fiveStarDirectSelection")
        page_ssc.bet_pro_all("fiveStar", "fiveStarDirectSelection")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "2,000.00", self.OrderInfoTrace_No, "1", "100000"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_02_CAJC_pro_normal_fiveStar_fiveStarOrder(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "fiveStar", "fiveStarOrder")
        page_ssc.bet_pro_all("fiveStar", "fiveStarOrder", betting_number="12345,12346;12347*12348")

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

    def test_03_CAJC_pro_normal_fiveStar_selection120(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "fiveStar", "selection120")
        page_ssc.bet_pro_all("fiveStar", "selection120")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "5.04", self.OrderInfoTrace_No, "1", "252"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_04_CAJC_pro_normal_fiveStar_selection60(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "fiveStar", "selection60")
        page_ssc.bet_pro_all("fiveStar", "selection60")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "16.80", self.OrderInfoTrace_No, "1", "840"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_05_CAJC_pro_normal_fiveStar_selection30(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "fiveStar", "selection30")
        page_ssc.bet_pro_all("fiveStar", "selection30")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "7.20", self.OrderInfoTrace_No, "1", "360"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_06_CAJC_pro_normal_fiveStar_selection20(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "fiveStar", "selection20")
        page_ssc.bet_pro_all("fiveStar", "selection20")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "7.20", self.OrderInfoTrace_No, "1", "360"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_07_CAJC_pro_normal_fiveStar_selection10(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "fiveStar", "selection10")
        page_ssc.bet_pro_all("fiveStar", "selection10")

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

    def test_08_CAJC_pro_normal_fiveStar_selection5(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "fiveStar", "selection5")
        page_ssc.bet_pro_all("fiveStar", "selection5")

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

    def test_09_CAJC_pro_normal_threeStar_front3Choice(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "threeStar", "front3Choice")
        page_ssc.bet_pro_all("threeStar", "front3Choice")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "20.00", self.OrderInfoTrace_No, "1", "1000"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_10_CAJC_pro_normal_threeStar_front3Order(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "threeStar", "front3Order")
        page_ssc.bet_pro_all("threeStar", "front3Order", betting_number="123,124;125*126")

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

    def test_11_CAJC_pro_normal_threeStar_middle3Choice(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "threeStar", "middle3Choice")
        page_ssc.bet_pro_all("threeStar", "middle3Choice")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "20.00", self.OrderInfoTrace_No, "1", "1000"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_12_CAJC_pro_normal_threeStar_middle3Order(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "threeStar", "middle3Order")
        page_ssc.bet_pro_all("threeStar", "middle3Order", betting_number="123,124;125*126")

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

    def test_13_CAJC_pro_normal_threeStar_back3Choice(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "threeStar", "back3Choice")
        page_ssc.bet_pro_all("threeStar", "back3Choice")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "20.00", self.OrderInfoTrace_No, "1", "1000"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_14_CAJC_pro_normal_threeStar_back3Order(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "threeStar", "back3Order")
        page_ssc.bet_pro_all("threeStar", "back3Order", betting_number="123,124;125*126")

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

    def test_15_CAJC_pro_normal_threeStar_front3Mix(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "threeStar", "front3Mix")
        page_ssc.bet_pro_all("threeStar", "front3Mix", betting_number="123,124;125*126")

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

    def test_16_CAJC_pro_normal_threeStar_middle3Mix(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "threeStar", "middle3Mix")
        page_ssc.bet_pro_all("threeStar", "middle3Mix", betting_number="123,124;125*126")

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

    def test_17_CAJC_pro_normal_threeStar_back3Mix(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "threeStar", "back3Mix")
        page_ssc.bet_pro_all("threeStar", "back3Mix", betting_number="123,124;125*126")

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

    def test_18_CAJC_pro_normal_threeStarGroup3_front3Group3(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "threeStarGroup3", "front3Group3")
        page_ssc.bet_pro_all("threeStarGroup3", "front3Group3")

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

    def test_19_CAJC_pro_normal_threeStarGroup3_middle3Group3(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "threeStarGroup3", "middle3Group3")
        page_ssc.bet_pro_all("threeStarGroup3", "middle3Group3")

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

    def test_20_CAJC_pro_normal_threeStarGroup3_back3Group3(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "threeStarGroup3", "back3Group3")
        page_ssc.bet_pro_all("threeStarGroup3", "back3Group3")

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

    def test_21_CAJC_pro_normal_threeStarGroup6_front3Group6(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "threeStarGroup6", "front3Group6")
        page_ssc.bet_pro_all("threeStarGroup6", "front3Group6")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "2.40", self.OrderInfoTrace_No, "1", "120"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_22_CAJC_pro_normal_threeStarGroup6_middle3Group6(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "threeStarGroup6", "middle3Group6")
        page_ssc.bet_pro_all("threeStarGroup6", "middle3Group6")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "2.40", self.OrderInfoTrace_No, "1", "120"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_23_CAJC_pro_normal_threeStarGroup6_back3Group6(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "threeStarGroup6", "back3Group6")
        page_ssc.bet_pro_all("threeStarGroup6", "back3Group6")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "2.40", self.OrderInfoTrace_No, "1", "120"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_24_CAJC_pro_normal_twoStar_frontDirect(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "twoStar", "frontDirect")
        page_ssc.bet_pro_all("twoStar", "frontDirect")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "2.00", self.OrderInfoTrace_No, "1", "100"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_25_CAJC_pro_normal_twoStar_frontGroup(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "twoStar", "frontGroup")
        page_ssc.bet_pro_all("twoStar", "frontGroup")

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

    def test_26_CAJC_pro_normal_twoStar_frontOrder(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "twoStar", "frontOrder")
        page_ssc.bet_pro_all("twoStar", "frontOrder", betting_number="12,13;14*15")

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

    def test_27_CAJC_pro_normal_twoStar_backDirect(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "twoStar", "backDirect")
        page_ssc.bet_pro_all("twoStar", "backDirect")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "2.00", self.OrderInfoTrace_No, "1", "100"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_28_CAJC_pro_normal_twoStar_backGroup(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "twoStar", "backGroup")
        page_ssc.bet_pro_all("twoStar", "backGroup")

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

    def test_29_CAJC_pro_normal_twoStar_backOrder(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "twoStar", "backOrder")
        page_ssc.bet_pro_all("twoStar", "backOrder", betting_number="12,13;14*15")

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

    def test_30_CAJC_pro_normal_dingweidan(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "dingweidan")
        page_ssc.bet_pro_all("dingweidan")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "1.00", self.OrderInfoTrace_No, "1", "50"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_31_CAJC_pro_normal_budingweidan_front3(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "budingweidan", "front3")
        page_ssc.bet_pro_all("budingweidan", "front3")

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

    def test_32_CAJC_pro_normal_budingweidan_middle3(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "budingweidan", "middle3")
        page_ssc.bet_pro_all("budingweidan", "middle3")

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

    def test_33_CAJC_pro_normal_budingweidan_back3(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "budingweidan", "back3")
        page_ssc.bet_pro_all("budingweidan", "back3")

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

    def test_34_CAJC_pro_normal_bigSmallOddEven(self):
        page_ssc = GamePageSSC(self.driver)
        page_ssc.switch_pro_game("normal", "bigSmallOddEven")
        page_ssc.bet_pro_all("bigSmallOddEven")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.32", self.OrderInfoTrace_No, "1", "16"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    @classmethod
    def tearDownClass(cls):
        cls.driver = Driver
        bet_flow = GamePageCommon(cls.driver)
        bet_flow.back_to_homepage()
        bet_flow.check_homepage_showing()


if __name__ == '__main__':
    unittest.main()
