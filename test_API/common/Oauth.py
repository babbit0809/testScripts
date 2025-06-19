from config.SetAPIConfig import get_api_info, get_api_AuthSetting
from config.RequestData import get_payload_Oauth
from utils.Request import HTTPClient
from utils.DataExtractor import extract_json


def api_Authorization_Token(account, password):
    url, method = get_api_info("Oauth", "Authorization", "Token")
    data = get_payload_Oauth("Authorization", "Token")
    data.update({"username": account, "password": password})
    res = HTTPClient(url, method, headers=get_api_AuthSetting()).send(data=data, dtype="str")
    return res


def get_access_token(account, password):
    res = api_Authorization_Token(account, password).text
    access_token = extract_json('access_token', res)
    return access_token


if __name__ == '__main__':
    pass
