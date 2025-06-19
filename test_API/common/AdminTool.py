import random
import os
import filetype
from random import choice
from requests_toolbelt import MultipartEncoder
from decimal import *
from config.PathConfig import Download_path
from config.SetAPIConfig import Project, get_api_info, get_api_LanguageSetting, PlatformCode
from config.RequestData import get_payload_AT
from utils.Request import HTTPClient
from utils.DataExtractor import extract_json, extract_text
from utils import Assertion

def api_User_Login():
    headers = {'Content-Type': 'application/json'}
    url, method = get_api_info("AdminTool", "User", "Login")
    data = get_payload_AT("User", "Login")
    res = HTTPClient(url, method, headers=headers).send(data=data)
    return res


# 同步金額格式與前端一致為小數點兩位以下無條件捨去用
def convert_amount_format(*ori_amount):
    amount_before = list(ori_amount)
    return [str(Decimal(amount).quantize(Decimal('.00'), ROUND_DOWN)) for amount in amount_before]


# 下載Excel檔案用
def download_excel_file(res):
    content_disposition = res.headers['Content-Disposition']
    filename = extract_text("attachment; filename=(.+)", content_disposition)
    excel_file = os.path.join(Download_path, filename)
    with open(excel_file, "wb") as f:
        f.write(res.content)
    return excel_file


# 重新開獎用(BonusNumber先以隨機排列為主, 後續視情況調整)
def redraw_BonusNumber(BonusNumber):
    BonusNumberList = BonusNumber.split(',')
    random.shuffle(BonusNumberList)
    BonusNumber_Update = ",".join(BonusNumberList)
    return BonusNumber_Update


class AdminTool(object):  # 帳號管理/ 一般會員管理 & 代理商管理因功能大部分相同, 故放在一起
    def __init__(self):
        res = api_User_Login()
        self.cookies = res.cookies
        self.headers = {'Content-Type': 'application/json',
                        'Language': get_api_LanguageSetting()}
        self.agentId = {'sta': "5", 'vt': "9"}

    # 選單/ 取得銀行清單
    def api_Option_MemberBank(self):
        url, method = get_api_info("AdminTool", "Option", "MemberBank")
        res = HTTPClient(url, method, self.headers, self.cookies).send()
        return res

    # 獲取MemberBankIDList用(refer to api_Option_MemberBank)
    def get_MemberBankIDList(self):
        res = self.api_Option_MemberBank().text
        MemberBankList = extract_json('Data', res)
        print("銀行總數:", len(MemberBankList), "\n")
        MemberBankIDList = []
        count = 0
        while count < len(MemberBankList):
            MemberBankID = extract_json('Data[' + str(count) + '].Id', res)
            MemberBankIDList.append(MemberBankID)
            count += 1
        return MemberBankIDList

    # 選單/ 取得轉賬對象清單
    def api_Option_TransferTypes(self):
        url, method = get_api_info("AdminTool", "Option", "TransferTypes")
        res = HTTPClient(url, method, self.headers, self.cookies).send()
        return res

    # 獲取TransferIDList用(refer to api_Option_TransferTypes)
    def get_TransferIDList(self):
        res = self.api_Option_TransferTypes().text
        TransferList = extract_json('Data', res)
        print("轉賬對象總數:", len(TransferList), "\n")
        TransferIDList = []
        count = 0
        while count < len(TransferList):
            MemberBankID = extract_json('Data[' + str(count) + '].Id', res)
            TransferIDList.append(MemberBankID)
            count += 1
        return TransferIDList

    # 選單/ 取得彩種類型清單(移除第三方)
    def api_Option_No3rdLotteries(self):
        url, method = get_api_info("AdminTool", "Option", "No3rdLotteries")
        res = HTTPClient(url, method, self.headers, self.cookies).send()
        return res

    # 選單/ 取得第三方遊戲清單
    def api_Option_ThirdPartyLotteryTypes(self, ShowAll=False):
        url, method = get_api_info("AdminTool", "Option", "ThirdPartyLotteryTypes")
        params = None
        if ShowAll is True:
            params = {"ShowAll": True}
        res = HTTPClient(url, method, self.headers, self.cookies).send(params=params)
        return res

    # 獲取GameCode/遊戲名稱用(refer to api_Option_No3rdLotteries & api_Option_ThirdPartyLotteryTypes)
    def get_GameNameMappingTable(self, game_type, ShowAll=False):
        if game_type == 'Lottery':  # 彩票
            res = self.api_Option_No3rdLotteries().text
        else:  # 第三方
            res = self.api_Option_ThirdPartyLotteryTypes(ShowAll=ShowAll).text
        GameTypeList = extract_json('Data', res)
        print("遊戲類型總數:", len(GameTypeList), "\n")
        GameCodeList, GameNameMappingTable = [], {}
        count = 0
        while count < len(GameTypeList):
            GameCode = extract_json('Data[' + str(count) + '].SubItems', res)
            GameCodeList.append(GameCode)
            print("遊戲類型Index:", count, "遊戲名稱總數:", len(GameCodeList[count]), "\n")
            num = 0
            while num < len(GameCodeList[count]):
                GameCode = GameCodeList[count][num]
                print(GameCode['Id'], GameCode['Name'])
                GameNameMappingTable[GameCode['Id']] = GameCode['Name']
                num += 1
            count += 1
        return GameNameMappingTable

    # 獲取GameCodeIDList用(refer to api_Option_No3rdLotteries & api_Option_ThirdPartyLotteryTypes)
    def get_GameCodeIDList(self, game_type, ShowAll=False):
        if game_type == 'Lottery':  # 彩票
            res = self.api_Option_No3rdLotteries().text
        else:  # 第三方
            res = self.api_Option_ThirdPartyLotteryTypes(ShowAll=ShowAll).text
        GameTypeList = extract_json('Data', res)
        print("遊戲類型總數:", len(GameTypeList), "\n")
        GameCodeList, GameCodeIDList = [], []
        count = 0
        while count < len(GameTypeList):
            GameCode = extract_json('Data[' + str(count) + '].SubItems', res)
            GameCodeList.append(GameCode)
            print("遊戲類型Index:", count, "遊戲名稱總數:", len(GameCodeList[count]), "\n")
            num = 0
            while num < len(GameCodeList[count]):
                GameCodeID = GameCodeList[count][num]['Id']
                print("GameCodeID", GameCodeID)
                GameCodeIDList.append(GameCodeID)
                num += 1
            count += 1
        return GameCodeIDList

    # 全站管理/ 簡訊驗證碼/ 查詢
    def api_Member_smsLog(self, account):
        url, method = get_api_info("AdminTool", "Member", "smsLog")
        params = {"MemberName": account}
        res = HTTPClient(url, method, self.headers, self.cookies).send(params=params)
        return res

    # 獲取電話號碼和簡訊驗證碼
    def get_smsLog(self, account):
        res = self.api_Member_smsLog(account).text
        CellPhoneNo = extract_json('Data.CellPhoneNo', res)
        ValidationCode = extract_json('Data.ValidationCode', res)
        print('CellPhoneNo: ' + CellPhoneNo)
        print('ValidationCode: ' + ValidationCode)
        return [CellPhoneNo, ValidationCode]

    # 帳號管理/ 一般會員管理/ 查詢
    def api_Member_Search(self, account=None):
        url, method = get_api_info("AdminTool", "Member", "Search")
        data = get_payload_AT("Member", "Search")
        if account:
            data.update({'AdvancedSearchConditionValue': account})
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # 帳號管理/ 代理商管理/ 查詢
    def api_Affiliate_Search(self, account=None):
        url, method = get_api_info("AdminTool", "Affiliate", "Search")
        data = get_payload_AT("Affiliate", "Search")
        if account:
            data.update({'AdvancedSearchConditionValue': account})
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # 獲取MemberId用(refer to api_Member_Search/api_Affiliate_Search)
    def get_account_MemberId(self, account, MemberType):  # MemberType: 1(一般會員)/2(代理商)
        if MemberType == 1:
            res = self.api_Member_Search(account).text
        else:
            res = self.api_Affiliate_Search(account).text
        MemberId = extract_json('Data.Data[0].MemberId', res)
        return MemberId

    # def get_account_NickName(self, account, MemberType):  # MemberType: 1(一般會員)/2(代理商)
    #     if MemberType == 1:
    #         res = self.api_Member_Search(account).text
    #     else:
    #         res = self.api_Affiliate_Search(account).text
    #     NickName = extract_json('Data.Data[0].NickName', res)
    #     return NickName

    # 帳號管理/ 一般會員管理 & 代理商管理/ 檢視/ 基本資料
    def api_Member_Member(self, MemberId):
        url, method = get_api_info("AdminTool", "Member", "Member")
        res = HTTPClient(url + MemberId, method, self.headers, self.cookies).send()
        return res

    # 獲取BasicInfo用(refer to api_Member_Member)
    def get_account_BasicInfo(self, account, MemberType):
        MemberId = self.get_account_MemberId(account, MemberType)
        res = self.api_Member_Member(MemberId).text
        NickName = extract_json('Data.NickName', res)
        Status = extract_json('Data.Status', res)
        MemberLevelId = extract_json('Data.MemberLevelId', res)
        MemberLevelName = extract_json('Data.MemberLevelName', res)
        ReturnPoint = extract_json('Data.ReturnPoint', res)
        IsBetPlaceable = extract_json('Data.IsBetPlaceable', res)
        IsDepositable = extract_json('Data.IsDepositable', res)
        IsWithdrawable = extract_json('Data.IsWithdrawable', res)
        IsFundTransferable = extract_json('Data.IsFundTransferable', res)
        keys = ["MemberId", "NickName", "Status", "MemberLevelId", "MemberLevelName", "ReturnPoint",
                "IsBetPlaceable", "IsDepositable", "IsWithdrawable", "IsFundTransferable"]
        values = [MemberId, NickName, Status, MemberLevelId, MemberLevelName, ReturnPoint,
                  IsBetPlaceable, IsDepositable, IsWithdrawable, IsFundTransferable]
        return dict(zip(keys, values))

    # 獲取GameTransferStatus用(refer to api_Member_Member)
    def get_account_GameTransferStatus(self, account, MemberType):
        MemberId = self.get_account_MemberId(account, MemberType)
        res = self.api_Member_Member(MemberId).text
        GameTransferSetting = extract_json('Data.GameTransferSetting', res)
        GameTransferStatus = []
        count = 0
        while count < len(GameTransferSetting):
            status = extract_json('Data.GameTransferSetting[' + str(count) + '].TransferLock', res)
            # 判斷TransferLock狀態, Ture即為停用, 反之則為啟用
            if status is True:
                GameTransferStatus.append("false")
            else:
                GameTransferStatus.append("true")
            count += 1
        return GameTransferStatus

    # 帳號管理/ 一般會員管理/ 檢視/ 提現帳戶/ 銀行卡
    def api_Member_MemberBank_GET(self, MemberId):
        url, method = get_api_info("AdminTool", "Member", "MemberBank_GET")
        res = HTTPClient(url + MemberId, method, self.headers, self.cookies).send()
        return res

    # 帳號管理/ 代理商管理/ 檢視/ 提現帳戶/ 銀行卡
    def api_Affiliate_MemberBank_GET(self, MemberId):
        url, method = get_api_info("AdminTool", "Affiliate", "MemberBank_GET")
        res = HTTPClient(url + MemberId, method, self.headers, self.cookies).send()
        return res

    def api_Member_MemberBank_Patch(self, account, MemberType, cardNum, status=True):
        MemberBankInfo = self.get_account_MemberBankInfo_by_CardNum(account, MemberType, cardNum)
        url, method = get_api_info("AdminTool", "Member", "MemberBank_Patch")
        data = get_payload_AT("Member", "MemberBank_PATCH")
        data.update({'MemberBankId': MemberBankInfo[0]})
        data.update({'MemberId': MemberBankInfo[1]})
        data.update({'AccountName': MemberBankInfo[2]})
        data.update({'BankId': MemberBankInfo[3]})
        data.update({'MemberBankTypeId': MemberBankInfo[4]})
        data.update({'BankName': MemberBankInfo[5]})
        data.update({'CardNumber': cardNum})
        data.update({'CreateOn': MemberBankInfo[6]})
        data.update({'BindRemoteIp': MemberBankInfo[7]})
        data.update({'Enabled': status})
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # 獲取BankName用(refer to api_Member_MemberBank_GET/api_Affiliate_MemberBank_GET, 目前僅擷取第一張銀行卡名稱, 後續視情況調整)
    def get_account_BankName(self, account, MemberType):
        MemberId = self.get_account_MemberId(account, MemberType)
        if MemberType == 1:
            res = self.api_Member_MemberBank_GET(MemberId).text
        else:
            res = self.api_Affiliate_MemberBank_GET(MemberId).text
        BankName = extract_json('Data[0].BankName', res)
        return BankName

    def get_account_MemberBankInfo_by_CardNum(self, account, MemberType, CardNum):
        MemberId = self.get_account_MemberId(account, MemberType)
        if MemberType == 1:
            res = self.api_Member_MemberBank_GET(MemberId).text
        else:
            res = self.api_Affiliate_MemberBank_GET(MemberId).text
        BankCard = extract_json('Data', res)

        count = 0
        for count in range(len(BankCard)):
            BankCardNum = extract_json('Data[' + str(count) + '].CardNumber', res)
            if BankCardNum == CardNum:
                break

        MemberBankId = extract_json('Data[' + str(count) + '].MemberBankId', res)
        AccountName = extract_json('Data[' + str(count) + '].AccountName', res)
        BankId = extract_json('Data[' + str(count) + '].BankId', res)
        MemberBankTypeId = extract_json('Data[' + str(count) + '].MemberBankTypeId', res)
        BankName = extract_json('Data[' + str(count) + '].BankName', res)
        CreateOn = extract_json('Data[' + str(count) + '].CreateOn', res)
        BindRemoteIp = extract_json('Data[' + str(count) + '].BindRemoteIp', res)
        MemberBankInfo = [MemberBankId, MemberId, AccountName, BankId, MemberBankTypeId, BankName, CreateOn, BindRemoteIp]
        return MemberBankInfo

    # 帳號管理/ 一般會員管理/ 檢視/ 提現帳戶/ 虛擬幣錢包
    def api_Member_CryptoCurrencyWallet_GET(self, MemberId):
        url, method = get_api_info("AdminTool", "Member", "CryptoCurrencyWallet_GET")
        res = HTTPClient(url + MemberId, method, self.headers, self.cookies).send()
        return res

    # 帳號管理/ 代理商管理/ 檢視/ 提現帳戶/ 虛擬幣錢包
    def api_Affiliate_CryptoCurrencyWallet_GET(self, MemberId):
        url, method = get_api_info("AdminTool", "Affiliate", "CryptoCurrencyWallet_GET")
        res = HTTPClient(url + MemberId, method, self.headers, self.cookies).send()
        return res

    def api_Member_CryptoCurrencyWallet_Patch(self, account, MemberType, CryptoCurrencyAddress, status=True):
        CryptoWalletInfo = self.get_account_CryptoWallet_by_Crypto_Address(account, MemberType, CryptoCurrencyAddress)
        url, method = get_api_info("AdminTool", "Member", "CryptoCurrencyWallet_Patch")
        data = get_payload_AT("Member", "CryptoCurrencyWallet_PATCH")
        data.update({'CryptoCurrencyWalletId': CryptoWalletInfo[0]})
        data.update({'CryptoProtocolId': CryptoWalletInfo[1]})
        data.update({'MemberId': CryptoWalletInfo[2]})
        data.update({'WalletAddress': CryptoWalletInfo[3]})
        data.update({'WalletNickName': CryptoWalletInfo[4]})
        data.update({'Enabled': status})
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    def get_account_CryptoWallet_by_Crypto_Address(self, account, MemberType, CryptoCurrencyAddress):
        MemberId = self.get_account_MemberId(account, MemberType)
        if MemberType == 1:
            res = self.api_Member_CryptoCurrencyWallet_GET(MemberId).text
        else:
            res = self.api_Affiliate_CryptoCurrencyWallet_GET(MemberId).text
        Address = extract_json('Data', res)

        count = 0
        for count in range(len(Address)):
            CryptoAddress = extract_json('Data[' + str(count) + '].WalletAddress', res)
            if CryptoAddress == CryptoCurrencyAddress:
                break

        CryptoCurrencyWalletId = extract_json('Data[' + str(count) + '].CryptoCurrencyWalletId', res)
        CryptoProtocolId = extract_json('Data[' + str(count) + '].CryptoProtocolId', res)
        WalletAddress = extract_json('Data[' + str(count) + '].WalletAddress', res)
        WalletNickName = extract_json('Data[' + str(count) + '].WalletNickName', res)
        MemberCryptoWalletInfo = [CryptoCurrencyWalletId, CryptoProtocolId, MemberId, WalletAddress, WalletNickName]
        return MemberCryptoWalletInfo

    # 帳號管理/ 一般會員管理 & 代理商管理/ 檢視/ 帳號安全
    def api_Member_Security(self, MemberId):
        url, method = get_api_info("AdminTool", "Member", "Security")
        res = HTTPClient(url + MemberId, method, self.headers, self.cookies).send()
        return res

    # 獲取Birthday用(refer to api_Member_Security)
    def get_account_Birthday(self, account, MemberType):
        MemberId = self.get_account_MemberId(account, MemberType)
        res = self.api_Member_Security(MemberId).text
        Birthday = extract_json('Data.Settings.Birthday', res).replace('T00:00:00', '')
        return Birthday

    # 帳號管理/ 一般會員管理 & 代理商管理/ 檢視/ 綜合紀錄
    def api_Member_IntegratedRecord(self, MemberId):
        url, method = get_api_info("AdminTool", "Member", "IntegratedRecord")
        data = get_payload_AT("Member", "IntegratedRecord")
        data.update({"memberId": MemberId})
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # 獲取IntegratedRecord用(refer to api_Member_IntegratedRecord, 遊戲紀錄目前無擷取, 後續視情況調整)
    def get_account_IntegratedRecord(self, account, MemberType):
        MemberId = self.get_account_MemberId(account, MemberType)
        res = self.api_Member_IntegratedRecord(MemberId).text
        MemberLoginCount = extract_json('Data.MemberLoginCount', res)
        MemberLoginFaliCount = extract_json('Data.MemberLoginFaliCount', res)
        MemberChangePwdCount = extract_json('Data.MemberChangePwdCount', res)
        DepositRequestAmountTotal = extract_json('Data.DepositRequestAmountTotal', res)
        DepositCount = extract_json('Data.DepositCount', res)
        WithdrawalRequestAmountTotal = extract_json('Data.WithdrawalRequestAmountTotal', res)
        WithdrawalCount = extract_json('Data.WithdrawalCount', res)
        PreferentialTotal = extract_json('Data.PreferentialTotal', res)
        PersonalReturnPoint = extract_json('Data.PersonalReturnPoint', res)
        AffilateReturnPoint = extract_json('Data.AffilateReturnPoint', res)
        RealsommisionAmount = extract_json('Data.RealsommisionAmount', res)
        DailyAmount = extract_json('Data.DailyAmount', res)
        OtherAmount = extract_json('Data.OtherAmount', res)
        return [MemberLoginCount, MemberLoginFaliCount, MemberChangePwdCount, DepositRequestAmountTotal, DepositCount,
                WithdrawalRequestAmountTotal, WithdrawalCount, PreferentialTotal, PersonalReturnPoint,
                AffilateReturnPoint, RealsommisionAmount, DailyAmount, OtherAmount]

    # 帳號管理/ 一般會員管理 & 代理商管理/ 檢視/ 異動紀錄
    def api_Member_Log(self, MemberId):
        url, method = get_api_info("AdminTool", "Member", "Log")
        data = get_payload_AT("Member", "Log")
        res = HTTPClient(url + MemberId, method, self.headers, self.cookies).send(data=data)
        return res

    # 獲取ChangeColumn用(refer to api_Member_Log, 目前僅擷取第一個異動項目名稱, 後續視情況調整)
    def get_account_ChangeColumn(self, account, MemberType):
        MemberId = self.get_account_MemberId(account, MemberType)
        res = self.api_Member_Log(MemberId).text
        ChangeColumn = extract_json('Data[0].Column', res)
        return ChangeColumn

    # 帳號管理/ 一般會員管理/ 新增會員
    def api_Member_Create(self):
        url, method = get_api_info("AdminTool", "Member", "Create")
        data = get_payload_AT("Member", "Create")
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # 帳號管理/ 代理商管理/ 新增代理
    def api_Affiliate_Create(self):
        url, method = get_api_info("AdminTool", "Affiliate", "Create")
        data = get_payload_AT("Affiliate", "Create")
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # 帳號管理/ 一般會員管理/ 編輯/ 基本資料(refer to get_account_BasicInfo for ori_setting, update_setting請以key=value形式帶入)
    def api_Member_BasicSetting(self, ori_setting, **update_setting):
        url, method = get_api_info("AdminTool", "Member", "BasicSetting")
        data = ori_setting
        if update_setting:
            data.update(update_setting)
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # 帳號管理/ 代理商管理/ 編輯/ 基本資料(refer to get_account_BasicInfo for ori_setting, update_setting請以key=value形式帶入)
    def api_Affiliate_BasicSetting(self, ori_setting, **update_setting):
        url, method = get_api_info("AdminTool", "Affiliate", "BasicSetting")
        data = ori_setting
        if update_setting:
            data.update(update_setting)
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # 帳號管理/ 一般會員管理/ 編輯/ 提現帳戶/ 新增銀行卡(暫時以隨機選擇, 後續視情況調整)
    def api_Member_MemberBank_POST(self, MemberId):
        url, method = get_api_info("AdminTool", "Member", "MemberBank_POST")
        data = get_payload_AT("Member", "MemberBank_POST")
        data.update({"MemberId": MemberId, "MemberBankTypeId": choice(self.get_MemberBankIDList())})
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # 帳號管理/ 代理商管理/ 編輯/ 提現帳戶/ 新增銀行卡(暫時以隨機選擇, 後續視情況調整)
    def api_Affiliate_MemberBank_POST(self, MemberId):
        url, method = get_api_info("AdminTool", "Affiliate", "MemberBank_POST")
        data = get_payload_AT("Affiliate", "MemberBank_POST")
        data.update({"MemberId": MemberId, "MemberBankTypeId": choice(self.get_MemberBankIDList())})
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # 帳號管理/ 一般會員管理/ 編輯/ 提現帳戶/ 新增虛擬幣錢包
    # CryptoProtocolId: 1(ERC20)/2(TRC20)/3(Omni)
    def api_Member_CryptoCurrencyWallet_POST(self, MemberId, CryptoProtocolId):
        url, method = get_api_info("AdminTool", "Member", "CryptoCurrencyWallet_POST")
        data = get_payload_AT("Member", "CryptoCurrencyWallet_POST", CryptoProtocolId=CryptoProtocolId)
        data.update({"MemberId": MemberId})
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # 帳號管理/ 代理商管理/ 編輯/ 提現帳戶/ 新增虛擬幣錢包
    # CryptoProtocolId: 1(ERC20)/2(TRC20)/3(Omni)
    def api_Affiliate_CryptoCurrencyWallet_POST(self, MemberId, CryptoProtocolId):
        url, method = get_api_info("AdminTool", "Affiliate", "CryptoCurrencyWallet_POST")
        data = get_payload_AT("Affiliate", "CryptoCurrencyWallet_POST", CryptoProtocolId=CryptoProtocolId)
        data.update({"MemberId": MemberId})
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # 帳號管理/ 解除號碼綁定
    def api_ClearPhoneVerify(self, MemberId):
        url, method = get_api_info("AdminTool", "Member", "ClearPhoneVerify")
        res = HTTPClient(url + MemberId, method, self.headers, self.cookies).send()
        return res

    # 帳號管理/ 解除號碼綁定
    # MemberType: 1(一般會員)/2(代理商)
    def ClearPhoneVerify(self, account, MemberType):
        MemberId = self.get_account_MemberId(account, MemberType)
        res = self.api_ClearPhoneVerify(MemberId).text
        status = extract_json('Status', res)
        return status

    # 帳號管理/ 解除Email
    def api_Email(self, MemberId):
        url, method = get_api_info("AdminTool", "Member", "Email")
        res = HTTPClient(url + MemberId, method, self.headers, self.cookies).send()
        return res

    # 帳號管理/ 解除Email
    def ClearEmail(self, account, MemberType):
        MemberId = self.get_account_MemberId(account, MemberType)
        res = self.api_Email(MemberId).text
        status = extract_json('Status', res)
        return status

    # 代理商管理/ 分紅報表/ 查詢
    def api_Affiliate_Dividends(self):
        url, method = get_api_info("AdminTool", "Affiliate", "Dividends")
        data = get_payload_AT("Affiliate", "Dividends")
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # 出入款管理/ 充值清單/ 交易確認
    def api_Deposit_Deposit(self, depositNo):
        url, method = get_api_info("AdminTool", "Deposit", "Deposit")
        data = get_payload_AT("Deposit", "Deposit")
        res = HTTPClient(url + depositNo, method, cookies=self.cookies).send(data=data, dtype="str")
        return res

    # 出入款管理/ 流水審核/ 查詢
    def api_Turnover_Search(self, account):
        url, method = get_api_info("AdminTool", "Turnover", "Search")
        data = get_payload_AT("Turnover", "Search")
        data.update({"MemberName": account})
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # 獲取待流水審核項目用
    def get_ValidBetAuditIDList(self, account):
        res = self.api_Turnover_Search(account).text
        TotalCount = extract_json('Data.TotalCount', res)
        ValidBetAuditIDList = []
        count = 0
        while count < TotalCount:
            ValidBetAuditID = extract_json('Data.Container[' + str(count) + '].ValidBetAuditID', res)
            ValidBetAuditIDList.append(ValidBetAuditID)
            count += 1
        return ValidBetAuditIDList

    # 出入款管理/ 流水審核/ 一鍵放寬
    def api_Turnover_BatchUpdate(self, account):
        url, method = get_api_info("AdminTool", "Turnover", "BatchUpdate")
        data = {"ValidBetAuditIdList": self.get_ValidBetAuditIDList(account)}
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # 出入款管理/ 提現處理/ 審單
    def api_Withdrawal_Status(self, withdrawNo, status=2):  # status: 2(通過)/4(拒絕)/5(出款失敗)
        url, method = get_api_info("AdminTool", "Withdrawal", "Status")
        data = get_payload_AT("Withdrawal", "Status")
        data.update({"Status": status})
        res = HTTPClient(url + withdrawNo + "/Status", method, cookies=self.cookies).send(data=data, dtype="str")
        return res

    # 出入款管理/ 快速充值作業設定/ 查詢(根據Req #4709, 暫定預設類型-子類型為充值-充值上分(常態))
    def api_QuickDepositSetting_Search(self):
        url, method = get_api_info("AdminTool", "QuickDepositSetting", "Search")
        data = get_payload_AT("QuickDepositSetting", "Search")
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # 獲取QuickDepositSettingInfo用(refer to api_QuickDepositSetting_Search, 目前僅擷取list第一個的所需data, 後續視情況調整)
    def get_QuickDepositSettingInfo(self):
        res = self.api_QuickDepositSetting_Search().text
        DepositFastSettingId = extract_json('Data.Data[0].DepositFastSettingId', res)
        ItemName = extract_json('Data.Data[0].ItemName', res)
        IsAudit = extract_json('Data.Data[0].IsAudit', res)
        TurnoverMultiple = extract_json('Data.Data[0].TurnoverMultiple', res)
        keys = ["settingId", "Name", "IsAudit", "TurnoverMultiple"]
        values = [DepositFastSettingId, ItemName, IsAudit, TurnoverMultiple]
        return dict(zip(keys, values))

    # 出入款管理/ 快速充值作業設定/ 新增(根據Req #4709, 暫定預設類型-子類型為充值-充值上分(常態))
    def api_QuickDepositSetting_QuickDepositSetting_POST(self):
        url, method = get_api_info("AdminTool", "QuickDepositSetting", "QuickDepositSetting_POST")
        data = get_payload_AT("QuickDepositSetting", "QuickDepositSetting_POST")
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # 出入款管理/ 快速充值作業設定/ 編輯(refer to get_QuickDepositSettingInfo for ori_setting, update_setting請以key=value形式帶入)
    def api_QuickDepositSetting_QuickDepositSetting_PUT(self, settingId, ori_setting, **update_setting):
        url, method = get_api_info("AdminTool", "QuickDepositSetting", "QuickDepositSetting_PUT")
        data = ori_setting
        if update_setting:
            data.update(update_setting)
        res = HTTPClient(url + str(settingId), method, self.headers, self.cookies).send(data=data)
        return res

    # 出入款管理/ 快速充值/ 單筆作業&批次作業
    def api_QuickDeposit_QuickDeposit(self, settingId, amount, *account):
        url, method = get_api_info("AdminTool", "QuickDeposit", "QuickDeposit")
        data = {"SettingId": settingId, "Amount": amount, "MemberNames": list(account)}
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # 出入款管理/ 第三方轉帳管理/ 查詢
    def api_FundTransfer_Manage(self, transferNo=None):
        url, method = get_api_info("AdminTool", "FundTransfer", "Manage")
        data = get_payload_AT("FundTransfer", "Manage")
        data.update({"TransferType": self.get_TransferIDList()})
        if transferNo:
            data.update({"AdvancedSearchConditionValue": transferNo})
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # 出入款管理/ 帳變紀錄/ 查詢
    def api_TransactionLog_Search(self):
        url, method = get_api_info("AdminTool", "TransactionLog", "Search")
        data = get_payload_AT("TransactionLog", "Search")
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # 獲取帳變紀錄統計資料用(refer to api_TransactionLog_Search)
    def get_TransactionLog_Summary(self):
        res = self.api_TransactionLog_Search().text
        TotalCount = extract_json('Data.List.TotalCount', res)
        IncomingAmount = extract_json('Data.Summary.IncomingAmount', res)
        OutgoingAmount = extract_json('Data.Summary.OutgoingAmount', res)
        BalanceAmount = extract_json('Data.Summary.BalanceAmount', res)
        # 處理金額格式
        amount_list = convert_amount_format(IncomingAmount, OutgoingAmount, BalanceAmount)
        IncomingAmount, OutgoingAmount, BalanceAmount = amount_list[0], amount_list[1], amount_list[2]
        return [TotalCount, IncomingAmount, OutgoingAmount, BalanceAmount]

    # 遊戲紀錄/ 彩票投注紀錄/ 查詢
    def api_Bets_Search(self, start_delta=0, status=None):  # 1(已成立)/2(已結算)/3(已撤單)
        url, method = get_api_info("AdminTool", "Bets", "Search")
        data = get_payload_AT("Bets", "Search", start_delta)
        data.update({"Status": status})
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # 遊戲紀錄/ 彩票投注紀錄/ 投注詳情
    def api_Bets_Bets(self, betOrderNumber):
        url, method = get_api_info("AdminTool", "Bets", "Bets")
        res = HTTPClient(url + betOrderNumber, method, self.headers, self.cookies).send()
        return res

    # 遊戲紀錄/ 彩票投注紀錄/ 導出報表
    def api_Bets_Export(self):
        url, method = get_api_info("AdminTool", "Bets", "Export")
        data = get_payload_AT("Bets", "Export")
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # 遊戲紀錄/ 彩票投注紀錄/ 撤單
    def api_Bets_Cancel(self, *betOrder):  # 訂單狀態須為"已成立"
        url, method = get_api_info("AdminTool", "Bets", "Cancel")
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=list(betOrder))
        return res

    # 遊戲紀錄/ 彩票投注紀錄歷史/ 查詢
    def api_Bets_History(self, days=-61):
        url, method = get_api_info("AdminTool", "Bets", "History")
        data = get_payload_AT("Bets", "History", days)
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # 遊戲紀錄/ 第三方投注紀錄/ 查詢
    def api_ThirdPartyBetLog_Search(self, *GameProviderId):
        url, method = get_api_info("AdminTool", "ThirdPartyBetLog", "Search")
        data = get_payload_AT("ThirdPartyBetLog", "Search")
        if GameProviderId:
            data.update({"GameProviderIdList": list(GameProviderId)})
        else:
            data.update({"GameProviderIdList": self.get_GameCodeIDList("ThirdParty")})
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # 獲取第三方投注紀錄統計資料用(refer to api_ThirdPartyBetLog_Search)
    def get_ThirdPartyBetLog_Summary(self, *GameProviderId):
        res = self.api_ThirdPartyBetLog_Search(*GameProviderId).text
        TotalCount = extract_json('Data.List.TotalCount', res)
        NumberOfMembers = extract_json('Data.Summary.NumberOfMembers', res)
        BetAmount = extract_json('Data.Summary.BetAmount', res)
        ActualBetAmount = extract_json('Data.Summary.ActualBetAmount', res)
        BonusAmount = extract_json('Data.Summary.BonusAmount', res)
        WinLoss = extract_json('Data.Summary.WinLoss', res)
        # 處理金額格式
        amount_list = convert_amount_format(ActualBetAmount, BonusAmount, WinLoss)
        ActualBetAmount, BonusAmount, WinLoss = amount_list[0], amount_list[1], amount_list[2]
        return [TotalCount, NumberOfMembers, BetAmount, ActualBetAmount, BonusAmount, WinLoss]

    # 遊戲管理/ 彩票管理/ 基本設置/ 查詢
    def api_Lottery_Search(self, *lotteryCode):
        url, method = get_api_info("AdminTool", "Lottery", "Search")
        data = get_payload_AT("Lottery", "Search")
        if lotteryCode:
            data.update({"LotteryCode": list(lotteryCode)})
        else:
            data.update({"LotteryCode": self.get_GameCodeIDList("Lottery")})
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # 遊戲管理/ 彩票管理/ 彩種開關/ 查詢
    def api_Lottery_Switch_POST(self, platform, *lotteryCode):
        url, method = get_api_info("AdminTool", "Lottery", "Switch_POST")
        if lotteryCode:
            data = list(lotteryCode)
        else:
            data = self.get_GameCodeIDList("Lottery")
        res = HTTPClient(url + "?platform=" + PlatformCode[platform], method, self.headers, self.cookies).send(
            data=data)
        return res

    # 遊戲管理/ 彩票管理/ 彩種開關/ 開關
    def api_Lottery_Switch_PATCH(self, platform, **model):
        """可修改資料有LotteryType/BetPageName/BetType/BetSubType/BetRule, 請以key=value形式帶入, 資料格式如下:
        LotteryCode/BetPageNameId/BetTypeId/BetSubTypeId/BetRuleId參數值請參照AdminTool的遊戲彩種清單, int = 1(開啟)/2(關閉)
        LotteryType={"LotteryCode": int},
        BetPageName={"LotteryCode":{"BetPageNameId": int}},
        BetType={"BetTypeId": int},
        BetSubType={"BetSubTypeId": int},
        BetRule={"BetRuleId": int}"""
        url, method = get_api_info("AdminTool", "Lottery", "Switch_PATCH")
        data = {"Platform": PlatformCode[platform]}
        if model:
            data.update(model)
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # 遊戲管理/ 期數管理/ 查詢
    # status: 1(未開盤)/2(已開盤)/3(已封盤)/4(已結算)/5(開獎異常)/6(已取消)
    def api_IssueNumber_Search(self, start_delta=0, end_delta=0, SortColumn="AnnounceTime", **search_info):
        url, method = get_api_info("AdminTool", "IssueNumber", "Search")
        data = get_payload_AT("IssueNumber", "Search", start_delta, end_delta, SortColumn=SortColumn)
        data.update(search_info)
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # 獲取IssueNumberInfo用(refer to api_IssueNumber_Search, 目前僅擷取list第一個的所需data, 後續視情況調整)
    def get_IssueNumberInfo(self, start_delta=0, end_delta=0, SortColumn="AnnounceTime", **search_info):
        res = self.api_IssueNumber_Search(start_delta, end_delta, SortColumn=SortColumn, **search_info).text
        LotteryHistoryId = extract_json('Data.Data[0].LotteryHistoryId', res)
        LotteryCode = extract_json('Data.Data[0].LotteryCode', res)
        LotteryName = extract_json('Data.Data[0].LotteryName', res)
        IssueNumber = extract_json('Data.Data[0].IssueNumber', res)
        BonusNumber = extract_json('Data.Data[0].BonusNumber', res)
        AnnounceTime = extract_json('Data.Data[0].AnnounceTime', res)
        StartTime = extract_json('Data.Data[0].StartTime', res)
        TotalBet = extract_json('Data.Data[0].TotalBet', res)
        return [LotteryHistoryId, LotteryCode, LotteryName, IssueNumber, BonusNumber, AnnounceTime, StartTime, TotalBet]

    # 遊戲管理/ 期數管理/ 管理/ 編輯
    def api_IssueNumber_IssueNumber(self, lotteryHistoryId, IssueNumber):  # 期號狀態須為"1(未開盤)"
        url, method = get_api_info("AdminTool", "IssueNumber", "IssueNumber")
        data = get_payload_AT("IssueNumber", "IssueNumber")
        data.update({"IssueNumber": IssueNumber})
        res = HTTPClient(url + str(lotteryHistoryId), method, self.headers, self.cookies).send(data=data)
        return res

    # 遊戲管理/ 期數管理/ 管理/ 取消當期
    def api_IssueNumber_Cancel(self, lotteryHistoryId):  # 期號狀態須為"4(已結算)"
        url, method = get_api_info("AdminTool", "IssueNumber", "Cancel")
        res = HTTPClient(url + str(lotteryHistoryId) + "/Cancel", method, self.headers, self.cookies).send()
        return res

    # 遊戲管理/ 期數管理/ 管理/ 重新開獎/ 試算
    def api_IssueNumber_TrailCalculationBonus(self, lotteryHistoryId, BonusNumber):  # 期號狀態須為"4(已結算)"
        url, method = get_api_info("AdminTool", "IssueNumber", "TrailCalculationBonus")
        data = ({"BonusNumber": BonusNumber})
        res = HTTPClient(url + str(lotteryHistoryId) + "/TrailCalculationBonus", method,
                         self.headers, self.cookies).send(data=data)
        return res

    # 遊戲管理/ 期數管理/ 管理/ 重新開獎
    def api_IssueNumber_Settle(self, lotteryHistoryId, BonusNumber):  # 期號狀態須為"4(已結算)"
        url, method = get_api_info("AdminTool", "IssueNumber", "Settle")
        data = ({"BonusNumber": BonusNumber})
        res = HTTPClient(url + str(lotteryHistoryId) + "/Settle", method, self.headers, self.cookies).send(data=data)
        return res

    # 遊戲管理/ 賠率設定/ 玩法賠率模式設定/ 查詢
    def api_BetSection_Search(self, LotteryCode):
        url, method = get_api_info("AdminTool", "BetSection", "Search")
        data = get_payload_AT("BetSection", "Search")
        data.update({"LotteryCode": LotteryCode})
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # 獲取BetSectionInfo用(refer to api_BetSection_Search, 目前僅擷取list第一個的所需data, 後續視情況調整)
    def get_BetSectionInfo(self, LotteryCode):
        res = self.api_BetSection_Search(LotteryCode).text
        BetTypeId = extract_json('Data.Data[0].BetTypeId', res)
        BetSectionId = extract_json('Data.Data[0].BetSectionId', res)
        return [BetTypeId, BetSectionId]

    # 遊戲管理/ 賠率設定/ 玩法賠率模式設定/ 管理/ 編輯
    def api_BetSection_BetSection(self, betTypeId, BetSectionId):
        url, method = get_api_info("AdminTool", "BetSection", "BetSection")
        data = {"BetTypeId": betTypeId, "BetSectionId": BetSectionId}
        res = HTTPClient(url + str(betTypeId), method, self.headers, self.cookies).send(data=data)
        return res

    # 遊戲管理/ 賠率設定/ 投注項賠率設定/ 查詢
    def api_BetRule_Search(self, LotteryCode):
        url, method = get_api_info("AdminTool", "BetRule", "Search")
        data = get_payload_AT("BetRule", "Search")
        data.update({"LotteryCode": LotteryCode})
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # 獲取BetRuleInfo用(refer to api_BetRule_Search, 目前僅擷取list第一個的所需data, 後續視情況調整)
    def get_BetRuleInfo(self, LotteryCode):
        res = self.api_BetRule_Search(LotteryCode).text
        BetRuleId = extract_json('Data.Data[0].BetRuleId', res)
        Modulus = extract_json('Data.Data[0].Modulus', res)
        MaxBonusMode = extract_json('Data.Data[0].MaxBonusMode', res)
        return [BetRuleId, Modulus, MaxBonusMode]

    # 遊戲管理/ 賠率設定/ 投注項賠率設定/ 管理/ 編輯
    def api_BetRule_BetRule(self, betRuleId, Modulus, MaxBonusMode):
        url, method = get_api_info("AdminTool", "BetRule", "BetRule")
        data = {"BetRuleId": betRuleId, "Modulus": Modulus, "MaxBonusMode": MaxBonusMode}
        res = HTTPClient(url + str(betRuleId), method, self.headers, self.cookies).send(data=data)
        return res

    # 營運管理/ 輪播圖管理/ 取得BannerSetting
    def api_LobbyImage_BannerSetting(self):
        url, method = get_api_info("AdminTool", "LobbyImage", "BannerSetting")
        res = HTTPClient(url + self.agentId[Project], method, self.headers, self.cookies).send()
        return res

    # 獲取輪播圖管理的裝置區塊項目個數用(refer to api_LobbyImage_BannerSetting)
    # device: web/h5/ios/android, district: sliders(輪播版位)/gameButtons(遊戲按鈕)/links(行銷廣告)
    def get_BannerSetting_Quantity(self, device, district):
        res = self.api_LobbyImage_BannerSetting().text
        BannerSettingList = extract_json('Data.' + device + '.' + district, res)
        TotalCount = len(BannerSettingList)
        return TotalCount

    # 搜尋輪播圖管理所新增項目是否存在用(refer to api_LobbyImage_BannerSetting, 後續視情況調整位置)
    # device: web/h5/ios/android, district: sliders(輪播版位)/gameButtons(遊戲按鈕)/links(行銷廣告)
    def check_BannerSetting_Item(self, device, district, check_itemName, check_itemValue):
        res = self.api_LobbyImage_BannerSetting().text
        TotalCount = self.get_BannerSetting_Quantity(device, district)
        itemList = []
        count = 0
        while count < TotalCount:
            item = extract_json('Data.' + device + '.' + district + '[' + str(count) + '].' + check_itemName, res)
            itemList.append(item)
            count += 1
        print("Item value:", itemList, "\nCheck value:", check_itemValue)
        return True if check_itemValue in itemList else False

    # 營運管理/ 公告設定/ 查詢公告
    def api_operation_news_Search(self, title=None, releaseto=None, start_delta=None):
        url, method = get_api_info("AdminTool", "operation", "Search")
        data = get_payload_AT("operation", "Search", start_delta)
        data.update({"Title": title,
                     "ReleaseTo": releaseto, })
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # status: [0](會員)/[1](IP直屬) /[2](直屬) /[3](代理)
    def get_operation_news_TotalCount(self, title=None, releaseto=None, start_delta=None):
        res = self.api_operation_news_Search(title, releaseto, start_delta).text
        TotalCount = extract_json('Data.TotalCount', res)
        return TotalCount

    # 活動管理/ 活動類別管理/ 查詢
    def api_Activity_Type(self):
        url, method = get_api_info("AdminTool", "Activity", "Type")
        res = HTTPClient(url, method, self.headers, self.cookies).send()
        return res

    # 獲取ActivityTypeId用(refer to api_Activity_Type, 目前僅擷取第一個ID, 後續視情況調整)
    def get_ActivityTypeId(self):
        res = self.api_Activity_Type().text
        Id = extract_json('Data[0].Id', res)
        return Id

    # 活動管理/ 活動管理/ 查詢活動列表
    def api_Activity_Search(self, status=None, name=None, start_delta=None):
        url, method = get_api_info("AdminTool", "Activity", "Search")
        data = get_payload_AT("Activity", "Search", start_delta)
        data.update({"Name": name,
                     "Status": status,})
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # status: [1](未開始)/[2](運行中) /[3](已結束)
    def get_Activity_status_TotalCount(self, status=None, name=None, start_delta=None):
        res = self.api_Activity_Search(status, name, start_delta).text
        TotalCount = extract_json('Data.TotalCount', res)
        return TotalCount

    # 活動管理/ 活動管理/ 查詢單一活動
    def api_Activity_Activity_GET(self, activityId):
        url, method = get_api_info("AdminTool", "Activity", "Activity_GET")
        res = HTTPClient(url + str(activityId), method, self.headers, self.cookies).send()
        return res

    # 獲取ActivityInfo用(refer to api_Activity_Activity_GET, 目前僅擷取部分資訊, 後續視情況調整)
    def get_ActivityInfo(self, activityId):
        res = self.api_Activity_Activity_GET(activityId).text
        ActivityDisplayTypeId = extract_json('Data.ActivityDisplayTypeId', res)
        ActivityDisplayTargetIds = extract_json('Data.ActivityDisplayTargetIds', res)
        Subject = extract_json('Data.Subject', res)
        ActivityDisplayStartDate = extract_json('Data.ActivityDisplayStartDate', res)
        ActivityDisplayEndDate = extract_json('Data.ActivityDisplayEndDate', res)
        ActivityStartTime = extract_json('Data.ActivityStartTime', res)
        ActivityEndTime = extract_json('Data.ActivityEndTime', res)
        IsShowOnTop = extract_json('Data.IsShowOnTop', res)
        WebPicFileName = extract_json('Data.WebPicFileName', res)
        AppPicFileName = extract_json('Data.AppPicFileName', res)
        keys = ["ActivityId", "ActivityDisplayTypeId", "ActivityDisplayTargetIds", "Subject",
                "ActivityDisplayStartDate",
                "ActivityDisplayEndDate", "ActivityStartTime", "ActivityEndTime", "IsShowOnTop", "WebPicFileName",
                "AppPicFileName"]
        values = [activityId, ActivityDisplayTypeId, ActivityDisplayTargetIds, Subject, ActivityDisplayStartDate,
                  ActivityDisplayEndDate, ActivityStartTime, ActivityEndTime, IsShowOnTop, WebPicFileName,
                  AppPicFileName]
        return dict(zip(keys, values))

    # 活動管理/ 活動管理/ 新增活動/ 上傳圖片
    # pic_type: 1(Activity)/2(SiteMessage)/3(Promotion)/4(Logo)/5(Lobby)
    def api_Image_upload(self, pic_path, pic_type=1):
        url, method = get_api_info("AdminTool", "Image", "upload")
        file_name = os.path.basename(pic_path)
        with open(pic_path, 'rb') as f:
            file_handler = f.read()
        file_type = filetype.guess(pic_path)
        mime_type = file_type.mime
        fields = {"image": (file_name, file_handler, mime_type)}
        encode_data = MultipartEncoder(fields)
        res = HTTPClient(url + str(pic_type), method,
                         headers={"Content-Type": encode_data.content_type},
                         cookies=self.cookies).send(data=encode_data, dtype="str")
        return res

    # 上傳圖片並回傳storage_path上的路徑用(refer to api_Image_upload)
    def get_image_storage_path(self, pic_path):
        res = self.api_Image_upload(pic_path).text
        storage_path = extract_json('Data', res)
        return storage_path

    # 活動管理/ 活動管理/ 新增活動
    def api_Activity_Activity_POST(self, ActivityTypeId, pic_web_path, pic_mobile_path):
        url, method = get_api_info("AdminTool", "Activity", "Activity_POST")
        data = get_payload_AT("Activity", "Activity_POST")
        data.update({"ActivityDisplayTypeId": ActivityTypeId,
                     "WebPicFileName": self.get_image_storage_path(pic_web_path),
                     "AppPicFileName": self.get_image_storage_path(pic_mobile_path)})
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # 活動管理/ 活動管理/ 操作/ 編輯/ 基本設定(refer to get_ActivityInfo for ori_setting, update_setting請以key=value形式帶入)
    def api_Activity_Activity_PUT(self, ori_setting, **update_setting):
        url, method = get_api_info("AdminTool", "Activity", "Activity_PUT")
        data = ori_setting
        if update_setting:
            data.update(update_setting)
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # 活動管理/ 活動管理/ 查詢單一活動規則設定
    def api_Activity_Rule(self, activityId):
        url, method = get_api_info("AdminTool", "Activity", "Rule")
        res = HTTPClient(url + str(activityId), method, self.headers, self.cookies).send()
        return res

    # 獲取ActivityRuleInfo用(refer to api_Activity_Rule)
    def get_ActivityRuleInfo(self, activityId):
        res = self.api_Activity_Rule(activityId).text
        ActivityDisplayTargetIds = extract_json('Data.ActivityDisplayTargetIds', res)  # 適用會員
        SettleOccursId = extract_json('Data.SettleOccursId', res)  # 結算時間
        DispatchModeId = extract_json('Data.DispatchModeId', res)  # 派發方式
        ActivityBonus = extract_json('Data.ActivityBonus', res)  # 獎金金額
        ValidBetAmountRuleId = extract_json('Data.ValidBetAmountRuleId', res)  # 流水門檻-規則
        ValidBetAmountPeriodId = extract_json('Data.ValidBetAmountPeriodId', res)  # 流水門檻-區間
        ValidBetAmount = extract_json('Data.ValidBetAmount', res)  # 流水門檻-金額
        DepositRuleId = extract_json('Data.DepositRuleId', res)  # 充值門檻-規則
        DepositPeriodId = extract_json('Data.DepositPeriodId', res)  # 充值門檻-區間
        DepositAmount = extract_json('Data.DepositAmount', res)  # 充值門檻-金額
        WinLossRuleId = extract_json('Data.WinLossRuleId', res)  # 盈虧門檻-規則
        WinLossPeriodId = extract_json('Data.WinLossPeriodId', res)  # 盈虧門檻-區間
        WinLossAmount = extract_json('Data.WinLossAmount', res)  # 盈虧門檻-金額
        ExtraAudit = extract_json('Data.ExtraAudit', res)  # 額外條件
        ActivityBonusReceivePeriodId = extract_json('Data.ActivityBonusReceivePeriodId', res)  # 領取次數上限-區間
        ActivityBonusReceiveTimes = extract_json('Data.ActivityBonusReceiveTimes', res)  # 領取次數上限-次數
        ActivityBonusLimitModeId = extract_json('Data.ActivityBonusLimitModeId', res)  # 獎金上限-規則
        ActivityBonusUpperLimit = extract_json('Data.ActivityBonusUpperLimit', res)  # 獎金上限-金額
        ValidBetMultiple = extract_json('Data.ValidBetMultiple', res)  # 流水審核倍數
        keys = ["ActivityId", "ActivityDisplayTargetIds", "SettleOccursId", "DispatchModeId", "ActivityBonus",
                "ValidBetAmountRuleId", "ValidBetAmountPeriodId", "ValidBetAmount", "DepositRuleId", "DepositPeriodId",
                "DepositAmount", "WinLossRuleId", "WinLossPeriodId", "WinLossAmount", "ExtraAudit",
                "ActivityBonusReceivePeriodId", "ActivityBonusReceiveTimes", "ActivityBonusLimitModeId",
                "ActivityBonusUpperLimit", "ValidBetMultiple"]
        values = [activityId, ActivityDisplayTargetIds, SettleOccursId, DispatchModeId, ActivityBonus,
                  ValidBetAmountRuleId, ValidBetAmountPeriodId, ValidBetAmount, DepositRuleId, DepositPeriodId,
                  DepositAmount, WinLossRuleId, WinLossPeriodId, WinLossAmount, ExtraAudit,
                  ActivityBonusReceivePeriodId, ActivityBonusReceiveTimes, ActivityBonusLimitModeId,
                  ActivityBonusUpperLimit, ValidBetMultiple]
        return dict(zip(keys, values))

    # 活動管理/ 活動管理/ 操作/ 編輯/ 規則設定(refer to get_ActivityRuleInfo for ori_setting, update_setting請以key=value形式帶入)
    def api_Activity_Modify(self, ori_setting, **update_setting):
        url, method = get_api_info("AdminTool", "Activity", "Modify")
        # 獲取適用遊戲清單
        data = {"ActivityGame": self.get_GameCodeIDList(game_type="All", ShowAll=True)}
        # 讀取原有活動的規則設定值
        data.update(ori_setting)
        # 必填欄位, 故預設下列數值避免跳錯(後續視情況調整)
        data.update({"ActivityBonus": {"ModelId": 1,  # 獎金金額, 預設為全部, 如改為2(依會員等級)則需增加MemberLevelId欄位值
                                       "Rules": [{"ActivityBonusMode": 1,  # 預設為固定金額
                                                  "ActivityBonus": 100}]},
                     "ActivityBonusUpperLimit": 100, "ValidBetMultiple": 1})
        if update_setting:
            data.update(update_setting)
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # 營運報表/ 代理報表/ 查詢
    # filter_option: 1(代理團隊)/2(直屬上級)
    def api_OperatingReport_Search_Affiliate(self, filter_option=None, account=None):
        url, method = get_api_info("AdminTool", "OperatingReport", "Search_Affiliate")
        data = get_payload_AT("OperatingReport", "Search_Affiliate")
        if account:
            data.update({"AdvancedSearchConditionItem": filter_option, "AffiliateAccount": account})
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # 獲取代理報表統計資料用(refer to api_OperatingReport_Search_Affiliate)
    def get_AffiliateReport_Summary(self, filter_option=None, account=None):
        res = self.api_OperatingReport_Search_Affiliate(filter_option, account).text
        AffiliateCnt = extract_json('Data.Summary.AffilateCnt', res)
        MemberTreeCnt = extract_json('Data.Summary.MemberTreeCnt', res)
        RegisterCnt = extract_json('Data.Summary.RegisterCnt', res)
        DepositFirstTimeCnt = extract_json('Data.Summary.DepositFirstTimeCnt', res)
        DepositCnt = extract_json('Data.Summary.DepositCnt', res)
        Deposit3Cnt = extract_json('Data.Summary.Deposit3Cnt', res)
        Deposit5Cnt = extract_json('Data.Summary.Deposit5Cnt', res)
        BetMemberCnt = extract_json('Data.Summary.BetMemberCnt', res)
        BetOrderCnt = extract_json('Data.Summary.BetOrderCnt', res)
        BetAmount = extract_json('Data.Summary.BetAmount', res)
        ValidBetAmount = extract_json('Data.Summary.ValidBetAmount', res)
        BonusAmount = extract_json('Data.Summary.BonusAmount', res)
        WinLossAmount = extract_json('Data.Summary.WinLossAmount', res)
        DepositAmount = extract_json('Data.Summary.DepositAmount', res)
        WithdrawalAmount = extract_json('Data.Summary.WithdrawalAmount', res)
        DepWithAmount = extract_json('Data.Summary.DepWithAmount', res)
        DeductionAmount = extract_json('Data.Summary.DeductionAmount', res)
        RmAdditionAmount = extract_json('Data.Summary.RmAdditionAmount', res)
        PrePaymentAmount = extract_json('Data.Summary.PrePaymentAmount', res)
        CommissionAmount = extract_json('Data.Summary.CommissionAmount', res)
        ReturnPointAmount = extract_json('Data.Summary.ReturnPointAmount', res)
        Fee = extract_json('Data.Summary.Fee', res)
        AdministrationFee = extract_json('Data.Summary.AdministrationFee', res)
        MemberBalance = extract_json('Data.Summary.MemberBalance', res)
        TotalWinLossAmount = extract_json('Data.Summary.TotalWinLossAmount', res)
        return [AffiliateCnt, MemberTreeCnt, RegisterCnt, DepositFirstTimeCnt, DepositCnt, Deposit3Cnt, Deposit5Cnt,
                BetMemberCnt, BetOrderCnt, BetAmount, ValidBetAmount, BonusAmount, WinLossAmount, DepositAmount,
                WithdrawalAmount, DepWithAmount, DeductionAmount, RmAdditionAmount, PrePaymentAmount, CommissionAmount,
                ReturnPointAmount, Fee, AdministrationFee, MemberBalance, TotalWinLossAmount]

    # 營運報表/ 會員報表/ 查詢
    # filter_option: 1(會員帳號)/2(直屬上級)/3(代理團隊)
    def api_OperatingReport_Search_Member(self, filter_option=None, account=None):
        url, method = get_api_info("AdminTool", "OperatingReport", "Search_Member")
        data = get_payload_AT("OperatingReport", "Search_Member")
        if account:
            data.update({"AdvancedSearchConditionItem": filter_option, 'AdvancedSearchConditionValue': account})
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # 獲取會員報表統計資料用(refer to api_OperatingReport_Search_Member)
    def get_MemberReport_Summary(self, filter_option=None, account=None):
        res = self.api_OperatingReport_Search_Member(filter_option, account).text
        MemberCnt = extract_json('Data.Summary.MemberCnt', res)
        BetOrderCnt = extract_json('Data.Summary.BetOrderCnt', res)
        BetAmount = extract_json('Data.Summary.BetAmount', res)
        ValidBetAmount = extract_json('Data.Summary.ValidBetAmount', res)
        BonusAmount = extract_json('Data.Summary.BonusAmount', res)
        WinLossAmount = extract_json('Data.Summary.WinLossAmount', res)
        DepositCnt = extract_json('Data.Summary.DepositCnt', res)
        DepositAmount = extract_json('Data.Summary.DepositAmount', res)
        WithdrawalAmount = extract_json('Data.Summary.WithdrawalAmount', res)
        DepWithAmount = extract_json('Data.Summary.DepWithAmount', res)
        DeductionAmount = extract_json('Data.Summary.DeductionAmount', res)
        RmAdditionAmount = extract_json('Data.Summary.RmAdditionAmount', res)
        PrePaymentAmount = extract_json('Data.Summary.PrePaymentAmount', res)
        ReturnPointAmount = extract_json('Data.Summary.ReturnPointAmount', res)
        Fee = extract_json('Data.Summary.Fee', res)
        AdministrationFee = extract_json('Data.Summary.AdministrationFee', res)
        MemberBalance = extract_json('Data.Summary.MemberBalance', res)
        TotalWinLossAmount = extract_json('Data.Summary.TotalWinLossAmount', res)
        return [MemberCnt, BetOrderCnt, BetAmount, ValidBetAmount, BonusAmount, WinLossAmount, DepositCnt,
                DepositAmount,
                WithdrawalAmount, DepWithAmount, DeductionAmount, RmAdditionAmount, PrePaymentAmount, ReturnPointAmount,
                Fee, AdministrationFee, MemberBalance, TotalWinLossAmount]

    # 營運報表/ 平台報表/ 查詢
    def api_AgentReport_Search(self):
        url, method = get_api_info("AdminTool", "AgentReport", "Search")
        data = get_payload_AT("AgentReport", "Search")
        res = HTTPClient(url, method, self.headers, self.cookies).send(data=data)
        return res

    # 獲取平台報表統計資料用(refer to api_AgentReport_Search, 部分金額顯示與代理報表/會員報表不同, 需處理格式)
    def get_AgentReport_Summary(self):
        res = self.api_AgentReport_Search().text
        DepositCnt = extract_json('Data.Summary.DepositCnt', res)
        DepositAmount = extract_json('Data.Summary.DepositAmount', res)
        Fee = extract_json('Data.Summary.Fee', res)
        AdministrationFee = extract_json('Data.Summary.AdministrationFee', res)
        WithdrawalAmount = extract_json('Data.Summary.WithdrawalAmount', res)
        DepWithAmount = extract_json('Data.Summary.DepWithAmount', res)
        RmDeAmountnt = extract_json('Data.Summary.RmDeAmountnt', res)
        RmAddAmount = extract_json('Data.Summary.RmAddAmount', res)
        BalanceAmount = extract_json('Data.Summary.BalanceAmount', res)
        BetMemberCnt = extract_json('Data.Summary.BetMemberCnt', res)
        BetAmount = extract_json('Data.Summary.BetAmount', res)
        ValidBetAmount = extract_json('Data.Summary.ValidBetAmount', res)
        BonusAmount = extract_json('Data.Summary.BonusAmount', res)
        WinLossAmount = extract_json('Data.Summary.WinLossAmount', res)
        PreferentialAmount = extract_json('Data.Summary.PreferentialAmount', res)
        ReturnPointAmount = extract_json('Data.Summary.ReturnPointAmount', res)
        CommissionAmount = extract_json('Data.Summary.CommissionAmount', res)
        TotalWinLossAmount = extract_json('Data.Summary.TotalWinLossAmount', res)
        # 處理金額格式
        amount_list = convert_amount_format(
            BalanceAmount, BonusAmount, WinLossAmount, PreferentialAmount, TotalWinLossAmount)
        BalanceAmount, BonusAmount, WinLossAmount, PreferentialAmount, TotalWinLossAmount = \
            amount_list[0], amount_list[1], amount_list[2], amount_list[3], amount_list[4]
        return [DepositCnt, DepositAmount, Fee, AdministrationFee, WithdrawalAmount, DepWithAmount, RmDeAmountnt,
                RmAddAmount, BalanceAmount, BetMemberCnt, BetAmount, ValidBetAmount, BonusAmount, WinLossAmount,
                PreferentialAmount, ReturnPointAmount, CommissionAmount, TotalWinLossAmount]

    # 全站管理/ 会员等级管理 / VIP等级设定
    def api_Member_Levels(self):
        url, method = get_api_info("AdminTool", "Member", "Level")
        res = HTTPClient(url, method, self.headers, self.cookies).send()
        return res
    #  MemberLevelId: 0(VIP 0)/11(VIP )/ 12(VIP 2)/ 13(VIP 3)/ 14(VIP 4)/ 15(VIP 5)/ 16(VIP 6)/ 17(VIP 7)/ 18(VIP 8)/ 19(VIP 9)/ 20(VIP 10)
    def get_MemberLevelId(self, MemberLevelId=None):
        if MemberLevelId in [0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
            level = {0: 0, 11: 1, 12: 2, 13: 3, 14: 4, 15: 5, 16: 6,
                     17: 7, 18: 8, 19: 9, 20: 10}
            LevelId = level[MemberLevelId]
        return LevelId

    def get_Member_Levels(self, MemberLevelId=None):
        res = self.api_Member_Levels().text
        vip_level = self.get_MemberLevelId(MemberLevelId)
        count = vip_level
        MaxWithdrawAmount = extract_json('Data[' + str(count) + '].MaxWithdrawAmount', res)
        WithdrawTimes = str(extract_json('Data[' + str(count) + '].WithdrawTimes', res))
        if Project in ['vt']:
            Member_Levels = [MaxWithdrawAmount]
        else:
            Member_Levels = [MaxWithdrawAmount, WithdrawTimes]
        return Member_Levels

    def get_More_Member_Levels(self, vip_level=None):
        res = self.api_Member_Levels().text
        count = vip_level
        num = 0
        MemberLevelName  = extract_json('Data[' + str(count) + '].MemberLevelName', res)
        CumulativeDepositAmount = extract_json('Data[' + str(count) + '].CumulativeDepositAmount', res)
        CumulativeValidBetAmount = extract_json('Data[' + str(count) + '].CumulativeValidBetAmount', res)
        MinWithdrawAmount = extract_json('Data[' + str(count) + '].MinWithdrawAmount', res)
        # WithdrawFee = str(extract_json('Data[' + str(count) + '].WithdrawFee', res))
        WithdrawFee = extract_json('Data[' + str(count) + '].WithdrawFee', res)
        MaxWithdrawAmount = extract_json('Data[' + str(count) + '].MaxWithdrawAmount', res)
        # WithdrawTimes = str(extract_json('Data[' + str(count) + '].WithdrawTimes', res))
        WithdrawTimes = extract_json('Data[' + str(count) + '].WithdrawTimes', res)
        More_Member_Levels_data = [MemberLevelName, CumulativeDepositAmount, CumulativeValidBetAmount, MinWithdrawAmount,
                              WithdrawFee, MaxWithdrawAmount, WithdrawTimes]

        More_Member_Levels = []
        if Project == 'vt' and vip_level == 0:
            More_Member_Levels = [MinWithdrawAmount, WithdrawFee, MaxWithdrawAmount]
        elif vip_level == 0:
            More_Member_Levels = [MinWithdrawAmount, WithdrawFee, MaxWithdrawAmount, WithdrawTimes]
        else:
            for data in More_Member_Levels_data:
                if More_Member_Levels_data[num] != 0:
                    More_Member_Levels.append(data)
                num += 1

        return More_Member_Levels

    # 全站管理/ 会员等级管理 / VIP等级设定
    def api_Member_Level_Bonus(self):
        url, method = get_api_info("AdminTool", "Member", "LevelBonus")
        res = HTTPClient(url, method, self.headers, self.cookies).send()
        return res

    def get_Member_Level_Bonus(self, MemberLevelId=None):
        res = self.api_Member_Level_Bonus().text
        vip_level = AdminTool().get_MemberLevelId(MemberLevelId)
        PromoBonus = extract_json('Data[' + str(vip_level) + '].PromoBonus', res)
        BirthdayBonus = extract_json('Data[' + str(vip_level) + '].BirthdayBonus', res)
        MonthlyBonus = extract_json('Data[' + str(vip_level) + '].MonthlyBonus', res)
        ActiveBonus = extract_json('Data[' + str(vip_level) + '].ActiveBonus', res)
        TurnoverTimes = extract_json('Data[' + str(vip_level) + '].TurnoverTimes', res)
        if Project == 'vt' and MemberLevelId == '0':
            Member_Level_Bonus = [MonthlyBonus]
        elif BirthdayBonus > 0:
            if BirthdayBonus > 0 and ActiveBonus > 0 and TurnoverTimes > 0: #5
                Member_Level_Bonus = [PromoBonus, BirthdayBonus, MonthlyBonus, ActiveBonus, TurnoverTimes]
        elif BirthdayBonus == 0:
            if BirthdayBonus == 0 and ActiveBonus > 0 and TurnoverTimes > 0: #4
                Member_Level_Bonus = [PromoBonus, MonthlyBonus, ActiveBonus, TurnoverTimes]
            elif BirthdayBonus == 0 and ActiveBonus == 0 and TurnoverTimes == 0: #2
                Member_Level_Bonus = [PromoBonus, MonthlyBonus]

        return Member_Level_Bonus

    #  vip_level: 0(VIP 0)/1(VIP )/ 2(VIP 2)/ 3(VIP 3)/ 4(VIP 4)/ 5(VIP 5)/ 6(VIP 6)/ 7(VIP 7)/ 8(VIP 8)/ 9(VIP 9)/ 10(VIP 10)
    def get_More_Member_Level_Bonus_EDIT(self, vip_level=None):
        res = self.api_Member_Level_Bonus().text
        count = vip_level
        num = 0
        PromoBonus = extract_json('Data[' + str(count) + '].PromoBonus', res)
        BirthdayBonus = extract_json('Data[' + str(count) + '].BirthdayBonus', res)
        MonthlyBonus = extract_json('Data[' + str(count) + '].MonthlyBonus', res)
        ActiveBonus  = extract_json('Data[' + str(count) + '].ActiveBonus', res)
        ActiveBonusFrequency = extract_json('Data[' + str(count) + '].ActiveBonusFrequency', res)
        if ActiveBonusFrequency > 0:
            if Project == 'vt':
                if ActiveBonusFrequency in [1, 2]:
                    data = {1: '1tuần1lần', 2: 'Mỗitháng1lần'}
            elif ActiveBonusFrequency in [1, 2]:
                data = {1: '一周一次', 2: '每月一次'}
            ActiveBonusFrequency = data[ActiveBonusFrequency]
        TurnoverTimes = extract_json('Data[' + str(count) + '].TurnoverTimes', res)
        Level_Bonu_data = [PromoBonus, BirthdayBonus, MonthlyBonus, ActiveBonus, ActiveBonusFrequency, TurnoverTimes]
        nums = len(Level_Bonu_data)

        More_Member_Level_Bonus = []
        if Project == 'vt' and vip_level == 0:
            More_Member_Level_Bonus = [MonthlyBonus]
        else:
            for data in Level_Bonu_data:
                if Level_Bonu_data[num] != 0:
                    More_Member_Level_Bonus.append(data)
                num += 1

        return More_Member_Level_Bonus

    #  MemberLevelId: 0(VIP 0)/11(VIP )/ 12(VIP 2)/ 13(VIP 3)/ 14(VIP 4)/ 15(VIP 5)/ 16(VIP 6)/ 17(VIP 7)/ 18(VIP 8)/ 19(VIP 9)/ 20(VIP 10)
    def get_Member_vip_interests_info(self, MemberLevelId=None):
        Member_Levels = Assertion.transfer_list_format(self.get_Member_Levels(MemberLevelId))
        Member_Level_Bonus = Assertion.transfer_list_format(self.get_Member_Level_Bonus(MemberLevelId))
        data_list = len(Member_Level_Bonus)
        if MemberLevelId == 0:
            if Project in ['vt']:
                level_info = Member_Level_Bonus + Member_Levels
            else:
                level_info = Member_Levels
        else:
            if data_list == 5:
                level_info = Member_Level_Bonus[:3] + Member_Levels + Member_Level_Bonus[3:]
            elif data_list == 4:
                level_info = Member_Level_Bonus[:2] + Member_Levels + Member_Level_Bonus[2:]
            elif data_list == 2:
                level_info = Member_Level_Bonus + Member_Levels

        row = len(level_info)
        num = 0
        vip_interests_info = []

        while row > num:
            try:
                data = level_info[num].replace('.00', "")
                vip_interests_info.append(data)
                num += 1
            except Exception as e:
                print(e)

        return vip_interests_info

    #  vip_level: 0(VIP 0)/1(VIP )/ 2(VIP 2)/ 3(VIP 3)/ 4(VIP 4)/ 5(VIP 5)/ 6(VIP 6)/ 7(VIP 7)/ 8(VIP 8)/ 9(VIP 9)/ 10(VIP 10)
    def get_more_Member_vip_interests_info(self, vip_level=None):
        More_Member_Levels = Assertion.transfer_list_format(self.get_More_Member_Levels(vip_level))
        # More_Member_Level_Bonus = Assertion.transfer_list_format(self.get_More_Member_Level_Bonus(vip_level))
        More_Member_Level_Bonus = Assertion.transfer_list_format(self.get_More_Member_Level_Bonus_EDIT(vip_level))
        data_list = len(More_Member_Level_Bonus)
        print('data_list')
        print(data_list)
        if data_list == 6:
            if vip_level == 0:
                if Project == 'vt':
                    level_info = More_Member_Levels[:2] + More_Member_Level_Bonus + More_Member_Levels[2:]
                else:
                    level_info = More_Member_Levels
            else:
                level_info = More_Member_Levels[:5] + More_Member_Level_Bonus[:3] + More_Member_Levels[5:] + More_Member_Level_Bonus[3:]
        elif data_list == 5:
            if vip_level == 0:
                if Project == 'vt':
                    level_info = More_Member_Levels[:2] + More_Member_Level_Bonus + More_Member_Levels[2:]
                else:
                    level_info = More_Member_Levels
            else:
                level_info = More_Member_Levels[:4] + More_Member_Level_Bonus[:2] + More_Member_Levels[4:] + More_Member_Level_Bonus[2:]
        elif data_list == 4:
            if vip_level == 0:
                if Project == 'vt':
                    level_info = More_Member_Levels[:2] + More_Member_Level_Bonus + More_Member_Levels[2:]
                else:
                    level_info = More_Member_Levels
            else:
                level_info = More_Member_Levels[:4] + More_Member_Level_Bonus[:2] + More_Member_Levels[4:] + More_Member_Level_Bonus[2:]
        elif data_list == 2 and More_Member_Levels[0] == 'VIP3':
            level_info = More_Member_Levels[:4] + More_Member_Level_Bonus[:2] + More_Member_Levels[4:] + More_Member_Level_Bonus[2:]

        else:
            if vip_level == 0:
                if Project == 'vt':
                    level_info = More_Member_Levels[:2] + More_Member_Level_Bonus + More_Member_Levels[2:]
                else:
                    level_info = More_Member_Levels[:2] + More_Member_Level_Bonus + More_Member_Levels[2:]
            else:
                if Project == 'vt':
                    level_info = More_Member_Levels[:5] + More_Member_Level_Bonus + More_Member_Levels[5:]
                else:
                    level_info = More_Member_Levels[:5] + More_Member_Level_Bonus[:2] + More_Member_Levels[5:] + More_Member_Level_Bonus[2:]

        row = len(level_info)
        num = 0
        vip_interests_info = []

        while row > num:
            try:
                data = level_info[num].replace('.00', "").replace('.0', "")
                vip_interests_info.append(data)
                num += 1
            except Exception as e:
                print(e)

        return vip_interests_info

    # 全站管理/ 会员等级管理 / VIP返点设定
    def api_Member_Level_LevelReturn(self):
        url, method = get_api_info("AdminTool", "Member", "LevelReturn")
        res = HTTPClient(url, method, self.headers, self.cookies).send()
        return res

    def get_Member_Level_LevelReturn(self, vip_level=None):
        res = self.api_Member_Level_LevelReturn().text
        count = vip_level
        if Project == 'vt':
            MemberLevelName = extract_json('Data[' + str(count) + '].MemberLevelName', res)
            AG_Baccarat = extract_json('Data[' + str(count) + '].\"AG Baccarat:2:2"', res)
            AG_Slots = extract_json('Data[' + str(count) + '].\"AG Slots:2:6"', res)
            AG_Fishing = extract_json('Data[' + str(count) + '].\"AG bắn cá:2:18"', res)
            IM_Sport = extract_json('Data[' + str(count) + '].\"IM thể thao:4:4"', res)
            IM_e_Sports = extract_json('Data[' + str(count) + '].\"IM e-Sports:4:5"', res)
            Saba_Sport = extract_json('Data[' + str(count) + '].\"Saba - Thể thao thông thường:5:7"', res)
            Saba_Balan = extract_json('Data[' + str(count) + '].\"Saba - Giải đấu Balan:5:8"', res)
            Saba_vr_Sport = extract_json('Data[' + str(count) + '].\"Saba - Thể thao ảo:5:9"', res)
            SABA_lottery = extract_json('Data[' + str(count) + '].\"Saba - Xổ số Happy:5:12"', res)
            BG_football = extract_json('Data[' + str(count) + '].\"BG bóng đá:6:10"', res)
            BG_basketball = extract_json('Data[' + str(count) + '].\"BG bóng rổ:6:11"', res)
            BG_Casino = extract_json('Data[' + str(count) + '].\"BG Casino:6:13"', res)
            BG_Fishing = extract_json('Data[' + str(count) + '].\"BG đại sư bắn cá:6:14"', res)
            BG_xiyo_Fishing = extract_json('Data[' + str(count) + '].\"BG xiyo bắn cá:6:15"', res)
            MG_Slots = extract_json('Data[' + str(count) + '].\"MG Slots:10:21"', res)
            Leihuo_e_Sports = extract_json('Data[' + str(count) + '].\"Leihuo e-Sports:18:29"', res)
            DG_Casino = extract_json('Data[' + str(count) + '].\"DG Casino:19:30"', res)
            WM_Casino = extract_json('Data[' + str(count) + '].\"WM Casino:20:31"', res)
            Sexy_Casino = extract_json('Data[' + str(count) + '].\"Sexy Casino:21:32"', res)
            SV388_CockFight = extract_json('Data[' + str(count) + '].\"SV388 Đá gà:21:46"', res)
            CMD_Sport = extract_json('Data[' + str(count) + '].\"CMD thể thao:22:33"', res)
            SBO_Casino = extract_json('Data[' + str(count) + '].\"SBO Casino:23:34"', res)
            SBO_Sport = extract_json('Data[' + str(count) + '].\"SBO thể thao:23:35"', res)
            SBO_Slots = extract_json('Data[' + str(count) + '].\"SBO Slots:23:36"', res)
            CQ9_SLOTS = extract_json('Data[' + str(count) + '].\"CQ9 SLOTS:24:37"', res)
            CQ9_Fishing = extract_json('Data[' + str(count) + '].\"CQ9 Bắn cá:24:41"', res)
            CG_SLOTS = extract_json('Data[' + str(count) + '].\"CG SLOTS:25:38"', res)
            V8_Poker = extract_json('Data[' + str(count) + '].\"V8 Bài:26:39"', res)
            BBIN_Casino = extract_json('Data[' + str(count) + '].\"BBIN Casino:27:40"', res)
            OK368_lottery = extract_json('Data[' + str(count) + '].\"OK368 Xổ số:28:42"', res)
            JDB_SLOTS = extract_json('Data[' + str(count) + '].\"JDB SLOTS:29:43"', res)
            PG_SLOTS = extract_json('Data[' + str(count) + '].\"PG SLOTS:32:47"', res)
            VR_lottery = extract_json('Data[' + str(count) + '].\"VR XỔ SỐ:33:48"', res)
            FC_SLOTS = extract_json('Data[' + str(count) + '].\"FC SLOTS:34:49"', res)
            JL_SLOTS = extract_json('Data[' + str(count) + '].\"JL SLOTS:35:50"', res)
            TCG_lottery = extract_json('Data[' + str(count) + '].\"TCG XỔ SỐ:36:51"', res)

            thirdParty = None
            if vip_level == 0 :
                thirdParty = [AG_Baccarat, AG_Fishing, AG_Slots, IM_Sport, IM_e_Sports,
                              Saba_Sport, Saba_Balan, Saba_vr_Sport, SABA_lottery,
                              BG_football, BG_basketball, BG_Casino, BG_Fishing, BG_xiyo_Fishing, MG_Slots,
                              Leihuo_e_Sports, DG_Casino, WM_Casino, Sexy_Casino, SV388_CockFight,
                              CMD_Sport, SBO_Casino, SBO_Sport, SBO_Slots, CQ9_SLOTS, CQ9_Fishing, CG_SLOTS,
                              CG_SLOTS, V8_Poker, BBIN_Casino, OK368_lottery, JDB_SLOTS, PG_SLOTS, VR_lottery, FC_SLOTS,
                              JL_SLOTS, TCG_lottery]
            else:
                thirdParty = [MemberLevelName, AG_Baccarat, AG_Fishing, AG_Slots, IM_Sport, IM_e_Sports,
                          Saba_Sport, Saba_Balan, Saba_vr_Sport, SABA_lottery, BG_football, BG_basketball, BG_Casino, BG_Fishing, BG_xiyo_Fishing, MG_Slots, Leihuo_e_Sports,DG_Casino, WM_Casino, Sexy_Casino, SV388_CockFight,
                          CMD_Sport, SBO_Casino, SBO_Sport, SBO_Slots, CQ9_SLOTS, CQ9_Fishing, CG_SLOTS, CG_SLOTS, V8_Poker, BBIN_Casino, OK368_lottery, JDB_SLOTS, PG_SLOTS, VR_lottery, FC_SLOTS, JL_SLOTS, TCG_lottery]

        else:
            MemberLevelName = extract_json('Data[' + str(count) + '].MemberLevelName', res)
            AG_Casino = extract_json('Data[' + str(count) + '].\"AG真人百家乐:2:2"', res)
            AG_Slot = extract_json('Data[' + str(count) + '].\"AG电子游戏:2:6"', res)
            AG_Fishing = extract_json('Data[' + str(count) + '].\"AG捕鱼:2:18"', res)
            LEG_Poker = extract_json('Data[' + str(count) + '].\"乐游棋牌:3:3"', res)
            IM_Sport = extract_json('Data[' + str(count) + '].\"IM体育:4:4"', res)
            IM_e_Sports = extract_json('Data[' + str(count) + '].\"IM电竞:4:5"', res)
            IM_Poker = extract_json('Data[' + str(count) + '].\"IM棋牌:12:23"', res)
            SABA_Sport = extract_json('Data[' + str(count) + '].\"沙巴-一般体育:5:7"', res)
            SABA_Balan = extract_json('Data[' + str(count) + '].\"沙巴-百练赛:5:8"', res)
            SABA_vr_Sport = extract_json('Data[' + str(count) + '].\"沙巴-虚拟运动:5:9"', res)
            SABA_lottery = extract_json('Data[' + str(count) + '].\"沙巴-快乐彩:5:12"', res)
            BG_football = extract_json('Data[' + str(count) + '].\"BG竞足:6:10"', res)
            BG_basketball = extract_json('Data[' + str(count) + '].\"BG竞篮:6:11"', res)
            BG_Casino = extract_json('Data[' + str(count) + '].\"BG真人:6:13"', res)
            BG_Fishing_Master = extract_json('Data[' + str(count) + '].\"BG捕鱼大师:6:14"', res)
            BG_XIYO_Fishing = extract_json('Data[' + str(count) + '].\"BG西游捕鱼:6:15"', res)
            BG_Slot = extract_json('Data[' + str(count) + '].\"BG电子:6:16"', res)
            BL_Poker = extract_json('Data[' + str(count) + '].\"博乐棋牌:7:17"', res)
            MG_Slot = extract_json('Data[' + str(count) + '].\"MG电子:10:21"', res)
            KY_Poker = extract_json('Data[' + str(count) + '].\"开元棋牌:9:20"', res)
            TF_e_Sports = extract_json('Data[' + str(count) + '].\"雷火电竞:18:29"', res)
            DG_Casino = extract_json('Data[' + str(count) + '].\"DG真人:19:30"', res)
            CMD_Sport = extract_json('Data[' + str(count) + '].\"CMD体育:22:33"', res)
            OB_Sport = extract_json('Data[' + str(count) + '].\"OB体育:30:44"', res)
            OB_Casino = extract_json('Data[' + str(count) + '].\"OB真人:31:45"', res)
            VR_lottery = extract_json('Data[' + str(count) + '].\"VR彩票:33:48"', res)

            if vip_level == 0:
                thirdParty = [AG_Casino, AG_Slot, AG_Fishing, LEG_Poker, IM_Sport, IM_e_Sports, IM_Poker, SABA_Sport, SABA_Balan, SABA_vr_Sport, SABA_lottery, BG_football, BG_basketball, BG_Casino, BG_Fishing_Master, BG_XIYO_Fishing, BG_Slot, BL_Poker, MG_Slot, KY_Poker, TF_e_Sports,
                              DG_Casino, CMD_Sport, OB_Sport, OB_Casino, VR_lottery]
            else:
                thirdParty = [MemberLevelName, AG_Casino, AG_Slot, AG_Fishing, LEG_Poker, IM_Sport, IM_e_Sports, IM_Poker, SABA_Sport, SABA_Balan, SABA_vr_Sport, SABA_lottery, BG_football, BG_basketball, BG_Casino, BG_Fishing_Master, BG_XIYO_Fishing, BG_Slot, BL_Poker, MG_Slot, KY_Poker, TF_e_Sports,
                              DG_Casino, CMD_Sport, OB_Sport, OB_Casino, VR_lottery]

        thirdParty = Assertion.transfer_list_format(thirdParty)
        return thirdParty

    def thirdParty_data(self, num=None):
        if num in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                     27, 28, 29, 30, 31, 32, 33, 34]:
            if Project == 'vt':
                data = {0: '\"AG Casino:2:2"', 1: '\"AG Slots:2:6"', 2: '\"AG Bắn Cá:2:18"', 3: '\"IM Thể Thao:4:4"',
                        4: '\"IM E-Sports:4:5"', 5: '\"SABA Thể Thao:5:7"',
                        6: '\"SABA-Giải Đấu Balan:5:8"', 7: '\"SABA-Thể Thao Ảo:5:9"',
                        8: '\"SABA-Xổ Số Happy:5:12"', 9: '\"BG Bóng Đá:6:10"', 10: '\"BG Bóng Rổ:6:11"',
                        11: '\"BG Casino:6:13"', 12: '\"BG Bóng Đá:6:10"',
                        13: '\"BG Bóng Rổ:6:11"', 14: '\"BG Casino:6:13"', 15: '\"BG Đại Sư Bắn Cá:6:14"',
                        16: '\"BG Slots:6:16"', 17: '\"MG Slots:10:21"',
                        18: '\"Leihuo E-Sports:18:29"', 19: '\"DG Casino:19:30"',
                        20: '\"WM Casino:20:31"', 21: '\"Sexy Casino:21:32"', 22: '\"SV388 Đá gà:21:46"',
                        23: '\"CMD Thể Thao:22:33"', 24: '\"SBO Casino:23:34"', 25: '\"SBO Thể Thao:23:35"',
                        26: '\"SBO Slots:23:36"', 27: '\"CQ9 Slots:24:37"',
                        28: '\"CQ9 Bắn Cá:24:41"', 29: '\"CG Slots:25:38"', 30: '\"V8 Game Bài:26:39"',
                        31: '\"BBIN Casino:27:40"', 32: '\"OK368 Xổ Số:28:42"', 33: '\"JDB Slots:29:43"',
                        34: '\"PG Slots:32:47"', 35: '\"VR Xổ Số:33:48"', 36: '\"FC Slots:34:49"', 37: '\"JL Slots:35:50"', 38: '\"TCG Xổ Số:36:51"'}

            else:
                data = {0: '\"AG真人百家乐:2:2"', 1: '\"AG电子:2:6"', 2: '\"AG捕鱼:2:18"', 3: '\"乐游棋牌:3:3"',
                        4: '\"IM体育:4:4"', 5: '\"IM电竞:4:5"', 6: '\"IM棋牌:12:23"', 7: '\"沙巴体育:5:7"', 8: '\"沙巴-百练赛:5:8"',
                        9: '\"沙巴-虚拟运动:5:9"', 10: '\"沙巴-快乐彩:5:12"', 11: '\"BG竞足:6:10"', 12: '\"BG竞篮:6:11"',
                        13: '\"BG真人百家乐:6:13"', 14: '\"BG捕鱼大师:6:14"', 15: '\"BG西游捕鱼:6:15"', 16: '\"BG电子:6:16"',
                        17: '\"博乐棋牌:7:17"', 18: '\"MG电子:10:21"', 19: '\"开元棋牌:9:20"', 20: '\"雷火电竞:18:29"', 21: '\"DG真人百家乐:19:30"',
                        22: '\"CMD体育:22:33"', 23: '\"OB体育:30:44"', 24: '\"OB真人百家乐:31:45"', 25: '\"VR彩票:33:48"', 26: '\"OB彩票:37:52"', 27: '\"OB电竞:38:53"', 28: '\"OB电子:39:54"', 29: '\"OB捕鱼:40:55"'}
            thirdParty_list = data[num]

        return thirdParty_list

    #  vip_level: 0(VIP 0)/1(VIP )/ 2(VIP 2)/ 3(VIP 3)/ 4(VIP 4)/ 5(VIP 5)/ 6(VIP 6)/ 7(VIP 7)/ 8(VIP 8)/ 9(VIP 9)/ 10(VIP 10)
    def get_vip_LevelReturn_info(self, vip_level=None):
        res = self.api_Member_Level_LevelReturn().text
        num = 0
        if Project in ['vt']:
            thirdParty_data_list = 39
        else:
            thirdParty_data_list = 30
        print('vip_level')
        print(vip_level)
        MemberLevelName = extract_json('Data[' + str(vip_level) + '].MemberLevelName', res)
        thirdParty_data = []

        while num < thirdParty_data_list:
            thirdParty_list = self.thirdParty_data(num)
            thirdParty = extract_json('Data[' + str(vip_level) + '].' + thirdParty_list, res)
            thirdParty_data.append(thirdParty)
            num += 1

        if vip_level == 0:
            thirdParty = Assertion.transfer_list_format_for_h5_vip(thirdParty_data)
        else:
            thirdParty = Assertion.transfer_list_format_for_h5_vip([MemberLevelName] + thirdParty_data)

        return thirdParty


if __name__ == '__main__':
    pass
