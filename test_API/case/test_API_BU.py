import unittest
from config.SetAPIConfig import Project
from config import RequestData
from test_API.common import Oauth
from test_API.common.BU import BU
from test_API.common.AdminTool import AdminTool
from utils.DataLoader import JsonLoader
from utils.DataExtractor import extract_json
from utils.Assertion import assertHTTPCode


class API_BU(unittest.TestCase):
    AdminTool = None

    @classmethod
    def setUpClass(cls):
        test_account = JsonLoader('TMP').get_tmp_data('API', 'account')
        test_password = JsonLoader('TMP').get_tmp_data('API', 'password')
        accessToken = Oauth.get_access_token(test_account, test_password)
        cls.BU = BU(accessToken)
        cls.AdminTool = AdminTool()
        # 建立餘額為0的新帳號供ErrorCode驗證用
        test_account_new = {'sta': "mb" + RequestData.test_date, 'vt': "ag" + RequestData.test_date}
        if Project == 'sta':
            cls.AdminTool.api_Member_Create()
        elif Project == 'vt':
            cls.AdminTool.api_Affiliate_Create()
        new_account = test_account_new[Project]
        accessToken_new = Oauth.get_access_token(new_account, new_account)
        cls.BU_newAccount = BU(accessToken_new)

    def test_01_00_create_betOrder_Success(self):  # 測試資料清單可參照RequestData.py
        """投注API/ Betting/ 新增投注訂單 [POST] api/betting/bulk\""""
        res = self.BU.api_Betting_bulk()
        res_code = extract_json("code", res.text)
        res_msg = extract_json("message", res.text)
        res_issueNumber = extract_json("data.issueNumber", res.text)
        res_orderNumber = extract_json("data.orderLists[0].orderNumber", res.text)

        assertHTTPCode(res)
        self.assertEqual(["0000", ["Success."]], [res_code, res_msg])
        self.assertRegex(res_issueNumber, "(.+\w)")
        self.assertRegex(res_orderNumber, "^(\w{13})$")

    def test_01_01_create_betOrder_InvalidOrderFormat(self):
        """投注API/ Betting/ 新增投注訂單 [POST] api/betting/bulk ErrorCode驗證: 注單格式錯誤(4202)\""""
        # 投注內容: 泰國60秒/雙面/雙面-第一球~第五球/第一球, betContent不正確(配合VT999以雙面盤投注)
        test_data = [{"lotteryCode": 68, "type": "twoface", "betRuleId": 68190111, "betContent": "B", "multiple": 1,
                      "betUnitPrice": "2.00", "roomId": 1, "sortOrder": 1, "chipSettingId": 1}]

        res = self.BU.api_Betting_bulk(test_data)
        res_code = extract_json("code", res.text)
        res_msg = extract_json("message", res.text)

        assertHTTPCode(res)
        self.assertEqual(["4202", ["Bet content error."]], [res_code, res_msg])

    def test_01_02_create_betOrder_InvalidUserBalance(self):
        """投注API/ Betting/ 新增投注訂單 [POST] api/betting/bulk ErrorCode驗證: 用戶錢包餘額不足(4203)\""""
        res = self.BU_newAccount.api_Betting_bulk()
        res_code = extract_json("code", res.text)
        res_msg = extract_json("message", res.text)

        assertHTTPCode(res)
        self.assertEqual(["4203", ["Not enough money."]], [res_code, res_msg])

    def test_01_03_create_betOrder_OverBonusLimit(self):
        """投注API/ Betting/ 新增投注訂單 [POST] api/betting/bulk ErrorCode驗證: 超過限紅(4207)\""""
        # 投注內容: 泰國60秒/雙面/雙面-第一球~第五球/第一球, betUnitPrice超過限紅(配合VT999以雙面盤投注)
        test_data = [{"lotteryCode": 68, "type": "twoface", "betRuleId": 68190111, "betContent": "b", "multiple": 1,
                      "betUnitPrice": "600000", "roomId": 1, "sortOrder": 1, "chipSettingId": 1}]

        res = self.BU.api_Betting_bulk(test_data)
        res_code = extract_json("code", res.text)
        res_msg = extract_json("message", res.text)

        assertHTTPCode(res)
        self.assertEqual(["4207", ["Over bonus limit."]], [res_code, res_msg])

    def test_01_04_create_betOrder_LotteryNotBegin(self):
        """投注API/ Betting/ 新增投注訂單 [POST] api/betting/bulk ErrorCode驗證: 彩種尚未開盤(4213)\""""
        # 投注內容: 江西11選5/雙面/雙面-第一球~第五球/第一球(配合VT999以雙面盤投注)
        test_data = [{"lotteryCode": 22, "type": "twoface", "betRuleId": 22200101, "betContent": "b", "multiple": 1,
                      "betUnitPrice": "2.00", "roomId": 1, "sortOrder": 1, "chipSettingId": 1}]

        res = self.BU.api_Betting_bulk(test_data)
        res_code = extract_json("code", res.text)
        res_msg = extract_json("message", res.text)

        assertHTTPCode(res)
        self.assertEqual(["4213", ["This Lottery is not Beginning."]], [res_code, res_msg])

    def test_01_05_create_betOrder_InvalidDataFormat(self):
        """投注API/ Betting/ 新增投注訂單 [POST] api/betting/bulk ErrorCode驗證: 資料錯誤(原4290, 現包含在1003)\""""
        # 投注內容: 泰國60秒/官方/常規-五星玩法/五星直選, 資料錯誤(lotteryCode為空)
        test_data = [{"lotteryCode": None, "type": "normalgame", "betRuleId": 68010101, "betContent": "0,1,2,3,02468",
                      "multiple": 1, "betUnitPrice": 2, "roomId": 1, "sortOrder": 1, "chipSettingId": 1}]

        res = self.BU.api_Betting_bulk(test_data)
        res_code = extract_json("code", res.text)
        res_msg = extract_json("message", res.text)

        assertHTTPCode(res)
        self.assertEqual(["1003", ["Model is invalid."]], [res_code, res_msg])

    def test_01_06_create_betOrder_InvalidIssueNumber(self):
        """投注API/ Betting/ 新增投注訂單 [POST] api/betting/bulk ErrorCode驗證: 期號不合法(4298)\""""
        # 投注內容: 泰國60秒/雙面/雙面-第一球~第五球/第一球, issueNumber不合法(配合VT999以雙面盤投注)
        test_data = [{"lotteryCode": 68, "type": "twoface", "issueNumber": "20210518-0632", "betRuleId": 68190111,
                      "betContent": "b", "multiple": 1, "betUnitPrice": "2.00", "roomId": 1, "sortOrder": 1,
                      "chipSettingId": 1}]

        res = self.BU.api_Betting_bulk(test_data)
        res_code = extract_json("code", res.text)
        res_msg = extract_json("message", res.text)

        assertHTTPCode(res)
        self.assertEqual(["4298", ["Issue number invalid."]], [res_code, res_msg])

    @unittest.skipIf(Project == 'vt', '越南站不支援刮刮彩')
    def test_02_00_create_betOrderScratch_Success(self):  # 測試資料清單可參照RequestData.py
        """投注API/ Betting/ 新增投注訂單並立即開獎 [POST] api/betting/instant\""""
        res = self.BU.api_Betting_instant()
        res_code = extract_json("code", res.text)
        res_msg = extract_json("message", res.text)
        res_issueNumber = extract_json("data.betOrders[0].issueNumber", res.text)
        res_orderNumber = extract_json("data.betOrders[0].betOrderNumber", res.text)

        assertHTTPCode(res)
        self.assertEqual(["0000", ["Success."]], [res_code, res_msg])
        self.assertRegex(res_issueNumber, "^(\w{12})$")
        self.assertRegex(res_orderNumber, "^(\w{13})$")

    @unittest.skipIf(Project == 'vt', '越南站不支援刮刮彩')
    def test_02_01_create_betOrderScratch_InvalidOrderFormat(self):
        """投注API/ Betting/ 新增投注訂單並立即開獎 [POST] api/betting/instant ErrorCode驗證: 注單格式錯誤(4202)\""""
        # 投注內容: 刮刮彩/官方/常規-五星玩法/五星直選, betContent不正確
        test_data = [{"lotteryCode": 11, "betRuleId": 11010101, "betContent": "0,1,2,3,", "multiple": 1,
                      "betUnitPrice": 2, "roomId": 1, "sortOrder": 1, "chipSettingId": 1}]

        res = self.BU.api_Betting_instant(test_data)
        res_code = extract_json("code", res.text)
        res_msg = extract_json("message", res.text)

        assertHTTPCode(res)
        self.assertEqual(["4202", ["Bet content error."]], [res_code, res_msg])

    @unittest.skipIf(Project == 'vt', '越南站不支援刮刮彩')
    def test_02_02_create_betOrderScratch_InvalidUserBalance(self):
        """投注API/ Betting/ 新增投注訂單並立即開獎 [POST] api/betting/instant ErrorCode驗證: 用戶錢包餘額不足(4203)\""""
        res = self.BU_newAccount.api_Betting_instant()
        res_code = extract_json("code", res.text)
        res_msg = extract_json("message", res.text)

        assertHTTPCode(res)
        self.assertEqual(["4203", ["Not enough money."]], [res_code, res_msg])

    @unittest.skipIf(Project == 'vt', '越南站不支援刮刮彩')
    def test_02_03_create_betOrderScratch_InvalidDataFormat(self):
        """投注API/ Betting/ 新增投注訂單並立即開獎 [POST] api/betting/instant ErrorCode驗證: 資料錯誤(原4290, 現包含在1003)\""""
        # 投注內容: 泰國60秒/官方/常規-五星玩法/五星直選, 資料錯誤(lotteryCode為空)
        test_data = [{"lotteryCode": None, "betRuleId": 11010101, "betContent": "0,1,2,3,02468", "multiple": 1,
                      "betUnitPrice": 2, "roomId": 1, "sortOrder": 1, "chipSettingId": 1}]

        res = self.BU.api_Betting_instant(test_data)
        res_code = extract_json("code", res.text)
        res_msg = extract_json("message", res.text)

        assertHTTPCode(res)
        self.assertEqual(["1003", ["Model is invalid."]], [res_code, res_msg])

    @unittest.skipIf(Project == 'vt', '越南站無追號功能')
    def test_03_00_create_betTraceOrder_Success(self):  # 測試資料清單可參照RequestData.py
        """投注API/ Planning/ 新增追號訂單 [POST] api/planning/create\""""
        res = self.BU.api_Planning_create()
        res_code = extract_json("code", res.text)
        res_msg = extract_json("message", res.text)
        res_beginIssueNumber = extract_json("data.traceResult.beginIssueNumber", res.text)
        res_traceOrderNumber = extract_json("data.traceResult.traceOrderNumber", res.text)

        assertHTTPCode(res)
        self.assertEqual(["0000", ["Success."]], [res_code, res_msg])
        self.assertRegex(res_beginIssueNumber, "(.+\w)")
        self.assertRegex(res_traceOrderNumber, "^(\w{13})$")

    @unittest.skipIf(Project == 'vt', '越南站無追號功能')
    def test_03_01_create_betTraceOrder_InvalidOrderFormat(self):
        """投注API/ Planning/ 新增追號訂單 [POST] api/planning/create ErrorCode驗證: 注單格式錯誤(4202)\""""
        # 投注內容: 泰國60秒/官方/常規-五星玩法/五星直選, betContent不正確
        test_data = {"betRuleId": 68010101, "lotteryCode": 68, "betContent": "0,1,2,3,", "isStopAfterWin": True,
                     "betUnitPrice": 2, "chipSettingId": 1, "roomId": 1,
                     "container": [{"sortOrder": 1, "multiple": 1}, {"sortOrder": 2, "multiple": 2}]}

        res = self.BU.api_Planning_create(test_data)
        res_code = extract_json("code", res.text)
        res_msg = extract_json("message", res.text)

        assertHTTPCode(res)
        self.assertEqual(["4202", ["Bet content error."]], [res_code, res_msg])

    @unittest.skipIf(Project == 'vt', '越南站無追號功能')
    def test_03_02_create_betTraceOrder_InvalidUserBalance(self):
        """投注API/ Planning/ 新增追號訂單 [POST] api/planning/create ErrorCode驗證: 用戶錢包餘額不足(4203)\""""
        res = self.BU_newAccount.api_Planning_create()
        res_code = extract_json("code", res.text)
        res_msg = extract_json("message", res.text)

        assertHTTPCode(res)
        self.assertEqual(["4203", ["Not enough money."]], [res_code, res_msg])

    @unittest.skipIf(Project == 'vt', '越南站無追號功能')
    def test_03_03_create_betTraceOrder_OverBonusLimit(self):
        """投注API/ Planning/ 新增追號訂單 [POST] api/planning/create ErrorCode驗證: 超過限紅(4207)\""""
        # 投注內容: 泰國60秒/官方/常規-五星玩法/五星直選, multiple超過限紅
        test_data = {"betRuleId": 68010101, "lotteryCode": 68, "betContent": "0,1,2,3,4", "isStopAfterWin": True,
                     "betUnitPrice": 10000, "chipSettingId": 1, "roomId": 1, "container":
                         [{"sortOrder": 1, "multiple": 10}, {"sortOrder": 2, "multiple": 100}]}

        res = self.BU.api_Planning_create(test_data)
        res_code = extract_json("code", res.text)
        res_msg = extract_json("message", res.text)

        assertHTTPCode(res)
        self.assertEqual(["4207", ["Over bonus limit."]], [res_code, res_msg])

    @unittest.skipIf(Project == 'vt', '越南站無追號功能')
    def test_03_04_create_betTraceOrder_LotteryNotBegin(self):
        """投注API/ Planning/ 新增追號訂單 [POST] api/planning/create ErrorCode驗證: 彩種尚未開盤(4213)\""""
        # 投注內容: 台灣11選5/官方/常規-任二/標準
        test_data = {"betRuleId": 22010101, "lotteryCode": 22, "betContent": "01 02", "isStopAfterWin": True,
                     "betUnitPrice": 2, "chipSettingId": 1, "roomId": 1,
                     "container": [{"sortOrder": 1, "multiple": 1}, {"sortOrder": 2, "multiple": 2}]}

        res = self.BU.api_Planning_create(test_data)
        res_code = extract_json("code", res.text)
        res_msg = extract_json("message", res.text)

        assertHTTPCode(res)
        self.assertEqual(["4213", ["This Lottery is not Beginning."]], [res_code, res_msg])


if __name__ == '__main__':
    unittest.main()
