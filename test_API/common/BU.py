from config.SetAPIConfig import get_api_info, get_api_LanguageSetting
from config.RequestData import get_payload_BU
from utils.Request import HTTPClient


class BU(object):
    def __init__(self, token):
        self.headers = {'Content-Type': 'application/json',
                        'Authorization': "Bearer " + token,
                        'Language': get_api_LanguageSetting()}

    # 新增投注訂單(不同lotteryCode需分開投注)
    def api_Betting_bulk(self, *BettingList):
        url, method = get_api_info("BU", "Betting", "bulk")
        if not BettingList:
            data = get_payload_BU("Betting", "bulk")
        else:
            data = list(*BettingList)
        res = HTTPClient(url, method, self.headers).send(data=data)
        return res

    # 新增投注訂單並立即開獎(刮刮彩only, lotteryCode=11)
    def api_Betting_instant(self, *BettingList):
        url, method = get_api_info("BU", "Betting", "instant")
        if not BettingList:
            data = get_payload_BU("Betting", "instant")
        else:
            data = list(*BettingList)
        res = HTTPClient(url, method, self.headers).send(data=data)
        return res

    # 新增追號訂單
    def api_Planning_create(self, *TraceData, traceMode=2):  # 1(智能追號)/2(翻倍追號)
        url, method = get_api_info("BU", "Planning", "create")
        if not TraceData:
            data = get_payload_BU("Planning", "create")
        else:
            data = TraceData[0]
        data.update({"traceMode": traceMode})
        res = HTTPClient(url, method, self.headers).send(data=data)
        return res


if __name__ == '__main__':
    pass
