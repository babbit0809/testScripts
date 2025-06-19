from utils.DataLoader import JsonLoader


def get_cmd_config(args):
    device_no, platform, target = None, None, None
    if args == "UI":
        # 確認測試平台
        device_no = JsonLoader('CMDArgs').get_cmd_args('DeviceNo')
        platform = JsonLoader('UIConfig').get_device_info(device_no, 'platformName')
        # 確認測試目標
        target = JsonLoader('CMDArgs').get_cmd_args('Target')
        if target.lower() not in ['app', 'h5', 'web', 'admintool']:
            print('UnSupport Target: [{0}]'.format(target) + ', please check again.')
        else:
            target = target.lower()
    # 確認測試環境
    env = JsonLoader('CMDArgs').get_cmd_args('Env')
    if env.lower() not in ['poc', 'dev', 'qat', 'stg']:  # 因應彩票獨立專案需求新增poc/dev
        print(f'UnSupport Env: [{0}]'.format(env) + ', use QAT by default.')
        env = 'qat'
    else:
        env = env.lower()
    # 確認測試專案
    project = JsonLoader('CMDArgs').get_cmd_args('Project')
    if project.lower() not in ['sta', 'vt', 'lottery']:  # lottery為彩票獨立專案用
        print(f'UnSupport Project: [{0}]'.format(project) + ', use STA by default.')
        project = 'sta'
    else:
        project = project.lower()
    return device_no, platform, target, env, project


if __name__ == '__main__':
    pass
