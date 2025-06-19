from utils.Request import HTTPClient
from config.SetAPIConfig import get_api_info, get_api_LanguageSetting, PlatformCode, Project
from utils.DataLoader import JsonLoader
from test_API.common import Oauth
from utils.DataExtractor import extract_json, extract_text
from utils import Assertion


AgentCode = {'sta': "STA01", 'vt': "VT999"}


def api_AllowAnonymous_check(platform, project):
    url, method = get_api_info("Version", "AllowAnonymous", "check")
    params = {"platform": PlatformCode[platform], "agentcode": AgentCode[project]}
    res = HTTPClient(url, method).send(params=params)
    return res

def get_latest_version(platform, project):
    res = api_AllowAnonymous_check(platform, project).text
    latest_version = extract_json('data.versions.latest', res)
    return latest_version

def api_User_Login():
    test_account = JsonLoader('TMP').get_tmp_data('API', 'account')
    test_password = JsonLoader('TMP').get_tmp_data('API', 'password')
    accessToken = Oauth.get_access_token(test_account, test_password)

    return accessToken


class Portal_info(object):
    def __init__(self):
        token = api_User_Login()
        self.headers = {'Content-Type': 'application/json',
                        'Authorization': 'Bearer ' + token,
                        'Language': get_api_LanguageSetting()}

    def api_members_me(self):
        url, method = get_api_info("Portal", "members", "me")
        res = HTTPClient(url, method, self.headers).send()
        return res

    def get_account_email(self):
        res = self.api_members_me().text
        email = extract_json('data.email', res)
        return email

    def api_members_me_vip(self):
        url, method = get_api_info("Portal", "members", "vip")
        res = HTTPClient(url, method, self.headers).send()
        return res

    def get_vip_levelId(self):
        res = self.api_members_me_vip().text
        levelId = extract_json('data.levelId', res)
        return levelId

    def vip_levelName(self):
        res = self.api_members_me_vip().text
        levelId = extract_json('data.levelId', res)
        levelName = None
        if levelId in [0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
            if Project in ['vt']:
                level = {0: 'Hội viên mới', 11: 'VIP 1', 12: 'VIP 2', 13: 'VIP 3', 14: 'VIP 4', 15: 'VIP 5', 16: 'VIP 6', 17: 'VIP 7', 18: 'VIP 8', 19: 'VIP 9', 20: 'VIP 10'}
            else:
                level = {0: '新进会员',  11: 'VIP 1', 12: 'VIP 2', 13: 'VIP 3', 14: 'VIP 4', 15: 'VIP 5', 16: 'VIP 6', 17: 'VIP 7', 18: 'VIP 8', 19: 'VIP 9', 20: 'VIP 10'}
            levelName = level[levelId]
        return levelName


if __name__ == '__main__':
    pass
