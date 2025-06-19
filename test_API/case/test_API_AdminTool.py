import unittest
import datetime
import random
from random import choice
from test_API.common import Oauth
from test_API.common.BU import BU
from test_API.common.AdminTool import AdminTool, download_excel_file, redraw_BonusNumber
from utils.DataLoader import JsonLoader
from utils.DataExtractor import extract_json, extract_text, extract_excel
from utils.Assertion import assertHTTPCode


class API_AdminTool(unittest.TestCase):
    AdminTool = None
    LotteryNameMappingTable = None

    @classmethod
    def setUpClass(cls):
        test_account = JsonLoader('TMP').get_tmp_data('API', 'account')
        test_password = JsonLoader('TMP').get_tmp_data('API', 'password')
        accessToken = Oauth.get_access_token(test_account, test_password)
        cls.BU = BU(accessToken)
        cls.AdminTool = AdminTool()
        cls.LotteryNameMappingTable = cls.AdminTool.get_GameNameMappingTable("Lottery")
        cls.LotteryCodeList = list(cls.LotteryNameMappingTable.keys())

    def test_01_00_get_LotteryBetLog_Success(self):
        """遊戲紀錄/ 彩票投注紀錄/ 查詢 [POST] api/Bets/Search\""""
        # 建立新的投注單供Query驗證用
        betting_data = self.BU.api_Betting_bulk()
        betting_orderNumber = extract_json("data.orderLists[0].orderNumber", betting_data.text)

        res = self.AdminTool.api_Bets_Search()
        res_status = extract_json("Status", res.text)
        res_code = extract_json("ErrorCode", res.text)
        res_BetOrderNo = extract_json("Data.List[0].BetOrderNo", res.text)

        assertHTTPCode(res)
        self.assertEqual([True, "", betting_orderNumber], [res_status, res_code, res_BetOrderNo])

    def test_01_01_get_LotteryBetLog_StartTimeOutOfRange(self):
        """遊戲紀錄/ 彩票投注紀錄/ 查詢 [POST] api/Bets/Search ErrorCode驗證: AdminTool-StarttimeOutOfRange\""""
        res = self.AdminTool.api_Bets_Search(start_delta=-61)  # 彩票投注紀錄/彩票投注記錄歷史的分水嶺為60天
        res_status = extract_json("Status", res.text)
        res_code = extract_json("ErrorCode", res.text)

        assertHTTPCode(res)
        self.assertEqual([False, "AdminTool-StarttimeOutOfRange"], [res_status, res_code])

    def test_02_get_LotteryBetDetail_Success(self):
        """遊戲紀錄/ 彩票投注紀錄/ 投注詳情 [GET] api/Bets/{betOrderNumber}\""""
        # 建立新的投注單供Query驗證用
        betting_data = self.BU.api_Betting_bulk()
        betting_orderNumber = extract_json("data.orderLists[0].orderNumber", betting_data.text)

        res = self.AdminTool.api_Bets_Bets(betting_orderNumber)
        res_status = extract_json("Status", res.text)
        res_code = extract_json("ErrorCode", res.text)
        res_BetOrderNo = extract_json("Data.BetOrderNo", res.text)

        assertHTTPCode(res)
        self.assertEqual([True, "", betting_orderNumber], [res_status, res_code, res_BetOrderNo])

    def test_03_export_LotteryBetLog_Success(self):
        """遊戲紀錄/ 彩票投注紀錄/ 導出報表 [POST] api/Bets/Export\""""
        ContentType = {'xlsx': "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"}
        # 建立新的投注單供匯出報表驗證用
        betting_data = self.BU.api_Betting_bulk()
        betting_orderNumber = extract_json("data.orderLists[0].orderNumber", betting_data.text)

        res = self.AdminTool.api_Bets_Export()
        res_contentType = res.headers['Content-Type']
        # 下載並讀取報表資訊
        download_file = download_excel_file(res)
        file_extension = extract_text("(\D+)$", download_file)
        latest_orderNumber = extract_excel(0, 0, download_file, skip_rows=3)

        assertHTTPCode(res)
        self.assertEqual([ContentType['xlsx'], ".xlsx", betting_orderNumber],
                         [res_contentType, file_extension, latest_orderNumber])

    def test_04_cancel_betOrder_Success(self):  # 1(已成立)/2(已結算)/3(已撤單)
        """遊戲紀錄/ 彩票投注紀錄/ 撤單 [PATCH] api/Bets/Cancel\""""
        # 建立新的投注單供撤單驗證用
        betting_data = self.BU.api_Betting_bulk()
        betting_orderNumber = extract_json("data.orderLists[0].orderNumber", betting_data.text)

        res = self.AdminTool.api_Bets_Cancel(betting_orderNumber)
        res_status = extract_json("Status", res.text)
        res_code = extract_json("ErrorCode", res.text)
        # 獲取撤單後狀態
        order_data = self.AdminTool.api_Bets_Bets(betting_orderNumber)
        res_orderStatus = extract_json("Data.Status", order_data.text)

        assertHTTPCode(res)
        self.assertEqual([True, "", 3], [res_status, res_code, res_orderStatus])

    def test_05_get_LotteryBetHistory_Success(self):
        """遊戲紀錄/ 彩票投注紀錄歷史/ 查詢 [POST] api/Bets/Search/History\""""
        res = self.AdminTool.api_Bets_History()
        res_status = extract_json("Status", res.text)
        res_code = extract_json("ErrorCode", res.text)
        res_TotalOrderNumber = extract_json("Data.Summary.TotalOrderNumber", res.text)

        assertHTTPCode(res)
        self.assertEqual([True, ""], [res_status, res_code])
        self.assertGreater(res_TotalOrderNumber, 0)

    def test_06_get_LotterySetting_Success(self):  # 根據Req 8794, 一般設定—僅供顯示彩種 & 限紅金額，更新時間、人員欄位暫不實作
        """遊戲管理/ 彩票管理/ 基本設置/ 查詢 [POST] api/lottery/search\""""
        test_lotteryCode = choice(self.LotteryCodeList)

        res = self.AdminTool.api_Lottery_Search(test_lotteryCode)
        res_status = extract_json("Status", res.text)
        res_code = extract_json("ErrorCode", res.text)
        res_LotteryName = extract_json("Data.Data[0].LotteryName", res.text)

        assertHTTPCode(res)
        self.assertEqual([True, "", self.LotteryNameMappingTable[test_lotteryCode]],
                         [res_status, res_code, res_LotteryName])

    def test_07_get_LotteryStatus_Success(self):
        """遊戲管理/ 彩票管理/ 彩種開關/ 查詢 [POST] api/Lottery/Switch?platform={platform}\""""
        test_platform = "Web"  # 1(iOS)/2(Android)/3(Web)/4(H5), 固定為Web, 避免選到mobile不支援彩種
        test_lotteryCode = 68  # 固定為泰國60秒, 避免選到已不支援彩種

        res = self.AdminTool.api_Lottery_Switch_POST(test_platform, test_lotteryCode)
        res_status = extract_json("Status", res.text)
        res_code = extract_json("ErrorCode", res.text)
        res_LotteryName = extract_json("Data.LotteryType[0].LotteryName", res.text)

        assertHTTPCode(res)
        self.assertEqual([True, "", self.LotteryNameMappingTable[test_lotteryCode]],
                         [res_status, res_code, res_LotteryName])

    def test_08_switch_LotteryStatus_Success(self):
        """遊戲管理/ 彩票管理/ 彩種開關/ 開關 [PATCH] api/Lottery/Switch\""""
        expectedModifyTime = datetime.datetime.today().strftime("%Y-%m-%d")
        test_platform = "Web"  # 1(iOS)/2(Android)/3(Web)/4(H5), 固定為Web, 避免選到mobile不支援彩種
        test_lotteryCode = 68  # 固定為泰國60秒, 避免選到已不支援彩種
        # 獲取五層開關的第一筆資料
        test_data = self.AdminTool.api_Lottery_Switch_POST(test_platform, test_lotteryCode)
        test_LotteryName = extract_json("Data.LotteryType[0].LotteryName", test_data.text)
        ori_LotteryStatus = extract_json("Data.LotteryType[0].LotteryStatus", test_data.text)
        test_BetPageNameId = extract_json("Data.BetPageName[0].BetPageNameId", test_data.text)
        test_BetPageNameText = extract_json("Data.BetPageName[0].BetPageNameText", test_data.text)
        ori_BetPageNameStatus = extract_json("Data.BetPageName[0].BetPageNameStatus", test_data.text)
        test_BetTypeId = extract_json("Data.BetType[0].BetTypeId", test_data.text)
        test_BetTypeName = extract_json("Data.BetType[0].BetTypeName", test_data.text)
        ori_BetTypeStatus = extract_json("Data.BetType[0].BetTypeStatus", test_data.text)
        test_BetSubTypeId = extract_json("Data.BetSubType[0].BetSubTypeId", test_data.text)
        test_BetSubTypeName = extract_json("Data.BetSubType[0].BetSubTypeName", test_data.text)
        ori_BetSubTypeStatus = extract_json("Data.BetSubType[0].BetSubTypeStatus", test_data.text)
        test_BetRuleId = extract_json("Data.BetRule[0].BetRuleId", test_data.text)
        test_BetRuleName = extract_json("Data.BetRule[0].BetRuleName", test_data.text)
        ori_BetRuleStatus = extract_json("Data.BetRule[0].BetRuleStatus", test_data.text)
        print("LotteryCode", test_lotteryCode, "LotteryName", test_LotteryName,
              "LotteryStatus", ori_LotteryStatus, "\n")
        print("BetPageNameId", test_BetPageNameId, "BetPageNameText", test_BetPageNameText,
              "BetPageNameStatus", ori_BetPageNameStatus, "\n")
        print("BetTypeId", test_BetTypeId, "BetTypeName", test_BetTypeName,
              "BetTypeStatus", ori_BetTypeStatus, "\n")
        print("BetSubTypeId", test_BetSubTypeId, "BetSubTypeName", test_BetSubTypeName,
              "res_BetSubTypeStatus", ori_BetSubTypeStatus, "\n")
        print("BetRuleId", test_BetRuleId, "BetRuleName", test_BetRuleName,
              "BetRuleStatus", ori_BetRuleStatus, "\n")
        # 根據原本狀態轉換預計開關狀態
        ori_status = [ori_LotteryStatus, ori_BetPageNameStatus, ori_BetTypeStatus, ori_BetSubTypeStatus,
                      ori_BetRuleStatus]
        test_status = [2 if value == 1 else 1 for value in ori_status]
        print("ori_status", ori_status, "test_status", test_status)

        # 切換開關狀態
        res = self.AdminTool.api_Lottery_Switch_PATCH(test_platform,
                                                      LotteryType={test_lotteryCode: test_status[0]},
                                                      BetPageName={
                                                          test_lotteryCode: {test_BetPageNameId: test_status[1]}},
                                                      BetType={test_BetTypeId: test_status[2]},
                                                      BetSubType={test_BetSubTypeId: test_status[3]},
                                                      BetRule={test_BetRuleId: test_status[4]})
        res_status = extract_json("Status", res.text)
        res_code = extract_json("ErrorCode", res.text)
        # 切換回原本狀態
        self.AdminTool.api_Lottery_Switch_PATCH(test_platform,
                                                LotteryType={test_lotteryCode: ori_status[0]},
                                                BetPageName={test_lotteryCode: {test_BetPageNameId: ori_status[1]}},
                                                BetType={test_BetTypeId: ori_status[2]},
                                                BetSubType={test_BetSubTypeId: ori_status[3]},
                                                BetRule={test_BetRuleId: ori_status[4]})
        # 獲取修改日期
        res2 = self.AdminTool.api_Lottery_Switch_POST(test_platform, test_lotteryCode)
        res2_ModifyTime1 = extract_json("Data.LotteryType[0].ModifyTime", res2.text)
        res2_ModifyTime2 = extract_json("Data.BetPageName[0].ModifyTime", res2.text)
        res2_ModifyTime3 = extract_json("Data.BetType[0].ModifyTime", res2.text)
        res2_ModifyTime4 = extract_json("Data.BetSubType[0].ModifyTime", res2.text)
        res2_ModifyTime5 = extract_json("Data.BetRule[-1].ModifyTime", res2.text)  # 此欄位在變更後會跳至最後一筆

        assertHTTPCode(res)
        self.assertEqual([True, ""], [res_status, res_code])
        self.assertRegex(res2_ModifyTime1, expectedModifyTime)
        self.assertRegex(res2_ModifyTime2, expectedModifyTime)
        self.assertRegex(res2_ModifyTime3, expectedModifyTime)
        self.assertRegex(res2_ModifyTime4, expectedModifyTime)
        self.assertRegex(res2_ModifyTime5, expectedModifyTime)

    def test_09_get_IssueNumber_Success(self):
        """遊戲管理/ 期數管理/ 查詢 [POST] api/IssueNumber/Search\""""
        test_lotteryCode = 68  # 固定為泰國60秒, 避免選到已停產期號彩種

        res = self.AdminTool.api_IssueNumber_Search(LotteryCode=test_lotteryCode)
        res_status = extract_json("Status", res.text)
        res_code = extract_json("ErrorCode", res.text)
        res_LotteryName = extract_json("Data.Data[0].LotteryName", res.text)

        assertHTTPCode(res)
        self.assertEqual([True, "", self.LotteryNameMappingTable[test_lotteryCode]],
                         [res_status, res_code, res_LotteryName])

    def test_10_00_update_IssueNumberTime_Success(self):
        """遊戲管理/ 期數管理/ 管理/ 編輯 [PUT] api/IssueNumber/{LotteryHistoryId}\""""
        expected_AnnounceTime = (datetime.datetime.today() + datetime.timedelta(days=+1)).strftime("%Y-%m-%d")
        expected_StartTime = (datetime.datetime.today() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
        # 測試期號狀態須為"1(未開盤)"
        test_data = self.AdminTool.get_IssueNumberInfo(Status=1)
        LotteryHistoryId = test_data[0]
        IssueNumber = test_data[3]

        res = self.AdminTool.api_IssueNumber_IssueNumber(LotteryHistoryId, IssueNumber)
        res_status = extract_json("Status", res.text)
        res_code = extract_json("ErrorCode", res.text)
        # 獲取修改後的開獎時間/開盤時間
        res2 = self.AdminTool.get_IssueNumberInfo(start_delta=-1, end_delta=+1, SortColumn="ModifyDate",
                                                  IssueNumber=IssueNumber)
        res2_AnnounceTime = res2[5]
        res2_StartTime = res2[6]

        assertHTTPCode(res)
        self.assertEqual([True, ""], [res_status, res_code])
        self.assertRegex(res2_AnnounceTime, expected_AnnounceTime)
        self.assertRegex(res2_StartTime, expected_StartTime)

    def test_10_01_update_IssueNumberTime_ProcessIsRunning(self):
        """遊戲管理/ 期數管理/ 管理/ 編輯 [PUT] api/IssueNumber/{LotteryHistoryId} ErrorCode驗證: AdminTool-ProcessIsRunning\""""
        # 測試期號狀態須為"1(未開盤)"
        test_data = self.AdminTool.get_IssueNumberInfo(Status=1)
        LotteryHistoryId = test_data[0]
        IssueNumber = test_data[3]

        res = self.AdminTool.api_IssueNumber_IssueNumber(LotteryHistoryId, IssueNumber)
        res_status = extract_json("Status", res.text)
        res_code = extract_json("ErrorCode", res.text)

        assertHTTPCode(res)
        self.assertEqual([False, "AdminTool-ProcessIsRunning"], [res_status, res_code])

    def test_11_00_cancel_IssueNumber_Success(self):  # 根據Req 15159, 台灣/澳洲系列獎源尚未有重開/取消機制, 如跳錯請先確認是否為此兩彩種
        """遊戲管理/ 期數管理/ 管理/ 取消當期 [PATCH] api/IssueNumber/{LotteryHistoryId}/Cancel\""""
        # 測試期號狀態須為"4(已結算)"
        test_data = self.AdminTool.get_IssueNumberInfo(Status=4)
        LotteryHistoryId = test_data[0]
        IssueNumber = test_data[3]

        res = self.AdminTool.api_IssueNumber_Cancel(LotteryHistoryId)
        res_status = extract_json("Status", res.text)
        res_code = extract_json("ErrorCode", res.text)
        # 獲取該筆"6(已取消)"期號所對應的LotteryHistoryId
        res2 = self.AdminTool.get_IssueNumberInfo(Status=6, IssueNumber=IssueNumber)
        res2_LotteryHistoryId = res2[0]

        assertHTTPCode(res)
        self.assertEqual([True, "", LotteryHistoryId], [res_status, res_code, res2_LotteryHistoryId])

    def test_11_01_cancel_IssueNumber_LotteryHistoryNotFound(self):
        """遊戲管理/ 期數管理/ 管理/ 取消當期 [PATCH] api/IssueNumber/{LotteryHistoryId}/Cancel ErrorCode驗證: AdminTool-LotteryHistoryNotFound\""""
        test_LotteryHistoryId = 12345678

        res = self.AdminTool.api_IssueNumber_Cancel(test_LotteryHistoryId)
        res_status = extract_json("Status", res.text)
        res_code = extract_json("ErrorCode", res.text)

        assertHTTPCode(res)
        self.assertEqual([False, "AdminTool-LotteryHistoryNotFound"], [res_status, res_code])

    def test_11_02_cancel_IssueNumber_LotteryHistoryAlreadyCanceled(self):
        """遊戲管理/ 期數管理/ 管理/ 取消當期 [PATCH] api/IssueNumber/{LotteryHistoryId}/Cancel ErrorCode驗證: AdminTool-LotteryHistoryAlreadyCanceled\""""
        # 測試期號狀態須為"4(已結算)"
        test_data = self.AdminTool.get_IssueNumberInfo(Status=4)
        LotteryHistoryId = test_data[0]

        # 取消當期
        self.AdminTool.api_IssueNumber_Cancel(LotteryHistoryId)
        # 再次取消相同期號
        res = self.AdminTool.api_IssueNumber_Cancel(LotteryHistoryId)
        res_status = extract_json("Status", res.text)
        res_code = extract_json("ErrorCode", res.text)

        assertHTTPCode(res)
        self.assertEqual([False, "AdminTool-LotteryHistoryAlreadyCanceled"], [res_status, res_code])

    def test_12_00_redraw_BonusNumberTrial_Success(self):
        """遊戲管理/ 期數管理/ 管理/ 重新開獎/ 試算 [POST] api/IssueNumber/{LotteryHistoryId}/TrailCalculationBonus\""""
        # 測試期號狀態須為"4(已結算)"
        test_data = self.AdminTool.get_IssueNumberInfo(SortColumn="TotalBet", Status=4)  # BonusTotalBet目前有排序問題, 已回報
        LotteryHistoryId = test_data[0]
        BonusNumber = test_data[4]
        TotalBet = test_data[7]
        BonusNumber_Update = redraw_BonusNumber(BonusNumber)

        # 獲取修改後的總投注數(中獎注數/中獎獎金因不可控, 故暫不列入驗證)
        res = self.AdminTool.api_IssueNumber_TrailCalculationBonus(LotteryHistoryId, BonusNumber_Update)
        res_status = extract_json("Status", res.text)
        res_code = extract_json("ErrorCode", res.text)
        res_TotalBet = extract_json("Data.TotalBet", res.text)

        assertHTTPCode(res)
        self.assertEqual([True, "", TotalBet], [res_status, res_code, res_TotalBet])

    def test_12_01_redraw_BonusNumberTrial_BonusNumberRegexNotMatch(self):
        """遊戲管理/ 期數管理/ 管理/ 重新開獎/ 試算 [POST] api/IssueNumber/{LotteryHistoryId}/TrailCalculationBonus ErrorCode驗證: AdminTool-BonusNumberRegexNotMatch\""""
        # 測試期號狀態須為"4(已結算)"
        test_data = self.AdminTool.get_IssueNumberInfo(SortColumn="TotalBet", Status=4)  # BonusTotalBet目前有排序問題, 已回報
        LotteryHistoryId = test_data[0]
        test_BonusNumber = 12345678

        res = self.AdminTool.api_IssueNumber_TrailCalculationBonus(LotteryHistoryId, test_BonusNumber)
        res_status = extract_json("Status", res.text)
        res_code = extract_json("ErrorCode", res.text)

        assertHTTPCode(res)
        self.assertEqual([False, "AdminTool-BonusNumberRegexNotMatch"], [res_status, res_code])

    def test_13_00_redraw_BonusNumberSettle_Success(self):  # 根據Req 15159, 台灣/澳洲系列獎源尚未有重開/取消機制, 如跳錯請先確認是否為此兩彩種
        """遊戲管理/ 期數管理/ 管理/ 重新開獎 [PATCH] api/IssueNumber/{LotteryHistoryId}/Settle\""""
        # 測試期號狀態須為"4(已結算)"
        test_data = self.AdminTool.get_IssueNumberInfo(Status=4)
        LotteryHistoryId = test_data[0]
        IssueNumber = test_data[3]
        BonusNumber = test_data[4]
        BonusNumber_Update = redraw_BonusNumber(BonusNumber)

        res = self.AdminTool.api_IssueNumber_Settle(LotteryHistoryId, BonusNumber_Update)
        res_status = extract_json("Status", res.text)
        res_code = extract_json("ErrorCode", res.text)
        # 獲取該筆重新開獎期號所對應的BonusNumber
        res2 = self.AdminTool.get_IssueNumberInfo(SortColumn="ModifyDate", Status=4, IssueNumber=IssueNumber)
        res2_BonusNumber = res2[4]

        assertHTTPCode(res)
        self.assertEqual([True, "", BonusNumber_Update], [res_status, res_code, res2_BonusNumber])

    def test_13_01_redraw_BonusNumberSettle_ProcessIsRunning(self):
        """遊戲管理/ 期數管理/ 管理/ 重新開獎 [PATCH] api/IssueNumber/{LotteryHistoryId}/Settle ErrorCode驗證: AdminTool-ProcessIsRunning\""""
        # 測試期號狀態須為"4(已結算)"
        test_data = self.AdminTool.get_IssueNumberInfo(Status=4)
        LotteryHistoryId = test_data[0]
        BonusNumber = test_data[4]
        BonusNumber_Update = redraw_BonusNumber(BonusNumber)

        res = self.AdminTool.api_IssueNumber_Settle(LotteryHistoryId, BonusNumber_Update)
        res_status = extract_json("Status", res.text)
        res_code = extract_json("ErrorCode", res.text)

        assertHTTPCode(res)
        self.assertEqual([False, "AdminTool-ProcessIsRunning"], [res_status, res_code])

    def test_14_get_BetSection_Success(self):
        """遊戲管理/ 賠率設定/ 玩法賠率模式設定/ 查詢 [POST] api/BetSection/Search\""""
        test_lotteryCode = choice(self.LotteryCodeList)

        res = self.AdminTool.api_BetSection_Search(test_lotteryCode)
        res_status = extract_json("Status", res.text)
        res_code = extract_json("ErrorCode", res.text)
        res_LotteryName = extract_json("Data.Data[0].LotteryName", res.text)

        assertHTTPCode(res)
        self.assertEqual([True, "", self.LotteryNameMappingTable[test_lotteryCode]],
                         [res_status, res_code, res_LotteryName])

    def test_15_update_BetSection_Success(self):
        """遊戲管理/ 賠率設定/ 玩法賠率模式設定/ 管理/ 編輯 [PUT] api/BetSection/{BetTypeId}\""""
        test_lotteryCode = choice(self.LotteryCodeList)
        test_data = self.AdminTool.get_BetSectionInfo(test_lotteryCode)
        test_BetTypeId = test_data[0]
        ori_BetSectionId = test_data[1]
        # 根據原本模式轉換預計切換模式
        if ori_BetSectionId == 0:
            test_BetSectionId = 1  # 返點等級
        else:
            test_BetSectionId = 0  # 最大賠率

        res = self.AdminTool.api_BetSection_BetSection(test_BetTypeId, test_BetSectionId)
        res_status = extract_json("Status", res.text)
        res_code = extract_json("ErrorCode", res.text)
        # 獲取修改後的BetSectionId
        res_2 = self.AdminTool.get_BetSectionInfo(test_lotteryCode)
        res_2_BetTypeId = res_2[0]
        res_2_BetSectionId = res_2[1]

        assertHTTPCode(res)
        self.assertEqual([True, "", test_BetTypeId, test_BetSectionId],
                         [res_status, res_code, res_2_BetTypeId, res_2_BetSectionId])

    def test_16_get_BetRule_Success(self):
        """遊戲管理/ 賠率設定/ 投注項賠率設定/ 查詢 [POST] api/BetRule/Search\""""
        test_lotteryCode = choice(self.LotteryCodeList)

        res = self.AdminTool.api_BetRule_Search(test_lotteryCode)
        res_status = extract_json("Status", res.text)
        res_code = extract_json("ErrorCode", res.text)
        res_LotteryName = extract_json("Data.Data[0].LotteryName", res.text)

        assertHTTPCode(res)
        self.assertEqual([True, "", self.LotteryNameMappingTable[test_lotteryCode]],
                         [res_status, res_code, res_LotteryName])

    def test_17_update_BetRule_Success(self):
        """遊戲管理/ 賠率設定/ 投注項賠率設定/ 管理/ 編輯 [PUT] api/BetRule/{BetRuleId}\""""
        test_lotteryCode = choice(self.LotteryCodeList)
        test_data = self.AdminTool.get_BetRuleInfo(test_lotteryCode)
        test_BetRuleId = test_data[0]
        test_Modulus = round(random.uniform(0, 10), 2)  # 機率, 暫定隨機選取0~10之間的2位小數
        test_MaxBonusMode = round(random.uniform(0, 10), 2)  # 最大賠率, 暫定隨機選取0~10之間的2位小數

        res = self.AdminTool.api_BetRule_BetRule(test_BetRuleId, test_Modulus, test_MaxBonusMode)
        res_status = extract_json("Status", res.text)
        res_code = extract_json("ErrorCode", res.text)
        # 獲取修改後的Modulus/MaxBonusMode
        res_2 = self.AdminTool.get_BetRuleInfo(test_lotteryCode)
        res_2_BetRuleId = res_2[0]
        res_2_Modulus = res_2[1]
        res_2_MaxBonusMode = res_2[2]

        assertHTTPCode(res)
        self.assertEqual([True, "", test_BetRuleId, test_Modulus, test_MaxBonusMode],
                         [res_status, res_code, res_2_BetRuleId, res_2_Modulus, res_2_MaxBonusMode])


if __name__ == '__main__':
    unittest.main()
