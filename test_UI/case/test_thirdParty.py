import unittest
from config.SetUIConfig import Driver
from test_UI.common.GamePageCommon import GamePageCommon
from config.SetUIConfig import Project
from test_UI.page.LoginPage import LoginPage
from test_UI.page.HomePage import HomePage
from test_UI.page.GamePage import GamePage
from test_UI.page.GamePageThirdParty import GamePageThirdParty
from utils import Assertion, Localization


class ThirdParty(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver
        login_page = LoginPage(cls.driver)
        login_page.execute_login()

        home_page = HomePage(cls.driver)
        home_page.switch_category("game")

    def test_01_thirdParty_cmd_login(self):
        game_page = GamePage(self.driver)
        game_name = game_page.switch_game("Sport", "cmd")
        entrance = GamePageCommon(self.driver)
        game_title = entrance.get_thirdParty_title()
        thirdPartyTitle = Assertion.assertThirdPartyTitle(game_title, game_name)

        Transfer = GamePageThirdParty(self.driver)
        Transfer.click_button_transfer_window_open()
        center_money, thirdParty_money = Transfer.store_transfer_info()
        thirdPartyResponse = Assertion.assertNotEqualData(thirdParty_money, "-")
        center_money_change, thirdParty_money_change = Transfer.execute_transfer_to_thirdParty_100()
        actual_result = [center_money_change, thirdParty_money_change]
        expect_result = [center_money-100, thirdParty_money+100]
        thirdPartyTransferResult = Assertion.assertEqualData(actual_result, expect_result)

        entrance.click_back_button()
        entrance.check_homepage_showing()

        results = [thirdPartyTitle, thirdPartyResponse, thirdPartyTransferResult]
        Assertion.assertFalseResult(results)

    @unittest.skip
    def test_02_thirdParty_saba_login(self):
        game_page = GamePage(self.driver)
        game_name = game_page.switch_game("Sport", "saba")
        entrance = GamePageCommon(self.driver)
        game_title = entrance.get_thirdParty_title()
        thirdPartyTitle = Assertion.assertThirdPartyTitle(game_title, game_name)

        entrance.click_back_button()
        entrance.check_homepage_showing()

        results = [thirdPartyTitle]
        Assertion.assertFalseResult(results)

    def test_03_thirdParty_imSport_login(self):
        game_page = GamePage(self.driver)
        game_name = game_page.switch_game("Sport", "imSport")
        entrance = GamePageCommon(self.driver)
        game_title = entrance.get_thirdParty_title()
        thirdPartyTitle = Assertion.assertThirdPartyTitle(game_title, game_name)

        Transfer = GamePageThirdParty(self.driver)
        Transfer.click_button_transfer_window_open()
        center_money, thirdParty_money = Transfer.store_transfer_info()
        Transfer.click_button_transfer_window_close()
        thirdPartyResponse = Assertion.assertNotEqualData(thirdParty_money, "-")

        entrance.click_back_button()
        entrance.check_homepage_showing()

        results = [thirdPartyTitle, thirdPartyResponse]
        Assertion.assertFalseResult(results)

    def test_04_thirdParty_imEsport_login(self):
        game_page = GamePage(self.driver)
        game_name = game_page.switch_game("Sport", "imEsport")
        entrance = GamePageCommon(self.driver)
        game_title = entrance.get_thirdParty_title()
        thirdPartyTitle = Assertion.assertThirdPartyTitle(game_title, game_name)

        Transfer = GamePageThirdParty(self.driver)
        Transfer.click_button_transfer_window_open()
        center_money, thirdParty_money = Transfer.store_transfer_info()
        Transfer.click_button_transfer_window_close()
        thirdPartyResponse = Assertion.assertNotEqualData(thirdParty_money, "-")

        entrance.click_back_button()
        entrance.check_homepage_showing()

        results = [thirdPartyTitle, thirdPartyResponse]
        Assertion.assertFalseResult(results)

    def test_05_thirdParty_leihuo_login(self):
        game_page = GamePage(self.driver)
        game_name = game_page.switch_game("Sport", "leihuo")
        entrance = GamePageCommon(self.driver)
        game_title = entrance.get_thirdParty_title()
        thirdPartyTitle = Assertion.assertThirdPartyTitle(game_title, game_name)

        Transfer = GamePageThirdParty(self.driver)
        Transfer.click_button_transfer_window_open()
        center_money, thirdParty_money = Transfer.store_transfer_info()
        Transfer.click_button_transfer_window_close()
        thirdPartyResponse = Assertion.assertNotEqualData(thirdParty_money, "-")

        entrance.click_back_button()
        entrance.check_homepage_showing()

        results = [thirdPartyTitle, thirdPartyResponse]
        Assertion.assertFalseResult(results)

    @unittest.skipIf(Project == 'vt', 'sta only')
    def test_06_thirdParty_obSport_login(self):
        game_page = GamePage(self.driver)
        game_name = game_page.switch_game("Sport", "obSport")
        entrance = GamePageCommon(self.driver)
        game_title = entrance.get_thirdParty_title()
        thirdPartyTitle = Assertion.assertThirdPartyTitle(game_title, game_name)

        Transfer = GamePageThirdParty(self.driver)
        Transfer.click_button_transfer_window_open()
        center_money, thirdParty_money = Transfer.store_transfer_info()
        thirdPartyResponse = Assertion.assertNotEqualData(thirdParty_money, "-")
        center_money_change, thirdParty_money_change = Transfer.execute_transfer_to_thirdParty_100()
        actual_result = [center_money_change, thirdParty_money_change]
        expect_result = [center_money-100, thirdParty_money+100]
        thirdPartyTransferResult = Assertion.assertEqualData(actual_result, expect_result)

        entrance.click_back_button()
        entrance.check_homepage_showing()

        results = [thirdPartyTitle, thirdPartyResponse, thirdPartyTransferResult]
        Assertion.assertFalseResult(results)

    @unittest.skipIf(Project == 'sta', 'vt only')
    def test_07_thirdParty_sboSport_login(self):
        game_page = GamePage(self.driver)
        game_name = game_page.switch_game("Sport", "sboSport")
        entrance = GamePageCommon(self.driver)
        game_title = entrance.get_thirdParty_title()
        thirdPartyTitle = Assertion.assertThirdPartyTitle(game_title, game_name)

        Transfer = GamePageThirdParty(self.driver)
        Transfer.click_button_transfer_window_open()
        center_money, thirdParty_money = Transfer.store_transfer_info()
        thirdPartyResponse = Assertion.assertNotEqualData(thirdParty_money, "-")
        center_money_change, thirdParty_money_change = Transfer.execute_transfer_to_thirdParty_100()
        actual_result = [center_money_change, thirdParty_money_change]
        expect_result = [center_money-100, thirdParty_money+100]
        thirdPartyTransferResult = Assertion.assertEqualData(actual_result, expect_result)

        entrance.click_back_button()
        entrance.check_homepage_showing()

        results = [thirdPartyTitle, thirdPartyResponse, thirdPartyTransferResult]
        Assertion.assertFalseResult(results)

    def test_08_thirdParty_agCasino_login(self):
        game_page = GamePage(self.driver)
        game_name = game_page.switch_game("LiveDealer", "agCasino")
        entrance = GamePageCommon(self.driver)
        game_title = entrance.get_thirdParty_title()
        thirdPartyTitle = Assertion.assertThirdPartyTitle(game_title, game_name)

        entrance.click_back_button()
        entrance.check_homepage_showing()

        results = [thirdPartyTitle]
        Assertion.assertFalseResult(results)

    @unittest.skipIf(Project == 'sta', 'vt only')
    def test_09_thirdParty_ok368_login(self):
        game_page = GamePage(self.driver)
        game_name = game_page.switch_game("Lottery", "ok368")
        control = GamePageThirdParty(self.driver)
        control.back_to_previous_page()

        entrance = GamePageCommon(self.driver)
        entrance.check_homepage_showing()

    @unittest.skipIf(Project == 'sta', 'vt only')
    def test_10_thirdParty_vr_login(self):
        game_page = GamePage(self.driver)
        game_name = game_page.switch_game("Lottery", "vr")
        entrance = GamePageCommon(self.driver)
        game_title = entrance.get_thirdParty_title()
        thirdPartyTitle = Assertion.assertThirdPartyTitle(game_title, game_name)

        Transfer = GamePageThirdParty(self.driver)
        Transfer.click_button_transfer_window_open()
        center_money, thirdParty_money = Transfer.store_transfer_info()
        thirdPartyResponse = Assertion.assertNotEqualData(thirdParty_money, "-")
        center_money_change, thirdParty_money_change = Transfer.execute_transfer_to_thirdParty_100()
        actual_result = [center_money_change, thirdParty_money_change]
        expect_result = [center_money - 100, thirdParty_money + 100]
        thirdPartyTransferResult = Assertion.assertEqualData(actual_result, expect_result)

        entrance.click_back_button()
        entrance.check_homepage_showing()

        results = [thirdPartyTitle, thirdPartyResponse, thirdPartyTransferResult]
        Assertion.assertFalseResult(results)

    def test_11_thirdParty_bgCasino_login(self):
        game_page = GamePage(self.driver)
        game_name = game_page.switch_game("LiveDealer", "bgCasino")
        entrance = GamePageCommon(self.driver)
        game_title = entrance.get_thirdParty_title()
        thirdPartyTitle = Assertion.assertThirdPartyTitle(game_title, game_name)

        Transfer = GamePageThirdParty(self.driver)
        Transfer.click_button_transfer_window_open()
        center_money, thirdParty_money = Transfer.store_transfer_info()
        thirdPartyResponse = Assertion.assertNotEqualData(thirdParty_money, "-")
        center_money_change, thirdParty_money_change = Transfer.execute_transfer_to_thirdParty_100()
        actual_result = [center_money_change, thirdParty_money_change]
        expect_result = [center_money - 100, thirdParty_money + 100]
        thirdPartyTransferResult = Assertion.assertEqualData(actual_result, expect_result)

        entrance.click_back_button()
        entrance.check_homepage_showing()

        results = [thirdPartyTitle, thirdPartyResponse, thirdPartyTransferResult]
        Assertion.assertFalseResult(results)

    def test_12_thirdParty_dgCasino_login(self):
        game_page = GamePage(self.driver)
        game_name = game_page.switch_game("LiveDealer", "dgCasino")
        entrance = GamePageCommon(self.driver)
        game_title = entrance.get_thirdParty_title()
        thirdPartyTitle = Assertion.assertThirdPartyTitle(game_title, game_name)

        Transfer = GamePageThirdParty(self.driver)
        Transfer.click_button_transfer_window_open()
        center_money, thirdParty_money = Transfer.store_transfer_info()
        thirdPartyResponse = Assertion.assertNotEqualData(thirdParty_money, "-")
        center_money_change, thirdParty_money_change = Transfer.execute_transfer_to_thirdParty_100()
        actual_result = [center_money_change, thirdParty_money_change]
        expect_result = [center_money - 100, thirdParty_money + 100]
        thirdPartyTransferResult = Assertion.assertEqualData(actual_result, expect_result)

        entrance.click_back_button()
        entrance.check_homepage_showing()

        results = [thirdPartyTitle, thirdPartyResponse, thirdPartyTransferResult]
        Assertion.assertFalseResult(results)

    @unittest.skipIf(Project == 'vt', 'sta only')
    def test_13_thirdParty_obCasino_login(self):
        game_page = GamePage(self.driver)
        game_name = game_page.switch_game("LiveDealer", "obCasino")
        entrance = GamePageCommon(self.driver)
        game_title = entrance.get_thirdParty_title()
        thirdPartyTitle = Assertion.assertThirdPartyTitle(game_title, game_name)

        Transfer = GamePageThirdParty(self.driver)
        Transfer.click_button_transfer_window_open()
        center_money, thirdParty_money = Transfer.store_transfer_info()
        thirdPartyResponse = Assertion.assertNotEqualData(thirdParty_money, "-")
        center_money_change, thirdParty_money_change = Transfer.execute_transfer_to_thirdParty_100()
        actual_result = [center_money_change, thirdParty_money_change]
        expect_result = [center_money - 100, thirdParty_money + 100]
        thirdPartyTransferResult = Assertion.assertEqualData(actual_result, expect_result)

        entrance.click_back_button()
        entrance.check_homepage_showing()

        results = [thirdPartyTitle, thirdPartyResponse, thirdPartyTransferResult]
        Assertion.assertFalseResult(results)

    @unittest.skipIf(Project == 'sta', 'vt only')
    def test_14_thirdParty_wmCasino_login(self):
        game_page = GamePage(self.driver)
        game_name = game_page.switch_game("LiveDealer", "wmCasino")
        entrance = GamePageCommon(self.driver)
        game_title = entrance.get_thirdParty_title()
        thirdPartyTitle = Assertion.assertThirdPartyTitle(game_title, game_name)

        Transfer = GamePageThirdParty(self.driver)
        Transfer.click_button_transfer_window_open()
        center_money, thirdParty_money = Transfer.store_transfer_info()
        thirdPartyResponse = Assertion.assertNotEqualData(thirdParty_money, "-")
        center_money_change, thirdParty_money_change = Transfer.execute_transfer_to_thirdParty_100()
        actual_result = [center_money_change, thirdParty_money_change]
        expect_result = [center_money - 100, thirdParty_money + 100]
        thirdPartyTransferResult = Assertion.assertEqualData(actual_result, expect_result)

        entrance.click_back_button()
        entrance.check_homepage_showing()

        results = [thirdPartyTitle, thirdPartyResponse, thirdPartyTransferResult]
        Assertion.assertFalseResult(results)

    @unittest.skipIf(Project == 'sta', 'vt only')
    def test_15_thirdParty_sexyCasino_login(self):
        game_page = GamePage(self.driver)
        game_name = game_page.switch_game("LiveDealer", "sexyCasino")
        entrance = GamePageCommon(self.driver)
        game_title = entrance.get_thirdParty_title()
        thirdPartyTitle = Assertion.assertThirdPartyTitle(game_title, game_name)

        Transfer = GamePageThirdParty(self.driver)
        Transfer.click_button_transfer_window_open()
        center_money, thirdParty_money = Transfer.store_transfer_info()
        thirdPartyResponse = Assertion.assertNotEqualData(thirdParty_money, "-")
        center_money_change, thirdParty_money_change = Transfer.execute_transfer_to_thirdParty_100()
        actual_result = [center_money_change, thirdParty_money_change]
        expect_result = [center_money - 100, thirdParty_money + 100]
        thirdPartyTransferResult = Assertion.assertEqualData(actual_result, expect_result)

        entrance.click_back_button()
        entrance.check_homepage_showing()

        results = [thirdPartyTitle, thirdPartyResponse, thirdPartyTransferResult]
        Assertion.assertFalseResult(results)

    @unittest.skipIf(Project == 'sta', 'vt only')
    def test_16_thirdParty_sboCasino_login(self):
        game_page = GamePage(self.driver)
        game_name = game_page.switch_game("LiveDealer", "sboCasino")
        entrance = GamePageCommon(self.driver)
        game_title = entrance.get_thirdParty_title()
        thirdPartyTitle = Assertion.assertThirdPartyTitle(game_title, game_name)

        Transfer = GamePageThirdParty(self.driver)
        Transfer.click_button_transfer_window_open()
        center_money, thirdParty_money = Transfer.store_transfer_info()
        thirdPartyResponse = Assertion.assertNotEqualData(thirdParty_money, "-")
        center_money_change, thirdParty_money_change = Transfer.execute_transfer_to_thirdParty_100()
        actual_result = [center_money_change, thirdParty_money_change]
        expect_result = [center_money - 100, thirdParty_money + 100]
        thirdPartyTransferResult = Assertion.assertEqualData(actual_result, expect_result)

        entrance.click_back_button()
        entrance.check_homepage_showing()

        results = [thirdPartyTitle, thirdPartyResponse, thirdPartyTransferResult]
        Assertion.assertFalseResult(results)

    @unittest.skipIf(Project == 'sta', 'vt only')
    def test_17_thirdParty_bbinCasino_login(self):
        game_page = GamePage(self.driver)
        game_name = game_page.switch_game("LiveDealer", "bbinCasino")
        control = GamePageThirdParty(self.driver)
        control.back_to_previous_page()

        entrance = GamePageCommon(self.driver)
        entrance.check_homepage_showing()

    @unittest.skipIf(Project == 'sta', 'vt only')
    def test_18_thirdParty_sv388_login(self):
        game_page = GamePage(self.driver)
        game_name = game_page.switch_game("CockFight", "sv388")
        entrance = GamePageCommon(self.driver)
        game_title = entrance.get_thirdParty_title()
        thirdPartyTitle = Assertion.assertThirdPartyTitle(game_title, game_name)

        Transfer = GamePageThirdParty(self.driver)
        Transfer.click_button_transfer_window_open()
        center_money, thirdParty_money = Transfer.store_transfer_info()
        thirdPartyResponse = Assertion.assertNotEqualData(thirdParty_money, "-")
        center_money_change, thirdParty_money_change = Transfer.execute_transfer_to_thirdParty_100()
        actual_result = [center_money_change, thirdParty_money_change]
        expect_result = [center_money - 100, thirdParty_money + 100]
        thirdPartyTransferResult = Assertion.assertEqualData(actual_result, expect_result)

        entrance.click_back_button()
        entrance.check_homepage_showing()

        results = [thirdPartyTitle, thirdPartyResponse, thirdPartyTransferResult]
        Assertion.assertFalseResult(results)

    @unittest.skipIf(Project == 'vt', 'sta only')
    def test_19_thirdParty_kyPoker_login(self):
        game_page = GamePage(self.driver)
        game_name = game_page.switch_game("Poker", "kyPoker")
        entrance = GamePageCommon(self.driver)
        game_title = entrance.get_thirdParty_title()
        thirdPartyTitle = Assertion.assertThirdPartyTitle(game_title, game_name)

        entrance.click_back_button()
        entrance.check_homepage_showing()

        results = [thirdPartyTitle]
        Assertion.assertFalseResult(results)

    @unittest.skipIf(Project == 'vt', 'sta only')
    def test_20_thirdParty_blPoker_login(self):
        game_page = GamePage(self.driver)
        game_name = game_page.switch_game("Poker", "blPoker")
        entrance = GamePageCommon(self.driver)
        game_title = entrance.get_thirdParty_title()
        thirdPartyTitle = Assertion.assertThirdPartyTitle(game_title, game_name)

        entrance.click_back_button()
        entrance.check_homepage_showing()

        results = [thirdPartyTitle]
        Assertion.assertFalseResult(results)

    @unittest.skipIf(Project == 'vt', 'sta only')
    def test_21_thirdParty_imPoker_login(self):
        game_page = GamePage(self.driver)
        game_name = game_page.switch_game("Poker", "imPoker")
        entrance = GamePageCommon(self.driver)
        game_title = entrance.get_thirdParty_title()
        thirdPartyTitle = Assertion.assertThirdPartyTitle(game_title, game_name)

        entrance.click_back_button()
        entrance.check_homepage_showing()

        results = [thirdPartyTitle]
        Assertion.assertFalseResult(results)

    @unittest.skipIf(Project == 'vt', 'sta only')
    def test_22_thirdParty_leg_login(self):
        game_page = GamePage(self.driver)
        game_name = game_page.switch_game("Poker", "leg")
        entrance = GamePageCommon(self.driver)
        game_title = entrance.get_thirdParty_title()
        thirdPartyTitle = Assertion.assertThirdPartyTitle(game_title, game_name)

        Transfer = GamePageThirdParty(self.driver)
        Transfer.click_button_transfer_window_open()
        center_money, thirdParty_money = Transfer.store_transfer_info()
        Transfer.click_button_transfer_window_close()
        thirdPartyResponse = Assertion.assertNotEqualData(thirdParty_money, "-")

        entrance.click_back_button()
        entrance.check_homepage_showing()

        results = [thirdPartyTitle, thirdPartyResponse]
        Assertion.assertFalseResult(results)

    @unittest.skipIf(Project == 'sta', 'vt only')
    def test_23_thirdParty_v8_login(self):
        game_page = GamePage(self.driver)
        game_name = game_page.switch_game("Poker", "v8")
        entrance = GamePageCommon(self.driver)
        game_title = entrance.get_thirdParty_title()
        thirdPartyTitle = Assertion.assertThirdPartyTitle(game_title, game_name)

        Transfer = GamePageThirdParty(self.driver)
        Transfer.click_button_transfer_window_open()
        center_money, thirdParty_money = Transfer.store_transfer_info()
        thirdPartyResponse = Assertion.assertNotEqualData(thirdParty_money, "-")
        center_money_change, thirdParty_money_change = Transfer.execute_transfer_to_thirdParty_100()
        actual_result = [center_money_change, thirdParty_money_change]
        expect_result = [center_money - 100, thirdParty_money + 100]
        thirdPartyTransferResult = Assertion.assertEqualData(actual_result, expect_result)

        entrance.click_back_button()
        entrance.check_homepage_showing()

        results = [thirdPartyTitle, thirdPartyResponse, thirdPartyTransferResult]
        Assertion.assertFalseResult(results)

    def test_24_thirdParty_mgSlot_login(self):
        game_page = GamePage(self.driver)
        game_name = game_page.switch_game("Slot", "mgSlot")
        entrance = GamePageCommon(self.driver)
        game_title = entrance.get_thirdParty_title()
        thirdPartyTitle = Assertion.assertThirdPartyTitle(game_title, game_name)

        Transfer = GamePageThirdParty(self.driver)
        Transfer.click_slots_first_game()
        Transfer.click_button_transfer_window_open()
        center_money, thirdParty_money = Transfer.store_transfer_info()
        thirdPartyResponse = Assertion.assertNotEqualData(thirdParty_money, "-")
        center_money_change, thirdParty_money_change = Transfer.execute_transfer_to_thirdParty_100()
        actual_result = [center_money_change, thirdParty_money_change]
        expect_result = [center_money - 100, thirdParty_money + 100]
        thirdPartyTransferResult = Assertion.assertEqualData(actual_result, expect_result)

        entrance.click_back_button()
        entrance.check_homepage_showing()

        results = [thirdPartyTitle, thirdPartyResponse, thirdPartyTransferResult]
        Assertion.assertFalseResult(results)

    def test_25_thirdParty_agSlot_login(self):
        game_page = GamePage(self.driver)
        game_name = game_page.switch_game("Slot", "agSlot")
        control = GamePageThirdParty(self.driver)
        control.back_to_previous_page()
        entrance = GamePageCommon(self.driver)
        entrance.check_homepage_showing()

    @unittest.skipIf(Project == 'vt', 'sta only')
    def test_26_thirdParty_bgSlot_login(self):
        game_page = GamePage(self.driver)
        game_name = game_page.switch_game("Slot", "bgSlot")
        entrance = GamePageCommon(self.driver)
        game_title = entrance.get_thirdParty_title()
        thirdPartyTitle = Assertion.assertThirdPartyTitle(game_title, game_name)

        Transfer = GamePageThirdParty(self.driver)
        Transfer.click_button_transfer_window_open()
        center_money, thirdParty_money = Transfer.store_transfer_info()
        thirdPartyResponse = Assertion.assertNotEqualData(thirdParty_money, "-")
        center_money_change, thirdParty_money_change = Transfer.execute_transfer_to_thirdParty_100()
        actual_result = [center_money_change, thirdParty_money_change]
        expect_result = [center_money - 100, thirdParty_money + 100]
        thirdPartyTransferResult = Assertion.assertEqualData(actual_result, expect_result)

        entrance.click_back_button()
        entrance.check_homepage_showing()

        results = [thirdPartyTitle, thirdPartyResponse, thirdPartyTransferResult]
        Assertion.assertFalseResult(results)

    @unittest.skipIf(Project == 'sta', 'vt only')
    def test_27_thirdParty_cq9Slot_login(self):
        game_page = GamePage(self.driver)
        game_name = game_page.switch_game("Slot", "cq9Slot")
        entrance = GamePageCommon(self.driver)
        game_title = entrance.get_thirdParty_title()
        thirdPartyTitle = Assertion.assertThirdPartyTitle(game_title, game_name)

        Transfer = GamePageThirdParty(self.driver)
        Transfer.click_slots_first_game()
        Transfer.click_button_transfer_window_open()
        center_money, thirdParty_money = Transfer.store_transfer_info()
        thirdPartyResponse = Assertion.assertNotEqualData(thirdParty_money, "-")
        center_money_change, thirdParty_money_change = Transfer.execute_transfer_to_thirdParty_100()
        actual_result = [center_money_change, thirdParty_money_change]
        expect_result = [center_money - 100, thirdParty_money + 100]
        thirdPartyTransferResult = Assertion.assertEqualData(actual_result, expect_result)

        entrance.click_back_button()
        entrance.check_homepage_showing()

        results = [thirdPartyTitle, thirdPartyResponse, thirdPartyTransferResult]
        Assertion.assertFalseResult(results)

    @unittest.skipIf(Project == 'sta', 'vt only')
    def test_28_thirdParty_cgSlot_login(self):
        game_page = GamePage(self.driver)
        game_name = game_page.switch_game("Slot", "cgSlot")
        entrance = GamePageCommon(self.driver)
        game_title = entrance.get_thirdParty_title()
        thirdPartyTitle = Assertion.assertThirdPartyTitle(game_title, game_name)

        Transfer = GamePageThirdParty(self.driver)
        Transfer.click_slots_first_game()
        Transfer.click_button_transfer_window_open()
        center_money, thirdParty_money = Transfer.store_transfer_info()
        thirdPartyResponse = Assertion.assertNotEqualData(thirdParty_money, "-")
        center_money_change, thirdParty_money_change = Transfer.execute_transfer_to_thirdParty_100()
        actual_result = [center_money_change, thirdParty_money_change]
        expect_result = [center_money - 100, thirdParty_money + 100]
        thirdPartyTransferResult = Assertion.assertEqualData(actual_result, expect_result)

        entrance.click_back_button()
        entrance.check_homepage_showing()

        results = [thirdPartyTitle, thirdPartyResponse, thirdPartyTransferResult]
        Assertion.assertFalseResult(results)

    @unittest.skipIf(Project == 'sta', 'vt only')
    def test_29_thirdParty_sboSlot_login(self):
        game_page = GamePage(self.driver)
        game_name = game_page.switch_game("Slot", "sboSlot")
        entrance = GamePageCommon(self.driver)
        game_title = entrance.get_thirdParty_title()
        thirdPartyTitle = Assertion.assertThirdPartyTitle(game_title, game_name)

        Transfer = GamePageThirdParty(self.driver)
        Transfer.click_slots_first_game()
        Transfer.click_button_transfer_window_open()
        center_money, thirdParty_money = Transfer.store_transfer_info()
        thirdPartyResponse = Assertion.assertNotEqualData(thirdParty_money, "-")
        center_money_change, thirdParty_money_change = Transfer.execute_transfer_to_thirdParty_100()
        actual_result = [center_money_change, thirdParty_money_change]
        expect_result = [center_money - 100, thirdParty_money + 100]
        thirdPartyTransferResult = Assertion.assertEqualData(actual_result, expect_result)

        entrance.click_back_button()
        entrance.check_homepage_showing()

        results = [thirdPartyTitle, thirdPartyResponse, thirdPartyTransferResult]
        Assertion.assertFalseResult(results)

    @unittest.skipIf(Project == 'sta', 'vt only')
    def test_30_thirdParty_jdbSlot_login(self):
        game_page = GamePage(self.driver)
        game_name = game_page.switch_game("Slot", "jdbSlot")
        entrance = GamePageCommon(self.driver)
        game_title = entrance.get_thirdParty_title()
        thirdPartyTitle = Assertion.assertThirdPartyTitle(game_title, game_name)

        Transfer = GamePageThirdParty(self.driver)
        Transfer.click_slots_first_game()
        Transfer.click_button_transfer_window_open()
        center_money, thirdParty_money = Transfer.store_transfer_info()
        thirdPartyResponse = Assertion.assertNotEqualData(thirdParty_money, "-")
        center_money_change, thirdParty_money_change = Transfer.execute_transfer_to_thirdParty_100()
        actual_result = [center_money_change, thirdParty_money_change]
        expect_result = [center_money - 100, thirdParty_money + 100]
        thirdPartyTransferResult = Assertion.assertEqualData(actual_result, expect_result)

        entrance.click_back_button()
        entrance.check_homepage_showing()

        results = [thirdPartyTitle, thirdPartyResponse, thirdPartyTransferResult]
        Assertion.assertFalseResult(results)

    @unittest.skipIf(Project == 'sta', 'vt only')
    def test_31_thirdParty_pgSlot_login(self):
        game_page = GamePage(self.driver)
        game_name = game_page.switch_game("Slot", "pgSlot")
        entrance = GamePageCommon(self.driver)
        game_title = entrance.get_thirdParty_title()
        thirdPartyTitle = Assertion.assertThirdPartyTitle(game_title, game_name)

        Transfer = GamePageThirdParty(self.driver)
        Transfer.click_slots_first_game()
        Transfer.click_button_transfer_window_open()
        center_money, thirdParty_money = Transfer.store_transfer_info()
        thirdPartyResponse = Assertion.assertNotEqualData(thirdParty_money, "-")
        center_money_change, thirdParty_money_change = Transfer.execute_transfer_to_thirdParty_100()
        actual_result = [center_money_change, thirdParty_money_change]
        expect_result = [center_money - 100, thirdParty_money + 100]
        thirdPartyTransferResult = Assertion.assertEqualData(actual_result, expect_result)

        entrance.click_back_button()
        entrance.check_homepage_showing()

        results = [thirdPartyTitle, thirdPartyResponse, thirdPartyTransferResult]
        Assertion.assertFalseResult(results)

    def test_32_thirdParty_bgFishingMaster_login(self):
        game_page = GamePage(self.driver)
        game_name = game_page.switch_game("Fishing", "bgFishingMaster")
        entrance = GamePageCommon(self.driver)
        game_title = entrance.get_thirdParty_title()
        thirdPartyTitle = Assertion.assertThirdPartyTitle(game_title, game_name)

        Transfer = GamePageThirdParty(self.driver)
        Transfer.click_button_transfer_window_open()
        center_money, thirdParty_money = Transfer.store_transfer_info()
        thirdPartyResponse = Assertion.assertNotEqualData(thirdParty_money, "-")
        center_money_change, thirdParty_money_change = Transfer.execute_transfer_to_thirdParty_100()
        actual_result = [center_money_change, thirdParty_money_change]
        expect_result = [center_money - 100, thirdParty_money + 100]
        thirdPartyTransferResult = Assertion.assertEqualData(actual_result, expect_result)

        entrance.click_back_button()
        entrance.check_homepage_showing()

        results = [thirdPartyTitle, thirdPartyResponse, thirdPartyTransferResult]
        Assertion.assertFalseResult(results)

    def test_33_thirdParty_bgFishing_login(self):
        game_page = GamePage(self.driver)
        game_name = game_page.switch_game("Fishing", "bgFishing")
        entrance = GamePageCommon(self.driver)
        game_title = entrance.get_thirdParty_title()
        thirdPartyTitle = Assertion.assertThirdPartyTitle(game_title, game_name)

        Transfer = GamePageThirdParty(self.driver)
        Transfer.click_button_transfer_window_open()
        center_money, thirdParty_money = Transfer.store_transfer_info()
        thirdPartyResponse = Assertion.assertNotEqualData(thirdParty_money, "-")
        center_money_change, thirdParty_money_change = Transfer.execute_transfer_to_thirdParty_100()
        actual_result = [center_money_change, thirdParty_money_change]
        expect_result = [center_money - 100, thirdParty_money + 100]
        thirdPartyTransferResult = Assertion.assertEqualData(actual_result, expect_result)

        entrance.click_back_button()
        entrance.check_homepage_showing()

        results = [thirdPartyTitle, thirdPartyResponse, thirdPartyTransferResult]
        Assertion.assertFalseResult(results)

    def test_34_thirdParty_agFishing_login(self):
        game_page = GamePage(self.driver)
        game_name = game_page.switch_game("Fishing", "agFishing")
        entrance = GamePageCommon(self.driver)
        game_title = entrance.get_thirdParty_title()
        thirdPartyTitle = Assertion.assertThirdPartyTitle(game_title, game_name)

        entrance.click_back_button()
        entrance.check_homepage_showing()

        results = [thirdPartyTitle]
        Assertion.assertFalseResult(results)

    def test_35_thirdParty_cq9Fishing_login(self):
        game_page = GamePage(self.driver)
        game_name = game_page.switch_game("Fishing", "cq9Fishing")
        entrance = GamePageCommon(self.driver)
        game_title = entrance.get_thirdParty_title()
        thirdPartyTitle = Assertion.assertThirdPartyTitle(game_title, game_name)

        Transfer = GamePageThirdParty(self.driver)
        Transfer.click_slots_first_game()
        Transfer.click_button_transfer_window_open()
        center_money, thirdParty_money = Transfer.store_transfer_info()
        thirdPartyResponse = Assertion.assertNotEqualData(thirdParty_money, "-")
        center_money_change, thirdParty_money_change = Transfer.execute_transfer_to_thirdParty_100()
        actual_result = [center_money_change, thirdParty_money_change]
        expect_result = [center_money - 100, thirdParty_money + 100]
        thirdPartyTransferResult = Assertion.assertEqualData(actual_result, expect_result)

        entrance.click_back_button()
        entrance.check_homepage_showing()

        results = [thirdPartyTitle, thirdPartyResponse, thirdPartyTransferResult]
        Assertion.assertFalseResult(results)

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()
