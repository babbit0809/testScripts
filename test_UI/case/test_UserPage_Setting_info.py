import unittest
import time
from config.SetUIConfig import Driver, Platform, Target, Project
from test_API.common.Portal import Portal_info
from test_UI.page.LoginPage import LoginPage
from test_UI.page.HomePage import HomePage
from test_UI.page.UserPage import UserPage
from test_API.common.AdminTool import AdminTool
from test_API.common.Financial import Financial
from utils.DataLoader import JsonLoader
from test_API.common import AdminTool as AdminTool_API
from utils import Assertion
from test_API.common import Portal
import test_UI.page.LoginPage

expect_vip_level = None
MemberLevelId = None
expect_vip_interests = None
expect_ios_version = None
expect_android_version = None
class UserPageTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global expect_vip_level, MemberLevelId, expect_vip_interests, expect_ios_version, expect_android_version
        expect_vip_level = Portal_info().vip_levelName()
        MemberLevelId = Portal_info().get_vip_levelId()
        expect_ios_version = Portal.get_latest_version("iOS", Project)
        expect_android_version = Portal.get_latest_version("Android", Project)
        print('MemberLevelId')
        print(MemberLevelId)
        print('expect_ios_version')
        print(expect_ios_version)
        print('expect_android_version')
        print(expect_android_version)

        expect_vip_interests = AdminTool_API.AdminTool().get_Member_vip_interests_info(MemberLevelId)
        cls.driver = Driver
        login_page = LoginPage(cls.driver)
        login_page.execute_login()
        cls.account = JsonLoader('TMP').get_tmp_data(Platform, Project, 'account')
        cls.AdminTool = AdminTool()
        cls.Financial = Financial()
        home_page = HomePage(cls.driver)
        home_page.switch_category("user")

    def test_01_Edit_nick_name(self):
        page_user = UserPage(self.driver)
        home_page = HomePage(self.driver)
        page_user.switch_setting_option("setting_info")
        expect_default_nick_name = JsonLoader('CMDArgs').get_cmd_args('Account')
        actual_nick_name = page_user.data_setting_info_nick_name().text
        self.assertEqual(expect_default_nick_name, actual_nick_name)
        expect_edit_nick_name = page_user.edit_setting_info_nick_name()
        setting_info_nick_name = page_user.data_setting_info_nick_name().text
        self.assertEqual(expect_edit_nick_name, setting_info_nick_name)
        page_user.back_to_UserPage()
        actual_user_page_nick_name = page_user.data_user_page_nick_name().text
        self.assertEqual(expect_edit_nick_name, actual_user_page_nick_name)
        home_page.switch_category('home')
        actual_home_page_nick_name = home_page.data_home_page_nick_name().text
        self.assertEqual(expect_edit_nick_name, actual_home_page_nick_name)

        home_page.switch_category("user")
        page_user.switch_setting_option("setting_info")
        expect_default_nick_name = page_user.edit_setting_info_nick_name_to_account_name(expect_default_nick_name)
        setting_info_nick_name = page_user.data_setting_info_nick_name().text
        self.assertEqual(expect_default_nick_name, setting_info_nick_name)
        page_user.back_to_UserPage()
        actual_user_page_nick_name = page_user.data_user_page_nick_name().text
        self.assertEqual(expect_default_nick_name, actual_user_page_nick_name)
        home_page.switch_category('home')
        actual_home_page_nick_name = home_page.data_home_page_nick_name().text
        self.assertEqual(expect_default_nick_name, actual_home_page_nick_name)

    def test_02_Edit_pin_code(self):
        home_page = HomePage(self.driver)
        home_page.switch_category("user")
        page_user = UserPage(self.driver)
        page_user.switch_setting_option("setting_info")
        default_pin_code = JsonLoader('CMDArgs').get_cmd_args('PinCode')
        new_pin_code = '222222'

        actual_input_box_ping_code = page_user.input_verify_ping_code(default_pin_code)
        self.assertEqual(default_pin_code, actual_input_box_ping_code)
        actual_input_box_edit_ping_code = page_user.edit_ping_code(new_pin_code)
        self.assertEqual([new_pin_code, new_pin_code], actual_input_box_edit_ping_code)

        actual_input_box_ping_code = page_user.input_verify_ping_code(new_pin_code)
        self.assertEqual(new_pin_code, actual_input_box_ping_code)
        actual_input_box_edit_ping_code = page_user.edit_ping_code(default_pin_code)
        self.assertEqual([default_pin_code, default_pin_code], actual_input_box_edit_ping_code)
        page_user.back_to_UserPage()

    def test_03_edit_login_password(self):
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)
        home_page.switch_category("user")
        page_user = UserPage(self.driver)
        page_user.switch_setting_option("setting_info")
        default_password = JsonLoader('CMDArgs').get_cmd_args('Password')
        new_password = default_password + "qa"

        actual_input_box_ping_code = page_user.input_verify_login_password(default_password)
        self.assertEqual(default_password, actual_input_box_ping_code)
        actual_input_box_edit_ping_code = page_user.edit_login_password(new_password)
        self.assertEqual([new_password, new_password], actual_input_box_edit_ping_code)

        actual_input_box_ping_code = page_user.input_verify_login_password(new_password)
        self.assertEqual(new_password, actual_input_box_ping_code)
        actual_input_box_edit_ping_code = page_user.edit_login_password(default_password)
        self.assertEqual([default_password, default_password], actual_input_box_edit_ping_code)
        page_user.input_wrong_verify_login_password(new_password)
        login_page.execute_login()
        home_page.switch_category("user")

    def test_04_edit_phone_number(self):
        home_page = HomePage(self.driver)
        home_page.switch_category("user")
        page_user = UserPage(self.driver)
        account = JsonLoader('CMDArgs').get_cmd_args('Account')
        page_user.switch_setting_option("setting_info")
        if Project in ['vt']:
            AdminTool_API.AdminTool().ClearPhoneVerify(account, 2)
        else:
            AdminTool_API.AdminTool().ClearPhoneVerify(account, 1)
        expect_phone_number = page_user.new_phone_number()
        smsLog = AdminTool_API.AdminTool().get_smsLog(account)
        actual_phone_number = smsLog[0]
        phoneCaptcha = smsLog[1]
        page_user.input_phone_captcha(phoneCaptcha)
        self.assertEqual(expect_phone_number, actual_phone_number)
        page_user.back_to_UserPage()

    def test_05_edit_email(self):
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)
        home_page.switch_category("user")
        page_user = UserPage(self.driver)
        account = JsonLoader('CMDArgs').get_cmd_args('Account')
        page_user.switch_setting_option("setting_info")
        AdminTool_API.AdminTool().ClearEmail(account, 1)
        expect_security_email = page_user.new_security_email()
        self.driver.refresh()
        actual_security_email = page_user.input_security_email(expect_security_email)
        self.assertEqual(expect_security_email, actual_security_email)

        actual_API_security_email = Portal_info().get_account_email()
        self.assertEqual(expect_security_email, actual_API_security_email)
        self.driver.refresh()

        time.sleep(20)
        login_page.execute_login()

    # vip特權 / 會員等級
    def test_06_01_homePage_member_data_entrance_and_check_vip_level_and_interests(self):
        global expect_vip_level,expect_vip_interests
        home_page = HomePage(self.driver)
        page_user = UserPage(self.driver)
        home_page.switch_category("home")
        page_user.click_button_member_data_vip_level()
        actual_vip_level = page_user.get_vip_level()
        self.assertEqual(expect_vip_level, actual_vip_level)
        actual_vip_interests = page_user.check_my_vip_interest()
        self.assertEqual(expect_vip_interests, actual_vip_interests)
        page_user.back_to_UserPage()

    def test_06_02_homePage_navigationBar_entrance_and_check_vip_level_and_interests(self):
        global expect_vip_level, expect_vip_interests
        home_page = HomePage(self.driver)
        page_user = UserPage(self.driver)
        home_page.switch_category("home")
        page_user.click_navigationBar_button_vip()
        actual_vip_level = page_user.get_vip_level()
        self.assertEqual(expect_vip_level, actual_vip_level)
        actual_vip_interests = page_user.check_my_vip_interest()
        self.assertEqual(expect_vip_interests, actual_vip_interests)
        page_user.back_to_UserPage()

    def test_06_03_userPage_member_data_entrance_and_check_vip_level_and_interests(self):
        global expect_vip_level, expect_vip_interests
        home_page = HomePage(self.driver)
        page_user = UserPage(self.driver)
        home_page.switch_category("user")
        page_user.click_button_member_data_vip_level()
        actual_vip_level = page_user.get_vip_level()
        self.assertEqual(expect_vip_level, actual_vip_level)
        actual_vip_interests = page_user.check_my_vip_interest()
        self.assertEqual(expect_vip_interests, actual_vip_interests)
        page_user.back_to_UserPage()

    def test_06_04_userPage_navigationBar_entrance_and_check_vip_level_and_interests(self):
        global expect_vip_level, expect_vip_interests
        home_page = HomePage(self.driver)
        page_user = UserPage(self.driver)
        home_page.switch_category("user")
        page_user.click_navigationBar_button_vip()
        actual_vip_level = page_user.get_vip_level()
        self.assertEqual(expect_vip_level, actual_vip_level)
        actual_vip_interests = page_user.check_my_vip_interest()
        self.assertEqual(expect_vip_interests, actual_vip_interests)
        page_user.back_to_UserPage()

    # vip特權 / 会员特权
    def test_07_homePage_member_data_check_more_vip_level_and_interests(self):
        home_page = HomePage(self.driver)
        page_user = UserPage(self.driver)

        home_page.switch_category("home")
        page_user.click_button_member_data_vip_level()
        page_user.click_button_more_vip_interest()

        vip_level = 0
        page_user.click_button_tab_vip(vip_level)
        expect_vip_interests = AdminTool_API.AdminTool().get_more_Member_vip_interests_info(vip_level)
        actual_vip_interests = page_user.check_my_vip_interest()
        self.assertEqual(expect_vip_interests, actual_vip_interests)

        vip_level = 1
        page_user.click_button_tab_vip(vip_level)
        expect_vip_interests = AdminTool_API.AdminTool().get_more_Member_vip_interests_info(vip_level)
        actual_vip_interests = page_user.check_my_vip_interest()
        self.assertEqual(expect_vip_interests, actual_vip_interests)

        vip_level = 2
        page_user.click_button_tab_vip(vip_level)
        expect_vip_interests = AdminTool_API.AdminTool().get_more_Member_vip_interests_info(vip_level)
        actual_vip_interests = page_user.check_my_vip_interest()
        self.assertEqual(expect_vip_interests, actual_vip_interests)

        vip_level = 3
        page_user.click_button_tab_vip(vip_level)
        expect_vip_interests = AdminTool_API.AdminTool().get_more_Member_vip_interests_info(vip_level)
        actual_vip_interests = page_user.check_my_vip_interest()
        self.assertEqual(expect_vip_interests, actual_vip_interests)

        vip_level = 4
        page_user.click_button_tab_vip(vip_level)
        expect_vip_interests = AdminTool_API.AdminTool().get_more_Member_vip_interests_info(vip_level)
        actual_vip_interests = page_user.check_my_vip_interest()
        self.assertEqual(expect_vip_interests, actual_vip_interests)

        vip_level = 5
        page_user.click_button_tab_vip(vip_level)
        expect_vip_interests = AdminTool_API.AdminTool().get_more_Member_vip_interests_info(vip_level)
        actual_vip_interests = page_user.check_my_vip_interest()
        self.assertEqual(expect_vip_interests, actual_vip_interests)

        vip_level = 6
        page_user.click_button_tab_vip(vip_level)
        expect_vip_interests = AdminTool_API.AdminTool().get_more_Member_vip_interests_info(vip_level)
        actual_vip_interests = page_user.check_my_vip_interest()
        self.assertEqual(expect_vip_interests, actual_vip_interests)

        vip_level = 7
        page_user.click_button_tab_vip(vip_level)
        expect_vip_interests = AdminTool_API.AdminTool().get_more_Member_vip_interests_info(vip_level)
        actual_vip_interests = page_user.check_my_vip_interest()
        self.assertEqual(expect_vip_interests, actual_vip_interests)

        vip_level = 8
        page_user.click_button_tab_vip(vip_level)
        expect_vip_interests = AdminTool_API.AdminTool().get_more_Member_vip_interests_info(vip_level)
        actual_vip_interests = page_user.check_my_vip_interest()
        self.assertEqual(expect_vip_interests, actual_vip_interests)

        vip_level = 9
        page_user.click_button_tab_vip(vip_level)
        expect_vip_interests = AdminTool_API.AdminTool().get_more_Member_vip_interests_info(vip_level)
        actual_vip_interests = page_user.check_my_vip_interest()
        self.assertEqual(expect_vip_interests, actual_vip_interests)

        vip_level = 10
        page_user.click_button_tab_vip(vip_level)
        expect_vip_interests = AdminTool_API.AdminTool().get_more_Member_vip_interests_info(vip_level)
        actual_vip_interests = page_user.check_my_vip_interest()
        self.assertEqual(expect_vip_interests, actual_vip_interests)

        page_user.back_to_UserPage()
        page_user.back_to_UserPage()
        home_page.switch_category("home")

    def test_08_activityPage_activity(self):
        home_page = HomePage(self.driver)
        page_user = UserPage(self.driver)

        home_page.switch_category("activity")
        page_user.activity_total_count()
        expect_activity_total_count = AdminTool().get_Activity_status_TotalCount(status=[2],start_delta=-365)
        actual_activity_total_count = page_user.activity_total_count()
        self.assertEqual(expect_activity_total_count, actual_activity_total_count)

    def test_09_activityPage_notice_board(self):
        home_page = HomePage(self.driver)
        page_user = UserPage(self.driver)

        home_page.switch_category("activity")
        page_user.click_button_notice_board()
        expect_activity_total_count = AdminTool().get_operation_news_TotalCount(releaseto=[0,1,2,3],start_delta=-365)
        actual_activity_total_count = page_user.notice_board_total_count()
        self.assertEqual(expect_activity_total_count, actual_activity_total_count)

    # vip特權 / 返水優惠
    def test_10_userPage_navigationBar_check_more_vip_level_and_LevelReturn(self):
        home_page = HomePage(self.driver)
        page_user = UserPage(self.driver)

        home_page.switch_category("user")
        page_user.click_navigationBar_button_vip()
        page_user.click_button_more_vip_interest()

        vip_level = 0
        page_user.click_button_tab_vip(vip_level)
        page_user.click_button_member_return()
        expect_vip_return = AdminTool_API.AdminTool().get_vip_LevelReturn_info(vip_level)
        actual_vip_return = page_user.check_my_vip_interest()
        self.assertEqual(expect_vip_return, actual_vip_return)

        vip_level = 1
        page_user.click_button_tab_vip(vip_level)
        page_user.click_button_member_return()
        expect_vip_return = AdminTool_API.AdminTool().get_vip_LevelReturn_info(vip_level)
        actual_vip_return = page_user.check_my_vip_interest()
        self.assertEqual(expect_vip_return, actual_vip_return)

        vip_level = 2
        page_user.click_button_tab_vip(vip_level)
        page_user.click_button_member_return()
        expect_vip_return = AdminTool_API.AdminTool().get_vip_LevelReturn_info(vip_level)
        actual_vip_return = page_user.check_my_vip_interest()
        self.assertEqual(expect_vip_return, actual_vip_return)

        vip_level = 3
        page_user.click_button_tab_vip(vip_level)
        page_user.click_button_member_return()
        expect_vip_return = AdminTool_API.AdminTool().get_vip_LevelReturn_info(vip_level)
        actual_vip_return = page_user.check_my_vip_interest()
        self.assertEqual(expect_vip_return, actual_vip_return)

        vip_level = 4
        page_user.click_button_tab_vip(vip_level)
        page_user.click_button_member_return()
        expect_vip_return = AdminTool_API.AdminTool().get_vip_LevelReturn_info(vip_level)
        actual_vip_return = page_user.check_my_vip_interest()
        self.assertEqual(expect_vip_return, actual_vip_return)

        vip_level = 5
        page_user.click_button_tab_vip(vip_level)
        page_user.click_button_member_return()
        expect_vip_return = AdminTool_API.AdminTool().get_vip_LevelReturn_info(vip_level)
        actual_vip_return = page_user.check_my_vip_interest()
        self.assertEqual(expect_vip_return, actual_vip_return)

        vip_level = 6
        page_user.click_button_tab_vip(vip_level)
        page_user.click_button_member_return()
        expect_vip_return = AdminTool_API.AdminTool().get_vip_LevelReturn_info(vip_level)
        actual_vip_return = page_user.check_my_vip_interest()
        self.assertEqual(expect_vip_return, actual_vip_return)

        vip_level = 7
        page_user.click_button_tab_vip(vip_level)
        page_user.click_button_member_return()
        expect_vip_return = AdminTool_API.AdminTool().get_vip_LevelReturn_info(vip_level)
        actual_vip_return = page_user.check_my_vip_interest()
        self.assertEqual(expect_vip_return, actual_vip_return)

        vip_level = 8
        page_user.click_button_tab_vip(vip_level)
        page_user.click_button_member_return()
        expect_vip_return = AdminTool_API.AdminTool().get_vip_LevelReturn_info(vip_level)
        actual_vip_return = page_user.check_my_vip_interest()
        self.assertEqual(expect_vip_return, actual_vip_return)

        vip_level = 9
        page_user.click_button_tab_vip(vip_level)
        page_user.click_button_member_return()
        expect_vip_return = AdminTool_API.AdminTool().get_vip_LevelReturn_info(vip_level)
        actual_vip_return = page_user.check_my_vip_interest()
        self.assertEqual(expect_vip_return, actual_vip_return)

        vip_level = 10
        page_user.click_button_tab_vip(vip_level)
        page_user.click_button_member_return()
        expect_vip_return = AdminTool_API.AdminTool().get_vip_LevelReturn_info(vip_level)
        actual_vip_return = page_user.check_my_vip_interest()
        self.assertEqual(expect_vip_return, actual_vip_return)

        page_user.back_to_UserPage()
        page_user.back_to_UserPage()
        home_page.switch_category("home")

    def test_11_userPage_download_check_app_version(self):
        global expect_ios_version, expect_android_version
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)
        page_user = UserPage(self.driver)

        home_page.switch_category("user")
        page_user.click_button_user_page_download_app()
        page_user.click_button_ios_tab()
        page_user.click_download_page_app_version()
        actual_ios_version = page_user.get_download_page_app_version()
        self.assertEqual(expect_ios_version, actual_ios_version)
        page_user.back_to_UserPage()

        home_page.switch_category("user")
        page_user.click_button_user_page_download_app()
        page_user.click_button_android_tab()
        page_user.click_download_page_app_version()
        actual_android_version = page_user.get_download_page_app_version()
        self.assertEqual(expect_android_version, actual_android_version)
        page_user.back_to_UserPage()

    def test_12_loginPage_download_check_app_version(self):
        global expect_ios_version, expect_android_version
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)
        page_user = UserPage(self.driver)
        time.sleep(3)
        home_page.switch_category("user")
        page_user.click_button_user_page_logout()
        page_user.click_button_confirm_logout()

        login_page.click_button_download_app()
        page_user.click_button_ios_tab()
        page_user.click_download_page_app_version()
        actual_ios_version = page_user.get_download_page_app_version()
        self.assertEqual(expect_ios_version, actual_ios_version)

        page_user.click_button_android_tab()
        page_user.click_download_page_app_version()
        actual_android_version = page_user.get_download_page_app_version()
        self.assertEqual(expect_android_version, actual_android_version)
        page_user.back_to_UserPage()
        login_page.execute_login()
        home_page.switch_category("user")

    @classmethod
    def tearDownClass(cls):
        cls.driver = Driver
        home_page = HomePage(cls.driver)
        home_page.switch_category("home")


if __name__ == '__main__':
    unittest.main()
