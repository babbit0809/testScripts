from config.SetUIConfig import Project
from utils.DataLoader import JsonLoader


def get_loc(pageName, locatorName, thirdParty_name=""):
    if Project in ['vt']:
        localization = 'VN'
    else:
        localization = 'CN'
    return JsonLoader('Localization').get_loc(localization, pageName, locatorName + thirdParty_name)


if __name__ == '__main__':
    pass
