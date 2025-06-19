from utils.FileReader import JsonReader
from config.PathConfig import CMDArgs, Config_TMP, Config_UI, Config_API, Config_API_Lottery, GameNameList, Localization


class JsonLoader(object):
    def __init__(self, file_name):
        path = {'CMDArgs': CMDArgs,
                'TMP': Config_TMP,
                'UIConfig': Config_UI,
                'APIConfig': Config_API,  # 現有的彩立方專案config
                'APIConfig_Lottery': Config_API_Lottery,  # 新的彩票獨立專案config
                'GameNameList': GameNameList,
                'Localization': Localization}

        self.data = JsonReader(path[file_name]).read_file

    def get_cmd_args(self, key):
        return self.data[key]

    def get_tmp_data(self, *key):
        key = list(key)
        if len(key) == 2:
            return self.data[key[0]][key[1]]
        else:
            return self.data[key[0]][key[1]][key[2]]

    def get_server_setting(self, key):
        return self.data[key]

    def get_client_setting(self, key1, key2):
        return self.data[key1][key2]

    def get_device_info(self, index, key):
        try:
            return self.data['Device_List'][int(index)][key]

        except IndexError:
            return "Error device no. Please check input."

    def get_loc(self, key1, key2, key3):
        return self.data[key1][key2][key3]

    def get_api_domain(self, domain_name, env):
        return self.data["domain"][domain_name][env]

    def get_api_path(self, domain_name, *api_path):
        api_path = list(api_path)
        if len(api_path) == 1:
            return self.data["path"][domain_name][api_path[0]][1]
        else:
            return self.data["path"][domain_name][api_path[0]][api_path[1]][1]

    def get_api_method(self, domain_name, *api_path):
        api_path = list(api_path)
        if len(api_path) == 1:
            return self.data["path"][domain_name][api_path[0]][0]
        else:
            return self.data["path"][domain_name][api_path[0]][api_path[1]][0]


if __name__ == '__main__':
    pass
