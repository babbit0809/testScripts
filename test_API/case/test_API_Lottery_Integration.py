import unittest
from datetime import datetime, timezone
from config import RequestData
from test_API.common.Lottery_Integration import Lottery_Integration
from utils.Generator import random_str
from utils.DataExtractor import extract_json
from utils.Assertion import assertHTTPCode


class API_Lottery_Integration(unittest.TestCase):
    test_merchant = None

    @classmethod
    def setUpClass(cls):
        cls.test_merchant = "LOTTO"
        test_date = RequestData.test_date
        cls.test_account = cls.test_merchant + test_date
        cls.Lottery_Integration = Lottery_Integration()
        cls.MerchantID = {'LOTTO': "999", 'CLF88': "101", 'XH201': "102", 'VT999': "103"}
        cls.currencyCode = {'LOTTO': "CNY", 'CLF88': "CNY", 'XH201': "CNY", 'VT999': "VND"}

    def test_01_00_create_player_Success(self):
        """錢包通用：建立玩家帳號 ["POST","/create-player"]"""
        expected_playerId = self.MerchantID[self.test_merchant] + "\d{9}"
        expected_createTime = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M")

        res = self.Lottery_Integration.api_create_player(self.test_account, self.currencyCode[self.test_merchant])
        res_code = extract_json("code", res.text)
        res_msg = extract_json("message", res.text)
        res_playerId = extract_json("result.playerId", res.text)
        res_createdAt = extract_json("result.createdAt", res.text)
        res_traceId = extract_json("traceId", res.text)

        assertHTTPCode(res)
        self.assertEqual(["000000", "SUCCESS", int], [res_code, res_msg, type(res_playerId)])
        self.assertRegex(str(res_playerId), expected_playerId)
        self.assertIn(expected_createTime, res_createdAt)
        self.assertIsNotNone(res_traceId)

    def test_01_01_create_player_DUPLICATE_PLAYER_NAME(self):
        """錢包通用：建立玩家帳號 ["POST","/create-player"] ErrorCode驗證: DUPLICATE_PLAYER_NAME"""
        res = self.Lottery_Integration.api_create_player(self.test_account, self.currencyCode[self.test_merchant])
        res_code = extract_json("code", res.text)
        res_msg = extract_json("message", res.text)
        res_traceId = extract_json("traceId", res.text)

        assertHTTPCode(res, [400])
        self.assertEqual(["020001", "DUPLICATE_PLAYER_NAME"], [res_code, res_msg])
        self.assertIsNotNone(res_traceId)

    def test_01_02_create_player_API_INVALID_playerName(self):
        """錢包通用：建立玩家帳號 ["POST","/create-player"] ErrorCode驗證: API_INVALID_PARAMS(playerName)"""
        test_playerName = random_str()

        res = self.Lottery_Integration.api_create_player(test_playerName, self.currencyCode[self.test_merchant])
        res_code = extract_json("code", res.text)
        res_msg = extract_json("message", res.text)
        res_traceId = extract_json("traceId", res.text)

        assertHTTPCode(res, [400])
        self.assertEqual(["000001", "API_INVALID_PARAMS"], [res_code, res_msg])
        self.assertIsNotNone(res_traceId)

    def test_01_03_create_player_API_INVALID_currencyCode(self):
        """錢包通用：建立玩家帳號 ["POST","/create-player"] ErrorCode驗證: API_INVALID_PARAMS(currencyCode)"""
        test_currencyCode = random_str()

        res = self.Lottery_Integration.api_create_player(self.test_account, test_currencyCode)
        res_code = extract_json("code", res.text)
        res_msg = extract_json("message", res.text)
        res_traceId = extract_json("traceId", res.text)

        assertHTTPCode(res, [400])
        self.assertEqual(["000001", "API_INVALID_PARAMS"], [res_code, res_msg])
        self.assertIsNotNone(res_traceId)

    def test_01_04_create_player_MERCHANT_NOT_FOUND(self):
        """錢包通用：建立玩家帳號 ["POST","/create-player"] ErrorCode驗證: MERCHANT_NOT_FOUND"""
        test_merchant = "nonexistent"

        res = Lottery_Integration(merchant=test_merchant).api_create_player(self.test_account, self.currencyCode[self.test_merchant])
        res_code = extract_json("code", res.text)
        res_msg = extract_json("message", res.text)
        res_traceId = extract_json("traceId", res.text)

        assertHTTPCode(res, [403])
        self.assertEqual(["010001", "MERCHANT_NOT_FOUND"], [res_code, res_msg])
        self.assertIsNotNone(res_traceId)

    def test_01_05_create_player_MERCHANT_AUTH_FAILED(self):
        """錢包通用：建立玩家帳號 ["POST","/create-player"] ErrorCode驗證: MERCHANT_AUTH_FAILED"""
        test_secretKey = "error_secretKey"

        res = Lottery_Integration(secretKey=test_secretKey).api_create_player(self.test_account, self.currencyCode[self.test_merchant])
        res_code = extract_json("code", res.text)
        res_msg = extract_json("message", res.text)
        res_traceId = extract_json("traceId", res.text)

        assertHTTPCode(res, [403])
        self.assertEqual(["010002", "MERCHANT_AUTH_FAILED"], [res_code, res_msg])
        self.assertIsNotNone(res_traceId)

    def test_02_00_logout_player_Success(self):
        """錢包通用：登出玩家 ["POST","/logout-player"]"""
        res = self.Lottery_Integration.api_logout_player(self.test_account)
        res_code = extract_json("code", res.text)
        res_msg = extract_json("message", res.text)
        res_traceId = extract_json("traceId", res.text)

        assertHTTPCode(res)
        self.assertEqual(["000000", "SUCCESS"], [res_code, res_msg])
        self.assertIsNotNone(res_traceId)

    def test_02_01_logout_player_PLAYER_NOT_FOUND(self):
        """錢包通用：登出玩家 ["POST","/logout-player"] ErrorCode驗證: PLAYER_NOT_FOUND"""
        test_playerName = "nonexistent"

        res = self.Lottery_Integration.api_logout_player(test_playerName)
        res_code = extract_json("code", res.text)
        res_msg = extract_json("message", res.text)
        res_traceId = extract_json("traceId", res.text)

        assertHTTPCode(res, [404])
        self.assertEqual(["020002", "PLAYER_NOT_FOUND"], [res_code, res_msg])
        self.assertIsNotNone(res_traceId)

    def test_02_02_logout_player_MERCHANT_NOT_FOUND(self):
        """錢包通用：登出玩家 ["POST","/logout-player"] ErrorCode驗證: MERCHANT_NOT_FOUND"""
        test_merchant = "nonexistent"

        res = Lottery_Integration(merchant=test_merchant).api_logout_player(self.test_account)
        res_code = extract_json("code", res.text)
        res_msg = extract_json("message", res.text)
        res_traceId = extract_json("traceId", res.text)

        assertHTTPCode(res, [403])
        self.assertEqual(["010001", "MERCHANT_NOT_FOUND"], [res_code, res_msg])
        self.assertIsNotNone(res_traceId)

    def test_02_03_logout_player_MERCHANT_AUTH_FAILED(self):
        """錢包通用：登出玩家 ["POST","/logout-player"] ErrorCode驗證: MERCHANT_AUTH_FAILED"""
        test_secretKey = "error_secretKey"

        res = Lottery_Integration(secretKey=test_secretKey).api_logout_player(self.test_account)
        res_code = extract_json("code", res.text)
        res_msg = extract_json("message", res.text)
        res_traceId = extract_json("traceId", res.text)

        assertHTTPCode(res, [403])
        self.assertEqual(["010002", "MERCHANT_AUTH_FAILED"], [res_code, res_msg])
        self.assertIsNotNone(res_traceId)

    def test_03_00_launch_game_Success(self):
        """錢包通用：啟動遊戲 ["POST","/launch-game"]"""
        res = self.Lottery_Integration.api_launch_game(self.test_account)
        res_code = extract_json("code", res.text)
        res_msg = extract_json("message", res.text)
        res_accessToken = extract_json("result.accessToken", res.text)
        res_traceId = extract_json("traceId", res.text)

        assertHTTPCode(res)
        self.assertEqual(["000000", "SUCCESS"], [res_code, res_msg])
        self.assertRegex(res_accessToken, ".+\w")
        self.assertIsNotNone(res_traceId)

    def test_03_01_launch_game_PLAYER_NOT_FOUND(self):
        """錢包通用：啟動遊戲 ["POST","/launch-game"] ErrorCode驗證: PLAYER_NOT_FOUND"""
        test_playerName = "nonexistent"

        res = self.Lottery_Integration.api_launch_game(test_playerName)
        res_code = extract_json("code", res.text)
        res_msg = extract_json("message", res.text)
        res_traceId = extract_json("traceId", res.text)

        assertHTTPCode(res, [404])
        self.assertEqual(["020002", "PLAYER_NOT_FOUND"], [res_code, res_msg])
        self.assertIsNotNone(res_traceId)

    def test_03_02_launch_game_MERCHANT_NOT_FOUND(self):
        """錢包通用：啟動遊戲 ["POST","/launch-game"] ErrorCode驗證: MERCHANT_NOT_FOUND"""
        test_merchant = "nonexistent"

        res = Lottery_Integration(merchant=test_merchant).api_launch_game(self.test_account)
        res_code = extract_json("code", res.text)
        res_msg = extract_json("message", res.text)
        res_traceId = extract_json("traceId", res.text)

        assertHTTPCode(res, [403])
        self.assertEqual(["010001", "MERCHANT_NOT_FOUND"], [res_code, res_msg])
        self.assertIsNotNone(res_traceId)

    def test_03_03_launch_game_MERCHANT_AUTH_FAILED(self):
        """錢包通用：啟動遊戲 ["POST","/launch-game"] ErrorCode驗證: MERCHANT_AUTH_FAILED"""
        test_secretKey = "error_secretKey"

        res = Lottery_Integration(secretKey=test_secretKey).api_launch_game(self.test_account)
        res_code = extract_json("code", res.text)
        res_msg = extract_json("message", res.text)
        res_traceId = extract_json("traceId", res.text)

        assertHTTPCode(res, [403])
        self.assertEqual(["010002", "MERCHANT_AUTH_FAILED"], [res_code, res_msg])
        self.assertIsNotNone(res_traceId)


if __name__ == '__main__':
    unittest.main()
