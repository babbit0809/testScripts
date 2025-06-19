from config.SetAPIConfig import get_api_info
from config.RequestData import get_payload_Fin, get_payoutInfo
from utils.Request import HTTPClient
from utils.DataExtractor import extract_json


def api_Auth_login(role="admin"):  # 分為admin/payout, 預設為admin
    url, method = get_api_info("Financial", "Auth", "login")
    data = get_payload_Fin("Auth", "login", role=role)
    res = HTTPClient(url, method, headers={'Content-Type': 'application/json'}).send(data=data)
    return res


class Financial(object):
    def __init__(self):
        res = api_Auth_login()
        self.cookies = res.cookies
        self.headers = {'Content-Type': 'application/json'}
        userInfo = res.text
        self.userId = extract_json('data.id', userInfo)
        payoutInfo = get_payoutInfo()
        self.userId_payout = payoutInfo[3]
        self.accountID_payout = payoutInfo[4]

    # 充值訂單/ 查詢
    def api_Deposit_deposit(self, depositType, depositNo):  # depositType: 1(銀行)/2(第三方)/3(虛擬貨幣)
        url, method = get_api_info("Financial", "Deposit", "deposit")
        data = get_payload_Fin("Deposit", "deposit")
        data.update({"depositType": depositType, "depositNo": depositNo})
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # 獲取充值訂單資訊用(refer to api_Deposit_deposit)
    def get_DepositOrderInfo(self, depositType, depositNo):
        res = self.api_Deposit_deposit(depositType, depositNo).text
        createTime = extract_json('data[0].createTime', res)
        requestAmount = extract_json('data[0].requestAmount', res)
        depositFee = extract_json('data[0].depositFee', res)
        updateTime = extract_json('data[0].updateTime', res)
        bankName = extract_json('data[0].bankName', res)
        paymentTypeName = extract_json('data[0].paymentTypeName', res)
        accountName = extract_json('data[0].accountName', res)
        amount = extract_json('data[0].amount', res)
        keys = ["depositType", "depositNo", "createTime", "requestAmount", "depositFee", "updateTime", "bankName",
                "paymentTypeName", "account", "accountName", "amount"]
        values = [depositType, depositNo, createTime, requestAmount, depositFee, updateTime, bankName,
                  paymentTypeName, accountName, amount]
        return dict(zip(keys, values))

    # 充值訂單/ 交易確認(refer to get_DepositOrderInfo for order_info)
    def api_Deposit_update(self, order_info, status=2):  # status: 2(已確認)/3(查無款項)/8(金額不符)/7(金額調整)
        url, method = get_api_info("Financial", "Deposit", "update")
        data = order_info
        # 更新充值訂單資訊(金額調整的值先抓requestAmount*10的值)
        data.update({"userId": self.userId, "status": status, "amount": order_info["requestAmount"]})
        if status == 7:
            data.update({"amount": order_info["requestAmount"] * 10})
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # Home/ 出款作業/ 查詢(目前無單筆查詢功能)
    def api_Main_loadPayout(self):
        url, method = get_api_info("Financial", "Main", "loadPayout")
        data = get_payload_Fin("Main", "loadPayout")
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # Home/ 虛擬幣出款作業/ 查詢(目前無單筆查詢功能)
    def api_Main_loadPayout_cryptoCurrency(self):
        url, method = get_api_info("Financial", "Main", "loadPayout_cryptoCurrency")
        data = get_payload_Fin("Main", "loadPayout_cryptoCurrency")
        data.update({"cryptoProtocols": [1, 2, 3]})
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # 獲取第一筆訂單資訊用(refer to api_Main_loadPayout&api_Main_loadPayout_cryptoCurrency)
    def get_WithdrawOrderInfo(self, withdrawType):
        MappingTable = {"bankcard": self.api_Main_loadPayout().text,
                        "USDT": self.api_Main_loadPayout_cryptoCurrency().text}
        res = MappingTable[withdrawType]
        payoutID = extract_json('data.list[0].id', res)
        sitesID = extract_json('data.list[0].sitesID', res)
        withdrawalNo = extract_json('data.list[0].withdrawalNo', res)
        memberName = extract_json('data.list[0].memberName', res)
        realAmount = extract_json('data.list[0].realAmount', res)
        withdrawalTypeName = extract_json('data.list[0].withdrawalTypeName', res)
        bankName = extract_json('data.list[0].bankName', res)
        accountName = extract_json('data.list[0].accountName', res)
        accountNumber = extract_json('data.list[0].accountNumber', res)
        approverID = extract_json('data.list[0].approverID', res)
        createTime = extract_json('data.list[0].createTime', res)
        sitesName = extract_json('data.list[0].sitesName', res)
        keys = ["payoutID", "sitesID", "withdrawalNo", "memberName", "realAmount", "withdrawalTypeName", "bankName",
                "accountName", "accountNumber", "approverID", "createTime", "sitesName"]
        values = [payoutID, sitesID, withdrawalNo, memberName, realAmount, withdrawalTypeName, bankName,
                  accountName, accountNumber, approverID, createTime, sitesName]
        return dict(zip(keys, values))

    # Home/ 出款作業/ 轉單
    def api_Main_transfer(self, payoutID):
        url, method = get_api_info("Financial", "Main", "transfer")
        params = {"id": str(payoutID), "userId": str(self.userId_payout)}
        res = HTTPClient(url, method, self.headers, self.cookies).send(params=params)
        return res

    # Home/ 出款作業/ 出款作業(refer to get_WithdrawOrderInfo for order_info)
    def api_Main_payout(self, order_info, status=3):  # status: 3(已處理)/5(出款失敗)
        self.api_Main_transfer(order_info["payoutID"])  # 需先轉單給出款人員
        url, method = get_api_info("Financial", "Main", "payout")
        data = order_info
        # 更新提現訂單資訊(amon的值先抓realAmount的值)
        data.update({"approverID": self.userId_payout, "accountID": self.accountID_payout,
                     "status": status, "amon": order_info["realAmount"]})
        if status == 5:  # errorId: 23(銀行卡無效)/24(帳號錯誤)/25(帳號姓名不符)/29(開戶支行錯誤)/-1(其他理由), 暫定先帶23
            data.update({"errorId": 23})
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res


if __name__ == '__main__':
    pass
