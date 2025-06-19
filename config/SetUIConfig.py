import json
from appium import webdriver
from config.GetCMDArgs import get_cmd_config
from config.CheckAppVersion import download_app
from config.PathConfig import Config_TMP
from utils.DataLoader import JsonLoader

# 讀取Config
DeviceNo, Platform, Target, Env, Project = get_cmd_config("UI")
UIConfig = JsonLoader('UIConfig')
# 儲存測試帳號資料供後續使用
account = JsonLoader('CMDArgs').get_cmd_args('Account')
with open(Config_TMP, 'r+') as f:
    data = json.load(f)
    data[Platform][Project]['account'] = account
    f.seek(0)
    json.dump(data, f, indent=4)
    f.truncate()


def set_driver_config():
    # 確認app版本是否更新
    app_file = download_app()
    # 初始化: 獲取共通參數(browserName: Safari目前有問題且暫無解法, 先以Android Chrome為H5主要測試瀏覽器)
    print("\nStart init Appium/Selenium WebDriver.")
    server_ip = f"http://{UIConfig.get_server_setting('Server_ip')}"
    device_name = UIConfig.get_device_info(DeviceNo, 'deviceName')
    device_port = UIConfig.get_device_info(DeviceNo, 'Device_port')
    platformVersion = UIConfig.get_device_info(DeviceNo, 'platformVersion')
    print("\nDevice Name:", device_name, "\nPlatform:", Platform, "\nPlatform Version:", platformVersion)
    dc = {'deviceName': device_name,
          'platformName': Platform,
          'platformVersion': platformVersion,
          'newCommandTimeout': 150,  # 預設150(Sec), 避免某些測試情境因等待過久而session timeout
          'noReset': "true"}
    automationName = {'Android': "Espresso", 'iOS': "XCUITest"}
    browserName = {'Android': "Chromium", 'iOS': "Safari", 'windows': "chrome"}
    # 初始化: 判斷是否安裝新版App
    if app_file is True:
        app_path = JsonLoader('TMP').get_tmp_data(Platform, Project, f"app_path_{Env}")
        dc.update({'app': app_path})
    else:
        if Platform == 'Android':
            dc.update({'appPackage': UIConfig.get_client_setting(f"Android_{Env}_{Project}", "appPackage"),
                       'appActivity': UIConfig.get_client_setting("Android_appActivity", "appActivity")})
        elif Platform == 'iOS':
            dc.update({'bundleId': UIConfig.get_client_setting(f"iOS_{Env}_{Project}", "bundleId")})
    # 初始化: 獲取H5/Web/AdminTool的初始網址
    url_h5 = UIConfig.get_client_setting(f"H5_{Env}_{Project}", "InitialUrl")
    url_web = UIConfig.get_client_setting(f"Web_{Env}_{Project}", "InitialUrl")
    url_adminTool = UIConfig.get_client_setting(f"AdminTool_{Env}", "InitialUrl")
    initialUrl = {'h5': url_h5, 'web': url_web, 'admintool': url_adminTool}
    # 初始化: 獲取測試裝置資訊
    if Platform in ['Android', 'iOS']:
        # 判斷是否為模擬器
        if device_name in ['Android Emulator 1', 'Android Emulator 2']:
            serial_number = UIConfig.get_device_info(DeviceNo, "serialnumber")
            dc.update({'automationName': automationName[Platform],
                       'serialnumber': serial_number,
                       'emulator': "true"})
        else:
            udid = UIConfig.get_device_info(DeviceNo, "udid")
            dc.update({'automationName': automationName[Platform],
                       'udid': udid})
    # 初始化: 判斷是否為Mobile/PC Browser
    if Target == 'h5' or Platform == 'windows':
        dc.update({"browserName": browserName[Platform]})
    # 初始化: Request Automation Session.
    driver = webdriver.Remote(f"{server_ip}:{device_port}/wd/hub", dc)
    if Target in ['h5', 'web', 'admintool']:
        driver.get(initialUrl[Target])
        if Platform == 'windows':
            driver.maximize_window()
    return driver


Driver = set_driver_config()

if __name__ == '__main__':
    pass
    print('\nDriver:', Driver, '\nTarget:', Target, '\nEnv:', Env, '\nProject:', Project)
