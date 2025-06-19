import json
from config.GetCMDArgs import get_cmd_config
from config.PathConfig import Config_TMP
from utils.DataLoader import JsonLoader
from utils.DataExtractor import extract_text

# 讀取Config
Config = get_cmd_config("API")
Platform, Env, Project = 'Web', Config[3], Config[4]  # 為了拆分UI/API架構, 先預設為Web, 後續視情況調整
# 儲存測試帳號資料供後續使用
if Project not in 'lottery':
    account = JsonLoader('CMDArgs').get_cmd_args('Account')
    password = JsonLoader('CMDArgs').get_cmd_args('Password')
    with open(Config_TMP, 'r+') as f:
        data = json.load(f)
        data['API']['account'] = account
        data['API']['password'] = password
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
# Following dictionaries for Request Headers/Params
PlatformCode = {'iOS': "1", 'Android': "2", 'Web': "3", 'H5': "4"}


# 因應彩票獨立專案差異, project: lottery用來判斷讀取的config
def get_api_info(domain_name, *api_path):
    if Project == 'lottery':
        APIConfig = JsonLoader('APIConfig_Lottery')
    else:
        APIConfig = JsonLoader('APIConfig')
    domain = APIConfig.get_api_domain(domain_name, Env)
    path = APIConfig.get_api_path(domain_name, *api_path)
    url = extract_text("(^https?:\/\/\S+){|(^https?:\/\/\S+)", f"{domain}{path}")
    method = APIConfig.get_api_method(domain_name, *api_path)
    return url, method


# Following Functions for Request Headers
def get_api_AuthSetting():
    print("Get API Authorization Setting.")
    Authorization = {'qat': "Basic b3JhbmdlX3Rlc3Q6", 'stg': "Basic b3JhbmdlX3N0YWdpbmc6"}
    return {'Authorization': Authorization[Env], 'X-Platform': PlatformCode[Platform]}


def get_api_LanguageSetting():
    print("Get API Language Setting.")
    Language = {'sta': "zh-CN", 'vt': "vi-VN"}
    return Language[Project]


if __name__ == '__main__':
    pass
