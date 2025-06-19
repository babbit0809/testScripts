import unittest
from config.SetUIConfig import Driver
from test_UI.common.GamePageCommon import GamePageCommon
from test_UI.page.LoginPage import LoginPage
from test_UI.page.HomePage import HomePage
from test_UI.page.GamePage import GamePage
from test_UI.page.GamePageMarkSix import GamePageMarkSix
from utils import Assertion, Localization


class Mark6(unittest.TestCase):  # 六合彩沒有分官方盤/雙面盤(亦無常規/趣味之分)
    # 2020/02/20: 營運關閉下列子玩法-連碼/不中/六肖/連肖/連尾
    @classmethod
    def setUpClass(cls):
        cls.driver = Driver
        login_page = LoginPage(cls.driver)
        login_page.execute_login()

        home_page = HomePage(cls.driver)
        home_page.switch_category("game")

        game_page = GamePage(cls.driver)
        cls.game_name = game_page.switch_game("MarkSix", "mark6")
        cls.OrderInfoTrace_No = Localization.get_loc("GamePage_Common", 'OrderInfoTrace_No')

    def test_01_Mark6_pro_normal_specialNo(self):
        page_markSix = GamePageMarkSix(self.driver)
        page_markSix.switch_pro_game("specialNo")
        page_markSix.bet_pro_all("specialNo")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "1.34", self.OrderInfoTrace_No, "19", "67"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_02_Mark6_pro_normal_mainNo(self):
        page_markSix = GamePageMarkSix(self.driver)
        page_markSix.switch_pro_game("mainNo")
        page_markSix.bet_pro_all("mainNo")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "1.14", self.OrderInfoTrace_No, "9", "57"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_03_Mark6_pro_normal_main1to6_main1st(self):
        page_markSix = GamePageMarkSix(self.driver)
        page_markSix.switch_pro_game("main1to6", "main1st")
        page_markSix.bet_pro_all("main1to6", "main1st")

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

    def test_04_Mark6_pro_normal_main1to6_main2nd(self):
        page_markSix = GamePageMarkSix(self.driver)
        page_markSix.switch_pro_game("main1to6", "main2nd")
        page_markSix.bet_pro_all("main1to6", "main2nd")

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

    def test_05_Mark6_pro_normal_main1to6_main3rd(self):
        page_markSix = GamePageMarkSix(self.driver)
        page_markSix.switch_pro_game("main1to6", "main3rd")
        page_markSix.bet_pro_all("main1to6", "main3rd")

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

    def test_06_Mark6_pro_normal_main1to6_main4th(self):
        page_markSix = GamePageMarkSix(self.driver)
        page_markSix.switch_pro_game("main1to6", "main4th")
        page_markSix.bet_pro_all("main1to6", "main4th")

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

    def test_07_Mark6_pro_normal_main1to6_main5th(self):
        page_markSix = GamePageMarkSix(self.driver)
        page_markSix.switch_pro_game("main1to6", "main5th")
        page_markSix.bet_pro_all("main1to6", "main5th")

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

    def test_08_Mark6_pro_normal_main1to6_main6th(self):
        page_markSix = GamePageMarkSix(self.driver)
        page_markSix.switch_pro_game("main1to6", "main6th")
        page_markSix.bet_pro_all("main1to6", "main6th")

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

    def test_09_Mark6_pro_normal_mainSpecial_main1Special(self):
        page_markSix = GamePageMarkSix(self.driver)
        page_markSix.switch_pro_game("mainSpecial", "main1Special")
        page_markSix.bet_pro_all("mainSpecial", "main1Special")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "1.20", self.OrderInfoTrace_No, "12", "60"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_10_Mark6_pro_normal_mainSpecial_main2Special(self):
        page_markSix = GamePageMarkSix(self.driver)
        page_markSix.switch_pro_game("mainSpecial", "main2Special")
        page_markSix.bet_pro_all("mainSpecial", "main2Special")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "1.20", self.OrderInfoTrace_No, "12", "60"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_11_Mark6_pro_normal_mainSpecial_main3Special(self):
        page_markSix = GamePageMarkSix(self.driver)
        page_markSix.switch_pro_game("mainSpecial", "main3Special")
        page_markSix.bet_pro_all("mainSpecial", "main3Special")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "1.20", self.OrderInfoTrace_No, "12", "60"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_12_Mark6_pro_normal_mainSpecial_main4Special(self):
        page_markSix = GamePageMarkSix(self.driver)
        page_markSix.switch_pro_game("mainSpecial", "main4Special")
        page_markSix.bet_pro_all("mainSpecial", "main4Special")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "1.20", self.OrderInfoTrace_No, "12", "60"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_13_Mark6_pro_normal_mainSpecial_main5Special(self):
        page_markSix = GamePageMarkSix(self.driver)
        page_markSix.switch_pro_game("mainSpecial", "main5Special")
        page_markSix.bet_pro_all("mainSpecial", "main5Special")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "1.20", self.OrderInfoTrace_No, "12", "60"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_14_Mark6_pro_normal_mainSpecial_main6Special(self):
        page_markSix = GamePageMarkSix(self.driver)
        page_markSix.switch_pro_game("mainSpecial", "main6Special")
        page_markSix.bet_pro_all("mainSpecial", "main6Special")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "1.20", self.OrderInfoTrace_No, "12", "60"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    # def test_15_Mark6_pro_normal_multiNo_bet3Winning3(self):
    #     bet_case = (
    #         # A tuple of (params_value, subTest_description)
    #         ("multiNoCase1", "1-10"),
    #         ("multiNoCase2", "11-20"),
    #         ("multiNoCase3", "21-30"),
    #         ("multiNoCase4", "31-40"),
    #         ("multiNoCase5", "40-49")
    #     )
    #
    #     for params_value, subTest_description in bet_case:
    #         with self.subTest(subTest_description):
    #             page_markSix = GamePageMarkSix(self.driver)
    #             page_markSix.switch_pro_game("multiNo", "bet3Winning3")
    #             page_markSix.bet_pro_all("multiNo", "bet3Winning3", params_value)
    #
    #             bet_flow = GamePageCommon(self.driver)
    #             bet_flow.set_pro_bet_setting("cent")
    #             bet_flow.click_bet_basket()
    #
    #             bet_flow.click_payment("pro")
    #             order_info_confirm = bet_flow.check_order_info()
    #
    #             bet_flow.click_order_confirm()
    #             order_info_done = bet_flow.check_order_info()
    #             bet_flow.click_order_done()
    #
    #             expect_data = [self.game_name, "", "2.40", self.OrderInfoTrace_No, "1", "120"]
    #             Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)
    #
    # def test_16_Mark6_pro_normal_multiNo_bet3Winning2(self):
    #     bet_case = (
    #         # A tuple of (params_value, subTest_description)
    #         ("multiNoCase1", "1-10"),
    #         ("multiNoCase2", "11-20"),
    #         ("multiNoCase3", "21-30"),
    #         ("multiNoCase4", "31-40"),
    #         ("multiNoCase5", "40-49")
    #     )
    #
    #     for params_value, subTest_description in bet_case:
    #         with self.subTest(subTest_description):
    #             page_markSix = GamePageMarkSix(self.driver)
    #             page_markSix.switch_pro_game("multiNo", "bet3Winning2")
    #             page_markSix.bet_pro_all("multiNo", "bet3Winning2", params_value)
    #
    #             bet_flow = GamePageCommon(self.driver)
    #             bet_flow.set_pro_bet_setting("cent")
    #             bet_flow.click_bet_basket()
    #
    #             bet_flow.click_payment("pro")
    #             order_info_confirm = bet_flow.check_order_info()
    #
    #             bet_flow.click_order_confirm()
    #             order_info_done = bet_flow.check_order_info()
    #             bet_flow.click_order_done()
    #
    #             expect_data = [self.game_name, "", "2.40", self.OrderInfoTrace_No, "1", "120"]
    #             Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)
    #
    # def test_17_Mark6_pro_normal_multiNo_bet2Winning2(self):
    #     bet_case = (
    #         # A tuple of (params_value, subTest_description)
    #         ("multiNoCase1", "1-10"),
    #         ("multiNoCase2", "11-20"),
    #         ("multiNoCase3", "21-30"),
    #         ("multiNoCase4", "31-40"),
    #         ("multiNoCase5", "40-49")
    #     )
    #
    #     for params_value, subTest_description in bet_case:
    #         with self.subTest(subTest_description):
    #             page_markSix = GamePageMarkSix(self.driver)
    #             page_markSix.switch_pro_game("multiNo", "bet2Winning2")
    #             page_markSix.bet_pro_all("multiNo", "bet2Winning2", params_value)
    #
    #             bet_flow = GamePageCommon(self.driver)
    #             bet_flow.set_pro_bet_setting("cent")
    #             bet_flow.click_bet_basket()
    #
    #             bet_flow.click_payment("pro")
    #             order_info_confirm = bet_flow.check_order_info()
    #
    #             bet_flow.click_order_confirm()
    #             order_info_done = bet_flow.check_order_info()
    #             bet_flow.click_order_done()
    #
    #             expect_data = [self.game_name, "", "0.90", self.OrderInfoTrace_No, "1", "45"]
    #             Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)
    #
    # def test_18_Mark6_pro_normal_multiNo_bet2WinningSpecial(self):
    #     bet_case = (
    #         # A tuple of (params_value, subTest_description)
    #         ("multiNoCase1", "1-10"),
    #         ("multiNoCase2", "11-20"),
    #         ("multiNoCase3", "21-30"),
    #         ("multiNoCase4", "31-40"),
    #         ("multiNoCase5", "40-49")
    #     )
    #
    #     for params_value, subTest_description in bet_case:
    #         with self.subTest(subTest_description):
    #             page_markSix = GamePageMarkSix(self.driver)
    #             page_markSix.switch_pro_game("multiNo", "bet2WinningSpecial")
    #             page_markSix.bet_pro_all("multiNo", "bet2WinningSpecial", params_value)
    #
    #             bet_flow = GamePageCommon(self.driver)
    #             bet_flow.set_pro_bet_setting("cent")
    #             bet_flow.click_bet_basket()
    #
    #             bet_flow.click_payment("pro")
    #             order_info_confirm = bet_flow.check_order_info()
    #
    #             bet_flow.click_order_confirm()
    #             order_info_done = bet_flow.check_order_info()
    #             bet_flow.click_order_done()
    #
    #             expect_data = [self.game_name, "", "0.90", self.OrderInfoTrace_No, "1", "45"]
    #             Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)
    #
    # def test_19_Mark6_pro_normal_multiNo_bet2WinningMix(self):
    #     bet_case = (
    #         # A tuple of (params_value, subTest_description)
    #         ("multiNoCase1", "1-10"),
    #         ("multiNoCase2", "11-20"),
    #         ("multiNoCase3", "21-30"),
    #         ("multiNoCase4", "31-40"),
    #         ("multiNoCase5", "40-49")
    #     )
    #
    #     for params_value, subTest_description in bet_case:
    #         with self.subTest(subTest_description):
    #             page_markSix = GamePageMarkSix(self.driver)
    #             page_markSix.switch_pro_game("multiNo", "bet2WinningMix")
    #             page_markSix.bet_pro_all("multiNo", "bet2WinningMix", params_value)
    #
    #             bet_flow = GamePageCommon(self.driver)
    #             bet_flow.set_pro_bet_setting("cent")
    #             bet_flow.click_bet_basket()
    #
    #             bet_flow.click_payment("pro")
    #             order_info_confirm = bet_flow.check_order_info()
    #
    #             bet_flow.click_order_confirm()
    #             order_info_done = bet_flow.check_order_info()
    #             bet_flow.click_order_done()
    #
    #             expect_data = [self.game_name, "", "0.90", self.OrderInfoTrace_No, "1", "45"]
    #             Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_20_Mark6_pro_normal_halfBall(self):
        page_markSix = GamePageMarkSix(self.driver)
        page_markSix.switch_pro_game("halfBall")
        page_markSix.bet_pro_all("halfBall")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.36", self.OrderInfoTrace_No, "18", "18"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_21_Mark6_pro_normal_tailNo(self):
        page_markSix = GamePageMarkSix(self.driver)
        page_markSix.switch_pro_game("tailNo")
        page_markSix.bet_pro_all("tailNo")

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

    # def test_22_Mark6_pro_normal_notWinning_notWinning5(self):
    #     bet_case = (
    #         # A tuple of (params_value, subTest_description)
    #         ("notWinningCase1", "1-8"),
    #         ("notWinningCase2", "9-16"),
    #         ("notWinningCase3", "17-24"),
    #         ("notWinningCase4", "25-32"),
    #         ("notWinningCase5", "33-40"),
    #         ("notWinningCase6", "41-48"),
    #         ("notWinningCase7", "42-49")
    #     )
    #
    #     for params_value, subTest_description in bet_case:
    #         with self.subTest(subTest_description):
    #             page_markSix = GamePageMarkSix(self.driver)
    #             page_markSix.switch_pro_game("notWinning", "notWinning5")
    #             page_markSix.bet_pro_all("notWinning", "notWinning5", params_value)
    #
    #             bet_flow = GamePageCommon(self.driver)
    #             bet_flow.set_pro_bet_setting("cent")
    #             bet_flow.click_bet_basket()
    #
    #             bet_flow.click_payment("pro")
    #             order_info_confirm = bet_flow.check_order_info()
    #
    #             bet_flow.click_order_confirm()
    #             order_info_done = bet_flow.check_order_info()
    #             bet_flow.click_order_done()
    #
    #             expect_data = [self.game_name, "", "1.12", self.OrderInfoTrace_No, "1", "56"]
    #             Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)
    #
    # def test_23_Mark6_pro_normal_notWinning_notWinning6(self):
    #     bet_case = (
    #         # A tuple of (params_value, subTest_description)
    #         ("notWinningCase1", "1-8"),
    #         ("notWinningCase2", "9-16"),
    #         ("notWinningCase3", "17-24"),
    #         ("notWinningCase4", "25-32"),
    #         ("notWinningCase5", "33-40"),
    #         ("notWinningCase6", "41-48"),
    #         ("notWinningCase7", "42-49")
    #     )
    #
    #     for params_value, subTest_description in bet_case:
    #         with self.subTest(subTest_description):
    #             page_markSix = GamePageMarkSix(self.driver)
    #             page_markSix.switch_pro_game("notWinning", "notWinning6")
    #             page_markSix.bet_pro_all("notWinning", "notWinning6", params_value)
    #
    #             bet_flow = GamePageCommon(self.driver)
    #             bet_flow.set_pro_bet_setting("cent")
    #             bet_flow.click_bet_basket()
    #
    #             bet_flow.click_payment("pro")
    #             order_info_confirm = bet_flow.check_order_info()
    #
    #             bet_flow.click_order_confirm()
    #             order_info_done = bet_flow.check_order_info()
    #             bet_flow.click_order_done()
    #
    #             expect_data = [self.game_name, "", "0.56", self.OrderInfoTrace_No, "1", "28"]
    #             Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)
    #
    # def test_24_Mark6_pro_normal_notWinning_notWinning7(self):
    #     bet_case = (
    #         # A tuple of (params_value, subTest_description)
    #         ("notWinningCase1", "1-10"),
    #         ("notWinningCase2", "11-20"),
    #         ("notWinningCase3", "21-30"),
    #         ("notWinningCase4", "31-40"),
    #         ("notWinningCase5", "40-49")
    #     )
    #
    #     for params_value, subTest_description in bet_case:
    #         with self.subTest(subTest_description):
    #             page_markSix = GamePageMarkSix(self.driver)
    #             page_markSix.switch_pro_game("notWinning", "notWinning7")
    #             page_markSix.bet_pro_all("notWinning", "notWinning7", params_value)
    #
    #             bet_flow = GamePageCommon(self.driver)
    #             bet_flow.set_pro_bet_setting("cent")
    #             bet_flow.click_bet_basket()
    #
    #             bet_flow.click_payment("pro")
    #             order_info_confirm = bet_flow.check_order_info()
    #
    #             bet_flow.click_order_confirm()
    #             order_info_done = bet_flow.check_order_info()
    #             bet_flow.click_order_done()
    #
    #             expect_data = [self.game_name, "", "2.40", self.OrderInfoTrace_No, "1", "120"]
    #             Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)
    #
    # def test_25_Mark6_pro_normal_notWinning_notWinning8(self):
    #     bet_case = (
    #         # A tuple of (params_value, subTest_description)
    #         ("notWinningCase1", "1-10"),
    #         ("notWinningCase2", "11-20"),
    #         ("notWinningCase3", "21-30"),
    #         ("notWinningCase4", "31-40"),
    #         ("notWinningCase5", "40-49")
    #     )
    #
    #     for params_value, subTest_description in bet_case:
    #         with self.subTest(subTest_description):
    #             page_markSix = GamePageMarkSix(self.driver)
    #             page_markSix.switch_pro_game("notWinning", "notWinning8")
    #             page_markSix.bet_pro_all("notWinning", "notWinning8", params_value)
    #
    #             bet_flow = GamePageCommon(self.driver)
    #             bet_flow.set_pro_bet_setting("cent")
    #             bet_flow.click_bet_basket()
    #
    #             bet_flow.click_payment("pro")
    #             order_info_confirm = bet_flow.check_order_info()
    #
    #             bet_flow.click_order_confirm()
    #             order_info_done = bet_flow.check_order_info()
    #             bet_flow.click_order_done()
    #
    #             expect_data = [self.game_name, "", "0.90", self.OrderInfoTrace_No, "1", "45"]
    #             Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)
    #
    # def test_26_Mark6_pro_normal_notWinning_notWinning9(self):
    #     bet_case = (
    #         # A tuple of (params_value, subTest_description)
    #         ("notWinningCase1", "1-10"),
    #         ("notWinningCase2", "11-20"),
    #         ("notWinningCase3", "21-30"),
    #         ("notWinningCase4", "31-40"),
    #         ("notWinningCase5", "40-49")
    #     )
    #
    #     for params_value, subTest_description in bet_case:
    #         with self.subTest(subTest_description):
    #             page_markSix = GamePageMarkSix(self.driver)
    #             page_markSix.switch_pro_game("notWinning", "notWinning9")
    #             page_markSix.bet_pro_all("notWinning", "notWinning9", params_value)
    #
    #             bet_flow = GamePageCommon(self.driver)
    #             bet_flow.set_pro_bet_setting("cent")
    #             bet_flow.click_bet_basket()
    #
    #             bet_flow.click_payment("pro")
    #             order_info_confirm = bet_flow.check_order_info()
    #
    #             bet_flow.click_order_confirm()
    #             order_info_done = bet_flow.check_order_info()
    #             bet_flow.click_order_done()
    #
    #             expect_data = [self.game_name, "", "0.20", self.OrderInfoTrace_No, "1", "10"]
    #             Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)
    #
    # def test_27_Mark6_pro_normal_notWinning_notWinning10(self):
    #     bet_case = (
    #         # A tuple of (params_value, subTest_description)
    #         ("notWinningCase1", "1-10"),
    #         ("notWinningCase2", "11-20"),
    #         ("notWinningCase3", "21-30"),
    #         ("notWinningCase4", "31-40"),
    #         ("notWinningCase5", "40-49")
    #     )
    #
    #     for params_value, subTest_description in bet_case:
    #         with self.subTest(subTest_description):
    #             page_markSix = GamePageMarkSix(self.driver)
    #             page_markSix.switch_pro_game("notWinning", "notWinning10")
    #             page_markSix.bet_pro_all("notWinning", "notWinning10", params_value)
    #
    #             bet_flow = GamePageCommon(self.driver)
    #             bet_flow.set_pro_bet_setting("cent")
    #             bet_flow.click_bet_basket()
    #
    #             bet_flow.click_payment("pro")
    #             order_info_confirm = bet_flow.check_order_info()
    #
    #             bet_flow.click_order_confirm()
    #             order_info_done = bet_flow.check_order_info()
    #             bet_flow.click_order_done()
    #
    #             expect_data = [self.game_name, "", "0.02", self.OrderInfoTrace_No, "1", "1"]
    #             Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_28_Mark6_pro_normal_zodiac1(self):
        page_markSix = GamePageMarkSix(self.driver)
        page_markSix.switch_pro_game("zodiac1")
        page_markSix.bet_pro_all("zodiac1")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.24", self.OrderInfoTrace_No, "1", "12"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_29_Mark6_pro_normal_specialZodiac(self):
        page_markSix = GamePageMarkSix(self.driver)
        page_markSix.switch_pro_game("specialZodiac")
        page_markSix.bet_pro_all("specialZodiac")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.24", self.OrderInfoTrace_No, "1", "12"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    # def test_30_Mark6_pro_normal_zodiac6_zodiac6Winning(self):
    #     bet_case = (
    #         # A tuple of (params_value, subTest_description)
    #         ("zodiac6Case1", "鼠-蛇"),
    #         ("zodiac6Case2", "馬-豬")
    #     )
    #
    #     for params_value, subTest_description in bet_case:
    #         with self.subTest(subTest_description):
    #             page_markSix = GamePageMarkSix(self.driver)
    #             page_markSix.switch_pro_game("zodiac6", "zodiac6Winning")
    #             page_markSix.bet_pro_all("zodiac6", "zodiac6Winning", params_value)
    #
    #             bet_flow = GamePageCommon(self.driver)
    #             bet_flow.set_pro_bet_setting("cent")
    #             bet_flow.click_bet_basket()
    #
    #             bet_flow.click_payment("pro")
    #             order_info_confirm = bet_flow.check_order_info()
    #
    #             bet_flow.click_order_confirm()
    #             order_info_done = bet_flow.check_order_info()
    #             bet_flow.click_order_done()
    #
    #             expect_data = [self.game_name, "", "0.02", self.OrderInfoTrace_No, "1", "1"]
    #             Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)
    #
    # def test_31_Mark6_pro_normal_zodiac6_zodiac6Lose(self):
    #     bet_case = (
    #         # A tuple of (params_value, subTest_description)
    #         ("zodiac6Case1", "鼠-蛇"),
    #         ("zodiac6Case2", "馬-豬")
    #     )
    #
    #     for params_value, subTest_description in bet_case:
    #         with self.subTest(subTest_description):
    #             page_markSix = GamePageMarkSix(self.driver)
    #             page_markSix.switch_pro_game("zodiac6", "zodiac6Lose")
    #             page_markSix.bet_pro_all("zodiac6", "zodiac6Lose", params_value)
    #
    #             bet_flow = GamePageCommon(self.driver)
    #             bet_flow.set_pro_bet_setting("cent")
    #             bet_flow.click_bet_basket()
    #
    #             bet_flow.click_payment("pro")
    #             order_info_confirm = bet_flow.check_order_info()
    #
    #             bet_flow.click_order_confirm()
    #             order_info_done = bet_flow.check_order_info()
    #             bet_flow.click_order_done()
    #
    #             expect_data = [self.game_name, "", "0.02", self.OrderInfoTrace_No, "1", "1"]
    #             Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    # def test_32_Mark6_pro_normal_zodiacs_zodiac2Winning(self):
    #     bet_case = (
    #         # A tuple of (params_value, subTest_description)
    #         ("zodiacsCase1", "鼠-蛇"),
    #         ("zodiacsCase2", "馬-豬")
    #     )
    #
    #     for params_value, subTest_description in bet_case:
    #         with self.subTest(subTest_description):
    #             page_markSix = GamePageMarkSix(self.driver)
    #             page_markSix.switch_pro_game("zodiacs", "zodiac2Winning")
    #             page_markSix.bet_pro_all("zodiacs", "zodiac2Winning", params_value)
    #
    #             bet_flow = GamePageCommon(self.driver)
    #             bet_flow.set_pro_bet_setting("cent")
    #             bet_flow.click_bet_basket()
    #
    #             bet_flow.click_payment("pro")
    #             order_info_confirm = bet_flow.check_order_info()
    #
    #             bet_flow.click_order_confirm()
    #             order_info_done = bet_flow.check_order_info()
    #             bet_flow.click_order_done()
    #
    #             expect_data = [self.game_name, "", "0.30", self.OrderInfoTrace_No, "1", "15"]
    #             Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)
    #
    # def test_33_Mark6_pro_normal_zodiacs_zodiac2Lose(self):
    #     bet_case = (
    #         # A tuple of (params_value, subTest_description)
    #         ("zodiacsCase1", "鼠-蛇"),
    #         ("zodiacsCase2", "馬-豬")
    #     )
    #
    #     for params_value, subTest_description in bet_case:
    #         with self.subTest(subTest_description):
    #             page_markSix = GamePageMarkSix(self.driver)
    #             page_markSix.switch_pro_game("zodiacs", "zodiac2Lose")
    #             page_markSix.bet_pro_all("zodiacs", "zodiac2Lose", params_value)
    #
    #             bet_flow = GamePageCommon(self.driver)
    #             bet_flow.set_pro_bet_setting("cent")
    #             bet_flow.click_bet_basket()
    #
    #             bet_flow.click_payment("pro")
    #             order_info_confirm = bet_flow.check_order_info()
    #
    #             bet_flow.click_order_confirm()
    #             order_info_done = bet_flow.check_order_info()
    #             bet_flow.click_order_done()
    #
    #             expect_data = [self.game_name, "", "0.30", self.OrderInfoTrace_No, "1", "15"]
    #             Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)
    #
    # def test_34_Mark6_pro_normal_zodiacs_zodiac3Winning(self):
    #     bet_case = (
    #         # A tuple of (params_value, subTest_description)
    #         ("zodiacsCase1", "鼠-蛇"),
    #         ("zodiacsCase2", "馬-豬")
    #     )
    #
    #     for params_value, subTest_description in bet_case:
    #         with self.subTest(subTest_description):
    #             page_markSix = GamePageMarkSix(self.driver)
    #             page_markSix.switch_pro_game("zodiacs", "zodiac3Winning")
    #             page_markSix.bet_pro_all("zodiacs", "zodiac3Winning", params_value)
    #
    #             bet_flow = GamePageCommon(self.driver)
    #             bet_flow.set_pro_bet_setting("cent")
    #             bet_flow.click_bet_basket()
    #
    #             bet_flow.click_payment("pro")
    #             order_info_confirm = bet_flow.check_order_info()
    #
    #             bet_flow.click_order_confirm()
    #             order_info_done = bet_flow.check_order_info()
    #             bet_flow.click_order_done()
    #
    #             expect_data = [self.game_name, "", "0.40", self.OrderInfoTrace_No, "1", "20"]
    #             Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)
    #
    # def test_35_Mark6_pro_normal_zodiacs_zodiac3Lose(self):
    #     bet_case = (
    #         # A tuple of (params_value, subTest_description)
    #         ("zodiacsCase1", "鼠-蛇"),
    #         ("zodiacsCase2", "馬-豬")
    #     )
    #
    #     for params_value, subTest_description in bet_case:
    #         with self.subTest(subTest_description):
    #             page_markSix = GamePageMarkSix(self.driver)
    #             page_markSix.switch_pro_game("zodiacs", "zodiac3Lose")
    #             page_markSix.bet_pro_all("zodiacs", "zodiac3Lose", params_value)
    #
    #             bet_flow = GamePageCommon(self.driver)
    #             bet_flow.set_pro_bet_setting("cent")
    #             bet_flow.click_bet_basket()
    #
    #             bet_flow.click_payment("pro")
    #             order_info_confirm = bet_flow.check_order_info()
    #
    #             bet_flow.click_order_confirm()
    #             order_info_done = bet_flow.check_order_info()
    #             bet_flow.click_order_done()
    #
    #             expect_data = [self.game_name, "", "0.40", self.OrderInfoTrace_No, "1", "20"]
    #             Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)
    #
    # def test_36_Mark6_pro_normal_zodiacs_zodiac4Winning(self):
    #     bet_case = (
    #         # A tuple of (params_value, subTest_description)
    #         ("zodiacsCase1", "鼠-蛇"),
    #         ("zodiacsCase2", "馬-豬")
    #     )
    #
    #     for params_value, subTest_description in bet_case:
    #         with self.subTest(subTest_description):
    #             page_markSix = GamePageMarkSix(self.driver)
    #             page_markSix.switch_pro_game("zodiacs", "zodiac4Winning")
    #             page_markSix.bet_pro_all("zodiacs", "zodiac4Winning", params_value)
    #
    #             bet_flow = GamePageCommon(self.driver)
    #             bet_flow.set_pro_bet_setting("cent")
    #             bet_flow.click_bet_basket()
    #
    #             bet_flow.click_payment("pro")
    #             order_info_confirm = bet_flow.check_order_info()
    #
    #             bet_flow.click_order_confirm()
    #             order_info_done = bet_flow.check_order_info()
    #             bet_flow.click_order_done()
    #
    #             expect_data = [self.game_name, "", "0.30", self.OrderInfoTrace_No, "1", "15"]
    #             Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)
    #
    # def test_37_Mark6_pro_normal_zodiacs_zodiac4Lose(self):
    #     bet_case = (
    #         # A tuple of (params_value, subTest_description)
    #         ("zodiacsCase1", "鼠-蛇"),
    #         ("zodiacsCase2", "馬-豬")
    #     )
    #
    #     for params_value, subTest_description in bet_case:
    #         with self.subTest(subTest_description):
    #             page_markSix = GamePageMarkSix(self.driver)
    #             page_markSix.switch_pro_game("zodiacs", "zodiac4Lose")
    #             page_markSix.bet_pro_all("zodiacs", "zodiac4Lose", params_value)
    #
    #             bet_flow = GamePageCommon(self.driver)
    #             bet_flow.set_pro_bet_setting("cent")
    #             bet_flow.click_bet_basket()
    #
    #             bet_flow.click_payment("pro")
    #             order_info_confirm = bet_flow.check_order_info()
    #
    #             bet_flow.click_order_confirm()
    #             order_info_done = bet_flow.check_order_info()
    #             bet_flow.click_order_done()
    #
    #             expect_data = [self.game_name, "", "0.30", self.OrderInfoTrace_No, "1", "15"]
    #             Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    # def test_38_Mark6_pro_normal_tails_tail2Winning(self):
    #     bet_case = (
    #         # A tuple of (params_value, subTest_description)
    #         ("tailsCase1", "0尾-4尾"),
    #         ("tailsCase2", "5尾-9尾")
    #     )
    #
    #     for params_value, subTest_description in bet_case:
    #         with self.subTest(subTest_description):
    #             page_markSix = GamePageMarkSix(self.driver)
    #             page_markSix.switch_pro_game("tails", "tail2Winning")
    #             page_markSix.bet_pro_all("tails", "tail2Winning", params_value)
    #
    #             bet_flow = GamePageCommon(self.driver)
    #             bet_flow.set_pro_bet_setting("cent")
    #             bet_flow.click_bet_basket()
    #
    #             bet_flow.click_payment("pro")
    #             order_info_confirm = bet_flow.check_order_info()
    #
    #             bet_flow.click_order_confirm()
    #             order_info_done = bet_flow.check_order_info()
    #             bet_flow.click_order_done()
    #
    #             expect_data = [self.game_name, "", "0.20", self.OrderInfoTrace_No, "1", "10"]
    #             Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)
    #
    # def test_39_Mark6_pro_normal_tails_tail2Lose(self):
    #     bet_case = (
    #         # A tuple of (params_value, subTest_description)
    #         ("tailsCase1", "0尾-4尾"),
    #         ("tailsCase2", "5尾-9尾")
    #     )
    #
    #     for params_value, subTest_description in bet_case:
    #         with self.subTest(subTest_description):
    #             page_markSix = GamePageMarkSix(self.driver)
    #             page_markSix.switch_pro_game("tails", "tail2Lose")
    #             page_markSix.bet_pro_all("tails", "tail2Lose", params_value)
    #
    #             bet_flow = GamePageCommon(self.driver)
    #             bet_flow.set_pro_bet_setting("cent")
    #             bet_flow.click_bet_basket()
    #
    #             bet_flow.click_payment("pro")
    #             order_info_confirm = bet_flow.check_order_info()
    #
    #             bet_flow.click_order_confirm()
    #             order_info_done = bet_flow.check_order_info()
    #             bet_flow.click_order_done()
    #
    #             expect_data = [self.game_name, "", "0.20", self.OrderInfoTrace_No, "1", "10"]
    #             Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)
    #
    # def test_40_Mark6_pro_normal_tails_tail3Winning(self):
    #     bet_case = (
    #         # A tuple of (params_value, subTest_description)
    #         ("tailsCase1", "0尾-4尾"),
    #         ("tailsCase2", "5尾-9尾")
    #     )
    #
    #     for params_value, subTest_description in bet_case:
    #         with self.subTest(subTest_description):
    #             page_markSix = GamePageMarkSix(self.driver)
    #             page_markSix.switch_pro_game("tails", "tail3Winning")
    #             page_markSix.bet_pro_all("tails", "tail3Winning", params_value)
    #
    #             bet_flow = GamePageCommon(self.driver)
    #             bet_flow.set_pro_bet_setting("cent")
    #             bet_flow.click_bet_basket()
    #
    #             bet_flow.click_payment("pro")
    #             order_info_confirm = bet_flow.check_order_info()
    #
    #             bet_flow.click_order_confirm()
    #             order_info_done = bet_flow.check_order_info()
    #             bet_flow.click_order_done()
    #
    #             expect_data = [self.game_name, "", "0.20", self.OrderInfoTrace_No, "1", "10"]
    #             Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)
    #
    # def test_41_Mark6_pro_normal_tails_tail3Lose(self):
    #     bet_case = (
    #         # A tuple of (params_value, subTest_description)
    #         ("tailsCase1", "0尾-4尾"),
    #         ("tailsCase2", "5尾-9尾")
    #     )
    #
    #     for params_value, subTest_description in bet_case:
    #         with self.subTest(subTest_description):
    #             page_markSix = GamePageMarkSix(self.driver)
    #             page_markSix.switch_pro_game("tails", "tail3Lose")
    #             page_markSix.bet_pro_all("tails", "tail3Lose", params_value)
    #
    #             bet_flow = GamePageCommon(self.driver)
    #             bet_flow.set_pro_bet_setting("cent")
    #             bet_flow.click_bet_basket()
    #
    #             bet_flow.click_payment("pro")
    #             order_info_confirm = bet_flow.check_order_info()
    #
    #             bet_flow.click_order_confirm()
    #             order_info_done = bet_flow.check_order_info()
    #             bet_flow.click_order_done()
    #
    #             expect_data = [self.game_name, "", "0.20", self.OrderInfoTrace_No, "1", "10"]
    #             Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)
    #
    # def test_42_Mark6_pro_normal_tails_tail4Winning(self):
    #     bet_case = (
    #         # A tuple of (params_value, subTest_description)
    #         ("tailsCase1", "0尾-4尾"),
    #         ("tailsCase2", "5尾-9尾")
    #     )
    #
    #     for params_value, subTest_description in bet_case:
    #         with self.subTest(subTest_description):
    #             page_markSix = GamePageMarkSix(self.driver)
    #             page_markSix.switch_pro_game("tails", "tail4Winning")
    #             page_markSix.bet_pro_all("tails", "tail4Winning", params_value)
    #
    #             bet_flow = GamePageCommon(self.driver)
    #             bet_flow.set_pro_bet_setting("cent")
    #             bet_flow.click_bet_basket()
    #
    #             bet_flow.click_payment("pro")
    #             order_info_confirm = bet_flow.check_order_info()
    #
    #             bet_flow.click_order_confirm()
    #             order_info_done = bet_flow.check_order_info()
    #             bet_flow.click_order_done()
    #
    #             expect_data = [self.game_name, "", "0.10", self.OrderInfoTrace_No, "1", "5"]
    #             Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)
    #
    # def test_43_Mark6_pro_normal_tails_tail4Lose(self):
    #     bet_case = (
    #         # A tuple of (params_value, subTest_description)
    #         ("tailsCase1", "0尾-4尾"),
    #         ("tailsCase2", "5尾-9尾")
    #     )
    #
    #     for params_value, subTest_description in bet_case:
    #         with self.subTest(subTest_description):
    #             page_markSix = GamePageMarkSix(self.driver)
    #             page_markSix.switch_pro_game("tails", "tail4Lose")
    #             page_markSix.bet_pro_all("tails", "tail4Lose", params_value)
    #
    #             bet_flow = GamePageCommon(self.driver)
    #             bet_flow.set_pro_bet_setting("cent")
    #             bet_flow.click_bet_basket()
    #
    #             bet_flow.click_payment("pro")
    #             order_info_confirm = bet_flow.check_order_info()
    #
    #             bet_flow.click_order_confirm()
    #             order_info_done = bet_flow.check_order_info()
    #             bet_flow.click_order_done()
    #
    #             expect_data = [self.game_name, "", "0.10", self.OrderInfoTrace_No, "1", "5"]
    #             Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    def test_44_Mark6_pro_normal_dt16(self):
        page_markSix = GamePageMarkSix(self.driver)
        page_markSix.switch_pro_game("dt16")
        page_markSix.bet_pro_all("dt16")

        bet_flow = GamePageCommon(self.driver)
        bet_flow.set_pro_bet_setting("cent")
        bet_flow.click_bet_basket()

        bet_flow.click_payment("pro")
        order_info_confirm = bet_flow.check_order_info()

        bet_flow.click_order_confirm()
        order_info_done = bet_flow.check_order_info()
        bet_flow.click_order_done()

        expect_data = [self.game_name, "", "0.60", self.OrderInfoTrace_No, "30", "30"]
        Assertion.assertOrderInfo(expect_data, order_info_confirm, order_info_done)

    @classmethod
    def tearDownClass(cls):
        cls.driver = Driver
        bet_flow = GamePageCommon(cls.driver)
        bet_flow.back_to_homepage()
        bet_flow.check_homepage_showing()


if __name__ == '__main__':
    unittest.main()
