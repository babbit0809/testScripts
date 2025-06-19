import glob
from selenium.webdriver.common.keys import Keys
from test_UI.common import BasePage
from test_UI.page.AdminTool_Locator import Xpath
from decimal import *
import time
import datetime
import random
import string
import math
from utils.DataExtractor import get_excel_columnName
from utils.Generator import pic_generator


class AdminTool(BasePage.BasePage):
    # Actions
    def switch_function(self, main_menu, submenu):
        # 切換選單-->子選單
        # # 系統管理
        if main_menu == 'control':
            main_menu = self.find_element(*Xpath.main_menu_control)
            main_menu.click()
            time.sleep(3)
            sub_menu = self.find_elements(*Xpath.control_sub)
            if submenu == 'setting':
                submenu = sub_menu[0]
            elif submenu == 'group':
                submenu = sub_menu[1]
            elif submenu == 'user':
                submenu = sub_menu[2]
        # # 全站管理
        elif main_menu == 'apartment':
            main_menu = self.find_element(*Xpath.main_menu_apartment)
            main_menu.click()
            time.sleep(3)
            sub_menu = self.find_elements(*Xpath.apartment_sub)
            if submenu == 'level':
                submenu = sub_menu[0]
            elif submenu == 'sms':
                submenu = sub_menu[1]
            elif submenu == 'site':
                submenu = sub_menu[2]
        # # 帳號管理
        elif main_menu == 'user':
            main_menu = self.find_element(*Xpath.main_menu_user)
            main_menu.click()
            time.sleep(3)
            sub_menu = self.find_elements(*Xpath.user_sub)
            if submenu == 'member':
                submenu = sub_menu[0]
            elif submenu == 'affiliates':
                submenu = sub_menu[1]
        # # 代理商管理
        elif main_menu == 'team':
            main_menu = self.find_element(*Xpath.main_menu_team)
            main_menu.click()
            time.sleep(3)
            sub_menu = self.find_elements(*Xpath.team_sub)
            if submenu == 'dividends':
                submenu = sub_menu[0]
            elif submenu == 'daily_wages':
                submenu = sub_menu[1]
            elif submenu == 'contract_daily_wages':
                submenu = sub_menu[2]
            elif submenu == 'contract_daily_dividends':
                submenu = sub_menu[3]
            elif submenu == 'contract_monthly_dividends':
                submenu = sub_menu[4]
            elif submenu == 'contract_management':
                submenu = sub_menu[5]
            elif submenu == 'agency_report':
                submenu = sub_menu[6]
            elif submenu == 'first_level_dividend':
                submenu = sub_menu[7]
        # # 出入款管理
        elif main_menu == 'transaction':
            main_menu = self.find_element(*Xpath.main_menu_transaction)
            main_menu.click()
            time.sleep(3)
            self.execute_script("window.scrollBy(0,200)", "")
            time.sleep(2)
            sub_menu = self.find_elements(*Xpath.transaction_sub)
            if submenu == 'payment_setting':
                submenu = sub_menu[0]
            elif submenu == 'deposit':
                submenu = sub_menu[1]
            elif submenu == 'turnover':
                submenu = sub_menu[2]
            elif submenu == 'withdraw':
                submenu = sub_menu[3]
            elif submenu == 'fast_deposit':
                submenu = sub_menu[4]
            elif submenu == 'quick_deposit_setting':
                submenu = sub_menu[5]
            elif submenu == 'transfer_management':
                submenu = sub_menu[6]
            elif submenu == 'transaction':
                submenu = sub_menu[7]
            elif submenu == 'member_transfer':
                submenu = sub_menu[8]
            elif submenu == 'crypto_currency':
                submenu = sub_menu[9]
        # # 遊戲紀錄
        elif main_menu == 'filesearch':
            time.sleep(3)
            self.execute_script("window.scrollBy(0,600)", "")
            time.sleep(3)
            main_menu = self.find_element(*Xpath.main_menu_filesearch)
            main_menu.click()
            time.sleep(3)
            sub_menu = self.find_elements(*Xpath.filesearch_sub)
            if submenu == 'lottery':
                submenu = sub_menu[0]
            elif submenu == 'trace':
                submenu = sub_menu[1]
            elif submenu == 'bet':
                submenu = sub_menu[2]
        # # 遊戲管理
        elif main_menu == 'desktop':
            main_menu = self.find_element(*Xpath.main_menu_desktop)
            main_menu.click()
            time.sleep(3)
            sub_menu = self.find_elements(*Xpath.desktop_sub)
            if submenu == 'lottery':
                submenu = sub_menu[0]
            elif submenu == 'issue_number':
                submenu = sub_menu[1]
            elif submenu == 'odds':
                submenu = sub_menu[2]
            elif submenu == 'third_party':
                submenu = sub_menu[3]
        # # 營運管理
        elif main_menu == 'shop':
            main_menu = self.find_element(*Xpath.main_menu_shop)
            main_menu.click()
            time.sleep(3)
            sub_menu = self.find_elements(*Xpath.shop_sub)
            if submenu == 'news':
                submenu = sub_menu[0]
            elif submenu == 'banner':
                submenu = sub_menu[1]
            elif submenu == 'template':
                submenu = sub_menu[2]
            elif submenu == 'promotion':
                submenu = sub_menu[3]
        # # 活動管理
        elif main_menu == 'activity':
            main_menu = self.find_element(*Xpath.main_menu_activity)
            main_menu.click()
            time.sleep(3)
            sub_menu = self.find_elements(*Xpath.activity_sub)
            self.execute_script("window.scrollBy(0,600)", "")
            if submenu == 'preferential_setting':
                submenu = sub_menu[0]
            elif submenu == 'activity_type':
                submenu = sub_menu[1]
            elif submenu == 'activity_management':
                submenu = sub_menu[2]
            elif submenu == 'activity_report':
                submenu = sub_menu[3]
            elif submenu == 'red_envelope':
                submenu = sub_menu[4]
            elif submenu == 'shengxibao':
                submenu = sub_menu[5]
        # # 營運報表
        elif main_menu == 'barchart':
            time.sleep(3)
            self.execute_script("window.scrollBy(0,600)", "")
            time.sleep(3)
            main_menu = self.find_element(*Xpath.main_menu_barchart)
            main_menu.click()
            sub_menu = self.find_elements(*Xpath.barchart_sub)
            if submenu == 'affiliate':
                submenu = sub_menu[0]
            elif submenu == 'member':
                submenu = sub_menu[1]
            elif submenu == 'agent':
                submenu = sub_menu[2]
            elif submenu == 'balance_statistics':
                submenu = sub_menu[3]
            elif submenu == 'rank':
                submenu = sub_menu[4]
            time.sleep(3)
            self.execute_script("window.scrollBy(0,600)", "")

        submenu.click()
        time.sleep(3)
        self.execute_script("window.scrollBy(0,-600)", "")

    def close_menu(self, main_menu):
        # 再次點選主選單進行初始化
        if main_menu == 'control':
            main_menu = self.find_element(*Xpath.main_menu_control)

        elif main_menu == 'apartment':
            main_menu = self.find_element(*Xpath.main_menu_apartment)

        elif main_menu == 'user':
            main_menu = self.find_element(*Xpath.main_menu_user)

        elif main_menu == 'team':
            main_menu = self.find_element(*Xpath.main_menu_team)

        elif main_menu == 'transaction':
            main_menu = self.find_element(*Xpath.main_menu_transaction)

        elif main_menu == 'filesearch':
            main_menu = self.find_element(*Xpath.main_menu_filesearch)

        elif main_menu == 'desktop':
            main_menu = self.find_element(*Xpath.main_menu_desktop)

        elif main_menu == 'shop':
            main_menu = self.find_element(*Xpath.main_menu_shop)

        elif main_menu == 'activity':
            main_menu = self.find_element(*Xpath.main_menu_activity)

        elif main_menu == 'barchart':
            main_menu = self.find_element(*Xpath.main_menu_barchart)

        main_menu.click()
        time.sleep(2)

    def generate_name(self):
        dt = datetime.datetime.today()  # 獲得當地時間
        dt_str = dt.strftime("%m%d%H%M")  # 格式化日期

        return dt_str

    def random_deposit_amount(self):
        count = 0
        amount = ''.join(random.choice(string.digits) for x in range(3))
        while amount == '000' and count < 10:
            amount = ''.join(random.choice(string.digits) for x in range(3))
            count += 1
        return amount

    def random_deposit_setting_amount(self):
        return ''.join(random.choice(string.digits) for x in range(6))

    def random_exchange_rate(self):
        count = 0
        amount = ''.join(random.choice(string.digits) for x in range(1))
        while amount == '0' and count < 10:
            amount = ''.join(random.choice(string.digits) for x in range(1))
            count += 1
        amount = amount + ".11"
        return amount

    def date_str_to_timestamp(self, date):
        date_time_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
        timestamp = date_time_obj.timestamp()

        return timestamp

    def close_drawer_mask(self):
        try:
            drawer_mask = self.find_element(*Xpath.drawer_mask)
            drawer_mask.click()
        except Exception as e:
            print(e)

    def switch_pagination_displayed(self, num):
        self.click_field_pagination()
        time.sleep(2)
        self.click_option_pagination(num)

    def upload_create_activity_web(self):
        path = pic_generator(width=562, height=406, file_name="test_pic_web")
        upload_create_activity_web = self.find_element(*Xpath.upload_create_activity_web)
        upload_create_activity_web.send_keys(path)

    def upload_create_activity_app(self):
        path = pic_generator(width=562, height=406, file_name="test_pic_app")
        upload_create_activity_app = self.find_element(*Xpath.upload_create_activity_app)
        upload_create_activity_app.send_keys(path)

    def upload_banner_carousel(self):
        path = pic_generator(width=562, height=406, file_name="test_pic_carousel")
        upload_add_banner = self.find_element(*Xpath.upload_add_banner)
        upload_add_banner.send_keys(path)

    def upload_banner_game(self):
        path = pic_generator(width=562, height=406, file_name="test_pic_game")
        upload_add_banner = self.find_element(*Xpath.upload_add_banner)
        upload_add_banner.send_keys(path)

    def click_field_pagination(self):
        field_pagination = self.find_element(*Xpath.field_pagination)
        field_pagination.click()

    def click_option_pagination(self, num):
        time.sleep(2)
        if num == 10:
            option_pagination = self.find_element(*Xpath.option_pagination_10)
        elif num == 25:
            option_pagination = self.find_element(*Xpath.option_pagination_25)
        elif num == 50:
            option_pagination = self.find_element(*Xpath.option_pagination_50)
        elif num == 100:
            option_pagination = self.find_element(*Xpath.option_pagination_100)
        else:
            option_pagination = self.find_element(*Xpath.option_pagination_25)
        option_pagination.click()
        time.sleep(10)

    def click_field_search_start_date(self):
        field_search_start_date = self.find_element(*Xpath.field_search_start_date)
        field_search_start_date.click()

    def click_field_search_end_date(self):
        field_search_end_date = self.find_element(*Xpath.field_search_end_date)
        field_search_end_date.click()

    def click_button_confirm_date(self):
        button_confirm_date = self.find_element(*Xpath.button_confirm_date)
        button_confirm_date.click()

    def click_create_member(self):
        button_create_member = self.find_element(*Xpath.button_create_member)
        button_create_member.click()

    def click_create_affiliate(self):
        button_create_affiliate = self.find_element(*Xpath.button_create_affiliate)
        button_create_affiliate.click()

    def click_edit_member(self):
        self.find_element(*Xpath.button_edit_member)
        button_edit_member = self.find_element(*Xpath.button_edit_member)
        button_edit_member.click()
        time.sleep(2)

    def click_member_button_freeze(self):
        member_button_freeze = self.find_element(*Xpath.member_button_freeze)
        member_button_freeze.click()
        time.sleep(2)

    def click_member_button_freeze_submit(self):
        member_button_freeze_submit = self.find_element(*Xpath.member_button_freeze_submit)
        member_button_freeze_submit.click()
        time.sleep(2)

    def click_member_button_freeze_confirm(self):
        member_button_freeze_confirm = self.find_element(*Xpath.member_button_freeze_confirm)
        member_button_freeze_confirm.click()
        time.sleep(2)

    def click_edit_member_tab(self, edit_member_tab):
        # 在編輯會員頁面切換tab
        try:
            # 基本資料
            if edit_member_tab == "basic_data":
                edit_member_tab = self.find_element(*Xpath.edit_member_tab_basic_data)
            # 銀行資料
            elif edit_member_tab == "bank_data":
                edit_member_tab = self.find_element(*Xpath.tab_bank_data)
            # 帳號設定
            elif edit_member_tab == "account_setting":
                edit_member_tab = self.find_element(*Xpath.tab_account_setting)
            # 帳號安全
            elif edit_member_tab == "account_security":
                edit_member_tab = self.find_element(*Xpath.tab_account_security)
            # 綜合紀錄
            elif edit_member_tab == "summarized_log":
                edit_member_tab = self.find_element(*Xpath.tab_summarized_log)
            # 異動記錄
            elif edit_member_tab == "change_log":
                edit_member_tab = self.find_element(*Xpath.tab_change_log)

            edit_member_tab.click()

        except Exception as e:
            print(e)
            time.sleep(5)
            if edit_member_tab == "basic_data":
                edit_member_tab = self.find_element(*Xpath.edit_member_tab_basic_data)
            elif edit_member_tab == "bank_data":
                edit_member_tab = self.find_element(*Xpath.tab_bank_data)
            elif edit_member_tab == "account_setting":
                edit_member_tab = self.find_element(*Xpath.tab_account_setting)
            elif edit_member_tab == "account_security":
                edit_member_tab = self.find_element(*Xpath.tab_account_security)
            elif edit_member_tab == "summarized_log":
                edit_member_tab = self.find_element(*Xpath.tab_summarized_log)
            elif edit_member_tab == "change_log":
                edit_member_tab = self.find_element(*Xpath.tab_change_log)

            edit_member_tab.click()

    def click_edit_member_button_status(self):
        edit_member_button_status = self.find_element(*Xpath.edit_member_button_status)
        edit_member_button_status.click()

    def click_edit_member_level(self):
        edit_member_field_member_level = self.find_element(*Xpath.edit_member_field_member_level)
        edit_member_field_member_level.click()
        time.sleep(2)
        edit_member_option_member_level = self.find_element(*Xpath.edit_member_option_member_level)
        edit_member_option_member_level.click()
        level = self.find_element(*Xpath.edit_member_field_member_level).text
        print('level')
        print(level)

    def click_edit_member_return_increase(self):
        edit_member_button_return_increase = self.find_element(*Xpath.edit_member_button_return_increase)
        edit_member_button_return_increase.click()
        edit_member_button_return_increase.click()

    def click_edit_member_button_placebet(self):
        edit_member_button_placebet = self.find_element(*Xpath.edit_member_button_placebet)
        edit_member_button_placebet.click()

    def click_edit_member_button_deposit(self):
        edit_member_button_deposit = self.find_element(*Xpath.edit_member_button_deposit)
        edit_member_button_deposit.click()

    def click_edit_member_button_withdraw(self):
        edit_member_button_withdraw = self.find_element(*Xpath.edit_member_button_withdraw)
        edit_member_button_withdraw.click()

    def click_edit_member_button_transfer(self):
        edit_member_button_transfer = self.find_element(*Xpath.edit_member_button_transfer)
        edit_member_button_transfer.click()

    def click_bank_data_button_create(self):
        bank_data_button_create = self.find_element(*Xpath.bank_data_button_create)
        bank_data_button_create.click()

    def click_bank_data_field_bank(self):
        bank_data_field_bank = self.find_element(*Xpath.bank_data_field_bank)
        bank_data_field_bank.click()

    def click_bank_data_option_bank(self):
        time.sleep(1)
        bank_data_option_bank = self.find_element(*Xpath.bank_data_option_bank)
        bank_data_option_bank.click()

    def click_account_security_button_password(self):
        account_security_button_password = self.find_element(*Xpath.account_security_button_password)
        account_security_button_password.click()

    def click_account_security_button_birthday(self):
        account_security_button_birthday = self.find_element(*Xpath.account_security_button_birthday)
        account_security_button_birthday.click()

    def click_account_security_button_confirm_birthday(self):
        account_security_button_confirm_birthday = self.find_element(*Xpath.account_security_button_confirm_birthday)
        account_security_button_confirm_birthday.click()

    def click_button_save_edit_member(self):
        button_save_edit_member = self.find_element(*Xpath.button_save_edit_member)
        button_save_edit_member.click()
        time.sleep(3)

    def click_button_edit_member_search(self):
        click_button_edit_member_search = self.find_element(*Xpath.button_edit_member_search)
        click_button_edit_member_search.click()

    def click_fast_deposit(self):
        button_fast_deposit = self.find_element(*Xpath.button_fast_deposit)
        button_fast_deposit.click()

    def click_tab_single_deposit(self):
        time.sleep(2)
        tab_single_deposit = self.find_element(*Xpath.tab_single_deposit)
        tab_single_deposit.click()

    def click_tab_batch_deposit(self):
        time.sleep(2)
        tab_batch_deposit = self.find_element(*Xpath.tab_batch_deposit)
        tab_batch_deposit.click()

    def click_tab_manual_deposit(self):
        time.sleep(2)
        tab_manual_deposit = self.find_element(*Xpath.tab_manual_deposit)
        tab_manual_deposit.click()

    def click_button_back(self):
        button_back = self.find_element(*Xpath.button_back)
        button_back.click()

    def click_button_single_fast_deposit_submit(self):
        time.sleep(3)
        button_single_fast_deposit_submit = self.find_element(*Xpath.button_single_fast_deposit_submit)
        button_single_fast_deposit_submit.click()

        status = False
        count = 0
        while status is False and count < 20:
            try:
                self.driver.find_element_by_xpath(Xpath.title_fast_deposit)
                time.sleep(1)
            except Exception as e:
                print(e)
                status = True
                pass

    def click_button_batch_fast_deposit_submit(self):
        time.sleep(3)
        button_batch_fast_deposit_submit = self.find_element(*Xpath.button_batch_fast_deposit_submit)
        button_batch_fast_deposit_submit.click()

        status = False
        while status is False:
            try:
                self.driver.find_element(*Xpath.title_fast_deposit)
            except Exception as e:
                print(e)
                status = True
                pass

    def click_button_manual_fast_deposit_submit(self):
        time.sleep(3)
        button_manual_fast_deposit_submit = self.find_element(*Xpath.button_manual_fast_deposit_submit)
        button_manual_fast_deposit_submit.click()

        status = False
        while status is False:
            try:
                self.driver.find_element(*Xpath.title_fast_deposit)
            except Exception as e:
                print(e)
                status = True
                pass

    def click_button_create_fast_deposit_setting(self):
        button_create_fast_deposit_setting = self.find_element(*Xpath.button_create_fast_deposit_setting)
        button_create_fast_deposit_setting.click()

    def click_field_fast_deposit_type(self):
        field_fast_deposit_type = self.find_element(*Xpath.field_fast_deposit_type)
        field_fast_deposit_type.click()

    def click_option_fast_deposit_type(self):
        time.sleep(1)
        option_fast_deposit_type = self.find_element(*Xpath.option_fast_deposit_type)
        option_fast_deposit_type.click()

    def click_field_fast_deposit_subtype(self):
        field_fast_deposit_subtype = self.find_element(*Xpath.field_fast_deposit_subtype)
        field_fast_deposit_subtype.click()

    def click_option_fast_deposit_subtype(self):
        time.sleep(1)
        option_fast_deposit_subtype = self.find_element(*Xpath.option_fast_deposit_subtype)
        option_fast_deposit_subtype.click()

    def click_button_fast_deposit_increase_turnover(self):
        button_fast_deposit_increase_turnover = self.find_element(*Xpath.button_fast_deposit_increase_turnover)
        button_fast_deposit_increase_turnover.click()

    def click_button_fast_deposit_increase_count_per_day(self):
        button_fast_deposit_increase_count_per_day = self.find_element(
            *Xpath.button_fast_deposit_increase_count_per_day)
        button_fast_deposit_increase_count_per_day.click()

    def click_button_fast_deposit_increase_calculated(self):
        button_fast_deposit_increase_calculated = self.find_element(*Xpath.button_fast_deposit_increase_calculated)
        button_fast_deposit_increase_calculated.click()

    def click_button_fast_deposit_setting_search(self):
        button_fast_deposit_setting_search = self.find_element(*Xpath.button_fast_deposit_setting_search)
        button_fast_deposit_setting_search.click()

    def click_field_bet_source_search(self):
        field_bet_search = self.find_element(*Xpath.field_bet_source_search)
        field_bet_search.click()
        time.sleep(2)

    def click_option_bet_source_search(self, bet_source):
        time.sleep(1)
        option_bet_search = self.find_elements(*Xpath.option_bet_source_search)

        if bet_source == 'all':
            option_bet_search = option_bet_search[0]
        elif bet_source == 'web':
            option_bet_search = option_bet_search[1]
        elif bet_source == 'app':
            option_bet_search = option_bet_search[2]

        option_source = option_bet_search.text
        option_bet_search.click()
        time.sleep(2)

        return option_source

    def click_field_bet_status_search(self):
        field_bet_search = self.find_element(*Xpath.field_bet_status_search)
        field_bet_search.click()
        time.sleep(2)

    def click_option_bet_status_search(self, bet_status):
        time.sleep(1)
        option_bet_search = self.find_elements(*Xpath.option_bet_status_search)

        if bet_status == 'all':
            option_bet_search = option_bet_search[0]
        elif bet_status == 'settled':
            option_bet_search = option_bet_search[1]
        elif bet_status == 'unsettled':
            option_bet_search = option_bet_search[2]
        elif bet_status == 'cancel':
            option_bet_search = option_bet_search[3]
        elif bet_status == 'early':
            option_bet_search = option_bet_search[4]

        option_status = option_bet_search.text
        option_bet_search.click()
        time.sleep(2)

        return option_status

    def click_field_bet_winLoss_search(self):
        time.sleep(2)
        field_bet_search = self.find_element(*Xpath.field_bet_winLoss_search)
        field_bet_search.click()

    def click_option_bet_winLoss_search(self, bet_winLoss):
        time.sleep(2)
        option_bet_search = self.find_elements(*Xpath.option_bet_winLoss_search)

        if bet_winLoss == 'all':
            option_bet_search = option_bet_search[0]
        elif bet_winLoss == 'win':
            option_bet_search = option_bet_search[1]
        elif bet_winLoss == 'loss':
            option_bet_search = option_bet_search[2]
        elif bet_winLoss == 'tie':
            option_bet_search = option_bet_search[3]

        option_status = option_bet_search.text
        option_bet_search.click()
        time.sleep(2)

        return option_status

    def click_field_transaction_type_search(self):
        time.sleep(2)
        field_transaction_search = self.find_element(*Xpath.field_transaction_search)
        field_transaction_search.click()

    def click_option_transaction_type_search(self, transaction_type):
        time.sleep(2)
        option_transaction_search = self.find_elements(*Xpath.option_transaction_search)

        if transaction_type == 'all':
            option_transaction_search = option_transaction_search[0]
        elif transaction_type == 'dispense':
            option_transaction_search = option_transaction_search[1]
        elif transaction_type == 'deposit':
            option_transaction_search = option_transaction_search[2]

        option_transaction = option_transaction_search.text
        option_transaction_search.click()
        time.sleep(2)

        return option_transaction

    def click_button_activity_type_edit(self):
        button_activity_type_edit = self.find_element(*Xpath.button_activity_type_edit)
        button_activity_type_edit.click()
        time.sleep(2)

    def click_button_activity_type_edit_status(self):
        button_activity_type_edit_status = self.find_element(*Xpath.button_activity_type_edit_status)
        button_activity_type_edit_status.click()

    def click_button_activity_type_edit_submit(self):
        button_activity_type_edit_submit = self.find_element(*Xpath.button_activity_type_edit_submit)
        button_activity_type_edit_submit.click()
        time.sleep(2)

    def click_button_create_activity(self):
        button_create_activity = self.find_element(*Xpath.button_create_activity)
        button_create_activity.click()
        time.sleep(2)

    def click_button_edit_activity(self):
        button_edit_activity = self.find_element(*Xpath.button_edit_activity)
        button_edit_activity.click()
        time.sleep(2)

    def click_field_create_activity_type(self):
        field_create_activity_type = self.find_element(*Xpath.field_create_activity_type)
        field_create_activity_type.click()

    def click_option_create_activity_type_first(self):
        option_create_activity_type_first = self.find_element(*Xpath.option_create_activity_type_first)
        option_create_activity_type_first.click()

    def click_button_create_activity_submit(self):
        button_create_activity_submit = self.find_element(*Xpath.button_create_activity_submit)
        time.sleep(2)
        button_create_activity_submit.click()
        time.sleep(2)

    def click_button_create_activity_confirm(self):
        button_create_activity_confirm = self.find_element(*Xpath.button_create_activity_confirm)
        button_create_activity_confirm.click()
        time.sleep(2)

    def click_button_create_activity_cancel(self):
        button_create_activity_cancel = self.find_element(*Xpath.button_create_activity_cancel)
        button_create_activity_cancel.click()
        time.sleep(2)

    def click_button_back_to_activity_list(self):
        button_back_to_activity_list = self.find_element(*Xpath.button_back_to_activity_list)
        button_back_to_activity_list.click()
        time.sleep(2)
        button_leave_activity_edit_confirm = self.find_element(*Xpath.button_leave_activity_edit_confirm)
        button_leave_activity_edit_confirm.click()
        time.sleep(2)

    def click_tab_banner_web(self):
        tab_banner_web = self.find_element(*Xpath.tab_banner_web)
        tab_banner_web.click()

    def click_tab_banner_h5(self):
        tab_banner_h5 = self.find_element(*Xpath.tab_banner_h5)
        tab_banner_h5.click()

    def click_tab_banner_ios(self):
        tab_banner_ios = self.find_element(*Xpath.tab_banner_ios)
        tab_banner_ios.click()

    def click_tab_banner_android(self):
        tab_banner_android = self.find_element(*Xpath.tab_banner_android)
        tab_banner_android.click()

    def click_button_add_banner_carousel(self):
        time.sleep(2)
        button_add_banner_carousel = self.find_element(*Xpath.button_add_banner_carousel)
        button_add_banner_carousel.click()

    def click_button_add_banner_game(self):
        time.sleep(2)
        button_add_banner_game = self.find_element(*Xpath.button_add_banner_game)
        button_add_banner_game.click()

    def click_field_add_banner_start(self):
        time.sleep(2)
        field_add_banner_start = self.find_element(*Xpath.field_add_banner_start)
        field_add_banner_start.click()

    def click_button_add_banner_now(self):
        time.sleep(2)
        button_add_banner_now = self.find_element(*Xpath.button_add_banner_now)
        button_add_banner_now.click()

    def click_button_add_banner_forever(self):
        time.sleep(2)
        button_add_banner_forever = self.find_element(*Xpath.button_add_banner_forever)
        button_add_banner_forever.click()

    def click_button_add_banner_submit(self):
        time.sleep(2)
        button_add_banner_submit = self.find_element(*Xpath.button_add_banner_submit)
        button_add_banner_submit.click()
        time.sleep(2)

    def click_button_edit_banner_carousel(self, num):
        time.sleep(2)
        button_edit_banner_carousel = self.find_elements(*Xpath.button_edit_banner_carousel)
        button_edit_banner_carousel[num - 1].click()  # API丟進來的數量需調整index給UI用

    def click_button_edit_banner_game(self, num):
        time.sleep(2)
        button_edit_banner_game = self.find_elements(*Xpath.button_edit_banner_game)
        button_edit_banner_game[num - 1].click()  # API丟進來的數量需調整index給UI用

    def click_button_delete_banner_carousel(self, num):
        button_delete_banner_carousel = self.find_elements(*Xpath.button_delete_banner_carousel)
        button_delete_banner_carousel[num - 1].click()  # API丟進來的數量需調整index給UI用

    def click_button_delete_banner_game(self, num):
        button_delete_banner_game = self.find_elements(*Xpath.button_delete_banner_game)
        button_delete_banner_game[num - 1].click()  # API丟進來的數量需調整index給UI用

    def click_button_delete_banner_confirm(self):
        time.sleep(2)
        button_delete_banner_confirm = self.find_element(*Xpath.button_delete_banner_confirm)
        button_delete_banner_confirm.click()
        time.sleep(2)

    def click_turnover_button_edit(self):
        turnover_button_edit = self.find_elements(*Xpath.turnover_button_edit)
        turnover_button_edit[0].click()
        time.sleep(2)

    def click_withdrawal_field_search_status(self):
        withdrawal_field_search_status = self.find_element(*Xpath.withdrawal_field_search_status)
        withdrawal_field_search_status.click()
        time.sleep(2)

    def click_withdrawal_detail_field_audit(self):
        withdrawal_detail_field_audit = self.find_element(*Xpath.withdrawal_detail_field_audit)
        withdrawal_detail_field_audit.click()
        time.sleep(2)

    def click_withdrawal_detail_option_audit_pass(self):
        withdrawal_detail_option_audit_pass = self.find_element(*Xpath.withdrawal_detail_option_audit_pass)
        withdrawal_detail_option_audit_pass.click()
        time.sleep(2)

    def click_withdrawal_detail_option_audit_fail(self):
        withdrawal_detail_option_audit_fail = self.find_element(*Xpath.withdrawal_detail_option_audit_fail)
        withdrawal_detail_option_audit_fail.click()
        time.sleep(2)

    def click_withdrawal_option_search_status(self, status):
        if status == "all":
            status = self.find_element(*Xpath.withdrawal_option_search_status_all)
        elif status == "unprocessed":
            status = self.find_element(*Xpath.withdrawal_option_search_status_unprocessed)
        elif status == "processing":
            status = self.find_element(*Xpath.withdrawal_option_search_status_processing)
        elif status == "finished":
            status = self.find_element(*Xpath.withdrawal_option_search_status_finished)
        elif status == "rejected":
            status = self.find_element(*Xpath.withdrawal_option_search_status_rejected)
        elif status == "failed":
            status = self.find_element(*Xpath.withdrawal_option_search_status_failed)

        status.click()

        self.find_element(*Xpath.withdrawal_field_search_order_id).send_keys(Keys.CONTROL, 'a')
        self.find_element(*Xpath.withdrawal_field_search_order_id).send_keys(Keys.DELETE)
        time.sleep(2)

    def click_withdrawal_button_audit(self):
        withdrawal_button_audit = self.find_element(*Xpath.withdrawal_button_audit)
        withdrawal_button_audit.click()
        time.sleep(2)

    def click_withdrawal_column_order_id(self):
        withdrawal_result_field_order_id = self.find_element(*Xpath.withdrawal_result_field_order_id)
        withdrawal_result_field_order_id.click()
        time.sleep(2)

    def click_withdrawal_detail_button_close(self):
        withdrawal_detail_button_close = self.find_element(*Xpath.withdrawal_detail_button_close)
        withdrawal_detail_button_close.click()
        time.sleep(2)

    def click_field_single_fast_deposit_type(self):
        field_single_fast_deposit_type = self.find_element(*Xpath.field_single_fast_deposit_type)
        field_single_fast_deposit_type.click()
        time.sleep(2)

    def click_option_single_fast_deposit_promote(self):
        option_single_fast_deposit_promote = self.find_element(*Xpath.option_single_fast_deposit_promote)
        option_single_fast_deposit_promote.click()
        time.sleep(2)

    def click_button_export(self):
        button_export = self.find_element(*Xpath.button_export)
        button_export.click()
        time.sleep(2)

    def click_button_deposit(self):
        button_deposit = self.find_element(*Xpath.button_deposit)
        button_deposit.click()
        time.sleep(2)

    def click_activity_result_name(self):
        column_activity_name = self.find_element(*Xpath.column_activity_name)
        column_activity_name.click()
        time.sleep(2)

    def click_tab_activity_detail_basic(self):
        tab_activity_detail_basic = self.find_element(*Xpath.tab_activity_detail_basic)
        tab_activity_detail_basic.click()
        time.sleep(2)

    def click_tab_activity_detail_rule(self):
        tab_activity_detail_rule = self.find_element(*Xpath.tab_activity_detail_rule)
        tab_activity_detail_rule.click()
        time.sleep(2)

    def click_tab_activity_detail_change(self):
        tab_activity_detail_change = self.find_element(*Xpath.tab_activity_detail_change)
        tab_activity_detail_change.click()
        time.sleep(2)

    def click_field_search_activity_status(self):
        field_search_activity_status = self.find_element(*Xpath.field_search_activity_status)
        field_search_activity_status.click()
        time.sleep(2)

    def click_option_search_activity_status_all(self):
        option_search_activity_status_all = self.find_element(*Xpath.option_search_activity_status_all)
        option_search_activity_status_all.click()
        time.sleep(2)

    def click_option_search_activity_status_standby(self):
        option_search_activity_caret_down = self.find_element(*Xpath.option_search_activity_caret_down)
        option_search_activity_caret_down.click()
        time.sleep(2)
        option_search_activity_status_all = self.find_element(*Xpath.option_search_activity_status_all)
        option_search_activity_status_all.click()
        option_search_activity_status_all.click()
        option_search_activity_status_standby = self.find_element(*Xpath.option_search_activity_status_standby)
        option_search_activity_status_standby.click()
        time.sleep(2)
        field_status_type_search = self.find_element(*Xpath.field_status_type_search)
        field_status_type_search.click()

    def click_option_search_activity_status_ongoing(self):
        option_search_activity_status_ongoing = self.find_element(*Xpath.option_search_activity_status_ongoing)
        option_search_activity_status_ongoing.click()
        time.sleep(2)

    def click_option_search_activity_status_finished(self):
        option_search_activity_status_finished = self.find_element(*Xpath.option_search_activity_status_finished)
        option_search_activity_status_finished.click()
        time.sleep(2)

    def click_tab_activity_rule_setting(self):
        tab_activity_rule_setting = self.find_element(*Xpath.tab_activity_rule_setting)
        tab_activity_rule_setting.click()
        time.sleep(2)

    def click_button_create_contract(self):
        button_create_contract = self.find_element(*Xpath.button_create_contract)
        button_create_contract.click()
        time.sleep(3)

    def click_field_create_contract_type(self):
        field_create_contract_type = self.find_element(*Xpath.field_create_contract_type)
        field_create_contract_type.click()
        time.sleep(2)

    def click_option_contract_daily_wages(self):
        option_contract_daily_wages = self.find_element(*Xpath.option_contract_daily_wages)
        option_contract_daily_wages.click()
        time.sleep(2)

    def click_option_contract_daily_dividends(self):
        option_contract_daily_dividends = self.find_element(*Xpath.option_contract_daily_dividends)
        option_contract_daily_dividends.click()
        time.sleep(2)

    def click_option_contract_monthly_dividends(self):
        option_contract_monthly_dividends = self.find_element(*Xpath.option_contract_monthly_dividends)
        option_contract_monthly_dividends.click()
        time.sleep(2)

    def click_field_search_contract_type(self):
        field_search_contract_type = self.find_element(*Xpath.field_search_contract_type)
        field_search_contract_type.click()
        time.sleep(2)

    def click_option_search_contract_daily_wages(self):
        option_search_contract_daily_wages = self.find_element(*Xpath.option_search_contract_daily_wages)
        option_search_contract_daily_wages.click()
        time.sleep(2)

    def click_option_search_contract_daily_dividends(self):
        option_search_contract_daily_dividends = self.find_element(*Xpath.option_search_contract_daily_dividends)
        option_search_contract_daily_dividends.click()
        time.sleep(2)

    def click_option_search_contract_monthly_dividends(self):
        option_search_contract_monthly_dividends = self.find_element(*Xpath.option_search_contract_monthly_dividends)
        option_search_contract_monthly_dividends.click()
        time.sleep(2)

    def click_button_reset_contract(self):
        button_reset_contract = self.find_element(*Xpath.button_reset_contract)
        button_reset_contract.click()
        time.sleep(2)

    def click_button_confirm_reset_contract(self):
        button_confirm_reset_contract = self.find_element(*Xpath.button_confirm_reset_contract)
        button_confirm_reset_contract.click()
        time.sleep(2)

    def click_button_edit_crypto(self):
        button_edit_crypto = self.find_element(*Xpath.button_edit_crypto)
        button_edit_crypto.click()
        time.sleep(2)

    def click_button_crypto_change_record(self):
        button_crypto_change_record = self.find_element(*Xpath.button_crypto_change_record)
        button_crypto_change_record.click()
        time.sleep(2)

    def click_button_crypto_change_record_query(self):
        button_crypto_change_record_query = self.find_element(*Xpath.button_crypto_change_record_query)
        button_crypto_change_record_query.click()
        time.sleep(2)

    def click_field_edit_crypto_protocol(self):
        field_edit_crypto_protocol = self.find_element(*Xpath.field_edit_crypto_protocol)
        field_edit_crypto_protocol.click()
        time.sleep(2)

    def click_option_crypto_protocol(self, protocol):
        if protocol == "ERC20":
            protocol = self.find_element(*Xpath.option_crypto_protocol_ERC20)
        elif protocol == "TRC20":
            protocol = self.find_element(*Xpath.option_crypto_protocol_TRC20)
        elif protocol == "Omni":
            protocol = self.find_element(*Xpath.option_crypto_protocol_Omni)
        protocol.click()
        time.sleep(2)

    def click_button_edit_crypto_status(self):
        button_edit_crypto_status = self.find_element(*Xpath.button_edit_crypto_status)
        button_edit_crypto_status.click()
        time.sleep(2)

    def click_button_edit_crypto_submit(self):
        button_edit_crypto_submit = self.find_element(*Xpath.button_edit_crypto_submit)
        button_edit_crypto_submit.click()
        time.sleep(2)

    def click_button_edit_crypto_submit_confirm(self):
        button_edit_crypto_submit_confirm = self.find_element(*Xpath.button_edit_crypto_submit_confirm)
        button_edit_crypto_submit_confirm.click()

        status = False
        while status is False:
            try:
                self.driver.find_element(*Xpath.title_edit_crypto)
            except Exception as e:
                print(e)
                status = True
                time.sleep(2)

    def click_button_crypto_change_record_close(self):
        button_crypto_change_record_close = self.find_element(*Xpath.button_crypto_change_record_close)
        button_crypto_change_record_close.click()

        status = False
        while status is False:
            try:
                self.driver.find_element(*Xpath.title_edit_crypto)
            except Exception as e:
                print(e)
                status = True
                time.sleep(2)

    def click_turnover_button_calculator(self):
        turnover_button_calculator = self.find_element(*Xpath.turnover_button_calculator)
        turnover_button_calculator.click()
        time.sleep(2)

    def click_turnover_button_calculator_submit(self):
        turnover_button_calculator_submit = self.find_element(*Xpath.turnover_button_calculator_submit)
        turnover_button_calculator_submit.click()
        time.sleep(2)

    def click_turnover_button_calculator_close(self):
        turnover_button_calculator_close = self.find_element(*Xpath.turnover_button_calculator_close)
        turnover_button_calculator_close.click()
        time.sleep(2)

        status = False
        while status is False:
            try:
                self.driver.find_element(*Xpath.turnover_title_calculator)
            except Exception as e:
                print(e)
                status = True
                time.sleep(2)

    def submit_query(self):
        button_search = self.find_element(*Xpath.button_search)
        button_search.click()

    def submit_create_member(self):
        create_member_button_submit = self.find_element(*Xpath.create_member_button_submit)
        create_member_button_submit.click()

    def submit_edit_member(self):
        button_edit_member_submit = self.find_element(*Xpath.button_edit_member_submit)
        button_edit_member_submit.click()

    def submit_fast_deposit_setting(self):
        submit_fast_deposit_setting = self.find_element(*Xpath.submit_fast_deposit_setting)
        submit_fast_deposit_setting.click()

    def submit_modified_required_turnover(self):
        turnover_submit_modify_required = self.find_element(*Xpath.turnover_submit_modify_required)
        turnover_submit_modify_required.click()

        status = False
        while status is False:
            try:
                self.driver.find_element(*Xpath.title_modify_required_turnover)
            except Exception as e:
                print(e)
                status = True
                time.sleep(2)

    def submit_withdrawal_audit_status(self):
        withdrawal_detail_button_audit_submit = self.find_element(*Xpath.withdrawal_detail_button_audit_submit)
        withdrawal_detail_button_audit_submit.click()

        status = False
        while status is False:
            try:
                self.driver.find_element(*Xpath.withdrawal_detail_title)
            except Exception as e:
                print(e)
                status = True
                time.sleep(2)

    def submit_deposit(self):
        button_deposit_submit = self.find_element(*Xpath.button_deposit_submit)
        button_deposit_submit.click()

        status = False
        while status is False:
            try:
                self.driver.find_element(*Xpath.title_deposit)
            except Exception as e:
                print(e)
                status = True
                time.sleep(2)

    def submit_create_contract(self):
        submit_create_contract = self.find_element(*Xpath.submit_create_contract)
        submit_create_contract.click()

        status = False
        while status is False:
            try:
                self.driver.find_element(*Xpath.title_create_contract)
            except Exception as e:
                print(e)
                status = True
                time.sleep(2)

    def switch_third_party_transfer(self):
        time.sleep(3)
        game_transfer_settings = self.find_elements(*Xpath.game_transfer_setting)
        for game_transfer_setting in game_transfer_settings:
            game_transfer_setting.click()
            time.sleep(1)

    def switch_withdrawal_detail_tab(self, tab):
        if tab == "info":
            tab = self.find_element(*Xpath.withdrawal_detail_tab_info)
        elif tab == "turnover":
            tab = self.find_element(*Xpath.withdrawal_detail_tab_turnover)
        elif tab == "summarized":
            tab = self.find_element(*Xpath.withdrawal_detail_tab_summarized)
        elif tab == "log":
            tab = self.find_element(*Xpath.withdrawal_detail_tab_log)
        elif tab == "change":
            tab = self.find_element(*Xpath.withdrawal_detail_tab_change)

        tab.click()
        time.sleep(2)

    def check_search_loading(self):
        time.sleep(2)
        status = False
        count = 0
        while status is False and count < 10:
            try:
                self.driver.find_element_by_xpath(*Xpath.no_result)
                count += 1
                print(count)
                time.sleep(2)
            except Exception as e:
                print(e)
                status = True

    def check_member_search_account(self, account):
        status = False
        count = 0
        while status is False and count < 10:
            try:
                result = self.find_element(*Xpath.member_search_result_account).text
                if result == account:
                    status = True
                count += 1
                time.sleep(2)
            except Exception as e:
                print(e)
                count += 1
                time.sleep(2)

    def check_bet_search_account(self, account):
        status = False
        count = 0
        while status is False and count < 10:
            try:
                result = self.find_element(*Xpath.bet_search_result_account).text
                print(result)
                if result == account:
                    status = True
                count += 1
                time.sleep(2)
            except Exception as e:
                print(e)
                count += 1
                time.sleep(2)

    def check_transaction_search_account(self, account):
        status = False
        count = 0
        while status is False and count < 10:
            try:
                result = self.find_element(*Xpath.transaction_search_result_account).text
                print(result)
                if result == account:
                    status = True
                count += 1
                time.sleep(2)
            except Exception as e:
                print(e)
                count += 1
                time.sleep(2)

    # 小計區預設是關閉故要點擊打開
    def expand_subtotal(self):
        open_subtotal = self.find_element(*Xpath.open_subtotal)
        open_subtotal.click()
        time.sleep(2)

    # 小計區為打開故要點擊關閉
    def collapse_subtotal(self):
        close_subtotal = self.find_element(*Xpath.close_subtotal)
        close_subtotal.click()
        time.sleep(2)

    def input_start_date(self, date):
        self.input(*Xpath.field_search_start_date, contents=date)

    def input_end_date(self, date):
        self.input(*Xpath.field_search_end_date, contents=date)

    def input_account(self, account):
        self.input(*Xpath.create_member_field_name, contents=account)

    def input_password(self, password):
        self.input(*Xpath.create_member_field_pwd, contents=password)

    def input_confirm_password(self, password):
        self.input(*Xpath.create_member_field_confirm_pwd, contents=password)

    def input_nickname(self, nickname):
        self.input(*Xpath.create_member_field_nickname, contents=nickname)

    def input_parent(self, parent):
        self.input(*Xpath.create_member_parent, contents=parent)

    def input_freeze_reason(self, reason):
        self.input(*Xpath.member_field_freeze_reason, contents=reason)

    def input_search_condition_value(self, value):
        self.find_element(*Xpath.advanced_condition_value).send_keys(Keys.CONTROL, 'a')
        self.find_element(*Xpath.advanced_condition_value).send_keys(Keys.DELETE)
        self.input(*Xpath.advanced_condition_value, contents=value)

    def input_turnover_account(self, value):
        self.find_element(*Xpath.turnover_field_account).send_keys(Keys.CONTROL, 'a')
        self.find_element(*Xpath.turnover_field_account).send_keys(Keys.DELETE)
        self.input(*Xpath.turnover_field_account, contents=value)

    def input_field_create_bank_card_name(self, name):
        self.input(*Xpath.bank_data_field_account_name, contents=name)

    def input_field_create_bank_card_num(self, num):
        self.input(*Xpath.bank_data_field_card_num, contents=num)

    def input_field_account_security_field_password(self, password):
        self.input(*Xpath.account_security_field_password, contents=password)

    def input_field_account_security_field_confirm_password(self, password):
        self.input(*Xpath.account_security_field_confirm_password, contents=password)

    def input_field_account_security_field_birthday(self, birthday):
        self.find_element(*Xpath.account_security_field_birthday).click()
        self.input(*Xpath.account_security_field_birthday, contents=birthday)
        self.find_element(*Xpath.account_security_field_birthday).send_keys(Keys.ENTER)

    def input_field_single_fast_deposit_account(self, account):
        self.input(*Xpath.field_single_fast_deposit_account, contents=account)

    def input_field_single_fast_deposit_amount(self, amount):
        self.input(*Xpath.field_single_fast_deposit_amount, contents=amount)
        time.sleep(2)  # 輸入金額，需等發起按鈕亮起

    def input_field_batch_fast_deposit_account(self, account):
        self.input(*Xpath.field_batch_fast_deposit_account, contents=account)

    def input_field_batch_fast_deposit_amount(self, amount):
        self.input(*Xpath.field_batch_fast_deposit_amount, contents=amount)
        time.sleep(2)  # 輸入金額，需等發起按鈕亮起

    def input_field_manual_fast_deposit_account(self, account):
        self.input(*Xpath.field_manual_fast_deposit_account, contents=account)
        time.sleep(2)

    def input_field_manual_fast_deposit_amount(self, amount):
        self.input(*Xpath.field_manual_fast_deposit_amount, contents=amount)

    def input_field_fast_deposit_name(self, name):
        self.find_element(*Xpath.field_fast_deposit_name).click()
        self.input(*Xpath.field_fast_deposit_name, contents=name)

    def input_field_fast_deposit_limit_amount(self, amount):
        self.find_element(*Xpath.field_fast_deposit_limit_amount).click()
        self.input(*Xpath.field_fast_deposit_limit_amount, contents=amount)
        time.sleep(3)  # 輸入金額，需等提交按鈕亮起

    def input_field_activity_type_edit_name(self, activity_type):
        self.find_element(*Xpath.field_activity_type_edit_name).send_keys(Keys.CONTROL, 'a')
        self.find_element(*Xpath.field_activity_type_edit_name).send_keys(Keys.DELETE)
        self.find_element(*Xpath.field_activity_type_edit_name).click()
        self.input(*Xpath.field_activity_type_edit_name, contents=activity_type)

    def input_field_activity_name(self, name):
        self.find_element(*Xpath.field_create_activity_name).send_keys(Keys.CONTROL, 'a')
        self.find_element(*Xpath.field_create_activity_name).send_keys(Keys.DELETE)
        self.find_element(*Xpath.field_create_activity_name).click()
        self.input(*Xpath.field_create_activity_name, contents=name)

    def input_search_activity_name(self, name):
        self.find_element(*Xpath.field_search_activity_name).send_keys(Keys.CONTROL, 'a')
        self.find_element(*Xpath.field_search_activity_name).send_keys(Keys.DELETE)
        self.find_element(*Xpath.field_search_activity_name).click()
        self.input(*Xpath.field_search_activity_name, contents=name)

    def input_field_add_banner_link(self, name):
        time.sleep(2)
        self.find_element(*Xpath.field_add_banner_link).send_keys(Keys.CONTROL, 'a')
        self.find_element(*Xpath.field_add_banner_link).send_keys(Keys.DELETE)
        self.find_element(*Xpath.field_add_banner_link).click()
        self.input(*Xpath.field_add_banner_link, contents=name)

    def input_turnover_field_modify_required(self, amount):
        self.input(*Xpath.turnover_field_modify_required, contents=amount)

    def input_field_search_withdrawal_order_id(self, order_id):
        self.input(*Xpath.withdrawal_field_search_order_id, contents=order_id)

    def input_field_deposit_account(self, account):
        self.input(*Xpath.field_deposit_account, contents=account)

    def input_field_deposit_amount(self, amount):
        self.input(*Xpath.field_deposit_amount, contents=amount)

    def input_field_activity_rule_bonus_amount(self, amount):
        self.input(*Xpath.field_activity_rule_bonus_amount, contents=amount)

    def input_field_activity_rule_turnover_amount(self, amount):
        self.input(*Xpath.field_activity_rule_turnover_amount, contents=amount)

    def input_field_activity_rule_receive_times(self, times):
        self.input(*Xpath.field_activity_rule_receive_times, contents=times)

    def input_field_activity_rule_bonus_upper(self, amount):
        self.input(*Xpath.field_activity_rule_bonus_upper, contents=amount)

    def input_field_activity_rule_valid_bet_multiple(self, multiple):
        self.input(*Xpath.field_activity_rule_ValidBetMultiple, contents=multiple)

    def input_field_create_contract_parent(self, parent):
        self.input(*Xpath.field_create_contract_parent, contents=parent)
        self.find_element(*Xpath.field_create_contract_parent).send_keys(Keys.ENTER)
        time.sleep(2)

    def input_field_create_contract_member(self, member):
        self.input(*Xpath.field_create_contract_member, contents=member)
        self.find_element(*Xpath.field_create_contract_member).send_keys(Keys.ENTER)
        time.sleep(2)

    def input_field_create_contract_headcount(self, headcount):
        self.input(*Xpath.field_create_contract_headcount, contents=headcount)

    def input_field_create_contract_profit(self, profit):
        self.input(*Xpath.field_create_contract_profit, contents=profit)

    def input_field_search_contract_parent(self, parent):
        self.input(*Xpath.field_search_contract_parent, contents=parent)
        self.find_element(*Xpath.field_search_contract_parent).send_keys(Keys.ENTER)
        time.sleep(2)

    def input_field_search_contract_member(self, member):
        self.input(*Xpath.field_search_contract_member, contents=member)
        time.sleep(2)

    def input_field_edit_crypto_rate(self, rate):
        self.input(*Xpath.field_edit_crypto_rate, contents=rate)
        time.sleep(2)

    def input_turnover_field_calculator_amount(self, amount):
        self.find_element(*Xpath.turnover_field_calculator_amount).click()
        self.input(*Xpath.turnover_field_calculator_amount, contents=amount)

    def clear_query_period(self):
        try:
            clear_query_period = self.find_element(*Xpath.clear_query_period)
            clear_query_period.click()
        except Exception as e:
            print(e)

    def clear_login_period(self):
        try:
            clear_login_period = self.find_element(*Xpath.clear_login_period)
            clear_login_period.click()
        except Exception as e:
            print(e)

    def query_account(self, account):
        self.input_search_condition_value(account)
        self.submit_query()

    def query_turnover(self, account):
        self.input_turnover_account(account)
        self.submit_query()

    def query_activity_name(self, name):
        self.input_search_activity_name(name)
        self.submit_query()

    def store_member_search_result(self):
        search_result_account = self.find_element(*Xpath.member_search_result_account).text
        search_result_nickname = self.find_element(*Xpath.member_search_result_nickname).text
        search_result_point = self.find_element(*Xpath.member_search_result_point).text
        search_result_type = self.find_element(*Xpath.member_search_result_type).text
        search_result_level = self.find_element(*Xpath.member_search_result_level).text
        member_result = [search_result_type, search_result_account, search_result_level, search_result_point,
                         search_result_nickname]

        return member_result

    def store_edit_member_basic_data(self):
        status = self.find_element(*Xpath.edit_member_button_status).get_attribute("aria-checked")
        level = self.find_element(*Xpath.edit_member_field_member_level).text
        return_point = self.find_element(*Xpath.edit_member_field_return).get_attribute("value")
        placebet = self.find_element(*Xpath.edit_member_button_placebet).get_attribute("aria-checked")
        deposit = self.find_element(*Xpath.edit_member_button_deposit).get_attribute("aria-checked")
        withdraw = self.find_element(*Xpath.edit_member_button_withdraw).get_attribute("aria-checked")
        transfer = self.find_element(*Xpath.edit_member_button_transfer).get_attribute("aria-checked")
        basic_data = [status, level, return_point, placebet, deposit, withdraw, transfer]

        return basic_data

    def store_edit_member_bank_card(self):
        bank_name = self.find_element(*Xpath.bank_data_field_bank_name).text
        return bank_name

    def store_edit_member_account_setting(self):
        count = 0
        game_transfer_settings = self.find_elements(*Xpath.game_transfer_setting)
        for game_transfer_setting in game_transfer_settings:
            game_transfer_settings[count] = game_transfer_setting.get_attribute("aria-checked")
            count += 1

        return game_transfer_settings

    def store_edit_member_summarized_log(self):
        count = 0
        status = False
        retry = 0

        while status is False and retry < 30:
            try:
                self.driver.find_element_by_xpath(Xpath.summarized_log)
                status = True
            except Exception as e:
                print(e)
                time.sleep(2)
                retry += 1

        summarized_log_columns = self.find_elements(*Xpath.summarized_log_column)
        summarized_log_columns.pop(0)
        for summarized_log_column in summarized_log_columns:
            data = summarized_log_column.text.split("\n")

            if count in [3, 5, 7, 10, 11, 12]:
                try:
                    data[1] = int(float(data[1].replace(",", "")))
                except Exception as e:
                    print(e)

            summarized_log_columns[count] = int(float(data[1]))
            count += 1

        return summarized_log_columns

    def store_edit_member_change_log(self):
        status = False
        retry = 0

        while status is False and retry < 30:
            try:
                self.driver.find_element_by_xpath(Xpath.change_log_item_exist)
                status = True
            except Exception as e:
                print(e)
                time.sleep(2)
                retry += 1

        change_item = self.find_element(*Xpath.change_log_first_item).text
        return change_item

    def store_member_freeze_change_log(self):
        status = False
        retry = 0

        while status is False and retry < 30:
            try:
                self.driver.find_element_by_xpath(Xpath.change_log_item_exist)
                status = True
            except Exception as e:
                print(e)
                time.sleep(2)
                retry += 1

        change_item = self.find_elements(*Xpath.change_log_items)
        change_log = []

        for data in change_item:
            change_log.append(data.text)

        return change_log

    def store_fast_deposit_subtotal(self):
        time.sleep(5)
        subtotal_deposit_order = self.find_element(*Xpath.subtotal_fast_deposit_order).text
        subtotal_deposit_account = self.find_element(*Xpath.subtotal_fast_deposit_account).text
        subtotal_deposit_amount = float(self.find_element(*Xpath.subtotal_fast_deposit_amount).text.replace(",", ""))
        subtotal_deposit_giveawayAmount = float(self.find_element(*Xpath.subtotal_fast_deposit_giveawayAmount)
                                                .text.replace(",", ""))
        subtotal_deposit_preferentialAmount = float(self.find_element(*Xpath.subtotal_fast_deposit_preferentialAmount)
                                                    .text.replace(",", ""))
        subtotal_deposit = [subtotal_deposit_order, subtotal_deposit_account, subtotal_deposit_amount,
                            subtotal_deposit_giveawayAmount, subtotal_deposit_preferentialAmount]
        return subtotal_deposit

    def store_fast_deposit_setting(self):
        fast_deposit_name = self.find_element(*Xpath.field_fast_deposit_name).get_attribute("value")
        fast_deposit_type = self.find_element(*Xpath.value_fast_deposit_type).text
        fast_deposit_subtype = self.find_element(*Xpath.field_fast_deposit_subtype).text
        fast_deposit_audit = self.find_element(*Xpath.button_fast_deposit_audit).text
        fast_deposit_turnover = self.find_element(*Xpath.field_fast_deposit_turnover).get_attribute(
            "aria-valuenow") + "倍"
        fast_deposit_count_per_day = self.find_element(*Xpath.field_fast_deposit_count_per_day).get_attribute(
            "aria-valuenow")
        fast_deposit_limit_amount = type(
            float(self.find_element(*Xpath.field_fast_deposit_limit_amount).get_attribute("value").replace(",", "")))
        fast_deposit_isEnable = self.find_element(*Xpath.button_fast_deposit_isEnable).get_attribute("aria-checked")

        if fast_deposit_isEnable == 'true':
            fast_deposit_isEnable = '启用'
        elif fast_deposit_isEnable == 'false':
            fast_deposit_isEnable = '停用'

        fast_deposit_setting = [fast_deposit_name, fast_deposit_type, fast_deposit_subtype, fast_deposit_audit,
                                fast_deposit_turnover, fast_deposit_count_per_day, fast_deposit_limit_amount,
                                fast_deposit_isEnable]
        return fast_deposit_setting

    def store_fast_deposit_setting_result(self):
        fast_deposit_name = self.find_element(*Xpath.fast_deposit_setting_result_name).text
        fast_deposit_type = self.find_element(*Xpath.fast_deposit_setting_result_type).text
        fast_deposit_subtype = self.find_element(*Xpath.fast_deposit_setting_result_subtype).text
        fast_deposit_audit = self.find_element(*Xpath.fast_deposit_setting_result_audit).text
        fast_deposit_turnover = self.find_element(*Xpath.fast_deposit_setting_result_turnover).text
        fast_deposit_count_per_day = self.find_element(*Xpath.fast_deposit_setting_result_count_per_day).text
        fast_deposit_limit_amount = type(
            float(self.find_element(*Xpath.fast_deposit_setting_result_limit_amount).text.replace(",", "")))
        fast_deposit_isEnable = self.find_element(*Xpath.fast_deposit_setting_result_isEnable).text
        fast_deposit_setting_result = [fast_deposit_name, fast_deposit_type, fast_deposit_subtype, fast_deposit_audit,
                                       fast_deposit_turnover, fast_deposit_count_per_day, fast_deposit_limit_amount,
                                       fast_deposit_isEnable]
        return fast_deposit_setting_result

    def store_bet_subtotal(self):
        time.sleep(5)
        subtotal_bet_order_count = self.find_element(*Xpath.subtotal_bet_order_count).text
        subtotal_bet_account = self.find_element(*Xpath.subtotal_bet_account).text
        subtotal_bet_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_bet_amount)).text.replace(",", "")).quantize(Decimal('.01'),
                                                                                                    rounding=ROUND_DOWN))
        subtotal_bet_available_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_bet_available_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        subtotal_bet_user_win_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_bet_user_win_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        subtotal_bet_platform_win_loss = str(
            Decimal((self.find_element(*Xpath.subtotal_bet_platform_win_loss)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))

        subtotal_bet = [subtotal_bet_order_count, subtotal_bet_account, subtotal_bet_amount,
                        subtotal_bet_available_amount,
                        subtotal_bet_user_win_amount, subtotal_bet_platform_win_loss]
        return subtotal_bet

    def store_transaction_subtotal(self):
        time.sleep(5)
        subtotal_total_count = self.find_element(*Xpath.subtotal_total_count).text.replace(",", "")
        subtotal_incoming_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_incoming_amount)).text.replace(",", "")).quantize(Decimal('.01'),
                                                                                                         rounding=ROUND_DOWN))
        subtotal_outgoing_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_outgoing_amount)).text.replace(",", "")).quantize(Decimal('.01'),
                                                                                                         rounding=ROUND_DOWN))
        subtotal_balance_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_balance_amount)).text.replace(",", "")).quantize(Decimal('.01'),
                                                                                                        rounding=ROUND_DOWN))

        subtotal_deposit = [subtotal_total_count, subtotal_incoming_amount, subtotal_outgoing_amount,
                            subtotal_balance_amount]
        return subtotal_deposit

    def store_column_bet_source(self):
        time.sleep(5)
        column_bet_source = self.find_elements(*Xpath.column_bet_source)
        return column_bet_source

    def store_column_bet_status(self):
        time.sleep(5)
        column_bet_status = self.find_elements(*Xpath.column_bet_status)
        return column_bet_status

    def store_column_bet_winLoss(self):
        time.sleep(5)
        column_bet_winLoss = self.find_elements(*Xpath.column_bet_winLoss)
        return column_bet_winLoss

    def store_column_bet_account(self):
        time.sleep(5)
        column_bet_account = self.find_elements(*Xpath.column_bet_account)
        return column_bet_account

    def store_column_transaction_type(self):
        time.sleep(5)
        column_transaction_type = self.find_elements(*Xpath.column_transaction_type)
        return column_transaction_type

    def store_column_transaction_account(self):
        time.sleep(5)
        column_transaction_account = self.find_elements(*Xpath.column_transaction_account)
        return column_transaction_account

    def store_field_activity_type_edit_name(self):
        field_activity_type_edit_name = self.find_element(*Xpath.field_activity_type_edit_name).get_attribute("value")
        return field_activity_type_edit_name

    def store_button_activity_type_edit_status(self):
        button_activity_type_edit_status = self.find_element(*Xpath.button_activity_type_edit_status).text
        return button_activity_type_edit_status

    def store_activity_type_config(self):
        activity_type_name = \
            ((self.find_elements(*Xpath.column_activity_type_name))[0].text.replace("\n停用", "").split(' '))[0]
        activity_type_status = (self.find_elements(*Xpath.column_activity_type_status))[0].text
        result = [activity_type_name, activity_type_status]
        return result

    def store_field_create_activity_name(self):
        field_create_activity_name = self.find_element(*Xpath.field_create_activity_name).get_attribute("value")
        return field_create_activity_name

    def store_field_create_activity_type(self):
        field_create_activity_type = self.find_element(*Xpath.field_create_activity_type).text
        return field_create_activity_type

    def store_column_activity_name(self):
        column_activity_name = self.find_element(*Xpath.column_activity_name).text
        return column_activity_name

    def store_column_activity_type(self):
        column_activity_type = self.find_element(*Xpath.column_activity_type).text
        return column_activity_type

    def store_affiliate_log_subtotal(self):
        time.sleep(5)
        affiliate_cnt = self.find_element(*Xpath.subtotal_affiliate_affilate_cnt).text.replace(",", "")
        member_tree_cnt = str(
            Decimal((self.find_element(*Xpath.subtotal_member_tree_cnt)).text.replace(",", "")).quantize(Decimal('.01'),
                                                                                                         rounding=ROUND_DOWN))
        register_cnt = str(
            Decimal((self.find_element(*Xpath.subtotal_affiliate_register_cnt)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        deposit_first_timeCnt = str(Decimal(
            (self.find_element(*Xpath.subtotal_affiliate_deposit_first_timeCnt)).text.replace(",", "")).quantize(
            Decimal('.01'), rounding=ROUND_DOWN))
        deposit_cnt = str(
            Decimal((self.find_element(*Xpath.subtotal_affiliate_deposit_cnt)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        deposit3_cnt = str(
            Decimal((self.find_element(*Xpath.subtotal_affiliate_deposit3_cnt)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        deposit5_cnt = str(
            Decimal((self.find_element(*Xpath.subtotal_affiliate_deposit5_cnt)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        bet_member_cnt = str(
            Decimal((self.find_element(*Xpath.subtotal_affiliate_bet_member_cnt)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        bet_order_cnt = str(
            Decimal((self.find_element(*Xpath.subtotal_affiliate_bet_order_cnt)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        bet_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_affiliate_bet_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        valid_bet_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_affiliate_valid_bet_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        bonus_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_affiliate_bonus_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        win_loss_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_affiliate_win_loss_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        deposit_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_affiliate_deposit_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        withdrawal_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_affiliate_withdrawal_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        dep_with_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_affiliate_dep_with_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        deduction_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_affiliate_deduction_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        rmAddition_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_affiliate_rmAddition_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        pre_payment_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_affiliate_pre_payment_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        commission_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_affiliate_commission_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        return_point_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_affiliate_return_point_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        fee = str(
            Decimal((self.find_element(*Xpath.subtotal_affiliate_fee)).text.replace(",", "")).quantize(Decimal('.01'),
                                                                                                       rounding=ROUND_DOWN))
        administration_fee = str(
            Decimal((self.find_element(*Xpath.subtotal_affiliate_administration_fee)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        member_balance = str(
            Decimal((self.find_element(*Xpath.subtotal_affiliate_member_balance)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        total_win_loss_amount = str(Decimal(
            (self.find_element(*Xpath.subtotal_affiliate_total_win_loss_amount)).text.replace(",", "")).quantize(
            Decimal('.01'), rounding=ROUND_DOWN))

        subtotal = [affiliate_cnt, member_tree_cnt, register_cnt, deposit_first_timeCnt, deposit_cnt, deposit3_cnt,
                    deposit5_cnt, bet_member_cnt, bet_order_cnt, bet_amount, valid_bet_amount, bonus_amount,
                    win_loss_amount, deposit_amount, withdrawal_amount, dep_with_amount, deduction_amount,
                    rmAddition_amount, pre_payment_amount, commission_amount, return_point_amount, fee,
                    administration_fee, member_balance, total_win_loss_amount]
        return subtotal

    def store_member_log_subtotal(self):
        time.sleep(5)
        member_cnt = self.find_element(*Xpath.subtotal_member_cnt).text.replace(",", "")
        bet_order_cnt = str(
            Decimal((self.find_element(*Xpath.subtotal_member_bet_order_cnt)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        bet_amount = str(Decimal((self.find_element(*Xpath.subtotal_member_bet_amount)).text.replace(",", "")).quantize(
            Decimal('.01'), rounding=ROUND_DOWN))
        valid_bet_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_member_valid_bet_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        bonus_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_member_bonus_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        win_loss_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_member_win_loss_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        deposit_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_member_deposit_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        withdrawal_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_member_withdrawal_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        dep_with_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_member_depwith_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        deduction_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_member_deduction_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        rmaddition_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_member_rmaddition_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        prepayment_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_member_prepayment_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        returnpoint_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_member_returnpoint_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        fee = str(
            Decimal((self.find_element(*Xpath.subtotal_member_fee)).text.replace(",", "")).quantize(Decimal('.01'),
                                                                                                    rounding=ROUND_DOWN))
        administration_fee = str(
            Decimal((self.find_element(*Xpath.subtotal_member_administration_fee)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        member_balance = str(
            Decimal((self.find_element(*Xpath.subtotal_member_member_balance)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        totalwinloss_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_member_totalwinloss_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))

        subtotal = [member_cnt, bet_order_cnt, bet_amount, valid_bet_amount, bonus_amount, win_loss_amount, "0",
                    deposit_amount, withdrawal_amount, dep_with_amount, deduction_amount, rmaddition_amount,
                    prepayment_amount, returnpoint_amount, fee, administration_fee, member_balance, totalwinloss_amount]
        return subtotal

    def store_agent_log_subtotal(self):
        time.sleep(5)
        bet_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_op_report_agent_bet_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        valid_bet_amount = str(Decimal(
            (self.find_element(*Xpath.subtotal_op_report_agent_validbet_amount)).text.replace(",", "")).quantize(
            Decimal('.01'), rounding=ROUND_DOWN))
        bonus_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_op_report_agent_bonus_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        win_loss_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_op_report_agent_winloss_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))

        subtotal = [bet_amount, valid_bet_amount, bonus_amount, win_loss_amount]

        return subtotal

    def store_affiliate_report_result(self):
        affiliate_cnt = self.find_element(*Xpath.column_affiliate_report_affiliate_cnt).text
        affiliate_cnt = affiliate_cnt.split(" ")
        status = False
        data = [affiliate_cnt[5], "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                "0", "0", "0", "0", "0", "0", "0"]

        while status is False:
            member_tree_cnt = self.find_elements(*Xpath.column_affiliate_report_member_tree_cnt)
            register_cnt = self.find_elements(*Xpath.column_affiliate_report_register_cnt)
            first_timeCnt = self.find_elements(*Xpath.column_affiliate_report_first_timeCnt)
            deposit_cnt = self.find_elements(*Xpath.column_affiliate_report_deposit_cnt)
            deposit3_cnt = self.find_elements(*Xpath.column_affiliate_report_deposit3_cnt)
            deposit5_cnt = self.find_elements(*Xpath.column_affiliate_report_deposit5_cnt)
            bet_member_cnt = self.find_elements(*Xpath.column_affiliate_report_bet_member_cnt)
            bet_order_cnt = self.find_elements(*Xpath.column_affiliate_report_bet_order_cnt)
            bet_amount = self.find_elements(*Xpath.column_affiliate_report_bet_amount)
            valid_bet_amount = self.find_elements(*Xpath.column_affiliate_report_valid_bet_amount)
            bonus_amount = self.find_elements(*Xpath.column_affiliate_report_bonus_amount)
            win_loss_amount = self.find_elements(*Xpath.column_affiliate_report_win_loss_amount)
            deposit_amount = self.find_elements(*Xpath.column_affiliate_report_deposit_amount)
            withdrawal_amount = self.find_elements(*Xpath.column_affiliate_report_withdrawal_amount)
            dep_with_amount = self.find_elements(*Xpath.column_affiliate_report_dep_with_amount)
            deduction_amount = self.find_elements(*Xpath.column_affiliate_report_deduction_amount)
            rmAddition_amount = self.find_elements(*Xpath.column_affiliate_report_rmAddition_amount)
            pre_payment_amount = self.find_elements(*Xpath.column_affiliate_report_pre_payment_amount)
            commission_amount = self.find_elements(*Xpath.column_affiliate_report_commission_amount)
            return_point_amount = self.find_elements(*Xpath.column_affiliate_report_return_point_amount)
            fee = self.find_elements(*Xpath.column_affiliate_report_fee)
            administration_fee = self.find_elements(*Xpath.column_affiliate_report_administration_fee)
            member_balance = self.find_elements(*Xpath.column_affiliate_report_member_balance)
            total_win_loss_amount = self.find_elements(*Xpath.column_affiliate_report_total_win_loss_amount)

            columns = [member_tree_cnt, register_cnt, first_timeCnt, deposit_cnt, deposit3_cnt, deposit5_cnt,
                       bet_member_cnt, bet_order_cnt, bet_amount, valid_bet_amount, bonus_amount, win_loss_amount,
                       deposit_amount, withdrawal_amount, dep_with_amount, deduction_amount, rmAddition_amount,
                       pre_payment_amount, commission_amount, return_point_amount, fee, administration_fee,
                       member_balance, total_win_loss_amount]

            count = 1
            for column in columns:
                for el in column:
                    sum_column = Decimal(data[count])
                    sum_column = sum_column + Decimal(el.text.replace(",", ""))
                    data[count] = str(sum_column.quantize(Decimal('.01'), rounding=ROUND_DOWN))

                count += 1

            try:
                self.find_element(*Xpath.button_next_page).click()
                time.sleep(10)
            except Exception as e:
                print(e)
                self.find_element(*Xpath.button_end_page)
                status = True
        return data

    def store_member_report_result(self):
        member_cnt = self.find_element(*Xpath.column_member_report_member_cnt).text
        member_cnt = member_cnt.split(" ")
        status = False
        data = [member_cnt[5], "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]

        while status is False:
            bet_order_cnt = self.find_elements(*Xpath.column_member_report_bet_order_cnt)
            bet_amount = self.find_elements(*Xpath.column_member_report_bet_amount)
            valid_bet_amount = self.find_elements(*Xpath.column_member_report_valid_bet_amount)
            bonus_amount = self.find_elements(*Xpath.column_member_report_bonus_amount)
            win_loss_amount = self.find_elements(*Xpath.column_member_report_win_loss_amount)
            deposit_amount = self.find_elements(*Xpath.column_member_report_deposit_amount)
            withdrawal_amount = self.find_elements(*Xpath.column_member_report_withdrawal_amount)
            depwith_amount = self.find_elements(*Xpath.column_member_report_depwith_amount)
            deduction_amount = self.find_elements(*Xpath.column_member_report_deduction_amount)
            rmaddition_amount = self.find_elements(*Xpath.column_member_report_rmaddition_amount)
            prepayment_amount = self.find_elements(*Xpath.column_member_report_prepayment_amount)
            returnpoint_amount = self.find_elements(*Xpath.column_member_report_returnpoint_amount)
            fee = self.find_elements(*Xpath.column_member_report_fee)
            administration_fee = self.find_elements(*Xpath.column_member_report_administration_fee)
            member_balance = self.find_elements(*Xpath.column_member_report_member_balance)
            totalwinloss_amount = self.find_elements(*Xpath.column_member_report_totalwinloss_amount)

            columns = [bet_order_cnt, bet_amount, valid_bet_amount, bonus_amount, win_loss_amount, "",
                       deposit_amount, withdrawal_amount, depwith_amount, deduction_amount, rmaddition_amount,
                       prepayment_amount, returnpoint_amount, fee, administration_fee, member_balance,
                       totalwinloss_amount]

            count = 1
            for column in columns:
                for el in column:
                    if count == 6:
                        data[count] = "0"
                    else:
                        sum_column = float(data[count])
                        sum_column = sum_column + float(el.text.replace(",", ""))
                        data[count] = str('%.2f' % sum_column)
                count += 1

            try:
                self.find_element(*Xpath.button_next_page).click()
                time.sleep(10)
            except Exception as e:
                print(e)
                self.find_element(*Xpath.button_end_page)
                status = True

        return data

    def store_agent_report_result(self):
        data = ["0", "0", "0", "0"]

        bet_amount = self.find_elements(*Xpath.column_op_report_agent_bet_amount)
        valid_bet_amount = self.find_elements(*Xpath.column_op_report_agent_validbet_amount)
        bonus_amount = self.find_elements(*Xpath.column_op_report_agent_bonus_amount)
        win_loss_amount = self.find_elements(*Xpath.column_op_report_agent_winloss_amount)

        columns = [bet_amount, valid_bet_amount, bonus_amount, win_loss_amount]

        count = 0
        for column in columns:
            for el in column:
                sum_column = float(data[count])
                sum_column = sum_column + float(el.text.replace(",", ""))
                data[count] = str('%.2f' % sum_column)
            count += 1

        return data

    def store_transaction_log_amount(self):
        status = False
        data = "0"

        while status is False:
            transaction_amount = self.find_elements(*Xpath.column_transaction_amount)
            for el in transaction_amount:
                sum_column = Decimal(data)
                sum_column = sum_column + Decimal(el.text.replace(",", ""))
                data = str(sum_column.quantize(Decimal('.01'), rounding=ROUND_DOWN))

            try:
                self.find_element(*Xpath.button_next_page).click()
                time.sleep(10)
            except Exception as e:
                print(e)
                self.find_element(*Xpath.button_end_page)
                status = True

            self.check_search_loading()

        return data

    def store_bet_log_result(self):
        time.sleep(5)
        status = False
        order_cnt = self.find_element(*Xpath.column_bet_order_cnt).text
        order_cnt = order_cnt.split(" ")
        data = [order_cnt[5], "0", "0", "0"]

        while status is False:
            bet_amount = self.find_elements(*Xpath.column_bet_amount)
            valid_bet_amount = self.find_elements(*Xpath.column_bet_valid_amount)
            bonus_amount = self.find_elements(*Xpath.column_bet_bonus_amount)
            columns = [bet_amount, valid_bet_amount, bonus_amount]

            count = 1
            for column in columns:
                for el in column:
                    sum_column = float(data[count])
                    sum_column = sum_column + float(el.text.replace(",", ""))
                    data[count] = str('%.2f' % sum_column)

                count += 1

            try:
                self.find_element(*Xpath.button_next_page).click()
                time.sleep(10)
            except Exception as e:
                print(e)
                self.find_element(*Xpath.button_end_page)
                status = True

        return data

    def store_turnover_list(self):
        amount_el = self.find_elements(*Xpath.turnover_column_amount)
        required_el = self.find_elements(*Xpath.turnover_column_required)
        amount = []
        required = []

        for el in amount_el:
            amount.append(el.text)

        for el in required_el:
            required.append(el.text)
        print('amount')
        print(amount)
        print('required')
        print(required)
        return amount, required

    def store_withdrawal_result_order_id(self):
        order_id = self.find_elements(*Xpath.withdrawal_result_field_order_id)
        return order_id[0].text

    def store_withdrawal_change_column_after(self):
        status = []
        column_after = self.find_elements(*Xpath.withdrawal_detail_change_column_after)

        for after in column_after:
            status.append(after.text)

        return status

    def store_deposit_subtotal(self):
        time.sleep(5)
        subtotal_deposit_order = self.find_element(*Xpath.subtotal_deposit_order).text
        subtotal_deposit_account = self.find_element(*Xpath.subtotal_deposit_account).text
        subtotal_deposit_order_amount = float(
            self.find_element(*Xpath.subtotal_deposit_order_amount).text.replace(",", ""))
        subtotal_deposit_incomeAmount = float(
            self.find_element(*Xpath.subtotal_deposit_incomeAmount).text.replace(",", ""))
        subtotal_deposit_fee_platform = float(
            self.find_element(*Xpath.subtotal_deposit_fee_platform).text.replace(",", ""))
        subtotal_deposit_fee_member = float(
            self.find_element(*Xpath.subtotal_deposit_fee_platform).text.replace(",", ""))
        subtotal_deposit_amount = float(self.find_element(*Xpath.subtotal_deposit_fee_platform).text.replace(",", ""))
        subtotal_deposit_preferentialAmount = float(
            self.find_element(*Xpath.subtotal_deposit_fee_platform).text.replace(",", ""))
        subtotal_deposit = [subtotal_deposit_order, subtotal_deposit_account, subtotal_deposit_order_amount,
                            subtotal_deposit_incomeAmount,
                            subtotal_deposit_fee_platform, subtotal_deposit_fee_member, subtotal_deposit_amount,
                            subtotal_deposit_preferentialAmount]

        return subtotal_deposit

    def store_activity_detail(self):
        column_activity_detail_bonus_amount = \
            self.find_element(*Xpath.column_activity_detail_bonus_amount).text.split(".")[0]
        column_activity_detail_turnover = self.find_element(*Xpath.column_activity_detail_turnover).text.split(".")[0]
        column_activity_detail_receive_times = self.find_element(*Xpath.column_activity_detail_receive_times).text
        column_activity_detail_bonus_upper = \
            self.find_element(*Xpath.column_activity_detail_bonus_upper).text.split(".")[0]
        column_activity_detail_ValidBetMultiple = \
            self.find_element(*Xpath.column_activity_detail_ValidBetMultiple).text.split(".")[0]
        detail = [column_activity_detail_bonus_amount, column_activity_detail_turnover,
                  column_activity_detail_receive_times,
                  column_activity_detail_bonus_upper, column_activity_detail_ValidBetMultiple]
        return detail

    def store_activity_bonus_upper(self):
        time.sleep(2)
        bonus_upper = self.find_element(*Xpath.field_activity_rule_bonus_upper).get_attribute("aria-valuenow")
        return bonus_upper

    def store_column_contract_search_result(self):
        time.sleep(2)
        column_contract_search_result = self.find_elements(*Xpath.column_contract_search_result)
        search_result = []

        for data in column_contract_search_result:
            search_result.append(data.text)

        return search_result

    def store_column_crypto_result_exchange_rate(self):
        time.sleep(2)
        exchange_rate = self.find_element(*Xpath.column_crypto_search_result_rate).text
        return exchange_rate

    def store_crypto_change_log(self):
        column_crypto_change_record_before = self.find_element(*Xpath.column_crypto_change_record_before).text
        column_crypto_change_record_after = self.find_element(*Xpath.column_crypto_change_record_after).text
        change_log = [column_crypto_change_record_before, column_crypto_change_record_after]
        return change_log

    def store_turnover_subtotal_valid_bet_amount(self):
        turnover_subtotal_valid_bet_amount = self.find_element(*Xpath.turnover_subtotal_valid_bet_amount).text.replace(
            ",", "")
        return turnover_subtotal_valid_bet_amount

    def store_turnover_subtotal_current(self):
        subtotal_current = self.find_elements(*Xpath.turnover_subtotal_current)
        turnover_subtotal_current = []

        for current in subtotal_current:
            turnover_subtotal_current.append(current.text.replace(",", ""))
        return turnover_subtotal_current

    def store_turnover_calculator_shortage_amount(self, required_turnover, valid_bet_amount):
        if required_turnover > valid_bet_amount:
            turnover_field_calculator_shortage_amount = \
                self.find_element(*Xpath.turnover_field_calculator_shortage_amount).text.split(" ")[1]
            return turnover_field_calculator_shortage_amount
        else:
            if self.find_element(*Xpath.turnover_field_calculator_shortage_amount):
                return "1"
            else:
                return "0"

    def fill_query_date(self):
        dt = datetime.datetime.today()  # 獲得當地時間
        dt_str = dt.strftime("%Y-%m-%d")  # 格式化日期
        start_timestamp = int(
            datetime.datetime.strptime(dt_str + " 00:00:00", '%Y-%m-%d %H:%M:%S').timestamp()) - 2678400
        start_date = datetime.datetime.fromtimestamp(start_timestamp).strftime("%Y-%m-%d %H:%M:%S")
        end_date = dt_str + " 23:59:59"

        self.click_field_search_start_date()
        self.input_start_date(start_date)
        self.click_field_search_end_date()
        self.input_end_date(end_date)
        self.click_button_confirm_date()

    def click_field_status_type_search(self):
        field_status_search = self.find_element(*Xpath.field_status_type_search)
        field_status_search.click()
        time.sleep(2)

    def click_option_status_type_search(self, status_types, num):
        self.click_field_status_type_search()
        option_status_search = self.find_elements(*Xpath.option_status_search)
        option_status = None
        if status_types == 'thirdparty-bet':
            # 0:全部 1:已結算 2:未结算 3:取消订单 4:提早结算
            print(num)
            option_status = option_status_search[num]

        status = option_status.text
        print('status')
        print(status)
        option_status.click()
        time.sleep(2)

    def select_activity_type(self):
        self.click_field_create_activity_type()
        self.click_option_create_activity_type_first()

    def create_affiliate(self, parent=""):
        dt = datetime.datetime.today()  # 獲得當地時間
        dt_str = dt.strftime("%Y%m%d%H%M")  # 格式化日期
        account = "qa" + dt_str
        password = "Aa12345"

        self.click_create_affiliate()
        member_type = self.find_element(*Xpath.create_member_field_type).text
        create_member_field_level = self.find_element(*Xpath.create_member_field_level).text
        create_member_field_return_point = self.find_element(*Xpath.create_member_field_point).get_attribute("value")
        self.input_account(account)
        self.input_password(password)
        self.input_confirm_password(password)
        self.input_nickname(account)
        self.input_parent(parent)
        time.sleep(5)
        self.submit_create_member()
        time.sleep(10)
        self.click_button_back()
        member_info = [member_type, account, create_member_field_level, create_member_field_return_point, account]

        return member_info

    def create_member(self, parent=""):
        dt = datetime.datetime.today()  # 獲得當地時間
        dt_str = dt.strftime("%Y%m%d%H%M")  # 格式化日期
        account = "qm" + dt_str
        password = "Aa12345"

        self.click_create_member()
        member_type = self.find_element(*Xpath.create_member_field_type).text
        create_member_field_level = self.find_element(*Xpath.create_member_field_level).text
        create_member_field_return_point = self.find_element(*Xpath.create_member_field_point).get_attribute("value")
        self.input_account(account)
        self.input_password(password)
        self.input_confirm_password(password)
        self.input_nickname(account)
        self.input_parent(parent)
        time.sleep(5)
        self.submit_create_member()
        time.sleep(10)
        self.click_button_back()

        member_info = [member_type, account, create_member_field_level, create_member_field_return_point, account]

        return member_info

    def create_bank_card(self):
        dt = datetime.datetime.today()  # 獲得當地時間
        dt_str = dt.strftime("%Y%m%d%H%M%S")  # 格式化日期
        account = "qa test"
        card_num = dt_str + "00"

        self.input_field_create_bank_card_name(account)
        self.click_bank_data_field_bank()
        time.sleep(1)
        self.click_bank_data_option_bank()
        self.input_field_create_bank_card_num(card_num)
        bank_name = self.store_edit_member_bank_card()
        self.submit_edit_member()

        return bank_name

    def modify_password(self, password):
        time.sleep(2)
        self.input_field_account_security_field_password(password)
        self.input_field_account_security_field_confirm_password(password)
        self.submit_edit_member()

    def modify_birthday(self, birthday):
        time.sleep(2)
        self.input_field_account_security_field_birthday(birthday)
        self.submit_edit_member()
        time.sleep(2)
        self.click_account_security_button_confirm_birthday()

    def execute_fast_deposit(self, deposit, account, amount):
        if deposit == 'single':
            self.click_tab_single_deposit()
            self.input_field_single_fast_deposit_account(account)
            self.input_field_single_fast_deposit_amount(amount)
            time.sleep(5)
            self.click_button_single_fast_deposit_submit()
        elif deposit == 'batch':
            self.click_tab_batch_deposit()
            self.input_field_batch_fast_deposit_account(account)
            self.input_field_batch_fast_deposit_amount(amount)
            time.sleep(5)
            self.click_button_batch_fast_deposit_submit()
        elif deposit == 'manual':
            self.click_tab_batch_deposit()
            self.click_tab_manual_deposit()
            self.input_field_manual_fast_deposit_account(account)
            self.input_field_manual_fast_deposit_amount(amount)
            time.sleep(5)
            self.click_button_manual_fast_deposit_submit()

    def execute_fast_deposit_promote(self, deposit, account, amount):
        if deposit == 'single':
            self.click_tab_single_deposit()
            self.input_field_single_fast_deposit_account(account)
            self.click_field_single_fast_deposit_type()
            self.click_option_single_fast_deposit_promote()
            self.input_field_single_fast_deposit_amount(amount)
            time.sleep(5)
            self.click_button_single_fast_deposit_submit()
        elif deposit == 'batch':
            self.click_tab_batch_deposit()
            self.input_field_batch_fast_deposit_account(account)
            self.input_field_batch_fast_deposit_amount(amount)
            time.sleep(5)
            self.click_button_batch_fast_deposit_submit()

    def execute_deposit(self, account, amount):
        self.input_field_deposit_account(account)
        self.input_field_deposit_amount(amount)
        time.sleep(5)
        self.submit_deposit()

    def create_fast_deposit_setting(self):
        dt = datetime.datetime.today()  # 獲得當地時間
        dt_str = dt.strftime("%Y%m%d%H%M")  # 格式化日期
        name = "qa" + dt_str
        amount = self.random_deposit_setting_amount()

        self.click_button_create_fast_deposit_setting()
        time.sleep(3)
        self.input_field_fast_deposit_name(name)
        self.click_field_fast_deposit_type()
        time.sleep(1)
        self.click_option_fast_deposit_type()
        self.click_field_fast_deposit_subtype()
        time.sleep(1)
        self.click_option_fast_deposit_subtype()
        self.click_button_fast_deposit_increase_turnover()
        self.click_button_fast_deposit_increase_count_per_day()
        # self.click_button_fast_deposit_increase_calculated()
        self.input_field_fast_deposit_limit_amount(amount)
        fast_deposit_setting = self.store_fast_deposit_setting()
        self.submit_fast_deposit_setting()

        return fast_deposit_setting

    def search_fast_deposit_setting(self):
        time.sleep(3)
        self.click_button_fast_deposit_setting_search()
        fast_deposit_setting_result = self.store_fast_deposit_setting_result()

        return fast_deposit_setting_result

    def set_banner_display_period(self):
        self.click_field_add_banner_start()
        self.click_button_add_banner_now()
        self.click_button_add_banner_forever()

    def input_search_operation_report_condition_value(self, value):  # Adam
        self.find_element(*Xpath.operation_report_advanced_condition_value).send_keys(Keys.CONTROL, 'a')
        self.find_element(*Xpath.operation_report_advanced_condition_value).send_keys(Keys.DELETE)
        self.input(*Xpath.operation_report_advanced_condition_value, contents=value)

    def operation_report_column_member_account(self):
        time.sleep(5)
        column_transaction_account = self.find_elements(*Xpath.column_member_accounts)
        return column_transaction_account

    def query_operation_report_account(self, account):
        self.input_search_operation_report_condition_value(account)
        self.submit_query()

    def OP_submit_query(self):
        self.submit_query()

    def operation_report_affiliate(self):
        time.sleep(5)
        affiliate_cnt = self.find_element(*Xpath.subtotal_affiliate_affilate_cnt).text.replace(",", "")
        member_tree_cnt = self.find_element(*Xpath.subtotal_member_tree_cnt).text.replace(",", "")
        register_cnt = self.find_element(*Xpath.subtotal_affiliate_register_cnt).text.replace(",", "")
        deposit_first_timeCnt = self.find_element(*Xpath.subtotal_affiliate_deposit_first_timeCnt).text.replace(",", "")
        deposit_cnt = self.find_element(*Xpath.subtotal_affiliate_deposit_cnt).text.replace(",", "")
        deposit3_cnt = self.find_element(*Xpath.subtotal_affiliate_deposit3_cnt).text.replace(",", "")
        deposit5_cnt = self.find_element(*Xpath.subtotal_affiliate_deposit5_cnt).text.replace(",", "")
        bet_member_cnt = self.find_element(*Xpath.subtotal_affiliate_bet_member_cnt).text.replace(",", "")
        bet_order_cnt = self.find_element(*Xpath.subtotal_affiliate_bet_order_cnt).text.replace(",", "")
        bet_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_affiliate_bet_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        valid_bet_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_affiliate_valid_bet_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        bonus_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_affiliate_bonus_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        win_loss_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_affiliate_win_loss_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        deposit_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_affiliate_deposit_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        withdrawal_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_affiliate_withdrawal_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        dep_with_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_affiliate_dep_with_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        deduction_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_affiliate_deduction_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        rmAddition_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_affiliate_rmAddition_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        pre_payment_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_affiliate_pre_payment_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        commission_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_affiliate_commission_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        return_point_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_affiliate_return_point_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        fee = str(
            Decimal((self.find_element(*Xpath.subtotal_affiliate_fee)).text.replace(",", "")).quantize(Decimal('.01'),
                                                                                                       rounding=ROUND_DOWN))
        administration_fee = str(
            Decimal((self.find_element(*Xpath.subtotal_affiliate_administration_fee)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        member_balance = str(
            Decimal((self.find_element(*Xpath.subtotal_affiliate_member_balance)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        total_win_loss_amount = str(Decimal(
            (self.find_element(*Xpath.subtotal_affiliate_total_win_loss_amount)).text.replace(",", "")).quantize(
            Decimal('.01'), rounding=ROUND_DOWN))

        subtotal_deposit = [affiliate_cnt, member_tree_cnt, register_cnt, deposit_first_timeCnt, deposit_cnt,
                            deposit3_cnt,
                            deposit5_cnt, bet_member_cnt, bet_order_cnt, bet_amount, valid_bet_amount, bonus_amount,
                            win_loss_amount,
                            deposit_amount, withdrawal_amount, dep_with_amount, deduction_amount, rmAddition_amount,
                            pre_payment_amount,
                            commission_amount, return_point_amount, fee, administration_fee, member_balance,
                            total_win_loss_amount]
        return subtotal_deposit

    def operation_report_member(self):
        time.sleep(5)
        member_cnt = str(self.find_element(*Xpath.subtotal_member_cnt).text.replace(",", ""))
        member_bet_order_cnt = str(self.find_element(*Xpath.subtotal_member_bet_order_cnt).text.replace(",", ""))
        member_bet_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_member_bet_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        member_valid_bet_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_member_valid_bet_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        member_bonus_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_member_bonus_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        member_win_loss_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_member_win_loss_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        member_deposit_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_member_deposit_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        member_withdrawal_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_member_withdrawal_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        member_depwith_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_member_depwith_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        member_deduction_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_member_deduction_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        member_rmaddition_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_member_rmaddition_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        member_prepayment_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_member_prepayment_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        member_returnpoint_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_member_returnpoint_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        member_fee = str(
            Decimal((self.find_element(*Xpath.subtotal_member_fee)).text.replace(",", "")).quantize(Decimal('.01'),
                                                                                                    rounding=ROUND_DOWN))
        member_administration_fee = str(
            Decimal((self.find_element(*Xpath.subtotal_member_administration_fee)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        member_member_balance = str(
            Decimal((self.find_element(*Xpath.subtotal_member_member_balance)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        member_totalwinloss_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_member_totalwinloss_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))

        subtotal_deposit = [member_cnt, member_bet_order_cnt, member_bet_amount, member_valid_bet_amount,
                            member_bonus_amount, member_win_loss_amount,
                            member_deposit_amount, member_withdrawal_amount, member_depwith_amount,
                            member_deduction_amount, member_rmaddition_amount,
                            member_prepayment_amount, member_returnpoint_amount, member_fee, member_administration_fee,
                            member_member_balance,
                            member_totalwinloss_amount]
        return subtotal_deposit

    def operation_report_agent(self):
        time.sleep(5)
        op_report_agent_deposit_amount = str(
            self.find_element(*Xpath.subtotal_op_report_agent_deposit_amount).text.replace(",", ""))
        op_report_agent_fee = str(self.find_element(*Xpath.subtotal_op_report_agent_fee).text.replace(",", ""))
        op_report_agent_administration_fee = str(Decimal(
            (self.find_element(*Xpath.subtotal_op_report_agent_administration_fee)).text.replace(",", "")).quantize(
            Decimal('.01'), rounding=ROUND_DOWN))
        op_report_agent_withdrawal_amount = str(Decimal(
            (self.find_element(*Xpath.subtotal_op_report_agent_withdrawal_amount)).text.replace(",", "")).quantize(
            Decimal('.01'), rounding=ROUND_DOWN))
        op_report_agent_depwith_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_op_report_agent_depwith_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        op_report_agent_rmde_amountnt = str(
            Decimal((self.find_element(*Xpath.subtotal_op_report_agent_rmde_amountnt)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        op_report_agent_rmadd_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_op_report_agent_rmadd_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        op_report_agent_balance_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_op_report_agent_balance_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        op_report_agent_bet_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_op_report_agent_bet_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        op_report_agent_validbet_amount = str(Decimal(
            (self.find_element(*Xpath.subtotal_op_report_agent_validbet_amount)).text.replace(",", "")).quantize(
            Decimal('.01'), rounding=ROUND_DOWN))
        op_report_agent_bonus_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_op_report_agent_bonus_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        op_report_agent_winloss_amount = str(
            Decimal((self.find_element(*Xpath.subtotal_op_report_agent_winloss_amount)).text.replace(",", "")).quantize(
                Decimal('.01'), rounding=ROUND_DOWN))
        op_report_agent_preferential_amount = str(Decimal(
            (self.find_element(*Xpath.subtotal_op_report_agent_preferential_amount)).text.replace(",", "")).quantize(
            Decimal('.01'), rounding=ROUND_DOWN))
        op_report_agent_returnpoint_amount = str(Decimal(
            (self.find_element(*Xpath.subtotal_op_report_agent_returnpoint_amount)).text.replace(",", "")).quantize(
            Decimal('.01'), rounding=ROUND_DOWN))
        op_report_agent_commission_amount = str(Decimal(
            (self.find_element(*Xpath.subtotal_op_report_agent_commission_amount)).text.replace(",", "")).quantize(
            Decimal('.01'), rounding=ROUND_DOWN))
        op_report_agent_totalwinloss_amount = str(Decimal(
            (self.find_element(*Xpath.subtotal_op_report_agent_totalwinloss_amount)).text.replace(",", "")).quantize(
            Decimal('.01'), rounding=ROUND_DOWN))

        subtotal_deposit = [op_report_agent_deposit_amount, op_report_agent_fee, op_report_agent_administration_fee,
                            op_report_agent_withdrawal_amount,
                            op_report_agent_depwith_amount, op_report_agent_rmde_amountnt, op_report_agent_rmadd_amount,
                            op_report_agent_balance_amount,
                            op_report_agent_bet_amount, op_report_agent_validbet_amount, op_report_agent_bonus_amount,
                            op_report_agent_winloss_amount,
                            op_report_agent_preferential_amount, op_report_agent_returnpoint_amount,
                            op_report_agent_commission_amount,
                            op_report_agent_totalwinloss_amount]

        return subtotal_deposit

    def click_field_affiliate_type_search(self):
        field_affiliate_search = self.find_element(*Xpath.field_operation_report_affiliate_search)
        field_affiliate_search.click()
        time.sleep(2)

    def click_option_affiliate_type_search(self, affiliate_types):
        option_affiliate_search = self.find_elements(*Xpath.option_affiliate_search)

        if affiliate_types == 'team':
            option_affiliate_search = option_affiliate_search[0]
        elif affiliate_types == 'superior':
            option_affiliate_search = option_affiliate_search[1]

        option_transaction = option_affiliate_search.text
        option_affiliate_search.click()
        time.sleep(2)

        return option_transaction

    def click_field_member_type_search(self):
        field_member_search = self.find_element(*Xpath.field_operation_report_member_search)
        field_member_search.click()
        time.sleep(2)

    def click_option_member_type_search(self, member_types):
        option_member_search = self.find_elements(*Xpath.option_member_search)

        if member_types == 'member':
            option_member_search = option_member_search[0]
        elif member_types == 'superior':
            option_member_search = option_member_search[1]
        elif member_types == 'team':
            option_member_search = option_member_search[2]

        option_transaction = option_member_search.text
        option_member_search.click()
        time.sleep(2)

        return option_transaction

    def clear_transaction_period(self):
        try:
            clear_transaction_period = self.find_element(*Xpath.clear_transaction_period)
            clear_transaction_period.click()
        except Exception as e:
            print(e)

    def freeze_member(self):
        self.click_member_button_freeze()
        self.input_freeze_reason("automation test")
        self.click_member_button_freeze_submit()
        self.click_member_button_freeze()
        self.click_member_button_freeze_confirm()

        status = False
        while status is False:
            try:
                self.driver.find_element(*Xpath.member_title_freeze)
            except Exception as e:
                print(e)
                status = True
                time.sleep(2)

    def get_export_file_name(self):
        list_of_files_before_download = glob.glob('C:\\Users\\alvis.chen\\Downloads\\*.xlsx')
        self.click_button_export()

        count = 0
        while count < 30:
            list_of_files_after_download = glob.glob('C:\\Users\\alvis.chen\\Downloads\\*.xlsx')
            newfile = list(set(list_of_files_after_download).difference(list_of_files_before_download))
            if len(newfile):
                return newfile[0]
            else:
                time.sleep(2)
                count += 1

    def get_export_file_data(self):
        file_path = self.get_export_file_name()
        columnName = get_excel_columnName(file_path)
        return columnName

    def create_activity(self, name):
        self.click_button_create_activity()
        self.input_field_activity_name("qa" + name)
        self.select_activity_type()
        self.upload_create_activity_web()
        self.upload_create_activity_app()
        activity_name = self.store_field_create_activity_name()
        activity_type = self.store_field_create_activity_type()
        self.click_button_create_activity_submit()
        self.click_button_create_activity_confirm()
        self.click_button_create_activity_confirm()
        self.input_field_activity_rule_bonus_amount("100")
        self.input_field_activity_rule_turnover_amount("100")
        self.input_field_activity_rule_receive_times("1")
        self.input_field_activity_rule_valid_bet_multiple("1")
        bonus_upper = self.store_activity_bonus_upper()
        field_value = [activity_name, activity_type, "100", "100", "1次", bonus_upper, "1"]
        self.click_button_create_activity_submit()
        self.click_button_create_activity_confirm()
        self.click_button_create_activity_confirm()

        return field_value

    def edit_activity(self, name):
        self.click_button_edit_activity()
        self.input_field_activity_name("qa" + name)
        self.select_activity_type()
        activity_name = self.store_field_create_activity_name()
        activity_type = self.store_field_create_activity_type()
        self.click_button_create_activity_submit()
        self.click_button_create_activity_confirm()
        self.click_button_create_activity_confirm()
        field_value = [activity_name, activity_type]

        return field_value

    def edit_activity_rule(self):
        self.click_button_edit_activity()
        self.click_tab_activity_rule_setting()
        self.input_field_activity_rule_bonus_amount("200")
        self.input_field_activity_rule_turnover_amount("200")
        self.input_field_activity_rule_receive_times("2")
        self.input_field_activity_rule_valid_bet_multiple("2")
        bonus_upper = self.store_activity_bonus_upper()
        field_value = ["200", "200", "2次", bonus_upper, "2"]
        self.click_button_create_activity_submit()
        self.click_button_create_activity_confirm()
        self.click_button_create_activity_confirm()

        return field_value

    def create_contract(self, contract, parent, affiliate):
        self.click_button_create_contract()
        self.click_field_create_contract_type()

        if contract == 'daily_wages':
            self.click_option_contract_daily_wages()
        elif contract == 'daily_dividends':
            self.click_option_contract_daily_dividends()
        elif contract == 'monthly_dividends':
            self.click_option_contract_monthly_dividends()

        self.input_field_create_contract_parent(parent)
        self.input_field_create_contract_member(affiliate)
        self.input_field_create_contract_headcount("10")
        self.input_field_create_contract_profit("0.1")
        self.submit_create_contract()

    def query_contract(self, contract, parent, affiliate):
        self.click_field_search_contract_type()

        if contract == 'daily_wages':
            self.click_option_search_contract_daily_wages()
        elif contract == 'daily_dividends':
            self.click_option_search_contract_daily_dividends()
        elif contract == 'monthly_dividends':
            self.click_option_search_contract_monthly_dividends()

        self.input_field_search_contract_parent(parent)
        self.input_field_search_contract_member(affiliate)
        self.submit_query()

    def reset_contract(self):
        self.click_button_reset_contract()
        self.click_button_confirm_reset_contract()

    def sum_turnover_current_valid_bet_amount(self, current):
        sum_current_valid_bet_amount = str(
            '%.2f' % (math.floor((float(current[5]) + float(current[6]) + float(current[7])
                                  + float(current[8]) + float(current[9]) + float(current[10]) + float(
                        current[11])) * 100) / 100))

        return sum_current_valid_bet_amount

    def calculate_shortage_turnover(self, required_turnover, valid_bet_amount):
        if float(required_turnover) > float(valid_bet_amount):
            shortage_amount = str(
                '%.2f' % (math.floor((float(required_turnover) - float(valid_bet_amount)) * 100) / 100))
        else:
            shortage_amount = "0"

        return shortage_amount


if __name__ == '__main__':
    pass
