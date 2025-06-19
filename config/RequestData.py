from datetime import datetime, timedelta
from random import choice
from config.SetAPIConfig import Env, Project
from utils.Auth import get_2FA
from utils.DataLoader import JsonLoader
from utils.Generator import random_card_number

# For combine test data
test_date = "test" + datetime.now().strftime("%Y%m%d")[2:]


def time_interval(delta=0):  # TODO: 多語系時區轉換(還差Portal跟Fin)
    timeZone = {'sta': "+08:00", 'vt': "+07:00"}
    now = datetime.now()
    interval = now + timedelta(days=delta)
    start_date = interval.strftime("%Y/%m/%d") + ' 00:00:00' + timeZone[Project]
    end_date = interval.strftime("%Y/%m/%d") + ' 23:59:59' + timeZone[Project]
    return start_date, end_date

# 獲取AT/Fin登入資訊用
def get_login_info(domain_name):
    mappingTable = {'AdminTool': "account_AT", 'Financial': "account_Fin"}
    account = JsonLoader('CMDArgs').get_cmd_args(mappingTable[domain_name])
    password = JsonLoader('APIConfig').get_loc(domain_name + "_" + Env + "_" + Project, account, "password")
    key = JsonLoader('APIConfig').get_loc(domain_name + "_" + Env + "_" + Project, account, "key")
    return account, password, key


# 獲取Fin的出款人員登入資訊用
def get_payoutInfo():
    mappingTable = {'sta': "clfoutput", 'vt': "vtoutput"}
    account = mappingTable[Project]
    password = JsonLoader('APIConfig').get_loc("Financial_" + Env + "_" + Project, account, "password")
    key = JsonLoader('APIConfig').get_loc("Financial_" + Env + "_" + Project, account, "key")
    userId = JsonLoader('APIConfig').get_loc("Financial_" + Env + "_" + Project, account, "userId")
    accountId = JsonLoader('APIConfig').get_loc("Financial_" + Env + "_" + Project, account, "accountId")
    return account, password, key, userId, accountId


# Following Functions for Request Body
def get_payload_Oauth(feature_name, api_name):
    agentCode = {'sta': "STA01", 'vt': "VT999"}
    data = None
    if feature_name in 'Authorization':
        if api_name in 'Token':
            data = {"grant_type": "password",
                    "scope": "BasicInfo",
                    "agentcode": agentCode[Project]}
    return data


def get_payload_BU(feature_name, api_name):
    data = None
    if feature_name in 'Betting':
        if api_name in 'bulk':
            # 測試用投注內容, 每站台依盤面挑幾組隨機選擇
            BettingList = {
                'sta': [
                    # 泰國60秒/官方/常規-五星玩法/五星直選
                    {"lotteryCode": 68, "type": "normalgame", "betRuleId": 68010101, "betContent": "0,1,2,3,02468",
                     "multiple": 1, "betUnitPrice": 2, "roomId": 1, "sortOrder": 1, "chipSettingId": 1},
                    # 台灣11選5/官方/常規-任二/標準
                    {"lotteryCode": 72, "type": "normalgame", "betRuleId": 72010101, "betContent": "01 11",
                     "multiple": 1, "betUnitPrice": 2, "roomId": 1, "sortOrder": 1, "chipSettingId": 1},
                    # 歡樂快3/官方/常規-和值
                    {"lotteryCode": 47, "type": "normalgame", "betRuleId": 47010101, "betContent": "b",
                     "multiple": 1, "betUnitPrice": 2, "roomId": 1, "sortOrder": 1, "chipSettingId": 1},
                    # F3賽車/官方/常規-猜冠軍
                    {"lotteryCode": 53, "type": "normalgame", "betRuleId": 53210101, "betContent": "01",
                     "multiple": 1, "betUnitPrice": 2, "roomId": 1, "sortOrder": 1, "chipSettingId": 1},
                    # 極速六合彩/官方/常規-特碼
                    {"lotteryCode": 49, "type": "normalgame", "betRuleId": 49010101, "betContent": "01",
                     "multiple": 1, "betUnitPrice": 2, "roomId": 1, "sortOrder": 1, "chipSettingId": 1},
                    # 極速3D/官方/常規-三星直選/標準
                    {"lotteryCode": 45, "type": "normalgame", "betRuleId": 45010101, "betContent": "0,1,2",
                     "multiple": 1, "betUnitPrice": 2, "roomId": 1, "sortOrder": 1, "chipSettingId": 1},
                    # 幸運28/官方/常規-兩面盤
                    {"lotteryCode": 40, "type": "normalgame", "betRuleId": 40010101, "betContent": "b",
                     "multiple": 1, "betUnitPrice": 2, "roomId": 1, "sortOrder": 1, "chipSettingId": 1},
                    # 骰寶/官方/常規-骰寶
                    {"lotteryCode": 35, "betRuleId": 35010101, "betContent": "b", "multiple": 1, "betUnitPrice": 2,
                     "roomId": 1, "sortOrder": 1, "chipSettingId": 1}],
                'vt': [
                    # 泰國60秒/雙面/雙面-第一球~第五球/第一球
                    {"lotteryCode": 68, "type": "twoface", "betRuleId": 68190111, "betContent": "b", "multiple": 1,
                     "betUnitPrice": "2.00", "roomId": 1, "sortOrder": 1, "chipSettingId": 1},
                    # 台灣11選5/雙面/雙面-第一球~第五球/第一球
                    {"lotteryCode": 72, "type": "twoface", "betRuleId": 72200101, "betContent": "b", "multiple": 1,
                     "betUnitPrice": "2.00", "roomId": 1, "sortOrder": 1, "chipSettingId": 1},
                    # 歡樂快3/雙面/雙面-三軍
                    {"lotteryCode": 47, "type": "twoface", "betRuleId": 47110101, "betContent": "1", "multiple": 1,
                     "betUnitPrice": "2.00", "roomId": 1, "sortOrder": 1, "chipSettingId": 1},
                    # F3賽車/雙面/雙面-兩面/冠軍
                    {"lotteryCode": 53, "type": "twoface", "betRuleId": 53170101, "betContent": "b", "multiple": 1,
                     "betUnitPrice": "2.00", "roomId": 1, "sortOrder": 1, "chipSettingId": 1}]}
            data = [choice(BettingList[Project])]
        elif api_name in 'instant':
            # 測試用投注內容, 每站台依盤面挑幾組隨機選擇
            BettingList_instant = {
                'sta': [
                    # 刮刮彩/官方/常規-五星玩法/五星直選
                    {"lotteryCode": 11, "betRuleId": 11010101, "betContent": "0,1,2,3,02468", "multiple": 1,
                     "betUnitPrice": 2,
                     "roomId": 1, "sortOrder": 1, "chipSettingId": 1},
                    # 刮刮彩/官方/趣味-型態通選/五星
                    {"lotteryCode": 11, "betRuleId": 11100101, "betContent": "continuous5All", "multiple": 1,
                     "betUnitPrice": 2,
                     "roomId": 1, "sortOrder": 1, "chipSettingId": 1}],
                'vt': ["越南站僅支援雙面盤, 無刮刮彩"]}
            data = [choice(BettingList_instant[Project])]

    elif feature_name in 'Planning':
        if api_name in 'create':
            # 測試用追號內容, 每站台依盤面挑幾組隨機選擇 (PK10/六合彩/幸運28/骰寶及雙面盤系列無追號功能)
            TraceList = {
                'sta': [
                    # 泰國60秒/官方/常規-五星玩法/五星直選
                    {"betRuleId": 68010101, "lotteryCode": 68, "betContent": "0,1,2,3,4", "isStopAfterWin": True,
                     "betUnitPrice": 2,
                     "chipSettingId": 1, "roomId": 1,
                     "container": [{"sortOrder": 1, "multiple": 1}, {"sortOrder": 2, "multiple": 2}]},
                    # 台灣11選5/官方/常規-任二/標準
                    {"betRuleId": 72010101, "lotteryCode": 72, "betContent": "01 02", "isStopAfterWin": True,
                     "betUnitPrice": 2,
                     "chipSettingId": 1, "roomId": 1,
                     "container": [{"sortOrder": 1, "multiple": 1}, {"sortOrder": 2, "multiple": 2}]},
                    # 歡樂快3/官方/常規-和值
                    {"betRuleId": 47010101, "lotteryCode": 47, "betContent": "b", "isStopAfterWin": True,
                     "betUnitPrice": 2,
                     "chipSettingId": 1, "roomId": 1,
                     "container": [{"sortOrder": 1, "multiple": 1}, {"sortOrder": 2, "multiple": 2}]},
                    # 極速3D/官方/常規-三星直選/標準
                    {"betRuleId": 45010101, "lotteryCode": 45, "betContent": "0,1,2", "isStopAfterWin": True,
                     "betUnitPrice": 2,
                     "chipSettingId": 1, "roomId": 1,
                     "container": [{"sortOrder": 1, "multiple": 1}, {"sortOrder": 2, "multiple": 2}]}
                ],
                'vt': ["越南站僅支援雙面盤, 無追號功能"]}
            data = choice(TraceList[Project])
    return data


def get_payload_AT(feature_name, api_name, start_delta=0, end_delta=0, CryptoProtocolId=None, SortColumn=None):
    domain_name, data = 'AdminTool', None
    if feature_name in 'User':
        if api_name in 'Login':
            data = {"account": get_login_info(domain_name)[0],
                    "password": get_login_info(domain_name)[1],
                    "verifyCode": get_2FA(get_login_info(domain_name)[2])}

    elif feature_name in ['Member', 'Affiliate']:
        if api_name in 'Search':
            AffiliateLevelId = {'Member': 99, 'Affiliate': [1, 2, 3]}
            data = {"AffiliateLevelId": AffiliateLevelId[feature_name],
                    "MemberLevelId": None,
                    "RegisterFrom": None,
                    "AdvancedSearchConditionItem": 1,
                    "DisableMemberIsNotShown": False,
                    "CreateTimeStart": None,
                    "CreateTimeEnd": None,
                    "PreLoginTimeStart": None,
                    "PreLoginTimeEnd": None,
                    "PaginationInfo": {"PageNumber": 1, "PageSize": 25},
                    "SortInfo": {"SortColumn": "CreateTime", "SortBy": "Desc"}}

        elif api_name in 'Create':
            account_info = {'Member': "mb" + test_date, 'Affiliate': "ag" + test_date}
            AffiliateLevelId = {'Member': 99, 'Affiliate': 3}  # 99(一般會員)/3(代理), 2為VIP直屬/1為股東號, 但返點等級須跟著調整
            ReturnPoint = {'sta': 1960, 'vt': 1960}
            data = {"MemberName": account_info[feature_name],
                    "Password": account_info[feature_name],
                    "NickName": account_info[feature_name],
                    "Status": True,
                    "Remarks": "",
                    "ParentMemberName": "",
                    "MemberTypeId": 1,  # 預設為平台會員(2為內部會員)
                    "AffiliateLevelId": AffiliateLevelId[feature_name],
                    "IsSameLevel": True,
                    "ReturnPoint": ReturnPoint[Project],
                    "IsBetPlaceable": True,
                    "IsDepositable": True,
                    "IsWithdrawable": True,
                    "IsFundTransferable": True,
                    "GameTransferSetting": []}  # 帶空值讓預設啟用, 避免不同專案混淆, 維護不易

        elif api_name in 'IntegratedRecord':
            data = {"startDate": time_interval(delta=-31)[0],
                    "endDate": time_interval()[1],
                    "isSearchTeamMember": False}

        elif api_name in 'Log':
            data = {"startDate": time_interval(delta=-1)[0],
                    "endDate": time_interval()[1]}

        elif api_name in 'MemberBank_POST':
            data = {"AccountName": test_date,
                    "CardNumber": random_card_number(),
                    "IsDefault": True,
                    "Enabled": True}

        elif api_name in 'MemberBank_PATCH':
            data = {"MemberBankId": 850,
                    "MemberId": "9bb967bc-a3b7-4128-b8d9-70430d4fe514",
                    "AccountName": "小*",
                    "BankId": 18,
                    "MemberBankTypeId": 18,
                    "BankName": "中国工商银行",
                    "CardNumber": "2021091611434500",
                    "CreateOn": "",
                    "BindRemoteIp": "125.227.43.43",
                    "IsDefault": False,
                    "Enabled": False,
                    "ApproveState": None,
                    "BankBranchName": None}

        elif api_name in 'CryptoCurrencyWallet_POST':
            WalletAddress = {1: "0x" + test_date, 2: "T" + test_date, 3: "1" + test_date}
            data = {"AccountName": test_date,
                    "CryptoProtocolId": CryptoProtocolId,
                    "WalletNickName": test_date,
                    "WalletAddress": WalletAddress[CryptoProtocolId],
                    "IsDefault": True,
                    "Enabled": True}

        elif api_name in 'CryptoCurrencyWallet_PATCH':
            data = {"AccountName": None,
                    "CryptoCurrencyWalletId": 755,
                    "CryptoProtocolId": 1,
                    "Enabled": True,
                    "IsDefault": False,
                    "MemberId": "6efff222-c70b-472d-a885-302b8fe6261e",
                    "WalletAddress": "0x7766554",
                    "WalletNickName": "0x7766554"
                    }

        elif api_name in 'Dividends':
            data = {"AffiliateLevel": [1, 2, 3],
                    "BeginDate": time_interval(delta=-7)[0],
                    "EndDate": time_interval()[1],
                    "CommissionMode": 1,  # 預設為日分紅(2為彩票虧損傭金/3為第三方月分紅)
                    "GroupName": "",
                    "ShowMinus": True,
                    "Status": [1, 2, 3, 4, 5],
                    "paginationInfo": {"pageNumber": 1, "pageSize": 25},
                    "sortInfo": {"SortColumn": "CalcuEndDate", "SortBy": "Desc"}}

    elif feature_name in 'Deposit':
        if api_name in 'Deposit':
            data = {"Remarks": ""}

    elif feature_name in 'Turnover':
        if api_name in 'Search':
            data = {"IsAudited": False,
                    "paginationInfo": {"pageNumber": 1, "pageSize": 999},
                    "sortInfo": {"SortColumn": "ValidBetAuditID", "SortBy": "Desc"}}

    elif feature_name in 'Withdrawal':
        if api_name in 'Status':
            data = {"Remarks": "",
                    "Status": "",
                    "WithdrawalFee": ""}

    elif feature_name in 'QuickDepositSetting':
        if api_name in 'Search':
            data = {"Status": True,
                    "TypeId": 1,  # 預設為充值
                    "SubTypeId": 1,  # 預設為充值上分(常態)
                    "paginationInfo": {"pageNumber": 1, "pageSize": 25},
                    "sortInfo": {"SortColumn": "DepositFastSettingId", "SortBy": "Desc"}}

        elif api_name in 'QuickDepositSetting_POST':
            data = {"IsAudit": True,
                    "Name": test_date,
                    "TypeId": 1,  # 預設為充值
                    "SubTypeId": 1,  # 預設為充值上分(常態)
                    "TurnoverMultiple": 1  # 預設流水倍數為1
                    }

    elif feature_name in 'FundTransfer':
        if api_name in 'Manage':
            data = {"AdvancedSearchConditionItem": 4,
                    "IncludeInnerMember": False,
                    "StartDate": time_interval()[0],
                    "EndDate": time_interval()[1],
                    "Status": [1, 2, 3, 4, 5],
                    "TransferModes": [0, 1, 2, 3, 4, 5, 6],
                    "paginationInfo": {"pageNumber": 1, "pageSize": 25},
                    "sortInfo": {"SortColumn": "CreateTime", "SortBy": "Desc"}}

    elif feature_name in 'TransactionLog':
        if api_name in 'Search':
            data = {"Type": None,
                    "MemberLevelId": [],
                    "AdvancedSearchConditionItem": 1,
                    "IncludeInnerMember": False,
                    "StartTime": time_interval()[0],
                    "EndTime": time_interval()[1],
                    "paginationInfo": {"pageNumber": 1, "pageSize": 25},
                    "sortInfo": {"SortColumn": "TransactionNo", "SortBy": "Desc"}}

    elif feature_name in 'Bets':
        if api_name in ['Search', 'Export', 'History']:
            data = {"StartDate": time_interval(delta=start_delta)[0],
                    "EndDate": time_interval()[1],
                    "Source": None,
                    "LotteryCode": None,
                    "BetTypeId": [],
                    "IssueNumber": None,
                    "Status": None,
                    "AdvancedSearchConditionItem": 1,
                    "BetOrderNo": None,
                    "MemberLevelId": None,
                    "IncludeInnerMember": False,
                    "paginationInfo": {"pageNumber": 1, "pageSize": 25},
                    "sortInfo": {"SortColumn": "CreateTime", "SortBy": "Desc"}}

    elif feature_name in 'ThirdPartyBetLog':
        if api_name in 'Search':
            data = {"Source": None,
                    "Status": None,
                    "WinLoss": None,
                    "MemberLevelId": [],
                    "AdvancedSearchConditionItem": 1,
                    "IncludeInnerMember": False,
                    "StartTime": time_interval(delta=-31)[0],
                    "EndTime": time_interval()[1],
                    "paginationInfo": {"pageNumber": 1, "pageSize": 25},
                    "sortInfo": {"SortColumn": "BetTime", "SortBy": "Desc"}}

    elif feature_name in 'Lottery':
        if api_name in 'Search':
            data = {"paginationInfo": {"pageNumber": 1, "pageSize": 25},
                    "sortInfo": {"SortColumn": "ModifyTime", "SortBy": "Desc"}}

    elif feature_name in 'IssueNumber':
        if api_name in 'Search':
            data = {"RangeStartDate": time_interval(delta=start_delta)[0],
                    "RangeEndDate": time_interval(delta=end_delta)[1],
                    "RangeTypeBy": 4,  # 預設為開獎時間
                    "paginationInfo": {"pageNumber": 1, "pageSize": 25},
                    "sortInfo": {"SortColumn": SortColumn, "SortBy": "Desc"}}

        elif api_name in 'IssueNumber':  # 開獎時間預查為當天, 編輯則改為開獎時間: 當天+1, 開盤時間: 當天-1
            data = {"AnnounceTime": time_interval(delta=+1)[0],
                    "StartTime": time_interval(delta=-1)[0]}

    elif feature_name in ['BetSection', 'BetRule']:
        if api_name in 'Search':
            data = {"BetTypeId": None,
                    "BetSubTypeId": None,
                    "IsEnabled": None,
                    "paginationInfo": {"pageNumber": 1, "pageSize": 25},
                    "sortInfo": {"SortColumn": "ModifyTime", "SortBy": "Desc"}}

    elif feature_name in 'Activity':
        if api_name in 'Search':
            data = {"DateType": 1,  # 預設為更新時間
                    "StartTime": time_interval(delta=start_delta)[0],
                    "EndTime": time_interval()[1],
                    "Status": [],
                    "Type": None,
                    "paginationInfo": {"pageNumber": 1, "pageSize": 25},
                    "sortInfo": {"SortColumn": "ActivityStartTime", "SortBy": "Desc"}}

        elif api_name in 'Activity_POST':
            data = {"Subject": test_date,
                    "ActivityDisplayTargetIds": [0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
                    "ActivityDisplayStartDate": time_interval()[0],
                    "ActivityDisplayEndDate": time_interval(delta=31)[1],
                    "ActivityStartTime": time_interval()[0],
                    "ActivityEndTime": time_interval(delta=31)[1],
                    "IsShowOnTop": False}

    elif feature_name in 'OperatingReport':
        if api_name in 'Search_Affiliate':
            data = {"StartDate": time_interval()[0],
                    "EndDate": time_interval()[1],
                    "paginationInfo": {"pageNumber": 1, "pageSize": 25},
                    "sortInfo": {"SortColumn": "BetAmount", "SortBy": "Desc"}}

        elif api_name in 'Search_Member':
            data = {"StartDate": time_interval()[0],
                    "EndDate": time_interval()[1],
                    "paginationInfo": {"pageNumber": 1},
                    "sortInfo": {"SortColumn": "BetAmount", "SortBy": "Desc"}}

    elif feature_name in 'AgentReport':
        if api_name in 'Search':
            data = {"IncludeInnerMember": False,
                    "BeginDate": time_interval()[0],
                    "EndDate": time_interval()[1],
                    "paginationInfo": {"pageNumber": 1, "pageSize": 25},
                    "sortInfo": {"SortColumn": "", "SortBy": "Desc"}}

    elif feature_name in 'operation':
        if api_name in 'Search':
            data = {"ReleaseTo": False,
                    "ReleasedStartDate": time_interval()[0],
                    "ReleasedEndDate": time_interval()[1],
                    "paginationInfo": {"pageNumber": 1, "pageSize": 25},
                    "sortInfo": {"SortColumn":"PostBeginTime","SortBy":"Desc"}}


    return data


def get_payload_Fin(feature_name, api_name, role="admin"):
    domain_name, data = 'Financial', None
    if feature_name in 'Auth':
        if api_name in 'login':
            if role in 'admin':
                data = {"id": 0,
                        "account": get_login_info(domain_name)[0],
                        "password": get_login_info(domain_name)[1],
                        "token": get_2FA(get_login_info(domain_name)[2])}

            elif role in 'payout':
                data = {"id": 0,
                        "account": get_payoutInfo()[0],
                        "password": get_payoutInfo()[1],
                        "token": get_2FA(get_payoutInfo()[2])}

    elif feature_name in 'Deposit':
        if api_name in 'deposit':
            data = {"groupId": None,
                    "bankId": [],
                    "paymentType": [],
                    "sites": [1, 5, 6, 7, 8, 9],  # 1: 彩立方, 5: 星輝, 6: 彩2, 7: 收米, 8: 金莎
                    "status": [5],  # 客服申訴(AT至Fin的預設狀態)
                    "appendMessage": "",
                    "period": {"startTime": None,
                               "endTime": None},
                    "events": {"first": 0,
                               "rows": 50,
                               "sortField": "createTime",
                               "sortOrder": -1}}

    elif feature_name in 'Main':
        if api_name in ['loadPayout', 'loadPayout_cryptoCurrency']:
            data = {"groupId": None,
                    "userId": None,
                    "sitesID": None,
                    "status": [2],  # 未處理
                    "period": {"startTime": None,
                               "endTime": None},
                    "events": {"first": 0,
                               "rows": 50,
                               "sortField": "createTime",
                               "sortOrder": -1}}

    return data


if __name__ == '__main__':
    pass
