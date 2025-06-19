import argparse
import subprocess
from config.PathConfig import CMDArgs, Base_path


def process_cmd_args():
    parser = argparse.ArgumentParser(description='API automation configuration.')
    parser.add_argument('Account', help="Input account")
    parser.add_argument('Password', help="Input password")
    parser.add_argument('account_AT', help="Input AdminTool account")
    parser.add_argument('-e', '--env', dest='Env', default='qat', help="Input test env")
    parser.add_argument('-p', '--project', dest='Project', default='sta', help="Input test project")
    args = parser.parse_args()

    with open(CMDArgs, 'w') as f:
        f.write("{"
                + '\n"Account":"' + args.Account + '",'
                + '\n"Password":"' + args.Password + '",'
                + '\n"Env":"' + args.Env + '",'
                + '\n"Project":"' + args.Project + '",'
                + '\n"account_AT":"' + args.account_AT + '"\n}')
    return True


def run_test_suite():
    cmd1 = r"cd %s" % Base_path
    subprocess.call(cmd1, shell=True)
    print("Switch to project path and start test run")
    print("Check input configuration...")
    cmd2 = r"python -m unittest test_API/suite/Test_Suite.py"
    subprocess.call(cmd2, shell=True)
    return True


cmd = process_cmd_args()
run = run_test_suite()

if __name__ == '__main__':
    pass
