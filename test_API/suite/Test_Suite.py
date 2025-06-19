import unittest
import os
from datetime import datetime
from config.PathConfig import API_TestCase, Report_path
from config.SetAPIConfig import Env, Project
from utils.HTMLTestRunner import HTMLTestRunner


def create_test_suite():
    print("\nStart set test suite.")
    suite = unittest.TestSuite()
    Demo = unittest.defaultTestLoader.discover(API_TestCase, pattern='test_API_Lottery_Integration.py')
    suite.addTests(Demo)
    return suite


def create_report_folder(project=Project.upper(), test_plan="API_Regression"):
    folder_name = '/' + project + '/' + test_plan + "_" + datetime.now().strftime('%Y%m%d')
    report_folder = Report_path + folder_name
    if not os.path.exists(report_folder):
        os.makedirs(report_folder)
    return os.path.join(report_folder)


def create_test_report():
    test_suite = create_test_suite()
    report_folder = create_report_folder()
    if test_suite is not None:
        report_file = os.path.join(report_folder, Env.upper() + "_" + 'Test_Report.html')
        with open(report_file, 'wb') as f:
            runner = HTMLTestRunner(f, verbosity=2)
            runner.run(test_suite)
    return True


Finish = create_test_report()

if __name__ == "__main__":
    pass
