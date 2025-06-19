import requests
import os
import json
from tqdm import tqdm
from config.GetCMDArgs import get_cmd_config
from config.PathConfig import Download_path, Config_TMP
from test_API.common import Portal
from utils.DataExtractor import extract_json
from utils.DataLoader import JsonLoader

# 讀取Config
Config = get_cmd_config("UI")
Platform, Target, Env, Project = Config[1], Config[2], Config[3], Config[4]
agentCode = {'sta': "STA01", 'vt': "VT999"}


def get_latest_version():
    if Target == 'app':
        versionInfo = Portal.api_AllowAnonymous_check(Platform, Project).text
        latest_version = extract_json('data.versions.latest', versionInfo)  # for App, 非App的回傳格式會有不同
        previous_version = JsonLoader('TMP').get_tmp_data(Platform, Project, 'version_' + Env)
        if previous_version != latest_version:
            download_version = latest_version
        else:
            download_version = None
        return download_version


def get_blob_url():
    download_version = get_latest_version()
    if download_version:
        domain = JsonLoader('UIConfig').get_client_setting("Blob_url", Env)
        projectCode = agentCode[Project].lower()
        extension = None
        if Platform == 'Android':
            extension = "apk"
        elif Platform == 'iOS':
            extension = "ipa"
        blob_url = f"{domain}{projectCode}/{extension}/{download_version}/{projectCode}-{download_version}.{extension}"
        return blob_url


def download_app():
    download_url = get_blob_url()
    if Target == 'app' and download_url:
        res = requests.get(download_url, stream=True)
        file_name = download_url.split('/')[-1]
        file_size = int(res.headers['content-length'])
        app_file = os.path.join(Download_path, file_name)
        print("Start download.")
        with tqdm(total=file_size, unit='B', unit_scale=True, unit_divisor=1024, ascii=True, desc=file_name) as bar:
            with open(app_file, 'wb') as f:
                for chunk in res.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        bar.update(len(chunk))
        # 儲存App路徑供後續使用
        with open(Config_TMP, 'r+') as f:
            data = json.load(f)
            data[Platform][Project][f"app_path_{Env}"] = app_file
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
        return True
    elif Target == 'app' and download_url is None:
        print("No need to update.")


if __name__ == '__main__':
    pass
