import unittest
from config.SetUIConfig import Driver, Platform, Target, Project
from test_UI.common.BasePage import BasePage
from test_UI.page.LoginPage import LoginPage
from test_UI.page.HomePage import HomePage
from test_UI.page.UserPage import UserPage
from test_API.common.AdminTool import AdminTool
from test_API.common.Financial import Financial
from utils import Assertion, Localization
from utils.DataLoader import JsonLoader
from utils.DataExtractor import extract_json


class UserPageTestCase(unittest.TestCase):  # TODO: 調整提現金額為依專案判斷

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver
        login_page = LoginPage(cls.driver)
        login_page.execute_login()
        cls.account = JsonLoader('TMP').get_tmp_data(Platform, Project, 'account')
        cls.AdminTool = AdminTool()
        cls.Financial = Financial()

        home_page = HomePage(cls.driver)
        home_page.switch_category("user")
        cls.DepositInfoStatus_New = Localization.get_loc("UserPage", 'DepositInfoStatus_New')
        cls.DepositInfoStatus_Done = Localization.get_loc("UserPage", 'DepositInfoStatus_Done')
        cls.WithdrawInfoStatus_New = Localization.get_loc("UserPage", 'WithdrawInfoStatus_New')
        cls.WithdrawInfoStatus_Review = Localization.get_loc("UserPage", 'WithdrawInfoStatus_Review')
        cls.WithdrawInfoStatus_Reject = Localization.get_loc("UserPage", 'WithdrawInfoStatus_Reject')
        cls.WithdrawInfoStatus_Done = Localization.get_loc("UserPage", 'WithdrawInfoStatus_Done')
        cls.WithdrawInfoStatus_Failed = Localization.get_loc("UserPage", 'WithdrawInfoStatus_Failed')
        cls.TransferStatus_Done = Localization.get_loc("AdminTool_TransferManagement", 'TransferStatus_Done')

    def test_01_00_Deposit_via_Bank_Success(self):
        page_user = UserPage(self.driver)
        previous_balance = page_user.check_account_info()
        page_user.switch_finance_option("deposit")
        deposit_amount = page_user.trigger_deposit("bank")
        deposit_info = page_user.check_deposit_info("bank")
        page_user.close_deposit_page()
        # 進入個人中心/ 充值紀錄確認金流過程訂單對應狀態
        depositNo = deposit_info[0]
        page_user.switch_report_option("deposit")
        depositReport_info = page_user.check_depositReport_info()
        # 前端發起: 狀態"未轉賬"
        self.assertEqual(self.DepositInfoStatus_New, depositReport_info[2])
        # AT交易確認
        self.AdminTool.api_Deposit_Deposit(depositNo)
        order_info = self.Financial.get_DepositOrderInfo(1, depositNo)
        # Fin交易確認
        self.Financial.api_Deposit_update(order_info)
        page_user.switch_report_option("deposit", wait_time=120)
        depositReport_info = page_user.check_depositReport_info()
        # AT/Fin交易確認: 狀態"已到帳"
        self.assertEqual(self.DepositInfoStatus_Done, depositReport_info[2])
        # 確認充值後金額與訂單資訊
        current_balance = page_user.check_account_info()

        expect_data = ["", deposit_amount + ".00", "", "", "", "", ""]
        Assertion.assertDepositInfo(previous_balance, "bank", deposit_info, expect_data, current_balance)

    def test_01_01_Deposit_via_Bank_Rejected_by_Fin_PaymentNotArrived(self):
        page_user = UserPage(self.driver)
        previous_balance = page_user.check_account_info()
        page_user.switch_finance_option("deposit")
        deposit_amount = page_user.trigger_deposit("bank")
        deposit_info = page_user.check_deposit_info("bank")
        page_user.close_deposit_page()
        # 進入個人中心/ 充值紀錄確認金流過程訂單對應狀態
        depositNo = deposit_info[0]
        page_user.switch_report_option("deposit")
        depositReport_info = page_user.check_depositReport_info()
        # 前端發起: 狀態"未轉賬"
        self.assertEqual(self.DepositInfoStatus_New, depositReport_info[2])
        # AT交易確認
        self.AdminTool.api_Deposit_Deposit(depositNo)
        order_info = self.Financial.get_DepositOrderInfo(1, depositNo)
        # Fin交易確認
        self.Financial.api_Deposit_update(order_info, status=3)
        page_user.switch_report_option("deposit")
        depositReport_info = page_user.check_depositReport_info()
        # AT交易確認 -> Fin回絕"查無款項": 狀態"未轉賬"
        self.assertEqual(self.DepositInfoStatus_New, depositReport_info[2])
        # 確認回絕後金額與訂單資訊
        current_balance = page_user.check_account_info()

        expect_data = ["", deposit_amount + ".00", "", "", "", "", ""]
        Assertion.assertDepositInfo(previous_balance, "bank", deposit_info, expect_data, current_balance,
                                    depositStatus="Rejected")

    def test_01_02_Deposit_via_Bank_Rejected_by_Fin_AmountNotMatch(self):
        page_user = UserPage(self.driver)
        previous_balance = page_user.check_account_info()
        page_user.switch_finance_option("deposit")
        deposit_amount = page_user.trigger_deposit("bank")
        deposit_info = page_user.check_deposit_info("bank")
        page_user.close_deposit_page()
        # 進入個人中心/ 充值紀錄確認金流過程訂單對應狀態
        depositNo = deposit_info[0]
        page_user.switch_report_option("deposit")
        depositReport_info = page_user.check_depositReport_info()
        # 前端發起: 狀態"未轉賬"
        self.assertEqual(self.DepositInfoStatus_New, depositReport_info[2])
        # AT交易確認
        self.AdminTool.api_Deposit_Deposit(depositNo)
        order_info = self.Financial.get_DepositOrderInfo(1, depositNo)
        # Fin交易確認
        self.Financial.api_Deposit_update(order_info, status=8)
        page_user.switch_report_option("deposit")
        depositReport_info = page_user.check_depositReport_info()
        # AT交易確認 -> Fin回絕"金額不符": 狀態"未轉賬"
        self.assertEqual(self.DepositInfoStatus_New, depositReport_info[2])
        # 確認回絕後金額與訂單資訊
        current_balance = page_user.check_account_info()

        expect_data = ["", deposit_amount + ".00", "", "", "", "", ""]
        Assertion.assertDepositInfo(previous_balance, "bank", deposit_info, expect_data, current_balance,
                                    depositStatus="Rejected")

    def test_01_03_Deposit_via_Bank_Success_Fin_AmountAdjusted(self):
        page_user = UserPage(self.driver)
        previous_balance = page_user.check_account_info()
        page_user.switch_finance_option("deposit")
        deposit_amount = page_user.trigger_deposit("bank")
        deposit_info = page_user.check_deposit_info("bank")
        page_user.close_deposit_page()
        # 進入個人中心/ 充值紀錄確認金流過程訂單對應狀態
        depositNo = deposit_info[0]
        page_user.switch_report_option("deposit")
        depositReport_info = page_user.check_depositReport_info()
        # 前端發起: 狀態"未轉賬"
        self.assertEqual(self.DepositInfoStatus_New, depositReport_info[2])
        # AT交易確認
        self.AdminTool.api_Deposit_Deposit(depositNo)
        order_info = self.Financial.get_DepositOrderInfo(1, depositNo)
        # Fin交易確認
        self.Financial.api_Deposit_update(order_info, status=7)
        page_user.switch_report_option("deposit", wait_time=120)
        depositReport_info = page_user.check_depositReport_info()
        # AT交易確認 -> Fin金額調整: 狀態"已到帳"
        self.assertEqual(self.DepositInfoStatus_Done, depositReport_info[2])
        # 確認調整後金額與訂單資訊
        current_balance = page_user.check_account_info()

        expect_data = ["", deposit_amount + ".00", "", "", "", "", ""]
        Assertion.assertDepositInfo(previous_balance, "bank", deposit_info, expect_data, current_balance,
                                    depositStatus="Adjusted")

    @unittest.skipIf(Project == 'vt', '越南站目前不支援第三方充值')
    def test_02_Deposit_via_thirdParty_Success(self):
        page_user = UserPage(self.driver)
        previous_balance = page_user.check_account_info()
        page_user.switch_finance_option("deposit")
        deposit_amount = page_user.trigger_deposit("thirdParty")
        deposit_info = page_user.check_deposit_info("thirdParty")
        page_user.close_deposit_page()
        # 進入個人中心/ 充值紀錄確認金流過程訂單對應狀態
        depositNo = deposit_info[0]
        page_user.switch_report_option("deposit")
        depositReport_info = page_user.check_depositReport_info()
        # 前端發起: 狀態"未轉賬"
        self.assertEqual(self.DepositInfoStatus_New, depositReport_info[2])
        # AT交易確認
        self.AdminTool.api_Deposit_Deposit(depositNo)
        order_info = self.Financial.get_DepositOrderInfo(2, depositNo)
        # Fin交易確認
        self.Financial.api_Deposit_update(order_info)
        page_user.switch_report_option("deposit", wait_time=120)
        depositReport_info = page_user.check_depositReport_info()
        # AT/Fin交易確認: 狀態"已到帳"
        self.assertEqual(self.DepositInfoStatus_Done, depositReport_info[2])
        # 確認充值後金額與訂單資訊
        current_balance = page_user.check_account_info()

        expect_data = ["", deposit_amount + ".00", "", ""]
        Assertion.assertDepositInfo(previous_balance, "thirdParty", deposit_info, expect_data, current_balance)

    @unittest.skipIf(Project == 'vt', '越南站目前不支援USDT充值')
    def test_03_Deposit_via_USDT_Success(self):
        page_user = UserPage(self.driver)
        previous_balance = page_user.check_account_info()
        page_user.switch_finance_option("deposit")
        deposit_amount = page_user.trigger_deposit("USDT")
        deposit_info = page_user.check_deposit_info("USDT")
        page_user.close_deposit_page()
        # 進入個人中心/ 充值紀錄確認金流過程訂單對應狀態
        depositNo = deposit_info[0]
        page_user.switch_report_option("deposit")
        depositReport_info = page_user.check_depositReport_info()
        # 前端發起: 狀態"未轉賬"
        self.assertEqual(self.DepositInfoStatus_New, depositReport_info[2])
        # AT交易確認
        self.AdminTool.api_Deposit_Deposit(depositNo)
        order_info = self.Financial.get_DepositOrderInfo(3, depositNo)
        # Fin交易確認
        self.Financial.api_Deposit_update(order_info)
        page_user.switch_report_option("deposit", wait_time=120)
        depositReport_info = page_user.check_depositReport_info()
        # AT/Fin交易確認: 狀態"已到帳"
        self.assertEqual(self.DepositInfoStatus_Done, depositReport_info[2])
        # 確認充值後金額與訂單資訊
        current_balance = page_user.check_account_info()

        expect_data = ["", deposit_amount + ".00", "", "", "", "", "", "", ""]
        Assertion.assertDepositInfo(previous_balance, "USDT", deposit_info, expect_data, current_balance)

    def test_04_00_Withdraw_via_Bank_Success(self):
        page_user = UserPage(self.driver)
        previous_balance = page_user.check_account_info()
        page_user.switch_finance_option("withdraw")
        if Target in ['app', 'h5']:
            page_user.input_pin_code()
        # Precondition: AT放寬流水審核
        self.AdminTool.api_Turnover_BatchUpdate(self.account)
        withdraw_account_info = page_user.trigger_withdraw("bankcard", "200")
        withdraw_info = page_user.check_withdraw_info()
        if Target in ['web']:
            page_user.input_pin_code()
        page_user.close_withdraw_page()
        # 進入個人中心/ 提現紀錄確認金流過程訂單對應狀態
        page_user.switch_report_option("withdraw")
        withdrawReport_info = page_user.check_withdrawReport_info()
        withdrawNo = withdrawReport_info[1]
        # 前端發起: 狀態"未處理"
        self.assertEqual(self.WithdrawInfoStatus_New, withdrawReport_info[2])
        # AT審單
        self.AdminTool.api_Withdrawal_Status(withdrawNo)
        page_user.switch_report_option("withdraw")
        withdrawReport_info = page_user.check_withdrawReport_info()
        # AT審單: 狀態"提現處理中"
        self.assertEqual(self.WithdrawInfoStatus_Review, withdrawReport_info[2])
        # Fin獲取第一筆訂單資訊用(目前無單筆查詢功能)
        order_info = self.Financial.get_WithdrawOrderInfo("bankcard")
        self.Financial.api_Main_payout(order_info)
        page_user.switch_report_option("withdraw", wait_time=120)
        withdrawReport_info = page_user.check_withdrawReport_info()
        # Fin出款: 狀態"已出款"
        self.assertEqual(self.WithdrawInfoStatus_Done, withdrawReport_info[2])
        # 確認提現後金額與訂單資訊
        current_balance = page_user.check_account_info()

        Assertion.assertWithdrawInfo(previous_balance, withdraw_account_info, "200.00", withdraw_info, current_balance)

    def test_04_01_Withdraw_via_Bank_Rejected_by_AT(self):
        page_user = UserPage(self.driver)
        previous_balance = page_user.check_account_info()
        page_user.switch_finance_option("withdraw")
        if Target in ['app', 'h5']:
            page_user.input_pin_code()
        # Precondition: AT放寬流水審核
        self.AdminTool.api_Turnover_BatchUpdate(self.account)
        withdraw_account_info = page_user.trigger_withdraw("bankcard", "200")
        withdraw_info = page_user.check_withdraw_info()
        if Target in ['web']:
            page_user.input_pin_code()
        page_user.close_withdraw_page()
        # 進入個人中心/ 提現紀錄確認金流過程訂單對應狀態
        page_user.switch_report_option("withdraw")
        withdrawReport_info = page_user.check_withdrawReport_info()
        withdrawNo = withdrawReport_info[1]
        # 前端發起: 狀態"未處理"
        self.assertEqual(self.WithdrawInfoStatus_New, withdrawReport_info[2])
        # AT審單
        self.AdminTool.api_Withdrawal_Status(withdrawNo, status=4)
        page_user.switch_report_option("withdraw")
        withdrawReport_info = page_user.check_withdrawReport_info()
        # AT審單: 狀態"已拒绝"
        self.assertEqual(self.WithdrawInfoStatus_Reject, withdrawReport_info[2])
        # 確認回絕後金額與訂單資訊
        current_balance = page_user.check_account_info()

        Assertion.assertWithdrawInfo(previous_balance, withdraw_account_info, "200.00", withdraw_info, current_balance,
                                     withdrawStatus="Rejected")

    def test_04_02_Withdraw_via_Bank_Failed_by_Fin(self):
        page_user = UserPage(self.driver)
        previous_balance = page_user.check_account_info()
        page_user.switch_finance_option("withdraw")
        if Target in ['app', 'h5']:
            page_user.input_pin_code()
        # Precondition: AT放寬流水審核
        self.AdminTool.api_Turnover_BatchUpdate(self.account)
        withdraw_account_info = page_user.trigger_withdraw("bankcard", "200")
        withdraw_info = page_user.check_withdraw_info()
        if Target in ['web']:
            page_user.input_pin_code()
        page_user.close_withdraw_page()
        # 進入個人中心/ 提現紀錄確認金流過程訂單對應狀態
        page_user.switch_report_option("withdraw")
        withdrawReport_info = page_user.check_withdrawReport_info()
        withdrawNo = withdrawReport_info[1]
        # 前端發起: 狀態"未處理"
        self.assertEqual(self.WithdrawInfoStatus_New, withdrawReport_info[2])
        # AT審單
        self.AdminTool.api_Withdrawal_Status(withdrawNo)
        page_user.switch_report_option("withdraw")
        withdrawReport_info = page_user.check_withdrawReport_info()
        # AT審單: 狀態"提現處理中"
        self.assertEqual(self.WithdrawInfoStatus_Review, withdrawReport_info[2])
        # Fin獲取第一筆訂單資訊用(目前無單筆查詢功能)
        order_info = self.Financial.get_WithdrawOrderInfo("bankcard")
        self.Financial.api_Main_payout(order_info, status=5)
        page_user.switch_report_option("withdraw", wait_time=120)
        withdrawReport_info = page_user.check_withdrawReport_info()
        # Fin出款: 狀態"出款失敗"
        self.assertEqual(self.WithdrawInfoStatus_Failed, withdrawReport_info[2])
        # 確認提現後金額與訂單資訊
        current_balance = page_user.check_account_info()

        Assertion.assertWithdrawInfo(previous_balance, withdraw_account_info, "200.00", withdraw_info, current_balance,
                                     withdrawStatus="Failed")

    @unittest.skipIf(Target == 'h5', '預計重構, 暫不執行')
    def test_05_00_Withdraw_via_USDT_Success(self):
        page_user = UserPage(self.driver)
        previous_balance = page_user.check_account_info()
        page_user.switch_finance_option("withdraw")
        if Target in ['app', 'h5']:
            page_user.input_pin_code()
        # Precondition: AT放寬流水審核
        self.AdminTool.api_Turnover_BatchUpdate(self.account)
        withdraw_account_info = page_user.trigger_withdraw("USDT", "200")
        withdraw_info = page_user.check_withdraw_info()
        if Target in ['web']:
            page_user.input_pin_code()
        page_user.close_withdraw_page()
        # 進入個人中心/ 提現紀錄確認金流過程訂單對應狀態
        page_user.switch_report_option("withdraw")
        withdrawReport_info = page_user.check_withdrawReport_info()
        withdrawNo = withdrawReport_info[1]
        # 前端發起: 狀態"未處理"
        self.assertEqual(self.WithdrawInfoStatus_New, withdrawReport_info[2])
        # AT審單
        self.AdminTool.api_Withdrawal_Status(withdrawNo)
        page_user.switch_report_option("withdraw")
        withdrawReport_info = page_user.check_withdrawReport_info()
        # AT審單: 狀態"提現處理中"
        self.assertEqual(self.WithdrawInfoStatus_Review, withdrawReport_info[2])
        # Fin獲取第一筆訂單資訊用(目前無單筆查詢功能)
        order_info = self.Financial.get_WithdrawOrderInfo("USDT")
        self.Financial.api_Main_payout(order_info)
        page_user.switch_report_option("withdraw", wait_time=120)
        withdrawReport_info = page_user.check_withdrawReport_info()
        # Fin出款: 狀態"已出款"
        self.assertEqual(self.WithdrawInfoStatus_Done, withdrawReport_info[2])
        # 確認提現後金額與訂單資訊
        current_balance = page_user.check_account_info()

        Assertion.assertWithdrawInfo(previous_balance, withdraw_account_info, "200.00", withdraw_info, current_balance)

    @unittest.skipIf(Project == 'vt', '越南站目前不支援樂遊')
    def test_06_01_Transfer_to_thirdParty_LEG(self):
        page_user = UserPage(self.driver)
        page_user.switch_finance_option("transfer")
        page_user.select_thirdParty_option("LEG")
        previous_balance = page_user.check_transfer_info("Center")
        previous_balance_thirdParty = page_user.check_transfer_info("LEG")

        page_user.trigger_transfer("toThirdParty", "100")
        current_balance = page_user.check_transfer_info("Center")
        current_balance_thirdParty = page_user.check_transfer_info("LEG")
        page_user.back_to_UserPage()

        Assertion.assertTransferInfo(previous_balance, previous_balance_thirdParty, "toThirdParty", "100",
                                     current_balance, current_balance_thirdParty)
        # 進入個人中心/ 轉賬紀錄確認金流過程訂單對應狀態
        page_user.switch_report_option("transfer")
        transferReport_info = page_user.check_transferReport_info()
        transferNo = transferReport_info[1]

        Assertion.assertTransferReport_info("toThirdParty", "100.00", transferReport_info[0], transferNo)
        # 因前端文案不一, 改由AT確認轉賬類型正確
        TransferInfo_AT = self.AdminTool.api_FundTransfer_Manage(transferNo)
        TransferType = extract_json('Data.List.Data[0].Description', TransferInfo_AT.text)
        TransferStatus = extract_json('Data.List.Data[0].StatusText', TransferInfo_AT.text)
        expect_data = Localization.get_loc("AdminTool_TransferManagement", "TransferType_", "LEG")
        # AT查詢: 轉賬方符合預期 & 狀態"已完成"
        self.assertEqual([expect_data, self.TransferStatus_Done], [TransferType, TransferStatus])

    @unittest.skipIf(Project == 'vt', '越南站目前不支援樂遊')
    def test_06_02_Transfer_from_thirdParty_LEG(self):
        page_user = UserPage(self.driver)
        page_user.switch_finance_option("transfer")
        page_user.select_thirdParty_option("LEG")
        previous_balance = page_user.check_transfer_info("Center")
        previous_balance_thirdParty = page_user.check_transfer_info("LEG")

        page_user.trigger_transfer("toCenter", "100")
        current_balance = page_user.check_transfer_info("Center")
        current_balance_thirdParty = page_user.check_transfer_info("LEG")
        page_user.back_to_UserPage()

        Assertion.assertTransferInfo(previous_balance, previous_balance_thirdParty, "toCenter", "100",
                                     current_balance, current_balance_thirdParty)
        # 進入個人中心/ 轉賬紀錄確認金流過程訂單對應狀態
        page_user.switch_report_option("transfer")
        transferReport_info = page_user.check_transferReport_info()
        transferNo = transferReport_info[1]

        Assertion.assertTransferReport_info("toCenter", "100.00", transferReport_info[0], transferNo)
        # 因前端文案不一, 改由AT確認轉賬類型正確
        TransferInfo_AT = self.AdminTool.api_FundTransfer_Manage(transferNo)
        TransferType = extract_json('Data.List.Data[0].Description', TransferInfo_AT.text)
        TransferStatus = extract_json('Data.List.Data[0].StatusText', TransferInfo_AT.text)
        expect_data = Localization.get_loc("AdminTool_TransferManagement", "TransferType_", "LEG")
        # AT查詢: 轉賬方符合預期 & 狀態"已完成"
        self.assertEqual([expect_data, self.TransferStatus_Done], [TransferType, TransferStatus])

    def test_06_03_Transfer_to_thirdParty_IM1(self):
        page_user = UserPage(self.driver)
        page_user.switch_finance_option("transfer")
        page_user.select_thirdParty_option("IM1")
        previous_balance = page_user.check_transfer_info("Center")
        previous_balance_thirdParty = page_user.check_transfer_info("IM1")

        page_user.trigger_transfer("toThirdParty", "100")
        current_balance = page_user.check_transfer_info("Center")
        current_balance_thirdParty = page_user.check_transfer_info("IM1")
        page_user.back_to_UserPage()

        Assertion.assertTransferInfo(previous_balance, previous_balance_thirdParty, "toThirdParty", "100",
                                     current_balance, current_balance_thirdParty)
        # 進入個人中心/ 轉賬紀錄確認金流過程訂單對應狀態
        page_user.switch_report_option("transfer")
        transferReport_info = page_user.check_transferReport_info()
        transferNo = transferReport_info[1]

        Assertion.assertTransferReport_info("toThirdParty", "100.00", transferReport_info[0], transferNo)
        # 因前端文案不一, 改由AT確認轉賬類型正確
        TransferInfo_AT = self.AdminTool.api_FundTransfer_Manage(transferNo)
        TransferType = extract_json('Data.List.Data[0].Description', TransferInfo_AT.text)
        TransferStatus = extract_json('Data.List.Data[0].StatusText', TransferInfo_AT.text)
        expect_data = Localization.get_loc("AdminTool_TransferManagement", "TransferType_", "IM1")
        # AT查詢: 轉賬方符合預期 & 狀態"已完成"
        self.assertEqual([expect_data, self.TransferStatus_Done], [TransferType, TransferStatus])

    def test_06_04_Transfer_from_thirdParty_IM1(self):
        page_user = UserPage(self.driver)
        page_user.switch_finance_option("transfer")
        page_user.select_thirdParty_option("IM1")
        previous_balance = page_user.check_transfer_info("Center")
        previous_balance_thirdParty = page_user.check_transfer_info("IM1")

        page_user.trigger_transfer("toCenter", "100")
        current_balance = page_user.check_transfer_info("Center")
        current_balance_thirdParty = page_user.check_transfer_info("IM1")
        page_user.back_to_UserPage()

        Assertion.assertTransferInfo(previous_balance, previous_balance_thirdParty, "toCenter", "100",
                                     current_balance, current_balance_thirdParty)
        # 進入個人中心/ 轉賬紀錄確認金流過程訂單對應狀態
        page_user.switch_report_option("transfer")
        transferReport_info = page_user.check_transferReport_info()
        transferNo = transferReport_info[1]

        Assertion.assertTransferReport_info("toCenter", "100.00", transferReport_info[0], transferNo)
        # 因前端文案不一, 改由AT確認轉賬類型正確
        TransferInfo_AT = self.AdminTool.api_FundTransfer_Manage(transferNo)
        TransferType = extract_json('Data.List.Data[0].Description', TransferInfo_AT.text)
        TransferStatus = extract_json('Data.List.Data[0].StatusText', TransferInfo_AT.text)
        expect_data = Localization.get_loc("AdminTool_TransferManagement", "TransferType_", "IM1")
        # AT查詢: 轉賬方符合預期 & 狀態"已完成"
        self.assertEqual([expect_data, self.TransferStatus_Done], [TransferType, TransferStatus])

    @unittest.skipIf(Project == 'vt', '越南站目前不支援IM棋牌')
    def test_06_05_Transfer_to_thirdParty_IM3(self):
        page_user = UserPage(self.driver)
        page_user.switch_finance_option("transfer")
        page_user.select_thirdParty_option("IM3")
        previous_balance = page_user.check_transfer_info("Center")
        previous_balance_thirdParty = page_user.check_transfer_info("IM3")

        page_user.trigger_transfer("toThirdParty", "100")
        current_balance = page_user.check_transfer_info("Center")
        current_balance_thirdParty = page_user.check_transfer_info("IM3")
        page_user.back_to_UserPage()

        Assertion.assertTransferInfo(previous_balance, previous_balance_thirdParty, "toThirdParty", "100",
                                     current_balance, current_balance_thirdParty)
        # 進入個人中心/ 轉賬紀錄確認金流過程訂單對應狀態
        page_user.switch_report_option("transfer")
        transferReport_info = page_user.check_transferReport_info()
        transferNo = transferReport_info[1]

        Assertion.assertTransferReport_info("toThirdParty", "100.00", transferReport_info[0], transferNo)
        # 因前端文案不一, 改由AT確認轉賬類型正確
        TransferInfo_AT = self.AdminTool.api_FundTransfer_Manage(transferNo)
        TransferType = extract_json('Data.List.Data[0].Description', TransferInfo_AT.text)
        TransferStatus = extract_json('Data.List.Data[0].StatusText', TransferInfo_AT.text)
        expect_data = Localization.get_loc("AdminTool_TransferManagement", "TransferType_", "IM3")
        # AT查詢: 轉賬方符合預期 & 狀態"已完成"
        self.assertEqual([expect_data, self.TransferStatus_Done], [TransferType, TransferStatus])

    @unittest.skipIf(Project == 'vt', '越南站目前不支援IM棋牌')
    def test_06_06_Transfer_from_thirdParty_IM3(self):
        page_user = UserPage(self.driver)
        page_user.switch_finance_option("transfer")
        page_user.select_thirdParty_option("IM3")
        previous_balance = page_user.check_transfer_info("Center")
        previous_balance_thirdParty = page_user.check_transfer_info("IM3")

        page_user.trigger_transfer("toCenter", "100")
        current_balance = page_user.check_transfer_info("Center")
        current_balance_thirdParty = page_user.check_transfer_info("IM3")
        page_user.back_to_UserPage()

        Assertion.assertTransferInfo(previous_balance, previous_balance_thirdParty, "toCenter", "100",
                                     current_balance, current_balance_thirdParty)
        # 進入個人中心/ 轉賬紀錄確認金流過程訂單對應狀態
        page_user.switch_report_option("transfer")
        transferReport_info = page_user.check_transferReport_info()
        transferNo = transferReport_info[1]

        Assertion.assertTransferReport_info("toCenter", "100.00", transferReport_info[0], transferNo)
        # 因前端文案不一, 改由AT確認轉賬類型正確
        TransferInfo_AT = self.AdminTool.api_FundTransfer_Manage(transferNo)
        TransferType = extract_json('Data.List.Data[0].Description', TransferInfo_AT.text)
        TransferStatus = extract_json('Data.List.Data[0].StatusText', TransferInfo_AT.text)
        expect_data = Localization.get_loc("AdminTool_TransferManagement", "TransferType_", "IM3")
        # AT查詢: 轉賬方符合預期 & 狀態"已完成"
        self.assertEqual([expect_data, self.TransferStatus_Done], [TransferType, TransferStatus])

    def test_06_07_Transfer_to_thirdParty_IBC(self):
        page_user = UserPage(self.driver)
        page_user.switch_finance_option("transfer")
        page_user.select_thirdParty_option("IBC")
        previous_balance = page_user.check_transfer_info("Center")
        previous_balance_thirdParty = page_user.check_transfer_info("IBC")

        page_user.trigger_transfer("toThirdParty", "100")
        current_balance = page_user.check_transfer_info("Center")
        current_balance_thirdParty = page_user.check_transfer_info("IBC")
        page_user.back_to_UserPage()

        Assertion.assertTransferInfo(previous_balance, previous_balance_thirdParty, "toThirdParty", "100",
                                     current_balance, current_balance_thirdParty)
        # 進入個人中心/ 轉賬紀錄確認金流過程訂單對應狀態
        page_user.switch_report_option("transfer")
        transferReport_info = page_user.check_transferReport_info()
        transferNo = transferReport_info[1]

        Assertion.assertTransferReport_info("toThirdParty", "100.00", transferReport_info[0], transferNo)
        # 因前端文案不一, 改由AT確認轉賬類型正確
        TransferInfo_AT = self.AdminTool.api_FundTransfer_Manage(transferNo)
        TransferType = extract_json('Data.List.Data[0].Description', TransferInfo_AT.text)
        TransferStatus = extract_json('Data.List.Data[0].StatusText', TransferInfo_AT.text)
        expect_data = Localization.get_loc("AdminTool_TransferManagement", "TransferType_", "IBC")
        # AT查詢: 轉賬方符合預期 & 狀態"已完成"
        self.assertEqual([expect_data, self.TransferStatus_Done], [TransferType, TransferStatus])

    def test_06_08_Transfer_from_thirdParty_IBC(self):
        page_user = UserPage(self.driver)
        page_user.switch_finance_option("transfer")
        page_user.select_thirdParty_option("IBC")
        previous_balance = page_user.check_transfer_info("Center")
        previous_balance_thirdParty = page_user.check_transfer_info("IBC")

        page_user.trigger_transfer("toCenter", "100")
        current_balance = page_user.check_transfer_info("Center")
        current_balance_thirdParty = page_user.check_transfer_info("IBC")
        page_user.back_to_UserPage()

        Assertion.assertTransferInfo(previous_balance, previous_balance_thirdParty, "toCenter", "100",
                                     current_balance, current_balance_thirdParty)
        # 進入個人中心/ 轉賬紀錄確認金流過程訂單對應狀態
        page_user.switch_report_option("transfer")
        transferReport_info = page_user.check_transferReport_info()
        transferNo = transferReport_info[1]

        Assertion.assertTransferReport_info("toCenter", "100.00", transferReport_info[0], transferNo)
        # 因前端文案不一, 改由AT確認轉賬類型正確
        TransferInfo_AT = self.AdminTool.api_FundTransfer_Manage(transferNo)
        TransferType = extract_json('Data.List.Data[0].Description', TransferInfo_AT.text)
        TransferStatus = extract_json('Data.List.Data[0].StatusText', TransferInfo_AT.text)
        expect_data = Localization.get_loc("AdminTool_TransferManagement", "TransferType_", "IBC")
        # AT查詢: 轉賬方符合預期 & 狀態"已完成"
        self.assertEqual([expect_data, self.TransferStatus_Done], [TransferType, TransferStatus])

    @unittest.skipIf(Project == 'vt', '越南站目前不支援BG')
    def test_06_09_Transfer_to_thirdParty_BG(self):
        page_user = UserPage(self.driver)
        page_user.switch_finance_option("transfer")
        page_user.select_thirdParty_option("BG")
        previous_balance = page_user.check_transfer_info("Center")
        previous_balance_thirdParty = page_user.check_transfer_info("BG")

        page_user.trigger_transfer("toThirdParty", "100")
        current_balance = page_user.check_transfer_info("Center")
        current_balance_thirdParty = page_user.check_transfer_info("BG")
        page_user.back_to_UserPage()

        Assertion.assertTransferInfo(previous_balance, previous_balance_thirdParty, "toThirdParty", "100",
                                     current_balance, current_balance_thirdParty)
        # 進入個人中心/ 轉賬紀錄確認金流過程訂單對應狀態
        page_user.switch_report_option("transfer")
        transferReport_info = page_user.check_transferReport_info()
        transferNo = transferReport_info[1]

        Assertion.assertTransferReport_info("toThirdParty", "100.00", transferReport_info[0], transferNo)
        # 因前端文案不一, 改由AT確認轉賬類型正確
        TransferInfo_AT = self.AdminTool.api_FundTransfer_Manage(transferNo)
        TransferType = extract_json('Data.List.Data[0].Description', TransferInfo_AT.text)
        TransferStatus = extract_json('Data.List.Data[0].StatusText', TransferInfo_AT.text)
        expect_data = Localization.get_loc("AdminTool_TransferManagement", "TransferType_", "BG")
        # AT查詢: 轉賬方符合預期 & 狀態"已完成"
        self.assertEqual([expect_data, self.TransferStatus_Done], [TransferType, TransferStatus])

    @unittest.skipIf(Project == 'vt', '越南站目前不支援BG')
    def test_06_10_Transfer_from_thirdParty_BG(self):
        page_user = UserPage(self.driver)
        page_user.switch_finance_option("transfer")
        page_user.select_thirdParty_option("BG")
        previous_balance = page_user.check_transfer_info("Center")
        previous_balance_thirdParty = page_user.check_transfer_info("BG")

        page_user.trigger_transfer("toCenter", "100")
        current_balance = page_user.check_transfer_info("Center")
        current_balance_thirdParty = page_user.check_transfer_info("BG")
        page_user.back_to_UserPage()

        Assertion.assertTransferInfo(previous_balance, previous_balance_thirdParty, "toCenter", "100",
                                     current_balance, current_balance_thirdParty)
        # 進入個人中心/ 轉賬紀錄確認金流過程訂單對應狀態
        page_user.switch_report_option("transfer")
        transferReport_info = page_user.check_transferReport_info()
        transferNo = transferReport_info[1]

        Assertion.assertTransferReport_info("toCenter", "100.00", transferReport_info[0], transferNo)
        # 因前端文案不一, 改由AT確認轉賬類型正確
        TransferInfo_AT = self.AdminTool.api_FundTransfer_Manage(transferNo)
        TransferType = extract_json('Data.List.Data[0].Description', TransferInfo_AT.text)
        TransferStatus = extract_json('Data.List.Data[0].StatusText', TransferInfo_AT.text)
        expect_data = Localization.get_loc("AdminTool_TransferManagement", "TransferType_", "BG")
        # AT查詢: 轉賬方符合預期 & 狀態"已完成"
        self.assertEqual([expect_data, self.TransferStatus_Done], [TransferType, TransferStatus])

    @unittest.skipIf(Project == 'vt', '越南站目前不支援開元')
    def test_06_11_Transfer_to_thirdParty_KY(self):
        page_user = UserPage(self.driver)
        page_user.switch_finance_option("transfer")
        page_user.select_thirdParty_option("KY")
        previous_balance = page_user.check_transfer_info("Center")
        previous_balance_thirdParty = page_user.check_transfer_info("KY")

        page_user.trigger_transfer("toThirdParty", "100")
        current_balance = page_user.check_transfer_info("Center")
        current_balance_thirdParty = page_user.check_transfer_info("KY")
        page_user.back_to_UserPage()

        Assertion.assertTransferInfo(previous_balance, previous_balance_thirdParty, "toThirdParty", "100",
                                     current_balance, current_balance_thirdParty)
        # 進入個人中心/ 轉賬紀錄確認金流過程訂單對應狀態
        page_user.switch_report_option("transfer")
        transferReport_info = page_user.check_transferReport_info()
        transferNo = transferReport_info[1]

        Assertion.assertTransferReport_info("toThirdParty", "100.00", transferReport_info[0], transferNo)
        # 因前端文案不一, 改由AT確認轉賬類型正確
        TransferInfo_AT = self.AdminTool.api_FundTransfer_Manage(transferNo)
        TransferType = extract_json('Data.List.Data[0].Description', TransferInfo_AT.text)
        TransferStatus = extract_json('Data.List.Data[0].StatusText', TransferInfo_AT.text)
        expect_data = Localization.get_loc("AdminTool_TransferManagement", "TransferType_", "KY")
        # AT查詢: 轉賬方符合預期 & 狀態"已完成"
        self.assertEqual([expect_data, self.TransferStatus_Done], [TransferType, TransferStatus])

    @unittest.skipIf(Project == 'vt', '越南站目前不支援開元')
    def test_06_12_Transfer_from_thirdParty_KY(self):
        page_user = UserPage(self.driver)
        page_user.switch_finance_option("transfer")
        page_user.select_thirdParty_option("KY")
        previous_balance = page_user.check_transfer_info("Center")
        previous_balance_thirdParty = page_user.check_transfer_info("KY")

        page_user.trigger_transfer("toCenter", "100")
        current_balance = page_user.check_transfer_info("Center")
        current_balance_thirdParty = page_user.check_transfer_info("KY")
        page_user.back_to_UserPage()

        Assertion.assertTransferInfo(previous_balance, previous_balance_thirdParty, "toCenter", "100",
                                     current_balance, current_balance_thirdParty)
        # 進入個人中心/ 轉賬紀錄確認金流過程訂單對應狀態
        page_user.switch_report_option("transfer")
        transferReport_info = page_user.check_transferReport_info()
        transferNo = transferReport_info[1]

        Assertion.assertTransferReport_info("toCenter", "100.00", transferReport_info[0], transferNo)
        # 因前端文案不一, 改由AT確認轉賬類型正確
        TransferInfo_AT = self.AdminTool.api_FundTransfer_Manage(transferNo)
        TransferType = extract_json('Data.List.Data[0].Description', TransferInfo_AT.text)
        TransferStatus = extract_json('Data.List.Data[0].StatusText', TransferInfo_AT.text)
        expect_data = Localization.get_loc("AdminTool_TransferManagement", "TransferType_", "KY")
        # AT查詢: 轉賬方符合預期 & 狀態"已完成"
        self.assertEqual([expect_data, self.TransferStatus_Done], [TransferType, TransferStatus])

    def test_06_13_Transfer_to_thirdParty_TF(self):
        page_user = UserPage(self.driver)
        page_user.switch_finance_option("transfer")
        page_user.select_thirdParty_option("TF")
        previous_balance = page_user.check_transfer_info("Center")
        previous_balance_thirdParty = page_user.check_transfer_info("TF")

        page_user.trigger_transfer("toThirdParty", "100")
        current_balance = page_user.check_transfer_info("Center")
        current_balance_thirdParty = page_user.check_transfer_info("TF")
        page_user.back_to_UserPage()

        Assertion.assertTransferInfo(previous_balance, previous_balance_thirdParty, "toThirdParty", "100",
                                     current_balance, current_balance_thirdParty)
        # 進入個人中心/ 轉賬紀錄確認金流過程訂單對應狀態
        page_user.switch_report_option("transfer")
        transferReport_info = page_user.check_transferReport_info()
        transferNo = transferReport_info[1]

        Assertion.assertTransferReport_info("toThirdParty", "100.00", transferReport_info[0], transferNo)
        # 因前端文案不一, 改由AT確認轉賬類型正確
        TransferInfo_AT = self.AdminTool.api_FundTransfer_Manage(transferNo)
        TransferType = extract_json('Data.List.Data[0].Description', TransferInfo_AT.text)
        TransferStatus = extract_json('Data.List.Data[0].StatusText', TransferInfo_AT.text)
        expect_data = Localization.get_loc("AdminTool_TransferManagement", "TransferType_", "TF")
        # AT查詢: 轉賬方符合預期 & 狀態"已完成"
        self.assertEqual([expect_data, self.TransferStatus_Done], [TransferType, TransferStatus])

    def test_06_14_Transfer_from_thirdParty_TF(self):
        page_user = UserPage(self.driver)
        page_user.switch_finance_option("transfer")
        page_user.select_thirdParty_option("TF")
        previous_balance = page_user.check_transfer_info("Center")
        previous_balance_thirdParty = page_user.check_transfer_info("TF")

        page_user.trigger_transfer("toCenter", "100")
        current_balance = page_user.check_transfer_info("Center")
        current_balance_thirdParty = page_user.check_transfer_info("TF")
        page_user.back_to_UserPage()

        Assertion.assertTransferInfo(previous_balance, previous_balance_thirdParty, "toCenter", "100",
                                     current_balance, current_balance_thirdParty)
        # 進入個人中心/ 轉賬紀錄確認金流過程訂單對應狀態
        page_user.switch_report_option("transfer")
        transferReport_info = page_user.check_transferReport_info()
        transferNo = transferReport_info[1]

        Assertion.assertTransferReport_info("toCenter", "100.00", transferReport_info[0], transferNo)
        # 因前端文案不一, 改由AT確認轉賬類型正確
        TransferInfo_AT = self.AdminTool.api_FundTransfer_Manage(transferNo)
        TransferType = extract_json('Data.List.Data[0].Description', TransferInfo_AT.text)
        TransferStatus = extract_json('Data.List.Data[0].StatusText', TransferInfo_AT.text)
        expect_data = Localization.get_loc("AdminTool_TransferManagement", "TransferType_", "TF")
        # AT查詢: 轉賬方符合預期 & 狀態"已完成"
        self.assertEqual([expect_data, self.TransferStatus_Done], [TransferType, TransferStatus])

    def test_06_15_Transfer_to_thirdParty_DG(self):
        page_user = UserPage(self.driver)
        page_user.switch_finance_option("transfer")
        page_user.select_thirdParty_option("DG")
        previous_balance = page_user.check_transfer_info("Center")
        previous_balance_thirdParty = page_user.check_transfer_info("DG")

        page_user.trigger_transfer("toThirdParty", "100")
        current_balance = page_user.check_transfer_info("Center")
        current_balance_thirdParty = page_user.check_transfer_info("DG")
        page_user.back_to_UserPage()

        Assertion.assertTransferInfo(previous_balance, previous_balance_thirdParty, "toThirdParty", "100",
                                     current_balance, current_balance_thirdParty)
        # 進入個人中心/ 轉賬紀錄確認金流過程訂單對應狀態
        page_user.switch_report_option("transfer")
        transferReport_info = page_user.check_transferReport_info()
        transferNo = transferReport_info[1]

        Assertion.assertTransferReport_info("toThirdParty", "100.00", transferReport_info[0], transferNo)
        # 因前端文案不一, 改由AT確認轉賬類型正確
        TransferInfo_AT = self.AdminTool.api_FundTransfer_Manage(transferNo)
        TransferType = extract_json('Data.List.Data[0].Description', TransferInfo_AT.text)
        TransferStatus = extract_json('Data.List.Data[0].StatusText', TransferInfo_AT.text)
        expect_data = Localization.get_loc("AdminTool_TransferManagement", "TransferType_", "DG")
        # AT查詢: 轉賬方符合預期 & 狀態"已完成"
        self.assertEqual([expect_data, self.TransferStatus_Done], [TransferType, TransferStatus])

    def test_06_16_Transfer_from_thirdParty_DG(self):
        page_user = UserPage(self.driver)
        page_user.switch_finance_option("transfer")
        page_user.select_thirdParty_option("DG")
        previous_balance = page_user.check_transfer_info("Center")
        previous_balance_thirdParty = page_user.check_transfer_info("DG")

        page_user.trigger_transfer("toCenter", "100")
        current_balance = page_user.check_transfer_info("Center")
        current_balance_thirdParty = page_user.check_transfer_info("DG")
        page_user.back_to_UserPage()

        Assertion.assertTransferInfo(previous_balance, previous_balance_thirdParty, "toCenter", "100",
                                     current_balance, current_balance_thirdParty)
        # 進入個人中心/ 轉賬紀錄確認金流過程訂單對應狀態
        page_user.switch_report_option("transfer")
        transferReport_info = page_user.check_transferReport_info()
        transferNo = transferReport_info[1]

        Assertion.assertTransferReport_info("toCenter", "100.00", transferReport_info[0], transferNo)
        # 因前端文案不一, 改由AT確認轉賬類型正確
        TransferInfo_AT = self.AdminTool.api_FundTransfer_Manage(transferNo)
        TransferType = extract_json('Data.List.Data[0].Description', TransferInfo_AT.text)
        TransferStatus = extract_json('Data.List.Data[0].StatusText', TransferInfo_AT.text)
        expect_data = Localization.get_loc("AdminTool_TransferManagement", "TransferType_", "DG")
        # AT查詢: 轉賬方符合預期 & 狀態"已完成"
        self.assertEqual([expect_data, self.TransferStatus_Done], [TransferType, TransferStatus])

    @unittest.skipUnless(Project == 'vt', '目前只有越南站支援')
    def test_06_17_Transfer_to_thirdParty_WM(self):
        page_user = UserPage(self.driver)
        page_user.switch_finance_option("transfer")
        page_user.select_thirdParty_option("WM")
        previous_balance = page_user.check_transfer_info("Center")
        previous_balance_thirdParty = page_user.check_transfer_info("WM")

        page_user.trigger_transfer("toThirdParty", "100")
        current_balance = page_user.check_transfer_info("Center")
        current_balance_thirdParty = page_user.check_transfer_info("WM")
        page_user.back_to_UserPage()

        Assertion.assertTransferInfo(previous_balance, previous_balance_thirdParty, "toThirdParty", "100",
                                     current_balance, current_balance_thirdParty)
        # 進入個人中心/ 轉賬紀錄確認金流過程訂單對應狀態
        page_user.switch_report_option("transfer")
        transferReport_info = page_user.check_transferReport_info()
        transferNo = transferReport_info[1]

        Assertion.assertTransferReport_info("toThirdParty", "100.00", transferReport_info[0], transferNo)
        # 因前端文案不一, 改由AT確認轉賬類型正確
        TransferInfo_AT = self.AdminTool.api_FundTransfer_Manage(transferNo)
        TransferType = extract_json('Data.List.Data[0].Description', TransferInfo_AT.text)
        TransferStatus = extract_json('Data.List.Data[0].StatusText', TransferInfo_AT.text)
        expect_data = Localization.get_loc("AdminTool_TransferManagement", "TransferType_", "WM")
        # AT查詢: 轉賬方符合預期 & 狀態"已完成"
        self.assertEqual([expect_data, self.TransferStatus_Done], [TransferType, TransferStatus])

    @unittest.skipUnless(Project == 'vt', '目前只有越南站支援')
    def test_06_18_Transfer_from_thirdParty_WM(self):
        page_user = UserPage(self.driver)
        page_user.switch_finance_option("transfer")
        page_user.select_thirdParty_option("WM")
        previous_balance = page_user.check_transfer_info("Center")
        previous_balance_thirdParty = page_user.check_transfer_info("WM")

        page_user.trigger_transfer("toCenter", "100")
        current_balance = page_user.check_transfer_info("Center")
        current_balance_thirdParty = page_user.check_transfer_info("WM")
        page_user.back_to_UserPage()

        Assertion.assertTransferInfo(previous_balance, previous_balance_thirdParty, "toCenter", "100",
                                     current_balance, current_balance_thirdParty)
        # 進入個人中心/ 轉賬紀錄確認金流過程訂單對應狀態
        page_user.switch_report_option("transfer")
        transferReport_info = page_user.check_transferReport_info()
        transferNo = transferReport_info[1]

        Assertion.assertTransferReport_info("toCenter", "100.00", transferReport_info[0], transferNo)
        # 因前端文案不一, 改由AT確認轉賬類型正確
        TransferInfo_AT = self.AdminTool.api_FundTransfer_Manage(transferNo)
        TransferType = extract_json('Data.List.Data[0].Description', TransferInfo_AT.text)
        TransferStatus = extract_json('Data.List.Data[0].StatusText', TransferInfo_AT.text)
        expect_data = Localization.get_loc("AdminTool_TransferManagement", "TransferType_", "WM")
        # AT查詢: 轉賬方符合預期 & 狀態"已完成"
        self.assertEqual([expect_data, self.TransferStatus_Done], [TransferType, TransferStatus])

    @unittest.skipUnless(Project == 'vt', '目前只有越南站支援')
    def test_06_19_Transfer_to_thirdParty_Sexy(self):
        page_user = UserPage(self.driver)
        page_user.switch_finance_option("transfer")
        page_user.select_thirdParty_option("Sexy")
        previous_balance = page_user.check_transfer_info("Center")
        previous_balance_thirdParty = page_user.check_transfer_info("Sexy")

        page_user.trigger_transfer("toThirdParty", "100")
        current_balance = page_user.check_transfer_info("Center")
        current_balance_thirdParty = page_user.check_transfer_info("Sexy")
        page_user.back_to_UserPage()

        Assertion.assertTransferInfo(previous_balance, previous_balance_thirdParty, "toThirdParty", "100",
                                     current_balance, current_balance_thirdParty)
        # 進入個人中心/ 轉賬紀錄確認金流過程訂單對應狀態
        page_user.switch_report_option("transfer")
        transferReport_info = page_user.check_transferReport_info()
        transferNo = transferReport_info[1]

        Assertion.assertTransferReport_info("toThirdParty", "100.00", transferReport_info[0], transferNo)
        # 因前端文案不一, 改由AT確認轉賬類型正確
        TransferInfo_AT = self.AdminTool.api_FundTransfer_Manage(transferNo)
        TransferType = extract_json('Data.List.Data[0].Description', TransferInfo_AT.text)
        TransferStatus = extract_json('Data.List.Data[0].StatusText', TransferInfo_AT.text)
        expect_data = Localization.get_loc("AdminTool_TransferManagement", "TransferType_", "Sexy")
        # AT查詢: 轉賬方符合預期 & 狀態"已完成"
        self.assertEqual([expect_data, self.TransferStatus_Done], [TransferType, TransferStatus])

    @unittest.skipUnless(Project == 'vt', '目前只有越南站支援')
    def test_06_20_Transfer_from_thirdParty_Sexy(self):
        page_user = UserPage(self.driver)
        page_user.switch_finance_option("transfer")
        page_user.select_thirdParty_option("Sexy")
        previous_balance = page_user.check_transfer_info("Center")
        previous_balance_thirdParty = page_user.check_transfer_info("Sexy")

        page_user.trigger_transfer("toCenter", "100")
        current_balance = page_user.check_transfer_info("Center")
        current_balance_thirdParty = page_user.check_transfer_info("Sexy")
        page_user.back_to_UserPage()

        Assertion.assertTransferInfo(previous_balance, previous_balance_thirdParty, "toCenter", "100",
                                     current_balance, current_balance_thirdParty)
        # 進入個人中心/ 轉賬紀錄確認金流過程訂單對應狀態
        page_user.switch_report_option("transfer")
        transferReport_info = page_user.check_transferReport_info()
        transferNo = transferReport_info[1]

        Assertion.assertTransferReport_info("toCenter", "100.00", transferReport_info[0], transferNo)
        # 因前端文案不一, 改由AT確認轉賬類型正確
        TransferInfo_AT = self.AdminTool.api_FundTransfer_Manage(transferNo)
        TransferType = extract_json('Data.List.Data[0].Description', TransferInfo_AT.text)
        TransferStatus = extract_json('Data.List.Data[0].StatusText', TransferInfo_AT.text)
        expect_data = Localization.get_loc("AdminTool_TransferManagement", "TransferType_", "Sexy")
        # AT查詢: 轉賬方符合預期 & 狀態"已完成"
        self.assertEqual([expect_data, self.TransferStatus_Done], [TransferType, TransferStatus])

    @unittest.skipUnless(Project == 'vt', '目前只有越南站支援')
    def test_06_21_Transfer_to_thirdParty_CMD(self):
        page_user = UserPage(self.driver)
        page_user.switch_finance_option("transfer")
        page_user.select_thirdParty_option("CMD")
        previous_balance = page_user.check_transfer_info("Center")
        previous_balance_thirdParty = page_user.check_transfer_info("CMD")

        page_user.trigger_transfer("toThirdParty", "100")
        current_balance = page_user.check_transfer_info("Center")
        current_balance_thirdParty = page_user.check_transfer_info("CMD")
        page_user.back_to_UserPage()

        Assertion.assertTransferInfo(previous_balance, previous_balance_thirdParty, "toThirdParty", "100",
                                     current_balance, current_balance_thirdParty)
        # 進入個人中心/ 轉賬紀錄確認金流過程訂單對應狀態
        page_user.switch_report_option("transfer")
        transferReport_info = page_user.check_transferReport_info()
        transferNo = transferReport_info[1]

        Assertion.assertTransferReport_info("toThirdParty", "100.00", transferReport_info[0], transferNo)
        # 因前端文案不一, 改由AT確認轉賬類型正確
        TransferInfo_AT = self.AdminTool.api_FundTransfer_Manage(transferNo)
        TransferType = extract_json('Data.List.Data[0].Description', TransferInfo_AT.text)
        TransferStatus = extract_json('Data.List.Data[0].StatusText', TransferInfo_AT.text)
        expect_data = Localization.get_loc("AdminTool_TransferManagement", "TransferType_", "CMD")
        # AT查詢: 轉賬方符合預期 & 狀態"已完成"
        self.assertEqual([expect_data, self.TransferStatus_Done], [TransferType, TransferStatus])

    @unittest.skipUnless(Project == 'vt', '目前只有越南站支援')
    def test_06_22_Transfer_from_thirdParty_CMD(self):
        page_user = UserPage(self.driver)
        page_user.switch_finance_option("transfer")
        page_user.select_thirdParty_option("CMD")
        previous_balance = page_user.check_transfer_info("Center")
        previous_balance_thirdParty = page_user.check_transfer_info("CMD")

        page_user.trigger_transfer("toCenter", "100")
        current_balance = page_user.check_transfer_info("Center")
        current_balance_thirdParty = page_user.check_transfer_info("CMD")
        page_user.back_to_UserPage()

        Assertion.assertTransferInfo(previous_balance, previous_balance_thirdParty, "toCenter", "100",
                                     current_balance, current_balance_thirdParty)
        # 進入個人中心/ 轉賬紀錄確認金流過程訂單對應狀態
        page_user.switch_report_option("transfer")
        transferReport_info = page_user.check_transferReport_info()
        transferNo = transferReport_info[1]

        Assertion.assertTransferReport_info("toCenter", "100.00", transferReport_info[0], transferNo)
        # 因前端文案不一, 改由AT確認轉賬類型正確
        TransferInfo_AT = self.AdminTool.api_FundTransfer_Manage(transferNo)
        TransferType = extract_json('Data.List.Data[0].Description', TransferInfo_AT.text)
        TransferStatus = extract_json('Data.List.Data[0].StatusText', TransferInfo_AT.text)
        expect_data = Localization.get_loc("AdminTool_TransferManagement", "TransferType_", "CMD")
        # AT查詢: 轉賬方符合預期 & 狀態"已完成"
        self.assertEqual([expect_data, self.TransferStatus_Done], [TransferType, TransferStatus])

    @unittest.skipUnless(Project == 'vt', '目前只有越南站支援')
    def test_06_23_Transfer_to_thirdParty_SBO(self):
        page_user = UserPage(self.driver)
        page_user.switch_finance_option("transfer")
        page_user.select_thirdParty_option("SBO")
        previous_balance = page_user.check_transfer_info("Center")
        previous_balance_thirdParty = page_user.check_transfer_info("SBO")

        page_user.trigger_transfer("toThirdParty", "100")
        current_balance = page_user.check_transfer_info("Center")
        current_balance_thirdParty = page_user.check_transfer_info("SBO")
        page_user.back_to_UserPage()

        Assertion.assertTransferInfo(previous_balance, previous_balance_thirdParty, "toThirdParty", "100",
                                     current_balance, current_balance_thirdParty)
        # 進入個人中心/ 轉賬紀錄確認金流過程訂單對應狀態
        page_user.switch_report_option("transfer")
        transferReport_info = page_user.check_transferReport_info()
        transferNo = transferReport_info[1]

        Assertion.assertTransferReport_info("toThirdParty", "100.00", transferReport_info[0], transferNo)
        # 因前端文案不一, 改由AT確認轉賬類型正確
        TransferInfo_AT = self.AdminTool.api_FundTransfer_Manage(transferNo)
        TransferType = extract_json('Data.List.Data[0].Description', TransferInfo_AT.text)
        TransferStatus = extract_json('Data.List.Data[0].StatusText', TransferInfo_AT.text)
        expect_data = Localization.get_loc("AdminTool_TransferManagement", "TransferType_", "SBO")
        # AT查詢: 轉賬方符合預期 & 狀態"已完成"
        self.assertEqual([expect_data, self.TransferStatus_Done], [TransferType, TransferStatus])

    @unittest.skipUnless(Project == 'vt', '目前只有越南站支援')
    def test_06_24_Transfer_from_thirdParty_SBO(self):
        page_user = UserPage(self.driver)
        page_user.switch_finance_option("transfer")
        page_user.select_thirdParty_option("SBO")
        previous_balance = page_user.check_transfer_info("Center")
        previous_balance_thirdParty = page_user.check_transfer_info("SBO")

        page_user.trigger_transfer("toCenter", "100")
        current_balance = page_user.check_transfer_info("Center")
        current_balance_thirdParty = page_user.check_transfer_info("SBO")
        page_user.back_to_UserPage()

        Assertion.assertTransferInfo(previous_balance, previous_balance_thirdParty, "toCenter", "100",
                                     current_balance, current_balance_thirdParty)
        # 進入個人中心/ 轉賬紀錄確認金流過程訂單對應狀態
        page_user.switch_report_option("transfer")
        transferReport_info = page_user.check_transferReport_info()
        transferNo = transferReport_info[1]

        Assertion.assertTransferReport_info("toCenter", "100.00", transferReport_info[0], transferNo)
        # 因前端文案不一, 改由AT確認轉賬類型正確
        TransferInfo_AT = self.AdminTool.api_FundTransfer_Manage(transferNo)
        TransferType = extract_json('Data.List.Data[0].Description', TransferInfo_AT.text)
        TransferStatus = extract_json('Data.List.Data[0].StatusText', TransferInfo_AT.text)
        expect_data = Localization.get_loc("AdminTool_TransferManagement", "TransferType_", "SBO")
        # AT查詢: 轉賬方符合預期 & 狀態"已完成"
        self.assertEqual([expect_data, self.TransferStatus_Done], [TransferType, TransferStatus])

    @unittest.skipUnless(Project == 'vt', '目前只有越南站支援')
    def test_06_25_Transfer_to_thirdParty_CQ9(self):
        page_user = UserPage(self.driver)
        page_user.switch_finance_option("transfer")
        page_user.select_thirdParty_option("CQ9")
        previous_balance = page_user.check_transfer_info("Center")
        previous_balance_thirdParty = page_user.check_transfer_info("CQ9")

        page_user.trigger_transfer("toThirdParty", "100")
        current_balance = page_user.check_transfer_info("Center")
        current_balance_thirdParty = page_user.check_transfer_info("CQ9")
        page_user.back_to_UserPage()

        Assertion.assertTransferInfo(previous_balance, previous_balance_thirdParty, "toThirdParty", "100",
                                     current_balance, current_balance_thirdParty)
        # 進入個人中心/ 轉賬紀錄確認金流過程訂單對應狀態
        page_user.switch_report_option("transfer")
        transferReport_info = page_user.check_transferReport_info()
        transferNo = transferReport_info[1]

        Assertion.assertTransferReport_info("toThirdParty", "100.00", transferReport_info[0], transferNo)
        # 因前端文案不一, 改由AT確認轉賬類型正確
        TransferInfo_AT = self.AdminTool.api_FundTransfer_Manage(transferNo)
        TransferType = extract_json('Data.List.Data[0].Description', TransferInfo_AT.text)
        TransferStatus = extract_json('Data.List.Data[0].StatusText', TransferInfo_AT.text)
        expect_data = Localization.get_loc("AdminTool_TransferManagement", "TransferType_", "CQ9")
        # AT查詢: 轉賬方符合預期 & 狀態"已完成"
        self.assertEqual([expect_data, self.TransferStatus_Done], [TransferType, TransferStatus])

    @unittest.skipUnless(Project == 'vt', '目前只有越南站支援')
    def test_06_26_Transfer_from_thirdParty_CQ9(self):
        page_user = UserPage(self.driver)
        page_user.switch_finance_option("transfer")
        page_user.select_thirdParty_option("CQ9")
        previous_balance = page_user.check_transfer_info("Center")
        previous_balance_thirdParty = page_user.check_transfer_info("CQ9")

        page_user.trigger_transfer("toCenter", "100")
        current_balance = page_user.check_transfer_info("Center")
        current_balance_thirdParty = page_user.check_transfer_info("CQ9")
        page_user.back_to_UserPage()

        Assertion.assertTransferInfo(previous_balance, previous_balance_thirdParty, "toCenter", "100",
                                     current_balance, current_balance_thirdParty)
        # 進入個人中心/ 轉賬紀錄確認金流過程訂單對應狀態
        page_user.switch_report_option("transfer")
        transferReport_info = page_user.check_transferReport_info()
        transferNo = transferReport_info[1]

        Assertion.assertTransferReport_info("toCenter", "100.00", transferReport_info[0], transferNo)
        # 因前端文案不一, 改由AT確認轉賬類型正確
        TransferInfo_AT = self.AdminTool.api_FundTransfer_Manage(transferNo)
        TransferType = extract_json('Data.List.Data[0].Description', TransferInfo_AT.text)
        TransferStatus = extract_json('Data.List.Data[0].StatusText', TransferInfo_AT.text)
        expect_data = Localization.get_loc("AdminTool_TransferManagement", "TransferType_", "CQ9")
        # AT查詢: 轉賬方符合預期 & 狀態"已完成"
        self.assertEqual([expect_data, self.TransferStatus_Done], [TransferType, TransferStatus])

    @unittest.skipUnless(Project == 'vt', '目前只有越南站支援')
    def test_06_27_Transfer_to_thirdParty_CG(self):
        page_user = UserPage(self.driver)
        page_user.switch_finance_option("transfer")
        page_user.select_thirdParty_option("CG")
        previous_balance = page_user.check_transfer_info("Center")
        previous_balance_thirdParty = page_user.check_transfer_info("CG")

        page_user.trigger_transfer("toThirdParty", "100")
        current_balance = page_user.check_transfer_info("Center")
        current_balance_thirdParty = page_user.check_transfer_info("CG")
        page_user.back_to_UserPage()

        Assertion.assertTransferInfo(previous_balance, previous_balance_thirdParty, "toThirdParty", "100",
                                     current_balance, current_balance_thirdParty)
        # 進入個人中心/ 轉賬紀錄確認金流過程訂單對應狀態
        page_user.switch_report_option("transfer")
        transferReport_info = page_user.check_transferReport_info()
        transferNo = transferReport_info[1]

        Assertion.assertTransferReport_info("toThirdParty", "100.00", transferReport_info[0], transferNo)
        # 因前端文案不一, 改由AT確認轉賬類型正確
        TransferInfo_AT = self.AdminTool.api_FundTransfer_Manage(transferNo)
        TransferType = extract_json('Data.List.Data[0].Description', TransferInfo_AT.text)
        TransferStatus = extract_json('Data.List.Data[0].StatusText', TransferInfo_AT.text)
        expect_data = Localization.get_loc("AdminTool_TransferManagement", "TransferType_", "CG")
        # AT查詢: 轉賬方符合預期 & 狀態"已完成"
        self.assertEqual([expect_data, self.TransferStatus_Done], [TransferType, TransferStatus])

    @unittest.skipUnless(Project == 'vt', '目前只有越南站支援')
    def test_06_28_Transfer_from_thirdParty_CG(self):
        page_user = UserPage(self.driver)
        page_user.switch_finance_option("transfer")
        page_user.select_thirdParty_option("CG")
        previous_balance = page_user.check_transfer_info("Center")
        previous_balance_thirdParty = page_user.check_transfer_info("CG")

        page_user.trigger_transfer("toCenter", "100")
        current_balance = page_user.check_transfer_info("Center")
        current_balance_thirdParty = page_user.check_transfer_info("CG")
        page_user.back_to_UserPage()

        Assertion.assertTransferInfo(previous_balance, previous_balance_thirdParty, "toCenter", "100",
                                     current_balance, current_balance_thirdParty)
        # 進入個人中心/ 轉賬紀錄確認金流過程訂單對應狀態
        page_user.switch_report_option("transfer")
        transferReport_info = page_user.check_transferReport_info()
        transferNo = transferReport_info[1]

        Assertion.assertTransferReport_info("toCenter", "100.00", transferReport_info[0], transferNo)
        # 因前端文案不一, 改由AT確認轉賬類型正確
        TransferInfo_AT = self.AdminTool.api_FundTransfer_Manage(transferNo)
        TransferType = extract_json('Data.List.Data[0].Description', TransferInfo_AT.text)
        TransferStatus = extract_json('Data.List.Data[0].StatusText', TransferInfo_AT.text)
        expect_data = Localization.get_loc("AdminTool_TransferManagement", "TransferType_", "CG")
        # AT查詢: 轉賬方符合預期 & 狀態"已完成"
        self.assertEqual([expect_data, self.TransferStatus_Done], [TransferType, TransferStatus])

    @unittest.skipUnless(Project == 'vt', '目前只有越南站支援')
    def test_06_29_Transfer_to_thirdParty_LC(self):
        page_user = UserPage(self.driver)
        page_user.switch_finance_option("transfer")
        page_user.select_thirdParty_option("LC")
        previous_balance = page_user.check_transfer_info("Center")
        previous_balance_thirdParty = page_user.check_transfer_info("LC")

        page_user.trigger_transfer("toThirdParty", "100")
        current_balance = page_user.check_transfer_info("Center")
        current_balance_thirdParty = page_user.check_transfer_info("LC")
        page_user.back_to_UserPage()

        Assertion.assertTransferInfo(previous_balance, previous_balance_thirdParty, "toThirdParty", "100",
                                     current_balance, current_balance_thirdParty)
        # 進入個人中心/ 轉賬紀錄確認金流過程訂單對應狀態
        page_user.switch_report_option("transfer")
        transferReport_info = page_user.check_transferReport_info()
        transferNo = transferReport_info[1]

        Assertion.assertTransferReport_info("toThirdParty", "100.00", transferReport_info[0], transferNo)
        # 因前端文案不一, 改由AT確認轉賬類型正確
        TransferInfo_AT = self.AdminTool.api_FundTransfer_Manage(transferNo)
        TransferType = extract_json('Data.List.Data[0].Description', TransferInfo_AT.text)
        TransferStatus = extract_json('Data.List.Data[0].StatusText', TransferInfo_AT.text)
        expect_data = Localization.get_loc("AdminTool_TransferManagement", "TransferType_", "LC")
        # AT查詢: 轉賬方符合預期 & 狀態"已完成"
        self.assertEqual([expect_data, self.TransferStatus_Done], [TransferType, TransferStatus])

    @unittest.skipUnless(Project == 'vt', '目前只有越南站支援')
    def test_06_30_Transfer_from_thirdParty_LC(self):
        page_user = UserPage(self.driver)
        page_user.switch_finance_option("transfer")
        page_user.select_thirdParty_option("LC")
        previous_balance = page_user.check_transfer_info("Center")
        previous_balance_thirdParty = page_user.check_transfer_info("LC")

        page_user.trigger_transfer("toCenter", "100")
        current_balance = page_user.check_transfer_info("Center")
        current_balance_thirdParty = page_user.check_transfer_info("LC")
        page_user.back_to_UserPage()

        Assertion.assertTransferInfo(previous_balance, previous_balance_thirdParty, "toCenter", "100",
                                     current_balance, current_balance_thirdParty)
        # 進入個人中心/ 轉賬紀錄確認金流過程訂單對應狀態
        page_user.switch_report_option("transfer")
        transferReport_info = page_user.check_transferReport_info()
        transferNo = transferReport_info[1]

        Assertion.assertTransferReport_info("toCenter", "100.00", transferReport_info[0], transferNo)
        # 因前端文案不一, 改由AT確認轉賬類型正確
        TransferInfo_AT = self.AdminTool.api_FundTransfer_Manage(transferNo)
        TransferType = extract_json('Data.List.Data[0].Description', TransferInfo_AT.text)
        TransferStatus = extract_json('Data.List.Data[0].StatusText', TransferInfo_AT.text)
        expect_data = Localization.get_loc("AdminTool_TransferManagement", "TransferType_", "LC")
        # AT查詢: 轉賬方符合預期 & 狀態"已完成"
        self.assertEqual([expect_data, self.TransferStatus_Done], [TransferType, TransferStatus])

    @unittest.skipUnless(Project == 'vt', '目前只有越南站支援')
    def test_06_31_Transfer_to_thirdParty_BBIN(self):
        page_user = UserPage(self.driver)
        page_user.switch_finance_option("transfer")
        page_user.select_thirdParty_option("BBIN")
        previous_balance = page_user.check_transfer_info("Center")
        previous_balance_thirdParty = page_user.check_transfer_info("BBIN")

        page_user.trigger_transfer("toThirdParty", "100")
        current_balance = page_user.check_transfer_info("Center")
        current_balance_thirdParty = page_user.check_transfer_info("BBIN")
        page_user.back_to_UserPage()

        Assertion.assertTransferInfo(previous_balance, previous_balance_thirdParty, "toThirdParty", "100",
                                     current_balance, current_balance_thirdParty)
        # 進入個人中心/ 轉賬紀錄確認金流過程訂單對應狀態
        page_user.switch_report_option("transfer")
        transferReport_info = page_user.check_transferReport_info()
        transferNo = transferReport_info[1]

        Assertion.assertTransferReport_info("toThirdParty", "100.00", transferReport_info[0], transferNo)
        # 因前端文案不一, 改由AT確認轉賬類型正確
        TransferInfo_AT = self.AdminTool.api_FundTransfer_Manage(transferNo)
        TransferType = extract_json('Data.List.Data[0].Description', TransferInfo_AT.text)
        TransferStatus = extract_json('Data.List.Data[0].StatusText', TransferInfo_AT.text)
        expect_data = Localization.get_loc("AdminTool_TransferManagement", "TransferType_", "BBIN")
        # AT查詢: 轉賬方符合預期 & 狀態"已完成"
        self.assertEqual([expect_data, self.TransferStatus_Done], [TransferType, TransferStatus])

    @unittest.skipUnless(Project == 'vt', '目前只有越南站支援')
    def test_06_32_Transfer_from_thirdParty_BBIN(self):
        page_user = UserPage(self.driver)
        page_user.switch_finance_option("transfer")
        page_user.select_thirdParty_option("BBIN")
        previous_balance = page_user.check_transfer_info("Center")
        previous_balance_thirdParty = page_user.check_transfer_info("BBIN")

        page_user.trigger_transfer("toCenter", "100")
        current_balance = page_user.check_transfer_info("Center")
        current_balance_thirdParty = page_user.check_transfer_info("BBIN")
        page_user.back_to_UserPage()

        Assertion.assertTransferInfo(previous_balance, previous_balance_thirdParty, "toCenter", "100",
                                     current_balance, current_balance_thirdParty)
        # 進入個人中心/ 轉賬紀錄確認金流過程訂單對應狀態
        page_user.switch_report_option("transfer")
        transferReport_info = page_user.check_transferReport_info()
        transferNo = transferReport_info[1]

        Assertion.assertTransferReport_info("toCenter", "100.00", transferReport_info[0], transferNo)
        # 因前端文案不一, 改由AT確認轉賬類型正確
        TransferInfo_AT = self.AdminTool.api_FundTransfer_Manage(transferNo)
        TransferType = extract_json('Data.List.Data[0].Description', TransferInfo_AT.text)
        TransferStatus = extract_json('Data.List.Data[0].StatusText', TransferInfo_AT.text)
        expect_data = Localization.get_loc("AdminTool_TransferManagement", "TransferType_", "BBIN")
        # AT查詢: 轉賬方符合預期 & 狀態"已完成"
        self.assertEqual([expect_data, self.TransferStatus_Done], [TransferType, TransferStatus])

    def test_07_01_Withdraw_Account_Management_Add_BankCard(self):
        page_user = UserPage(self.driver)
        page_user.switch_finance_option("withdraw_account")
        page_user.switch_withdraw_account_type("bank")
        page_user.click_button_add_bank_card()
        card_num = page_user.generate_bank_card_num()
        page_user.complete_input_bank_card_num(card_num)
        page_user.click_button_OTP_request()
        otp = self.AdminTool.get_smsLog(self.account)
        page_user.complete_input_otp(otp)
        page_user.back_to_UserPage()
        self.AdminTool.api_Member_MemberBank_Patch(self.account, 1, card_num, False)

    def test_07_02_Withdraw_Account_Management_Add_Crypto_Wallet(self):
        protocol = 'erc'  # protocol = 'erc' or 'trc' or 'omni'
        page_user = UserPage(self.driver)
        page_user.switch_finance_option("withdraw_account")
        page_user.switch_withdraw_account_type("crypto")
        page_user.click_button_add_crypto_wallet()
        CryptoCurrencyAddress = page_user.generate_crypto_wallet_address(protocol)
        page_user.complete_input_crypto_wallet_address(protocol, CryptoCurrencyAddress)
        page_user.click_button_OTP_request()
        otp = self.AdminTool.get_smsLog(self.account)
        page_user.complete_input_otp(otp)
        page_user.back_to_UserPage()
        self.AdminTool.api_Member_CryptoCurrencyWallet_Patch(self.account, 1, CryptoCurrencyAddress, False)

    def test_08_01_Costumer_Service_Nav_Entrance(self):
        page_user = UserPage(self.driver)
        page_user.click_button_cs_nav()
        actual_result = page_user.confirm_cs_loading_complete()
        page_user.back_to_UserPage()
        self.assertEqual(actual_result, True)

    def test_08_02_Costumer_Service_Mine_Entrance(self):
        page_user = UserPage(self.driver)
        page_user.click_button_cs_mine()
        actual_result = page_user.confirm_cs_loading_complete()
        page_user.back_to_UserPage()
        self.assertEqual(actual_result, True)

    @unittest.skipUnless(Project == 'vt', '目前只有越南站支援')
    def test_09_01_Promo_Costumer_Service(self):
        page_user = UserPage(self.driver)
        page_user.click_button_promo()
        page_user.click_button_promo_cs()
        actual_result = page_user.confirm_cs_loading_complete()
        page_user.back_to_UserPage()
        page_user.back_to_UserPage()
        self.assertEqual(actual_result, True)

    @unittest.skipUnless(Project == 'vt', '目前只有越南站支援')
    def test_09_02_Promo_Download_App(self):
        page_user = UserPage(self.driver)
        page_user.click_button_promo()
        page_user.click_button_promo_download()
        current_url = page_user.store_current_url()
        actual_result = page_user.check_keyword_in_string("download", current_url)
        base_page = BasePage(self.driver)
        base_page.back_prev_page()
        base_page.back_prev_page()
        self.assertEqual(actual_result, True)

    @unittest.skipUnless(Project == 'vt', '目前只有越南站支援')
    def test_09_03_Register_Url_With_Promo_Code(self):
        page_user = UserPage(self.driver)
        page_user.click_button_promo()
        promo_code = page_user.store_copy_promo_code()
        page_user.click_button_promo_qr_code()
        page_user.click_button_register_with_promo_code()
        register_url = page_user.store_clipboard_text_content()
        print(promo_code, register_url)
        actual_result = page_user.check_keyword_in_string(promo_code, register_url)
        base_page = BasePage(self.driver)
        base_page.back_prev_page()
        base_page.back_prev_page()
        self.assertEqual(actual_result, True)

    @unittest.skipUnless(Project == 'vt', '目前只有越南站支援')
    def test_09_04_Download_Promo_QR_Code(self):
        page_user = UserPage(self.driver)
        # 因推廣註冊頁的QR code圖片檔名都是一樣的，避免與之前的測試資料混淆，若存在相同檔名應予刪除
        page_user.delete_download_file_from_device('/storage/emulated/0/Download/image.png')
        page_user.click_button_promo()
        page_user.click_button_promo_qr_code()
        page_user.click_button_download_promo_qr_code()
        actual_result = page_user.get_download_file_from_device('/storage/emulated/0/Download/image.png')

        base_page = BasePage(self.driver)
        base_page.back_prev_page()
        base_page.back_prev_page()
        self.driver.refresh()
        self.assertEqual(actual_result, True)

    @classmethod
    def tearDownClass(cls):
        cls.driver = Driver
        home_page = HomePage(cls.driver)
        home_page.switch_category("home")


if __name__ == '__main__':
    unittest.main()
