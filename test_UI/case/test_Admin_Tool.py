import unittest
from config.SetUIConfig import Driver
from test_UI.common.AzureTestPlans import AzureTestPlan
from test_UI.page.LoginPage import LoginPage
from test_UI.page.AdminTool import AdminTool
from test_API.common import AdminTool as AdminTool_API
from utils import Assertion

# member = "alvistest202"
runID = None
member = "qm202104081421"
affiliate = "alvistest201"
parent = "xh0001"
account = "xhadam0000"  # stavins02
single_fast_deposit_amount = 0
single_fast_deposit_promote_amount = 0
batch_fast_deposit_amount = 0
manual_fast_deposit_amount = 0
deposit_amount = 0
exchange_rate_before = 0
exchange_rate_after = 0


class AdminToolTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global runID
        runID = AzureTestPlan().create_test_run(15403, 15404)
        cls.driver = Driver
        login_page = LoginPage(cls.driver)
        login_page.execute_login()

    def test_01_create_affiliate(self):
        global runID, affiliate, parent
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15413, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("user", "affiliates")
        member_info = adminTool.create_affiliate(parent)
        affiliate = member_info[1]

        adminTool.clear_login_period()
        adminTool.query_account(affiliate)
        adminTool.check_member_search_account(affiliate)
        member_result = adminTool.store_member_search_result()

        expect_data = member_info
        actual_data = member_result

        adminTool.close_menu("user")
        self.assertEqual(actual_data, expect_data)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15413, 0)

    def test_02_edit_affiliate_basic_data(self):
        global runID, affiliate
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15414, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("user", "affiliates")
        adminTool.clear_login_period()
        adminTool.query_account(affiliate)
        adminTool.check_member_search_account(affiliate)
        adminTool.click_edit_member()
        adminTool.click_edit_member_tab("basic_data")
        adminTool.click_edit_member_button_status()
        adminTool.click_edit_member_level()
        adminTool.click_edit_member_return_increase()
        adminTool.click_edit_member_button_placebet()
        adminTool.click_edit_member_button_deposit()
        adminTool.click_edit_member_button_withdraw()
        adminTool.click_edit_member_button_transfer()
        edited_basic_data = adminTool.store_edit_member_basic_data()
        adminTool.click_button_save_edit_member()
        adminTool.close_drawer_mask()
        member_basic_data = Assertion.transfer_list_format(
            AdminTool_API.AdminTool().get_account_BasicInfo(affiliate, 2))
        excepted_basic_data = [member_basic_data[2]] + member_basic_data[4:]
        # X = Assertion.transfer_list_format(member_basic_data)
        adminTool.close_menu("user")
        self.assertEqual(excepted_basic_data, edited_basic_data)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15414, 0)

    def test_03_edit_affiliate_bank_card(self):
        global runID, affiliate
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15415, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("user", "affiliates")
        adminTool.clear_login_period()
        adminTool.query_account(affiliate)
        adminTool.check_member_search_account(affiliate)
        adminTool.click_edit_member()
        adminTool.click_edit_member_tab("bank_data")
        adminTool.click_bank_data_button_create()
        bank_name = adminTool.create_bank_card()
        adminTool.close_drawer_mask()
        create_bank_name = AdminTool_API.AdminTool().get_account_BankName(affiliate, 2)

        adminTool.close_menu("user")
        self.assertEqual(create_bank_name, bank_name)
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15415, 0)

    def test_04_edit_affiliate_account_setting(self):
        global runID, affiliate
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15416, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("user", "affiliates")
        adminTool.clear_login_period()
        adminTool.query_account(affiliate)
        adminTool.check_member_search_account(affiliate)
        adminTool.click_edit_member()
        adminTool.click_edit_member_tab("account_setting")
        adminTool.switch_third_party_transfer()
        edited_account_setting = adminTool.store_edit_member_account_setting()
        adminTool.click_button_save_edit_member()
        adminTool.close_drawer_mask()
        account_setting = AdminTool_API.AdminTool().get_account_GameTransferStatus(affiliate, 2)

        adminTool.close_menu("user")
        self.assertEqual(account_setting, edited_account_setting)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15416, 0)

    def test_05_edit_affiliate_modify_password(self):
        global runID, affiliate
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15434, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("user", "affiliates")
        adminTool.clear_login_period()
        adminTool.query_account(affiliate)
        adminTool.check_member_search_account(affiliate)
        adminTool.click_edit_member()
        adminTool.click_edit_member_tab("account_security")
        adminTool.click_account_security_button_password()
        adminTool.modify_password("Aa12345")
        adminTool.close_drawer_mask()
        adminTool.close_menu("user")

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15434, 0)

    def test_06_edit_affiliate_modify_birthday(self):
        global runID, affiliate
        birthday = "2000-11-12"
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15435, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("user", "affiliates")
        adminTool.clear_login_period()
        adminTool.query_account(affiliate)
        adminTool.check_member_search_account(affiliate)
        adminTool.click_edit_member()
        adminTool.click_edit_member_tab("account_security")
        adminTool.click_account_security_button_birthday()
        adminTool.modify_birthday(birthday)
        expect_data = birthday
        actual_data = AdminTool_API.AdminTool().get_account_Birthday(affiliate, 2)

        adminTool.close_drawer_mask()
        adminTool.close_menu("user")

        self.assertEqual(actual_data, expect_data)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15435, 0)

    def test_07_edit_affiliate_summarized_log(self):
        global runID, affiliate
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15436, 1)
        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("user", "affiliates")
        adminTool.clear_login_period()
        adminTool.query_account(affiliate)
        adminTool.check_member_search_account(affiliate)
        adminTool.click_edit_member()
        adminTool.click_edit_member_tab("summarized_log")
        adminTool.click_button_edit_member_search()

        expect_data = adminTool.store_edit_member_summarized_log()
        actual_data = AdminTool_API.AdminTool().get_account_IntegratedRecord(affiliate, 2)

        adminTool.close_drawer_mask()
        adminTool.close_menu("user")

        self.assertEqual(actual_data, expect_data)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15436, 0)

    def test_08_edit_affiliate_change_log(self):
        global runID, affiliate
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15437, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("user", "affiliates")
        adminTool.clear_login_period()
        adminTool.query_account(affiliate)
        adminTool.check_member_search_account(affiliate)
        adminTool.click_edit_member()
        adminTool.click_edit_member_tab("change_log")
        adminTool.click_button_edit_member_search()

        expect_data = adminTool.store_edit_member_change_log()
        actual_data = AdminTool_API.AdminTool().get_account_ChangeColumn(affiliate, 2)

        adminTool.close_drawer_mask()
        adminTool.close_menu("user")

        self.assertEqual(actual_data, expect_data)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15437, 0)

    def test_09_create_member(self):
        global runID, member
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15438, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("user", "member")
        member_info = adminTool.create_member(affiliate)
        member = member_info[1]

        adminTool.clear_login_period()
        adminTool.query_account(member)
        adminTool.check_member_search_account(member)
        member_result = adminTool.store_member_search_result()

        expect_data = member_info
        actual_data = member_result

        adminTool.close_menu("user")
        self.assertEqual(actual_data, expect_data)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15438, 0)

    def test_10_edit_member_basic_data(self):
        global runID, member
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15439, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("user", "member")
        adminTool.clear_login_period()
        adminTool.query_account(member)
        adminTool.check_member_search_account(member)
        adminTool.click_edit_member()
        adminTool.click_edit_member_tab("basic_data")
        adminTool.click_edit_member_button_status()
        adminTool.click_edit_member_level()
        adminTool.click_edit_member_return_increase()
        adminTool.click_edit_member_button_placebet()
        adminTool.click_edit_member_button_deposit()
        adminTool.click_edit_member_button_withdraw()
        adminTool.click_edit_member_button_transfer()
        edited_basic_data = adminTool.store_edit_member_basic_data()
        adminTool.click_button_save_edit_member()
        adminTool.close_drawer_mask()
        member_basic_data = Assertion.transfer_list_format(AdminTool_API.AdminTool().get_account_BasicInfo(member, 1))
        excepted_basic_data = [member_basic_data[2]] + member_basic_data[4:]

        adminTool.close_menu("user")
        self.assertEqual(excepted_basic_data, edited_basic_data)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15439, 0)

    def test_11_edit_member_bank_card(self):
        global runID, member
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15440, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("user", "member")
        adminTool.clear_login_period()
        adminTool.query_account(member)
        adminTool.check_member_search_account(member)
        adminTool.click_edit_member()
        adminTool.click_edit_member_tab("bank_data")
        adminTool.click_bank_data_button_create()
        bank_name = adminTool.create_bank_card()
        adminTool.close_drawer_mask()
        create_bank_name = AdminTool_API.AdminTool().get_account_BankName(member, 1)

        adminTool.close_menu("user")
        self.assertEqual(create_bank_name, bank_name)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15440, 0)

    def test_12_edit_member_account_setting(self):
        global runID, member
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15441, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("user", "member")
        adminTool.clear_login_period()
        adminTool.query_account(member)
        adminTool.check_member_search_account(member)
        adminTool.click_edit_member()
        adminTool.click_edit_member_tab("account_setting")
        adminTool.switch_third_party_transfer()
        edited_account_setting = adminTool.store_edit_member_account_setting()
        adminTool.click_button_save_edit_member()
        adminTool.close_drawer_mask()
        account_setting = AdminTool_API.AdminTool().get_account_GameTransferStatus(member, 1)

        adminTool.close_menu("user")
        self.assertEqual(account_setting, edited_account_setting)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15441, 0)

    def test_13_edit_member_modify_password(self):
        global runID, member
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15442, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("user", "member")
        adminTool.clear_login_period()
        adminTool.query_account(member)
        adminTool.check_member_search_account(member)
        adminTool.click_edit_member()
        adminTool.click_edit_member_tab("account_security")
        adminTool.click_account_security_button_password()
        adminTool.modify_password("Aa12345")
        adminTool.close_drawer_mask()
        adminTool.close_menu("user")

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15442, 0)

    def test_14_edit_member_modify_birthday(self):
        global runID, member
        birthday = "2000-11-12"
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15443, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("user", "member")
        adminTool.clear_login_period()
        adminTool.query_account(member)
        adminTool.check_member_search_account(member)
        adminTool.click_edit_member()
        adminTool.click_edit_member_tab("account_security")
        adminTool.click_account_security_button_birthday()
        adminTool.modify_birthday(birthday)
        expect_data = birthday
        actual_data = AdminTool_API.AdminTool().get_account_Birthday(member, 1)

        adminTool.close_drawer_mask()
        adminTool.close_menu("user")

        self.assertEqual(actual_data, expect_data)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15443, 0)

    def test_15_edit_member_summarized_log(self):
        global runID, member
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15444, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("user", "member")
        adminTool.clear_login_period()
        adminTool.query_account(member)
        adminTool.check_member_search_account(member)
        adminTool.click_edit_member()
        adminTool.click_edit_member_tab("summarized_log")
        adminTool.click_button_edit_member_search()

        expect_data = adminTool.store_edit_member_summarized_log()
        actual_data = AdminTool_API.AdminTool().get_account_IntegratedRecord(member, 1)

        adminTool.close_drawer_mask()
        adminTool.close_menu("user")

        self.assertEqual(actual_data, expect_data)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15444, 0)

    def test_16_edit_member_change_log(self):
        global runID, member
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15445, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("user", "member")
        adminTool.clear_login_period()
        adminTool.query_account(member)
        adminTool.check_member_search_account(member)
        adminTool.click_edit_member()
        adminTool.click_edit_member_tab("change_log")
        adminTool.click_button_edit_member_search()

        expect_data = adminTool.store_edit_member_change_log()
        actual_data = AdminTool_API.AdminTool().get_account_ChangeColumn(member, 1)

        adminTool.close_drawer_mask()
        adminTool.close_menu("user")

        self.assertEqual(actual_data, expect_data)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15445, 0)

    def test_17_fast_deposit_single(self):
        global runID, account, single_fast_deposit_amount
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15446, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        single_fast_deposit_amount = adminTool.random_deposit_amount()
        adminTool.switch_function("transaction", "fast_deposit")
        adminTool.submit_query()
        adminTool.check_search_loading()
        adminTool.expand_subtotal()
        subtotal_before_deposit = adminTool.store_fast_deposit_subtotal()
        adminTool.click_fast_deposit()

        # 單筆作業：single, 批次作業：batch, 人工充值：manual
        adminTool.execute_fast_deposit("single", account, single_fast_deposit_amount)
        subtotal_after_deposit = adminTool.store_fast_deposit_subtotal()
        adminTool.collapse_subtotal()

        adminTool.close_menu("transaction")
        self.assertEqual(type(subtotal_after_deposit[2]),
                         type(subtotal_before_deposit[2] + float(single_fast_deposit_amount)))

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15446, 0)

    def test_18_fast_deposit_batch(self):
        global runID, account, batch_fast_deposit_amount
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15447, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        batch_fast_deposit_amount = adminTool.random_deposit_amount()
        adminTool.switch_function("transaction", "fast_deposit")
        adminTool.submit_query()
        adminTool.check_search_loading()
        adminTool.expand_subtotal()
        subtotal_before_deposit = adminTool.store_fast_deposit_subtotal()
        adminTool.click_fast_deposit()

        # 單筆作業：single, 批次作業：batch, 人工充值：manual
        adminTool.execute_fast_deposit("batch", account, batch_fast_deposit_amount)
        subtotal_after_deposit = adminTool.store_fast_deposit_subtotal()
        adminTool.collapse_subtotal()

        adminTool.close_menu("transaction")
        self.assertEqual(type(subtotal_after_deposit[2]),
                         type(subtotal_before_deposit[2] + float(batch_fast_deposit_amount)))

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15447, 0)

    def test_19_fast_deposit_manual(self):
        global runID, account, manual_fast_deposit_amount
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15448, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        manual_fast_deposit_amount = adminTool.random_deposit_amount()
        adminTool.switch_function("transaction", "fast_deposit")
        adminTool.submit_query()
        adminTool.check_search_loading()
        adminTool.expand_subtotal()
        subtotal_before_deposit = adminTool.store_fast_deposit_subtotal()
        adminTool.click_fast_deposit()

        # 單筆作業：single, 批次作業：batch, 人工充值：manual
        adminTool.execute_fast_deposit("manual", account, manual_fast_deposit_amount)
        subtotal_after_deposit = adminTool.store_fast_deposit_subtotal()
        adminTool.collapse_subtotal()

        adminTool.close_menu("transaction")
        self.assertEqual(type(subtotal_after_deposit[2]),
                         type(subtotal_before_deposit[2] + float(manual_fast_deposit_amount)))

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15448, 0)

    def test_20_create_fast_deposit_setting(self):
        global runID
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15449, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("transaction", "quick_deposit_setting")
        fast_deposit_setting = adminTool.create_fast_deposit_setting()
        fast_deposit_setting_result = adminTool.search_fast_deposit_setting()

        adminTool.close_menu("transaction")
        self.assertEqual(fast_deposit_setting_result, fast_deposit_setting)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15449, 0)

    # 6598 [Admin Tool][DB] 新營運報表/ 代理報表-"平台利潤"欄位顯示數值比所參考欄位的計算結果少0.01
    def test_21_bet_log_subtotal(self):
        global runID
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15450, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("filesearch", "bet")
        adminTool.clear_query_period()
        adminTool.fill_query_date()
        adminTool.submit_query()
        adminTool.check_search_loading()
        adminTool.expand_subtotal()
        subtotal_bet = adminTool.store_bet_subtotal()
        subtotal_bet_log = Assertion.transfer_list_format(AdminTool_API.AdminTool().get_ThirdPartyBetLog_Summary())

        adminTool.close_menu("filesearch")
        self.assertEqual(subtotal_bet, subtotal_bet_log)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15450, 0)

    def test_22_bet_log_filter_source(self):
        global runID
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15451, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("filesearch", "bet")
        adminTool.clear_query_period()
        adminTool.fill_query_date()

        bet_sources = ["web", "app"]
        for bet_source in bet_sources:
            adminTool.click_field_bet_source_search()
            option_bet_source = adminTool.click_option_bet_source_search(bet_source)
            adminTool.submit_query()
            adminTool.check_search_loading()
            column_bet_sources = adminTool.store_column_bet_source()

            for column_bet_source in column_bet_sources:
                print(column_bet_source.text, option_bet_source)
                self.assertEqual(column_bet_source.text, option_bet_source)

        adminTool.click_field_bet_source_search()
        adminTool.click_option_bet_source_search("all")
        adminTool.submit_query()
        adminTool.check_search_loading()

        adminTool.close_menu("filesearch")

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15451, 0)

    def test_23_bet_log_filter_status(self):
        global runID
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15452, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("filesearch", "bet")
        adminTool.clear_query_period()
        adminTool.fill_query_date()

        bet_status = ["settled", "unsettled", "cancel", "early"]
        for status in bet_status:
            adminTool.click_field_bet_status_search()
            option_bet_status = adminTool.click_option_bet_status_search(status)
            adminTool.submit_query()
            adminTool.check_search_loading()
            column_bet_status = adminTool.store_column_bet_status()

            for bet_status in column_bet_status:
                print(bet_status.text, option_bet_status)
                self.assertEqual(bet_status.text, option_bet_status)

        adminTool.click_field_bet_status_search()
        adminTool.click_option_bet_status_search("all")
        adminTool.submit_query()
        adminTool.check_search_loading()

        adminTool.close_menu("filesearch")

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15452, 0)

    def test_24_bet_log_filter_winLoss(self):
        global runID
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15453, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("filesearch", "bet")
        adminTool.clear_query_period()
        adminTool.fill_query_date()

        bet_winLoss = ["win", "loss", "tie"]
        for winLoss in bet_winLoss:
            adminTool.click_field_bet_winLoss_search()
            option_bet_winLoss = adminTool.click_option_bet_winLoss_search(winLoss)
            adminTool.submit_query()
            adminTool.check_search_loading()
            column_bet_winLoss = adminTool.store_column_bet_winLoss()

            for bet_winLoss in column_bet_winLoss:
                print(bet_winLoss.text, option_bet_winLoss)
                self.assertEqual(bet_winLoss.text, option_bet_winLoss)

        adminTool.click_field_bet_winLoss_search()
        adminTool.click_option_bet_winLoss_search("all")
        adminTool.submit_query()
        adminTool.check_search_loading()

        adminTool.close_menu("filesearch")

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15453, 0)

    def test_25_bet_log_filter_account(self):
        global runID, account
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15454, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("filesearch", "bet")
        adminTool.clear_query_period()
        adminTool.fill_query_date()

        adminTool.query_account(account)
        adminTool.check_bet_search_account(account)
        column_bet_accounts = adminTool.store_column_bet_account()

        for column_bet_account in column_bet_accounts:
            print(column_bet_account.text, account)
            self.assertEqual(column_bet_account.text, account)

        adminTool.close_menu("filesearch")

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15454, 0)

    # 6598 [Admin Tool][DB] 新營運報表/ 代理報表-"平台利潤"欄位顯示數值比所參考欄位的計算結果少0.01
    def test_26_transaction_log_subtotal(self):
        global runID
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15455, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("transaction", "transaction")
        adminTool.submit_query()
        adminTool.check_search_loading()
        adminTool.expand_subtotal()
        subtotal_transaction = adminTool.store_transaction_subtotal()
        subtotal_transaction_log = Assertion.transfer_list_format(
            AdminTool_API.AdminTool().get_TransactionLog_Summary())

        adminTool.close_menu("transaction")

        self.assertEqual(subtotal_transaction, subtotal_transaction_log)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15455, 0)

    def test_27_transaction_log_filter_type(self):
        global runID
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15456, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("transaction", "transaction")

        transaction_types = ["deposit", "dispense"]
        for transaction_type in transaction_types:
            adminTool.click_field_transaction_type_search()
            option_transaction = adminTool.click_option_transaction_type_search(transaction_type)
            adminTool.submit_query()
            adminTool.check_search_loading()
            column_transaction_types = adminTool.store_column_transaction_type()

            for column_transaction_type in column_transaction_types:
                print(column_transaction_type.text, option_transaction)
                self.assertEqual(column_transaction_type.text, option_transaction)

        adminTool.close_menu("transaction")

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15456, 0)

    def test_28_transaction_log_filter_account(self):
        global runID, account
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15457, 1)
        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("transaction", "transaction")

        adminTool.query_account(account)
        adminTool.check_transaction_search_account(account)
        column_transaction_accounts = adminTool.store_column_transaction_account()

        for column_transaction_account in column_transaction_accounts:
            print(column_transaction_account.text, account)
            self.assertEqual(column_transaction_account.text, account)

        adminTool.close_menu("transaction")

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15457, 0)

    def test_29_activity_type_edit(self):
        global runID
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15458, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        name = adminTool.generate_name()
        adminTool.switch_function("activity", "activity_type")
        adminTool.click_button_activity_type_edit()
        adminTool.input_field_activity_type_edit_name(name)
        adminTool.click_button_activity_type_edit_status()
        edit_name = adminTool.store_field_activity_type_edit_name()
        edit_status = adminTool.store_button_activity_type_edit_status()
        adminTool.click_button_activity_type_edit_submit()
        actual_result = adminTool.store_activity_type_config()
        expect_result = [edit_name, edit_status]

        adminTool.close_menu("activity")
        self.assertEqual(actual_result, expect_result)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15458, 0)

    def test_30_create_activity(self):
        global runID
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15459, 1)
        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        name = adminTool.generate_name()
        adminTool.switch_function("activity", "activity_management")

        activity = adminTool.create_activity(name)
        adminTool.query_activity_name("qa" + name)
        adminTool.check_search_loading()
        result_name = adminTool.store_column_activity_name()
        result_type = adminTool.store_column_activity_type()
        expect_result_1 = [activity[0], activity[1]]
        actual_result_1 = [result_name, result_type]

        adminTool.click_activity_result_name()
        adminTool.click_tab_activity_detail_rule()
        detail = adminTool.store_activity_detail()
        expect_result_2 = [activity[2], activity[3], activity[4], activity[5], activity[6]]
        actual_result_2 = detail

        adminTool.close_drawer_mask()
        adminTool.close_menu("activity")
        self.assertEqual(actual_result_1, expect_result_1)
        self.assertEqual(actual_result_2, expect_result_2)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15459, 0)

    def test_31_edit_activity(self):
        global runID
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15460, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        name = adminTool.generate_name()
        adminTool.switch_function("activity", "activity_management")
        adminTool.click_field_search_activity_status()
        adminTool.click_option_search_activity_status_standby()
        adminTool.submit_query()
        adminTool.check_search_loading()

        activity = adminTool.edit_activity(name)
        adminTool.query_activity_name("qa" + name)
        adminTool.check_search_loading()
        result_name = adminTool.store_column_activity_name()
        result_type = adminTool.store_column_activity_type()
        actual_result = [result_name, result_type]
        expect_result = activity

        adminTool.close_menu("activity")
        self.assertEqual(actual_result, expect_result)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15460, 0)

    def test_32_edit_activity_rule(self):
        global runID
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15461, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("activity", "activity_management")
        adminTool.click_field_search_activity_status()
        adminTool.click_option_search_activity_status_standby()
        adminTool.submit_query()
        adminTool.check_search_loading()
        activity_name = adminTool.store_column_activity_name()

        activity = adminTool.edit_activity_rule()
        adminTool.query_activity_name(activity_name)
        adminTool.check_search_loading()
        adminTool.click_activity_result_name()
        adminTool.click_tab_activity_detail_rule()
        detail = adminTool.store_activity_detail()
        actual_result = detail
        expect_result = activity

        adminTool.close_drawer_mask()
        adminTool.close_menu("activity")
        self.assertEqual(actual_result, expect_result)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15461, 0)

    def test_33_add_banner_carousel_web(self):
        global runID
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15462, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        name = adminTool.generate_name()
        adminTool.switch_function("shop", "banner")
        adminTool.click_tab_banner_web()
        adminTool.click_button_add_banner_carousel()
        adminTool.input_field_add_banner_link(name)
        adminTool.set_banner_display_period()
        adminTool.upload_banner_carousel()
        adminTool.click_button_add_banner_submit()
        actual_result = AdminTool_API.AdminTool().check_BannerSetting_Item("web", "sliders", "TargetUrl", name)

        adminTool.close_menu("shop")
        self.assertTrue(actual_result, True)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15462, 0)

    def test_34_edit_banner_carousel_web(self):
        global runID
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15463, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        name = adminTool.generate_name()
        num = AdminTool_API.AdminTool().get_BannerSetting_Quantity("web", "sliders")

        adminTool.switch_function("shop", "banner")
        adminTool.click_tab_banner_web()
        adminTool.click_button_edit_banner_carousel(num)
        adminTool.input_field_add_banner_link(name)
        adminTool.click_button_add_banner_submit()
        actual_result = AdminTool_API.AdminTool().check_BannerSetting_Item("web", "sliders", "TargetUrl", name)
        self.assertTrue(actual_result, True)

        adminTool.click_button_delete_banner_carousel(num)
        adminTool.click_button_delete_banner_confirm()
        actual_result = AdminTool_API.AdminTool().check_BannerSetting_Item("web", "sliders", "TargetUrl", name)

        adminTool.close_menu("shop")
        self.assertFalse(actual_result, False)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15463, 0)

    def test_35_add_banner_game_web(self):
        global runID
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15464, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        name = adminTool.generate_name()
        adminTool.switch_function("shop", "banner")
        adminTool.click_tab_banner_web()
        adminTool.click_button_add_banner_game()
        adminTool.input_field_add_banner_link(name)
        adminTool.set_banner_display_period()
        adminTool.upload_banner_game()
        adminTool.click_button_add_banner_submit()
        actual_result = AdminTool_API.AdminTool().check_BannerSetting_Item("web", "gameButtons", "TargetUrl", name)

        adminTool.close_menu("shop")
        self.assertTrue(actual_result, True)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15464, 0)

    def test_36_edit_banner_game_web(self):
        global runID
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15465, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        name = adminTool.generate_name()
        num = AdminTool_API.AdminTool().get_BannerSetting_Quantity("web", "gameButtons")

        adminTool.switch_function("shop", "banner")
        adminTool.click_tab_banner_web()
        adminTool.click_button_edit_banner_game(num)
        adminTool.input_field_add_banner_link(name)
        adminTool.click_button_add_banner_submit()
        actual_result = AdminTool_API.AdminTool().check_BannerSetting_Item("web", "gameButtons", "TargetUrl", name)
        self.assertTrue(actual_result, True)

        adminTool.click_button_delete_banner_game(num)
        adminTool.click_button_delete_banner_confirm()
        actual_result = AdminTool_API.AdminTool().check_BannerSetting_Item("web", "gameButtons", "TargetUrl", name)

        adminTool.close_menu("shop")
        self.assertFalse(actual_result, False)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15465, 0)

    def test_37_add_banner_carousel_h5(self):
        global runID
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15466, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        name = adminTool.generate_name()
        adminTool.switch_function("shop", "banner")
        adminTool.click_tab_banner_h5()
        adminTool.click_button_add_banner_carousel()
        adminTool.input_field_add_banner_link(name)
        adminTool.set_banner_display_period()
        adminTool.upload_banner_carousel()
        adminTool.click_button_add_banner_submit()
        actual_result = AdminTool_API.AdminTool().check_BannerSetting_Item("h5", "sliders", "TargetUrl", name)

        adminTool.close_menu("shop")
        self.assertTrue(actual_result, True)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15466, 0)

    def test_38_edit_banner_carousel_h5(self):
        global runID
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15467, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        name = adminTool.generate_name()
        num = AdminTool_API.AdminTool().get_BannerSetting_Quantity("h5", "sliders")

        adminTool.switch_function("shop", "banner")
        adminTool.click_tab_banner_h5()
        adminTool.click_button_edit_banner_carousel(num)
        adminTool.input_field_add_banner_link(name)
        adminTool.click_button_add_banner_submit()
        actual_result = AdminTool_API.AdminTool().check_BannerSetting_Item("h5", "sliders", "TargetUrl", name)
        self.assertTrue(actual_result, True)

        adminTool.click_button_delete_banner_carousel(num)
        adminTool.click_button_delete_banner_confirm()
        actual_result = AdminTool_API.AdminTool().check_BannerSetting_Item("h5", "sliders", "TargetUrl", name)

        adminTool.close_menu("shop")
        self.assertFalse(actual_result, False)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15467, 0)

    def test_39_add_banner_game_h5(self):
        global runID
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15468, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        name = adminTool.generate_name()
        adminTool.switch_function("shop", "banner")
        adminTool.click_tab_banner_h5()
        adminTool.click_button_add_banner_game()
        adminTool.input_field_add_banner_link(name)
        adminTool.set_banner_display_period()
        adminTool.upload_banner_game()
        adminTool.click_button_add_banner_submit()
        actual_result = AdminTool_API.AdminTool().check_BannerSetting_Item("h5", "gameButtons", "TargetUrl", name)

        adminTool.close_menu("shop")
        self.assertTrue(actual_result, True)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15468, 0)

    def test_40_edit_banner_game_h5(self):
        global runID
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15469, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        name = adminTool.generate_name()
        num = AdminTool_API.AdminTool().get_BannerSetting_Quantity("h5", "gameButtons")

        adminTool.switch_function("shop", "banner")
        adminTool.click_tab_banner_h5()
        adminTool.click_button_edit_banner_game(num)
        adminTool.input_field_add_banner_link(name)
        adminTool.click_button_add_banner_submit()
        actual_result = AdminTool_API.AdminTool().check_BannerSetting_Item("h5", "gameButtons", "TargetUrl", name)
        self.assertTrue(actual_result, True)

        adminTool.click_button_delete_banner_game(num)
        adminTool.click_button_delete_banner_confirm()
        actual_result = AdminTool_API.AdminTool().check_BannerSetting_Item("h5", "gameButtons", "TargetUrl", name)
        self.assertFalse(actual_result, False)

        adminTool.close_menu("shop")

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15469, 0)

    def test_41_add_banner_carousel_ios(self):
        global runID
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15470, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        name = adminTool.generate_name()
        adminTool.switch_function("shop", "banner")
        adminTool.click_tab_banner_ios()
        adminTool.click_button_add_banner_carousel()
        adminTool.input_field_add_banner_link(name)
        adminTool.set_banner_display_period()
        adminTool.upload_banner_carousel()
        adminTool.click_button_add_banner_submit()
        actual_result = AdminTool_API.AdminTool().check_BannerSetting_Item("ios", "sliders", "TargetUrl", name)
        self.assertTrue(actual_result, True)

        adminTool.close_menu("shop")

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15470, 0)

    def test_42_edit_banner_carousel_ios(self):
        global runID
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15471, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        name = adminTool.generate_name()
        num = AdminTool_API.AdminTool().get_BannerSetting_Quantity("ios", "sliders")

        adminTool.switch_function("shop", "banner")
        adminTool.click_tab_banner_ios()
        adminTool.click_button_edit_banner_carousel(num)
        adminTool.input_field_add_banner_link(name)
        adminTool.click_button_add_banner_submit()
        actual_result = AdminTool_API.AdminTool().check_BannerSetting_Item("ios", "sliders", "TargetUrl", name)
        self.assertTrue(actual_result, True)

        adminTool.click_button_delete_banner_carousel(num)
        adminTool.click_button_delete_banner_confirm()
        actual_result = AdminTool_API.AdminTool().check_BannerSetting_Item("h5", "sliders", "TargetUrl", name)
        self.assertFalse(actual_result, False)

        adminTool.close_menu("shop")

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15471, 0)

    def test_43_add_banner_game_ios(self):
        global runID
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15472, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        name = adminTool.generate_name()
        adminTool.switch_function("shop", "banner")
        adminTool.click_tab_banner_ios()
        adminTool.click_button_add_banner_game()
        adminTool.input_field_add_banner_link(name)
        adminTool.set_banner_display_period()
        adminTool.upload_banner_game()
        adminTool.click_button_add_banner_submit()
        actual_result = AdminTool_API.AdminTool().check_BannerSetting_Item("ios", "gameButtons", "TargetUrl", name)
        self.assertTrue(actual_result, True)

        adminTool.close_menu("shop")

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15472, 0)

    def test_44_edit_banner_game_ios(self):
        global runID
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15473, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        name = adminTool.generate_name()
        num = AdminTool_API.AdminTool().get_BannerSetting_Quantity("ios", "gameButtons")

        adminTool.switch_function("shop", "banner")
        adminTool.click_tab_banner_ios()
        adminTool.click_button_edit_banner_game(num)
        adminTool.input_field_add_banner_link(name)
        adminTool.click_button_add_banner_submit()
        actual_result = AdminTool_API.AdminTool().check_BannerSetting_Item("ios", "gameButtons", "TargetUrl", name)
        self.assertTrue(actual_result, True)

        adminTool.click_button_delete_banner_game(num)
        adminTool.click_button_delete_banner_confirm()
        actual_result = AdminTool_API.AdminTool().check_BannerSetting_Item("h5", "sliders", "TargetUrl", name)
        self.assertFalse(actual_result, False)

        adminTool.close_menu("shop")

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15473, 0)

    def test_45_add_banner_carousel_android(self):
        global runID
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15474, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        name = adminTool.generate_name()
        adminTool.switch_function("shop", "banner")
        adminTool.click_tab_banner_android()
        adminTool.click_button_add_banner_carousel()
        adminTool.input_field_add_banner_link(name)
        adminTool.set_banner_display_period()
        adminTool.upload_banner_carousel()
        adminTool.click_button_add_banner_submit()
        actual_result = AdminTool_API.AdminTool().check_BannerSetting_Item("android", "sliders", "TargetUrl", name)
        self.assertTrue(actual_result, True)

        adminTool.close_menu("shop")

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15474, 0)

    def test_46_edit_banner_carousel_android(self):
        global runID
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15475, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        name = adminTool.generate_name()
        num = AdminTool_API.AdminTool().get_BannerSetting_Quantity("android", "sliders")

        adminTool.switch_function("shop", "banner")
        adminTool.click_tab_banner_android()
        adminTool.click_button_edit_banner_carousel(num)
        adminTool.input_field_add_banner_link(name)
        adminTool.click_button_add_banner_submit()
        actual_result = AdminTool_API.AdminTool().check_BannerSetting_Item("android", "sliders", "TargetUrl", name)
        self.assertTrue(actual_result, True)

        adminTool.click_button_delete_banner_carousel(num)
        adminTool.click_button_delete_banner_confirm()
        actual_result = AdminTool_API.AdminTool().check_BannerSetting_Item("android", "sliders", "TargetUrl", name)
        self.assertFalse(actual_result, False)

        adminTool.close_menu("shop")

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15475, 0)

    def test_47_add_banner_game_android(self):
        global runID
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15476, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        name = adminTool.generate_name()
        adminTool.switch_function("shop", "banner")
        adminTool.click_tab_banner_android()
        adminTool.click_button_add_banner_game()
        adminTool.input_field_add_banner_link(name)
        adminTool.set_banner_display_period()
        adminTool.upload_banner_game()
        adminTool.click_button_add_banner_submit()
        actual_result = AdminTool_API.AdminTool().check_BannerSetting_Item("android", "gameButtons", "TargetUrl", name)
        self.assertTrue(actual_result, True)

        adminTool.close_menu("shop")

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15476, 0)

    def test_48_edit_banner_game_android(self):
        global runID
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15477, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        name = adminTool.generate_name()
        num = AdminTool_API.AdminTool().get_BannerSetting_Quantity("android", "gameButtons")

        adminTool.switch_function("shop", "banner")
        adminTool.click_tab_banner_android()
        adminTool.click_button_edit_banner_game(num)
        adminTool.input_field_add_banner_link(name)
        adminTool.click_button_add_banner_submit()
        actual_result = AdminTool_API.AdminTool().check_BannerSetting_Item("android", "gameButtons", "TargetUrl", name)
        self.assertTrue(actual_result, True)

        adminTool.click_button_delete_banner_game(num)
        adminTool.click_button_delete_banner_confirm()
        actual_result = AdminTool_API.AdminTool().check_BannerSetting_Item("android", "gameButtons", "TargetUrl", name)
        self.assertFalse(actual_result, False)

        adminTool.close_menu("shop")

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15477, 0)

    # 6598 [Admin Tool][DB] 新營運報表/ 代理報表-"平台利潤"欄位顯示數值比所參考欄位的計算結果少0.01
    def test_49_operation_report_affiliate_log_sum(self):
        global runID, account
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15478, 1)
        adminTool = AdminTool(self.driver)
        adminTool.switch_function("barchart", "affiliate")

        adminTool.expand_subtotal()
        subtotal_affiliate_log = adminTool.store_affiliate_log_subtotal()
        adminTool.collapse_subtotal()
        adminTool.switch_pagination_displayed(100)
        sum_affiliate_log = adminTool.store_affiliate_report_result()

        adminTool.close_menu("barchart")
        self.assertEqual(subtotal_affiliate_log, sum_affiliate_log)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15478, 0)

    # 6598 [Admin Tool][DB] 新營運報表/ 代理報表-"平台利潤"欄位顯示數值比所參考欄位的計算結果少0.01
    def test_50_operation_report_member_log_sum(self):
        global runID, account
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15479, 1)

        adminTool = AdminTool(self.driver)
        adminTool.switch_function("barchart", "member")

        adminTool.expand_subtotal()
        adminTool.query_account('xhadam0000')
        adminTool.submit_query()
        subtotal_member_log = adminTool.store_member_log_subtotal()
        adminTool.collapse_subtotal()
        adminTool.switch_pagination_displayed(100)
        sum_member_log = adminTool.store_member_report_result()
        print('subtotal_member_log')
        print(subtotal_member_log)
        print('sum_member_log')
        print(sum_member_log)
        adminTool.close_menu("barchart")
        self.assertEqual(subtotal_member_log, sum_member_log)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15479, 0)

    # 6598 [Admin Tool][DB] 新營運報表/ 代理報表-"平台利潤"欄位顯示數值比所參考欄位的計算結果少0.01
    def test_51_operation_report_agent_log_sum(self):
        global runID, account
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15480, 1)

        adminTool = AdminTool(self.driver)
        adminTool.switch_function("barchart", "agent")

        adminTool.expand_subtotal()
        subtotal_agent_log = adminTool.store_agent_log_subtotal()
        adminTool.collapse_subtotal()
        sum_agent_log = adminTool.store_agent_report_result()

        adminTool.close_menu("barchart")
        self.assertEqual(subtotal_agent_log, sum_agent_log)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15480, 0)

    def test_52_transaction_log_sum(self):
        global runID
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15481, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("transaction", "transaction")

        count = 1
        transaction_types = ["deposit", "dispense"]
        for transaction_type in transaction_types:
            adminTool.click_field_transaction_type_search()
            adminTool.click_option_transaction_type_search(transaction_type)
            adminTool.query_account('xhadam0000')
            adminTool.submit_query()
            adminTool.check_search_loading()
            adminTool.expand_subtotal()
            subtotal_transaction = adminTool.store_transaction_subtotal()
            adminTool.collapse_subtotal()
            adminTool.switch_pagination_displayed(100)
            adminTool.check_search_loading()
            column_transaction_amount = adminTool.store_transaction_log_amount()

            self.assertEqual(subtotal_transaction[count], column_transaction_amount)
            count += 1

        adminTool.close_menu("transaction")

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15481, 0)

    # 6598 [Admin Tool][DB] 新營運報表/ 代理報表-"平台利潤"欄位顯示數值比所參考欄位的計算結果少0.01
    def test_53_bet_log_sum(self):
        global runID
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15482, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("filesearch", "bet")

        adminTool.clear_query_period()
        adminTool.fill_query_date()
        adminTool.click_option_status_type_search('thirdparty-bet', 1)
        adminTool.submit_query()
        adminTool.check_search_loading()
        adminTool.expand_subtotal()
        subtotal_bet = adminTool.store_bet_subtotal()
        actual_result = [subtotal_bet[0], subtotal_bet[2], subtotal_bet[3], subtotal_bet[4]]
        adminTool.collapse_subtotal()
        adminTool.switch_pagination_displayed(100)
        adminTool.check_search_loading()
        subtotal_bet_log = adminTool.store_bet_log_result()

        adminTool.close_menu("filesearch")
        self.assertEqual(actual_result, subtotal_bet_log)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15482, 0)

    def test_54_insert_data_to_turnover_pending_list(self):
        global runID, account, single_fast_deposit_amount
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15483, 1)
        single_fast_deposit_amount = str('%.2f' % int(single_fast_deposit_amount))

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("transaction", "turnover")
        adminTool.query_turnover(account)
        adminTool.check_search_loading()
        amount, required = adminTool.store_turnover_list()

        if single_fast_deposit_amount in amount:
            status = True
        else:
            status = False

        adminTool.close_menu("transaction")
        self.assertEqual(status, True)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15483, 0)

    def test_55_modify_required_turnover(self):
        global runID, account
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15484, 1)

        modified_amount = "0.00"
        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("transaction", "turnover")
        adminTool.query_turnover(account)
        adminTool.check_search_loading()
        adminTool.click_turnover_button_edit()
        adminTool.input_turnover_field_modify_required(modified_amount)
        adminTool.submit_modified_required_turnover()
        amount, required = adminTool.store_turnover_list()

        adminTool.close_menu("transaction")
        self.assertEqual(required[0], modified_amount)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15484, 0)

    def test_56_accept_withdrawal(self):
        global runID
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15485, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("transaction", "withdraw")
        adminTool.clear_query_period()
        adminTool.click_withdrawal_field_search_status()

        # status = all, unprocessed, processing, finished, rejected, failed
        adminTool.click_withdrawal_option_search_status("unprocessed")
        adminTool.submit_query()
        adminTool.check_search_loading()
        order_id = adminTool.store_withdrawal_result_order_id()
        adminTool.click_withdrawal_button_audit()

        # tab = info, turnover, summarized, log, change
        adminTool.switch_withdrawal_detail_tab("info")
        adminTool.click_withdrawal_detail_field_audit()
        adminTool.click_withdrawal_detail_option_audit_pass()
        adminTool.submit_withdrawal_audit_status()

        adminTool.click_withdrawal_field_search_status()
        adminTool.click_withdrawal_option_search_status("processing")
        adminTool.input_field_search_withdrawal_order_id(order_id)
        adminTool.submit_query()
        adminTool.check_search_loading()

        adminTool.click_withdrawal_column_order_id()
        adminTool.switch_withdrawal_detail_tab("change")
        column_after = adminTool.store_withdrawal_change_column_after()
        adminTool.click_withdrawal_detail_button_close()

        if "待出款" in column_after:
            status = True
        else:
            status = False

        adminTool.close_menu("transaction")
        self.assertEqual(status, True)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15485, 0)

    def test_57_reject_withdrawal(self):
        global runID
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15486, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("transaction", "withdraw")
        adminTool.clear_query_period()
        adminTool.click_withdrawal_field_search_status()

        # status = all, unprocessed, processing, finished, rejected, failed
        adminTool.click_withdrawal_option_search_status("unprocessed")
        adminTool.submit_query()
        adminTool.check_search_loading()
        order_id = adminTool.store_withdrawal_result_order_id()
        adminTool.click_withdrawal_button_audit()

        # tab = info, turnover, summarized, log, change
        adminTool.switch_withdrawal_detail_tab("info")
        adminTool.click_withdrawal_detail_field_audit()
        adminTool.click_withdrawal_detail_option_audit_fail()
        adminTool.submit_withdrawal_audit_status()

        adminTool.click_withdrawal_field_search_status()
        adminTool.click_withdrawal_option_search_status("rejected")
        adminTool.input_field_search_withdrawal_order_id(order_id)
        adminTool.submit_query()
        adminTool.check_search_loading()

        adminTool.click_withdrawal_column_order_id()
        adminTool.switch_withdrawal_detail_tab("change")
        column_after = adminTool.store_withdrawal_change_column_after()
        adminTool.click_withdrawal_detail_button_close()

        if "已拒絕" in column_after:
            status = True
        else:
            status = False

        adminTool.close_menu("transaction")
        self.assertEqual(status, True)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15486, 0)

    def test_58_member_freeze(self):
        global runID, member
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15487, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("user", "member")
        adminTool.clear_login_period()
        adminTool.query_account(member)
        adminTool.check_member_search_account(member)
        adminTool.freeze_member()
        adminTool.click_edit_member()
        adminTool.click_edit_member_tab("change_log")
        adminTool.click_button_edit_member_search()

        expect_data = "MemberFreeze"
        actual_data = adminTool.store_member_freeze_change_log()

        if expect_data in actual_data:
            actual_data = expect_data

        adminTool.close_drawer_mask()
        adminTool.close_menu("user")

        self.assertEqual(actual_data, expect_data)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15487, 0)

    def test_59_affiliate_freeze(self):
        global runID, affiliate
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15488, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("user", "affiliates")
        adminTool.clear_login_period()
        adminTool.query_account(affiliate)
        adminTool.check_member_search_account(affiliate)
        adminTool.freeze_member()
        adminTool.click_edit_member()
        adminTool.click_edit_member_tab("change_log")
        adminTool.click_button_edit_member_search()

        expect_data = "MemberFreeze"
        actual_data = adminTool.store_member_freeze_change_log()

        if expect_data in actual_data:
            actual_data = expect_data

        adminTool.close_drawer_mask()
        adminTool.close_menu("user")

        self.assertEqual(actual_data, expect_data)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15488, 0)

    def test_60_fast_deposit_promote_single(self):
        global runID, account, single_fast_deposit_promote_amount
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15489, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        single_fast_deposit_promote_amount = adminTool.random_deposit_amount()
        adminTool.switch_function("transaction", "fast_deposit")
        adminTool.submit_query()
        adminTool.check_search_loading()
        adminTool.expand_subtotal()
        subtotal_before_deposit = adminTool.store_fast_deposit_subtotal()
        adminTool.click_fast_deposit()

        # 單筆作業：single, 批次作業：batch
        adminTool.execute_fast_deposit_promote("single", account, single_fast_deposit_promote_amount)
        subtotal_after_deposit = adminTool.store_fast_deposit_subtotal()
        adminTool.collapse_subtotal()

        adminTool.close_menu("transaction")
        print(type(subtotal_after_deposit[2]),
              type(subtotal_before_deposit[2] + float(single_fast_deposit_promote_amount)))
        self.assertEqual(type(subtotal_after_deposit[2]),
                         type(subtotal_before_deposit[2] + float(single_fast_deposit_promote_amount)))

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15489, 0)

    def test_61_withdrawal_export_file(self):
        global runID
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15490, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("transaction", "withdraw")
        adminTool.clear_query_period()
        adminTool.click_withdrawal_field_search_status()

        # status = all, unprocessed, processing, finished, rejected, failed
        adminTool.click_withdrawal_option_search_status("unprocessed")
        adminTool.submit_query()
        adminTool.check_search_loading()

        actual_data = adminTool.get_export_file_data()
        expect_data = ['订单ID', '申请时间', '会员帐号', '名称', '所属上级', '提现类型', '银行', '户名', '入款账户', '申请金额',
                       '行政费', '优惠扣除', '行政费', '金流手续费', '出款金额', '状态', '更新时间', '管理者']

        adminTool.close_menu("transaction")
        self.assertEqual(actual_data, expect_data)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15490, 0)

    def test_62_transaction_log_export_file(self):
        global runID
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15491, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("transaction", "transaction")
        adminTool.check_search_loading()
        actual_data = adminTool.get_export_file_data()
        expect_data = ['交易序号', '类型', '项目', '会员帐号', '来源单号', '交易金额', '交易前', '交易后', '交易时间', '备注']

        adminTool.close_menu("transaction")
        self.assertEqual(actual_data, expect_data)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15491, 0)

    def test_63_bet_log_export_file(self):
        global runID
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15492, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("filesearch", "bet")
        adminTool.clear_query_period()
        adminTool.fill_query_date()
        adminTool.submit_query()
        adminTool.check_search_loading()
        actual_data = adminTool.get_export_file_data()
        expect_data = ['订单ID', '投注时间', '来源', '平台', '游戏', '桌号', '局号', '会员帐号', '投注额', '输赢', '个人盈亏',
                       '有效投注额', '中奖金额', '状态', '结算时间', '更新时间', '赛事项目', '投注内容']

        adminTool.close_menu("filesearch")
        self.assertEqual(actual_data, expect_data)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15492, 0)

    def test_64_operation_report_affiliate_log_export_file(self):
        global runID, account
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15493, 1)

        adminTool = AdminTool(self.driver)
        adminTool.switch_function("barchart", "affiliate")
        adminTool.check_search_loading()
        actual_data = adminTool.get_export_file_data()
        expect_data = ['代理帐号数', '下级人数', '注册人数', '首充人数', '充值人数', '三存人数', '五存人数', '投注人数', '订单量',
                       '投注金额', '有效投注金额', '结算金额', '派彩(输赢)', '充值金额', '提现金额', '存提差', '扣款金额', '风控补分',
                       '优惠金额', '返点', '代理分红', '站台手续费', '行政费', '会员余额', '平台利润']

        adminTool.close_menu("barchart")
        self.assertEqual(actual_data, expect_data)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15493, 0)

    def test_65_operation_report_member_log_export_file(self):
        global runID, account
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15494, 1)

        adminTool = AdminTool(self.driver)
        adminTool.switch_function("barchart", "member")
        adminTool.check_search_loading()
        actual_data = adminTool.get_export_file_data()
        expect_data = ['会员帐号数', '订单量', '投注金额', '有效投注金额', '结算金额', '派彩(输赢)', '充值人数', '充值金额', '提现金额',
                       '存提差', '扣款金额', '风控补分', '优惠金额', '返点', '站台手续费', '行政费', '会员余额', '会员盈亏']

        adminTool.close_menu("barchart")
        self.assertEqual(actual_data, expect_data)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15494, 0)

    def test_66_fast_deposit_export_file(self):
        global runID, account, single_fast_deposit_promote_amount
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15495, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("transaction", "fast_deposit")
        adminTool.submit_query()
        adminTool.check_search_loading()
        actual_data = adminTool.get_export_file_data()
        expect_data = ['作业序号', '作业时间', '会员帐号', '会员名称', '所属上级', '类型', '子类型', '项目', '异动金额', '流水审核',
                       '异动时间(系统时间)', '管理者']

        adminTool.close_menu("transaction")
        self.assertEqual(actual_data, expect_data)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15495, 0)

    def test_67_member_export_file(self):
        global runID
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15496, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("user", "member")
        adminTool.check_search_loading()
        actual_data = adminTool.get_export_file_data()
        expect_data = ['会员帐号', '名称', '余额', '返点等级', '类型', '等级', '代理等级', '所属上级', '直属下级', '注册时间',
                       '登入时间', '登入IP', '状态', '在线状态']

        adminTool.close_menu("user")
        self.assertEqual(actual_data, expect_data)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15496, 0)

    def test_68_affiliate_export_file(self):
        global runID
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15497, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("user", "affiliates")
        adminTool.check_search_loading()
        actual_data = adminTool.get_export_file_data()
        expect_data = ['会员帐号', '名称', '余额', '返点等级', '类型', '等级', '代理等级', '所属上级', '直属下级', '团队人数',
                       '注册时间', '登入时间', '状态']

        adminTool.close_menu("user")
        self.assertEqual(actual_data, expect_data)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15497, 0)

    def test_69_deposit_execution(self):
        global runID, account, deposit_amount
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15498, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        deposit_amount = adminTool.random_deposit_amount()
        adminTool.switch_function("transaction", "deposit")
        adminTool.submit_query()
        adminTool.check_search_loading()
        adminTool.expand_subtotal()
        subtotal_before_deposit = adminTool.store_deposit_subtotal()
        adminTool.click_button_deposit()

        adminTool.execute_deposit(account, deposit_amount)
        subtotal_after_deposit = adminTool.store_deposit_subtotal()
        adminTool.collapse_subtotal()

        adminTool.close_menu("transaction")
        self.assertEqual(type(subtotal_after_deposit[2]),
                         type(subtotal_before_deposit[2] + float(single_fast_deposit_amount)))

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15498, 0)

    # 6598 [Admin Tool][DB] 新營運報表/ 代理報表-"平台利潤"欄位顯示數值比所參考欄位的計算結果少0.01
    def test_70_operation_report_affiliate_team_log_subtotal(self):
        global runID, account
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15499, 1)

        adminTool = AdminTool(self.driver)
        adminTool.switch_function("barchart", "affiliate")

        adminTool.click_field_affiliate_type_search()
        adminTool.click_option_affiliate_type_search('team')
        adminTool.query_operation_report_account(account)

        adminTool.expand_subtotal()
        column_transaction_accounts = adminTool.operation_report_column_member_account()

        for column_transaction_account in column_transaction_accounts:
            # print(column_transaction_account.text, account)
            self.assertEqual(column_transaction_account.text, account)

        subtotal_transaction = adminTool.operation_report_affiliate()
        # (account, 1) 代理團隊
        # subtotal_transaction_log = AdminTool_API.operation_report_Affiliate_Team(account, 1)
        subtotal_transaction_log = Assertion.transfer_list_format(
            AdminTool_API.AdminTool().get_AffiliateReport_Summary(account, 1))

        adminTool.collapse_subtotal()
        adminTool.close_menu("barchart")
        self.assertEqual(subtotal_transaction, subtotal_transaction_log)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15499, 0)

    def test_71_operation_report_affiliate_superior_log_subtotal(self):
        global runID, affiliate
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15500, 1)

        adminTool = AdminTool(self.driver)
        adminTool.switch_function("barchart", "affiliate")

        adminTool.click_field_affiliate_type_search()
        adminTool.click_option_affiliate_type_search('superior')
        adminTool.query_operation_report_account(affiliate)

        adminTool.expand_subtotal()
        subtotal_transaction = adminTool.operation_report_affiliate()
        # (account, 2) 直属上级(必填)
        # subtotal_transaction_log = AdminTool_API.operation_report_Affiliate_superior(affiliate, 2)
        subtotal_transaction_log = Assertion.transfer_list_format(
            AdminTool_API.AdminTool().get_AffiliateReport_Summary(affiliate, 2))

        adminTool.collapse_subtotal()
        adminTool.close_menu("barchart")
        self.assertEqual(subtotal_transaction, subtotal_transaction_log)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15500, 0)

    # 6598 [Admin Tool][DB] 新營運報表/ 代理報表-"平台利潤"欄位顯示數值比所參考欄位的計算結果少0.01
    def test_72_operation_report_member_log_subtotal(self):
        global runID, account
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15501, 1)

        adminTool = AdminTool(self.driver)
        adminTool.switch_function("barchart", "member")
        adminTool.click_field_member_type_search()
        adminTool.click_option_member_type_search('member')
        adminTool.query_operation_report_account(account)
        adminTool.expand_subtotal()

        column_transaction_accounts = adminTool.operation_report_column_member_account()
        for column_transaction_account in column_transaction_accounts:
            print(column_transaction_account.text, account)
            self.assertEqual(column_transaction_account.text, account)
        subtotal_transaction = adminTool.operation_report_member()
        # subtotal_transaction_log = AdminTool_API.operation_report_member(account, 1)
        subtotal_transaction_log = Assertion.transfer_list_format(
            AdminTool_API.AdminTool().get_MemberReport_Summary(account, 1))

        adminTool.collapse_subtotal()
        adminTool.close_menu("barchart")
        self.assertEqual(subtotal_transaction, subtotal_transaction_log)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15501, 0)

    # 6598 [Admin Tool][DB] 新營運報表/ 代理報表-"平台利潤"欄位顯示數值比所參考欄位的計算結果少0.01
    def test_73_operation_report_superior_filter_account(self):
        global runID, account
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15502, 1)

        account = 'alvistest201'
        adminTool = AdminTool(self.driver)
        adminTool.switch_function("barchart", "member")
        adminTool.click_field_member_type_search()
        adminTool.click_option_member_type_search('superior')
        adminTool.query_operation_report_account(account)
        adminTool.expand_subtotal()

        subtotal_transaction = adminTool.operation_report_member()

        # subtotal_transaction_log = AdminTool_API.operation_report_member(account, 2)
        subtotal_transaction_log = Assertion.transfer_list_format(
            AdminTool_API.AdminTool().get_MemberReport_Summary(account, 2))

        adminTool.collapse_subtotal()
        adminTool.close_menu("barchart")
        self.assertEqual(subtotal_transaction, subtotal_transaction_log)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15502, 0)

    # 6598 [Admin Tool][DB] 新營運報表/ 代理報表-"平台利潤"欄位顯示數值比所參考欄位的計算結果少0.01
    def test_74_operation_report_team_filter_account(self):
        global runID, account
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15503, 1)

        account = 'alvistest201'
        adminTool = AdminTool(self.driver)
        adminTool.switch_function("barchart", "member")
        adminTool.click_field_member_type_search()
        adminTool.click_option_member_type_search('team')
        adminTool.query_operation_report_account(account)
        adminTool.expand_subtotal()

        subtotal_transaction = adminTool.operation_report_member()
        # subtotal_transaction_log = AdminTool_API.operation_report_member(account, 3)
        subtotal_transaction_log = Assertion.transfer_list_format(
            AdminTool_API.AdminTool().get_MemberReport_Summary(account, 3))

        adminTool.collapse_subtotal()
        adminTool.close_menu("barchart")
        self.assertEqual(subtotal_transaction, subtotal_transaction_log)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15503, 0)

    # 6598 [Admin Tool][DB] 新營運報表/ 代理報表-"平台利潤"欄位顯示數值比所參考欄位的計算結果少0.01
    def test_75_operation_report_agent_log_subtotal(self):
        global runID, account
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15504, 1)

        adminTool = AdminTool(self.driver)
        adminTool.switch_function("barchart", "agent")
        adminTool.OP_submit_query()
        adminTool.expand_subtotal()
        subtotal_transaction = adminTool.operation_report_agent()
        subtotal_transaction_log = Assertion.transfer_list_format(AdminTool_API.AdminTool().get_AgentReport_Summary())

        adminTool.collapse_subtotal()
        adminTool.close_menu("barchart")

        self.assertEqual(subtotal_transaction, subtotal_transaction_log)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15504, 0)

    def test_76_create_contract_daily_wages(self):
        global runID, affiliate, parent
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15505, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("team", "contract_management")
        adminTool.create_contract('daily_wages', parent, affiliate)
        adminTool.query_contract('daily_wages', parent, affiliate)
        adminTool.check_search_loading()
        actual_result = adminTool.store_column_contract_search_result()
        expect_result = [parent, affiliate, "彩票契约日工资", "10", "0.1%", "启用"]

        adminTool.reset_contract()
        self.driver.refresh()
        adminTool.close_menu("team")
        self.assertEqual(actual_result, expect_result)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15505, 0)

    def test_77_create_contract_daily_dividends(self):
        global runID, affiliate, parent
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15506, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("team", "contract_management")
        adminTool.create_contract('daily_dividends', parent, affiliate)
        adminTool.query_contract('daily_dividends', parent, affiliate)
        adminTool.check_search_loading()
        actual_result = adminTool.store_column_contract_search_result()
        expect_result = [parent, affiliate, "彩票契约日分红", "10", "0.1%", "启用"]

        adminTool.reset_contract()
        self.driver.refresh()
        adminTool.close_menu("team")
        self.assertEqual(actual_result, expect_result)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15506, 0)

    def test_78_create_contract_monthly_dividends(self):
        global runID, affiliate, parent
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15507, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("team", "contract_management")
        adminTool.create_contract('monthly_dividends', parent, affiliate)
        adminTool.query_contract('monthly_dividends', parent, affiliate)
        adminTool.check_search_loading()
        actual_result = adminTool.store_column_contract_search_result()
        expect_result = [parent, affiliate, "游戏契约月分红", "10", "0.1%", "启用"]

        adminTool.reset_contract()
        self.driver.refresh()
        adminTool.close_menu("team")
        self.assertEqual(actual_result, expect_result)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15507, 0)

    def test_79_edit_crypto_currency(self):
        global runID, exchange_rate_before, exchange_rate_after
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15508, 1)

        adminTool = AdminTool(self.driver)
        exchange_rate_after = adminTool.random_exchange_rate()
        adminTool.close_drawer_mask()
        adminTool.switch_function("transaction", "crypto_currency")
        exchange_rate_before = adminTool.store_column_crypto_result_exchange_rate()
        adminTool.click_button_edit_crypto()
        adminTool.input_field_edit_crypto_rate(exchange_rate_after)
        adminTool.click_button_edit_crypto_submit()
        adminTool.click_button_edit_crypto_submit_confirm()
        actual_result = adminTool.store_column_crypto_result_exchange_rate()
        expect_result = exchange_rate_after

        adminTool.close_menu("transaction")
        self.assertEqual(actual_result, expect_result)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15508, 0)

    def test_80_query_crypto_currency_change_log(self):
        global runID, exchange_rate_before, exchange_rate_after
        # AzureTestPlan().update_test_status(runID, 15403, 15404, 15509, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("transaction", "crypto_currency")
        adminTool.click_button_crypto_change_record()
        adminTool.click_button_crypto_change_record_query()
        adminTool.check_search_loading()
        actual_result = adminTool.store_crypto_change_log()
        expect_result = [exchange_rate_before, exchange_rate_after]
        adminTool.click_button_crypto_change_record_close()
        print('actual_result')
        print(actual_result)
        print('expect_result')
        print(expect_result)
        adminTool.close_menu("transaction")
        self.assertEqual(actual_result, expect_result)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15509, 0)

    def test_81_check_turnover_subtotal(self):
        global runID, affiliate
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15510, 1)

        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("transaction", "turnover")
        adminTool.query_turnover(affiliate)
        adminTool.check_search_loading()
        adminTool.expand_subtotal()

        current = adminTool.store_turnover_subtotal_current()
        sum_current_valid_bet_amount = adminTool.sum_turnover_current_valid_bet_amount(current)
        current_valid_bet_amount = current[12]
        subtotal_valid_bet_amount = adminTool.store_turnover_subtotal_valid_bet_amount()

        adminTool.close_menu("transaction")
        self.assertEqual(sum_current_valid_bet_amount, current_valid_bet_amount)
        self.assertEqual(current_valid_bet_amount, subtotal_valid_bet_amount)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15510, 0)

    def test_82_turnover_trial_calculation(self):
        global runID, affiliate
        AzureTestPlan().update_test_status(runID, 15403, 15404, 15511, 1)

        affiliate = "alvistest201"
        adminTool = AdminTool(self.driver)
        adminTool.close_drawer_mask()
        adminTool.switch_function("transaction", "turnover")
        adminTool.query_turnover(affiliate)
        adminTool.check_search_loading()

        current = adminTool.store_turnover_subtotal_current()
        required_turnover = current[2]
        valid_bet_amount = current[12]
        shortage_bet_amount = adminTool.calculate_shortage_turnover(required_turnover, valid_bet_amount)
        adminTool.click_turnover_button_calculator()
        adminTool.input_turnover_field_calculator_amount("100")
        adminTool.click_turnover_button_calculator_submit()
        calculator_result = adminTool.store_turnover_calculator_shortage_amount(required_turnover, valid_bet_amount)
        adminTool.click_turnover_button_calculator_close()

        adminTool.close_menu("transaction")
        self.assertEqual(calculator_result, shortage_bet_amount)

        AzureTestPlan().update_test_status(runID, 15403, 15404, 15511, 0)

    @classmethod
    def tearDownClass(cls):
        global runID
        AzureTestPlan().update_test_run(runID)


if __name__ == '__main__':
    unittest.main()
