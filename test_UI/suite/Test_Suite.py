import unittest
import os
from datetime import datetime
from config.PathConfig import UI_TestCase, Report_path
from config.SetUIConfig import Platform, Target, Env, Project
from utils.HTMLTestRunner import HTMLTestRunner


def create_test_suite():
    print("\nStart set test suite.")
    suite = unittest.TestSuite()
    if Target in ['admintool']:
        case1 = unittest.defaultTestLoader.discover(UI_TestCase, pattern='test_Admin_Tool.py')
        suite.addTests(case1)
    else:
        case1 = unittest.defaultTestLoader.discover(UI_TestCase, pattern='test_UserPage_Setting_info.py')
        suite.addTests(case1)
        case2 = unittest.defaultTestLoader.discover(UI_TestCase, pattern='test_thirdParty.py')
        suite.addTests(case2)
        # if Project in ['vt']:  # 1. 越南站僅支援雙面盤 2. 快3/PK10在越南站順序有變且不支援六合彩
        #     case1 = unittest.defaultTestLoader.discover(UI_TestCase, pattern='test_GamePageSSC_Tg60_TwoSide.py')
        #     suite.addTests(case1)
        #     case2 = unittest.defaultTestLoader.discover(UI_TestCase, pattern='test_GamePage11x5_TW11x5_TwoSide.py')
        #     suite.addTests(case2)
        #     case3 = unittest.defaultTestLoader.discover(UI_TestCase, pattern='test_GamePagePK10_F3Racing_TwoSide.py')
        #     suite.addTests(case3)
        #     case4 = unittest.defaultTestLoader.discover(UI_TestCase, pattern='test_GamePageQuick3_HQuick3_TwoSide.py')
        #     suite.addTests(case4)
        # else:
        #     case1 = unittest.defaultTestLoader.discover(UI_TestCase, pattern='test_GamePageSSC_Tg60_*.py')
        #     suite.addTests(case1)
        #     case2 = unittest.defaultTestLoader.discover(UI_TestCase, pattern='test_GamePage11x5_TW11x5_*.py')
        #     suite.addTests(case2)
        #     case3 = unittest.defaultTestLoader.discover(UI_TestCase, pattern='test_GamePageQuick3_HQuick3_*.py')
        #     suite.addTests(case3)
        #     case4 = unittest.defaultTestLoader.discover(UI_TestCase, pattern='test_GamePagePK10_F3Racing_*.py')
        #     suite.addTests(case4)
        #     case5 = unittest.defaultTestLoader.discover(UI_TestCase, pattern='test_GamePageMarkSix_FMark6.py')
        #     suite.addTests(case5)
        case_UserPage = unittest.defaultTestLoader.discover(UI_TestCase, pattern='test_UserPage.py')
        suite.addTests(case_UserPage)

    test_Finished = unittest.defaultTestLoader.discover(UI_TestCase, pattern='test_Finished.py')
    suite.addTests(test_Finished)
    return suite


def create_report_folder(project=Project.upper(), test_plan="UI_Regression"):
    folder_name = '/' + project + '/' + test_plan + "_" + datetime.now().strftime('%Y%m%d')
    report_folder = Report_path + folder_name
    if not os.path.exists(report_folder):
        os.makedirs(report_folder)
    return os.path.join(report_folder)


def create_test_report():
    test_suite = create_test_suite()
    report_folder = create_report_folder()
    if test_suite is not None:
        report_file = os.path.join(report_folder,
                                   Platform + "_" + Target.upper() + "_" + Env.upper() + "_" + 'Test_Report.html')
        with open(report_file, 'wb') as f:
            runner = HTMLTestRunner(f, verbosity=2, Platform=Platform, Target=Target, Env=Env)
            runner.run(test_suite)
    return True


Finish = create_test_report()

if __name__ == "__main__":
    pass
