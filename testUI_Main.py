import argparse
import subprocess
from config.PathConfig import CMDArgs, Base_path


def process_cmd_args():
    parser = argparse.ArgumentParser(description='App automation configuration.')
    parser.add_argument('DeviceNo', help="Input test device no. (refer to Config_UI.json/ Device_List)")
    parser.add_argument('Target', help="Input test target: App/H5/Web/AdminTool")
    parser.add_argument('Account', help="Input account")
    parser.add_argument('Password', help="Input password")
    parser.add_argument('PinCode', help="Input pin_code")
    parser.add_argument('account_AT', help="Input AdminTool account")
    parser.add_argument('account_Fin', help="Input Financial account")
    parser.add_argument('-e', '--env', dest='Env', default='qat', help="Input test env.: qat/stg (default: qat)")
    parser.add_argument('-p', '--project', dest='Project', default='sta',
                        help="Input test project: sta/vt (default: sta)")
    args = parser.parse_args()

    with open(CMDArgs, 'w') as f:
        f.write("{"
                + '\n"DeviceNo":"' + args.DeviceNo + '",'
                + '\n"Target":"' + args.Target + '",'
                + '\n"Env":"' + args.Env + '",'
                + '\n"Project":"' + args.Project + '",'
                + '\n"Account":"' + args.Account + '",'
                + '\n"Password":"' + args.Password + '",'
                + '\n"PinCode":"' + args.PinCode + '",'
                + '\n"account_AT":"' + args.account_AT + '",'
                + '\n"account_Fin":"' + args.account_Fin + '"\n}')
    return True


def run_test_suite():
    cmd1 = r"cd %s" % Base_path
    subprocess.call(cmd1, shell=True)
    print("Switch to project path and start test run")
    print("Check input configuration...")
    cmd2 = r"python -m unittest test_UI/suite/Test_Suite.py"
    subprocess.call(cmd2, shell=True)
    return True


cmd = process_cmd_args()
run = run_test_suite()

if __name__ == '__main__':
    pass
