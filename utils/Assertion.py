import unittest
from decimal import *

self = unittest.TestCase()


# Following Functions for format convert
def transfer_amount_format(*ori_amount):
    amount_before = list(ori_amount)
    return [Decimal(amount.replace(',', "").replace('元', "")) for amount in amount_before]


def transfer_list_format(target):
    if type(target) == dict:
        target = list(target.values())
    str_list = []
    for value in target:
        if type(value) == bool:
            value = str(value).lower()
        elif type(value) == int:
            value = str(value)
        elif type(value) == float:
            value = str(Decimal(value).quantize(Decimal('.01'), rounding=ROUND_DOWN))
        elif type(value) == str:
            pass
        str_list.append(value)
    return str_list

def transfer_list_format_for_h5_vip(target):
    if type(target) == dict:
        target = list(target.values())
    str_list = []
    for value in target:
        if type(value) == bool:
            value = str(value).lower()
        elif type(value) == int:
            value = str(value)
        elif type(value) == float:
            value = str(value)
        elif type(value) == str:
            pass
        str_list.append(value)
    return str_list

# Following Functions for API use
def assertHTTPCode(response, code_list=None):
    res_code = response.status_code

    if not code_list:
        code_list = [200]

    if res_code not in code_list:
        raise AssertionError("Response code: {0} not in code list.".format(res_code))


# Following Functions for UI use
def assertOrderInfo(expect_data, order_info_confirm, order_info_done):
    count = 0
    while count < len(expect_data):  # 0: 彩種名, 1: 期號格式, 2: 投注總額, 3: 追號與否, 4: 投注項, 5: 注數
        if count == 1:
            self.assertRegex(order_info_confirm[count], "(.+\w)")
        else:
            self.assertEqual(expect_data[count], order_info_confirm[count])
        count += 1

    self.assertEqual(order_info_confirm, order_info_done)


def assertDepositInfo(pre_balance, channel, deposit_info, expect_data, current_balance, depositStatus="Success"):
    # 處理金額格式
    amount_list = transfer_amount_format(pre_balance[0], expect_data[1], current_balance[0])
    pre_balance, deposit_amount, current_balance = amount_list[0], amount_list[1], amount_list[2]
    # 驗證訂單資訊
    if channel == 'USDT':
        deposit_amount_usdt = deposit_amount * Decimal(deposit_info[7])
        channel_fee = Decimal(deposit_amount_usdt
                              * Decimal(deposit_info[2].replace('%', "")) / 100).quantize(Decimal('.00'), ROUND_DOWN)
        count = 0
        while count < len(expect_data):
            # 0: 訂單編號, 1: 充值金額, 2: 手續費(web無%), 3: 支付名稱, 4: 錢包協議, 5: 錢包地址, 6: 幣別, 7: 匯率, 8: 應上分金額
            if count == 0:
                self.assertRegex(deposit_info[count], "(.+\w)")
            elif count == 2:
                self.assertRegex(deposit_info[count], "(.+\d)")
            elif count in [3, 4, 5]:
                self.assertRegex(deposit_info[count], "(.+)")
            elif count == 6:
                self.assertRegex(deposit_info[count], "(.+\D)")
            elif count in [7, 8]:
                self.assertRegex(deposit_info[count], "(.+\d)")
            else:
                self.assertEqual(expect_data[count], deposit_info[count])
            count += 1
        # 驗證帳戶充值後餘額 = 充值前餘額 + 應上分金額 - 渠道手續費
        self.assertEqual(pre_balance + deposit_amount_usdt - channel_fee, current_balance)
    else:
        channel_fee = Decimal(deposit_amount
                              * Decimal(deposit_info[2].replace('%', "")) / 100).quantize(Decimal('.00'), ROUND_DOWN)
        if channel == 'bank':
            count = 0
            while count < len(expect_data):
                # 0: 訂單編號, 1: 充值金額, 2: 手續費(web無%), 3: 銀行名稱, 4: 銀行戶名, 5: 銀行帳號, 6: 幣別, 7: 匯率, 8: 充值附言
                if count == 0:
                    self.assertRegex(deposit_info[count], "(.+\w)")
                elif count == 2:
                    self.assertRegex(deposit_info[count], "(.+\d)")
                elif count in [3, 4]:
                    self.assertRegex(deposit_info[count], "(.+)")
                elif count in [5, 7]:
                    self.assertRegex(deposit_info[count], "(.+\d)")
                elif count == 6:
                    self.assertRegex(deposit_info[count], "(.+\D)")
                elif count == 8:
                    self.assertRegex(deposit_info[count], "(" + deposit_info[0] + "\(" + expect_data[1] + "\).+)")
                else:
                    self.assertEqual(expect_data[count], deposit_info[count])
                count += 1
        elif channel == 'thirdParty':
            count = 0
            while count < len(expect_data):
                # 0: 訂單編號, 1: 充值金額, 2: 手續費(web無%), 3: 支付方式
                if count == 0:
                    self.assertRegex(deposit_info[count], "(.+\w)")
                elif count == 2:
                    self.assertRegex(deposit_info[count], "(.+\d)")
                elif count == 3:
                    self.assertRegex(deposit_info[count], "(.+)")
                else:
                    self.assertEqual(expect_data[count], deposit_info[count])
                count += 1
        # 驗證帳戶充值後餘額 = 充值前餘額 + 充值金額 - 渠道手續費
        if depositStatus == 'Success':
            self.assertEqual(pre_balance + deposit_amount - channel_fee, current_balance)
        # 驗證帳戶調整後餘額 = 充值前餘額 + 充值金額 - 渠道手續費(金額調整的值先抓requestAmount*10的值)
        elif depositStatus == 'Adjusted':
            self.assertEqual(pre_balance + deposit_amount * 10 - channel_fee * 10, current_balance)
        # 驗證帳戶回絕後餘額 = 充值前餘額
        else:
            self.assertEqual(pre_balance, current_balance)


def assertWithdrawInfo(pre_balance, withdraw_account_info, withdraw_amount, withdraw_info, current_balance,
                       withdrawStatus="Success"):
    # 處理金額格式
    amount_list = transfer_amount_format(pre_balance[0], withdraw_amount, withdraw_info[3], withdraw_info[4],
                                         withdraw_info[5], withdraw_info[6], current_balance[0])
    pre_balance, withdraw_amount, admin_fee, discount_amount, handling_fee, final_withdraw_amount, current_balance \
        = amount_list[0], amount_list[1], amount_list[2], amount_list[3], amount_list[4], amount_list[5], amount_list[6]
    # 驗證訂單資訊
    count = 0
    while count < 7:  # 0: 銀行卡行名/USDT錢包名稱, 1: 銀行卡卡號/USDT錢包地址, 2: 提現金額, 3: 行政費, 4: 優惠金額, 5: 手續費, 6: 實際可提現金額
        if count == 0:
            self.assertEqual(withdraw_account_info[count].strip(), withdraw_info[count].strip())
        elif count == 1:
            self.assertEqual(withdraw_account_info[count], withdraw_info[count])
        elif count == 2:
            self.assertEqual(str(withdraw_amount), withdraw_info[count])
        elif count in [3, 4, 5]:  # 僅驗證為含小數點數字
            self.assertRegex(withdraw_info[count], "(.+\d)")
        elif count == 6:  # 實際可提現金額 = 提現金額 - 行政費 - 優惠金額 - 手續費
            self.assertEqual(withdraw_amount - admin_fee - discount_amount - handling_fee, final_withdraw_amount)
        count += 1
    # 驗證帳戶提現後餘額 = 提現前餘額 - 提現金額
    if withdrawStatus == 'Success':
        self.assertEqual(pre_balance - withdraw_amount, current_balance)
    # 驗證帳戶回絕/出款失敗後餘額 = 提現前餘額
    else:
        self.assertEqual(pre_balance, current_balance)


def assertTransferInfo(pre_balance, pre_balance_ta, direction, transfer_amount, current_balance, current_balance_ta):
    # 處理金額格式
    amount_list = transfer_amount_format(pre_balance, pre_balance_ta, transfer_amount,
                                         current_balance, current_balance_ta)
    pre_balance, pre_balance_ta, transfer_amount, current_balance, current_balance_ta \
        = amount_list[0], amount_list[1], amount_list[2], amount_list[3], amount_list[4]
    # 驗證主帳戶/第三方帳戶轉賬後餘額
    if direction == 'toThirdParty':
        current_balance_transferred = pre_balance - transfer_amount
        current_balance_ta_transferred = pre_balance_ta + transfer_amount
    else:
        current_balance_transferred = pre_balance + transfer_amount
        current_balance_ta_transferred = pre_balance_ta - transfer_amount
    self.assertEqual([current_balance_transferred, current_balance_ta_transferred],
                     [current_balance, current_balance_ta])


def assertTransferReport_info(direction, transfer_amount, transfer_amount_report, transferNo):
    count = 0
    while count < 2:  # 0: 轉賬金額, 1: 訂單編號, 2: 轉賬類型(目前前端文案不一, 統一改由AT驗證)
        if count == 0:
            transfer_amount_transferred = None
            if direction == 'toThirdParty':
                transfer_amount_transferred = str("-" + transfer_amount)
            elif direction == 'toCenter':
                transfer_amount_transferred = str("+" + transfer_amount)
            self.assertEqual(transfer_amount_transferred, transfer_amount_report)
        elif count == 1:
            self.assertRegex(transferNo, "(.+\w)")
        count += 1

def assertThirdPartyTitle(actualResult, expectResult):
    try:
        self.assertEqual(actualResult.lower(), expectResult.lower())
        return "Pass"
    except Exception as e:
        return f"Expect {expectResult} but {actualResult}"


def assertNotEqualData(actualResult, expectResult):
    try:
        self.assertNotEqual(actualResult, expectResult)
        return "Pass"
    except Exception as e:
        return f"Expect {expectResult} different from {actualResult}"


def assertEqualData(actualResult, expectResult):
    try:
        self.assertEqual(actualResult, expectResult)
        return "Pass"
    except Exception as e:
        return f"Expect {expectResult} but {actualResult}"


def assertFalseResult(results):

    if results.count("Pass") == len(results):
        pass
    else:
        self.assertFalse(results)


if __name__ == '__main__':
    pass
