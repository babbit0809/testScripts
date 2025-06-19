import os

Base_path = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
API_TestCase = os.path.join(Base_path, 'test_API', 'case')
UI_TestCase = os.path.join(Base_path, 'test_UI', 'case')
CMDArgs = os.path.join(Base_path, 'config', 'CMDArgs.json')
# 現有的彩立方專案config
Config_API = os.path.join(Base_path, 'config', 'Config_API.json')
# 新的彩票獨立專案config
Config_API_Lottery = os.path.join(Base_path, 'config', 'Config_API_Lottery.json')
Config_TMP = os.path.join(Base_path, 'config', 'Config_TMP.json')
Config_UI = os.path.join(Base_path, 'config', 'Config_UI.json')
GameNameList = os.path.join(Base_path, 'data', 'GameNameList.json')
Localization = os.path.join(Base_path, 'data', 'Localization.json')
Download_path = os.path.join(Base_path, 'download')
Report_path = os.path.join(Base_path, 'report')

if __name__ == '__main__':
    pass
