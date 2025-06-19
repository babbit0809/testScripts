from datetime import datetime
from config.SetAPIConfig import get_api_info
from utils.Encrypt import encrypt
from utils.Request import HTTPClient


class Lottery_Integration(object):
    def __init__(self, merchant="LOTTO", secretKey="E26B6CDE1E78023E17298D26509EDA30879A25B75F925387797584B2FDCE646C"):
        self.headers = {'Content-Type': 'application/json',
                        'Merchant-Code': merchant,
                        'Subscription-Key': "789f76ba965646d483601526ebf23d32"}
        self.secretKey = secretKey
        self.timestamp = int(datetime.now().timestamp())

    # 錢包通用：建立玩家帳號
    def api_create_player(self, playerName, currencyCode):  # currencyCode: CNY/VND
        url, method = get_api_info("Integration", "create_player")
        data = {"playerName": playerName,
                "currencyCode": currencyCode,
                "timestamp": self.timestamp,
                "signature": encrypt(playerName + "&" + currencyCode + "&" + str(self.timestamp) + "&" + self.secretKey)}
        res = HTTPClient(url, method, self.headers).send(data=data, verify=False)  # verify: 避開SSL Error用
        return res

    # 錢包通用：登出玩家
    def api_logout_player(self, playerName):
        url, method = get_api_info("Integration", "logout_player")
        data = {"playerName": playerName,
                "timestamp": self.timestamp,
                "signature": encrypt(playerName + "&" + str(self.timestamp) + "&" + self.secretKey)}
        res = HTTPClient(url, method, self.headers).send(data=data, verify=False)  # verify: 避開SSL Error用
        return res

    # 錢包通用：啟動遊戲
    def api_launch_game(self, playerName):
        url, method = get_api_info("Integration", "launch_game")
        data = {"playerName": playerName,
                "timestamp": self.timestamp,
                "signature": encrypt(playerName + "&" + str(self.timestamp) + "&" + self.secretKey)}
        res = HTTPClient(url, method, self.headers).send(data=data, verify=False)  # verify: 避開SSL Error用
        return res


if __name__ == '__main__':
    pass
