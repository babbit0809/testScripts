import datetime
import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from config.SetUIConfig import Platform, Target, Project
from test_UI.common import BasePage
from test_API.common.AdminTool import AdminTool
from utils import DataExtractor
from utils.DataLoader import JsonLoader
from test_UI.page.UserPage_Locator import Xpath


class UserPage(BasePage.BasePage):
    # Actions
    def check_account_info(self):
        if Target == 'h5':
            # 等待主帳戶錢包init
            WebDriverWait(self.driver, 20).until(ec.presence_of_element_located(Xpath.account_balance))
            icon_refresh = self.find_element(*Xpath.icon_refresh)
            icon_refresh.click()
            # 等待主帳戶餘額更新
            time.sleep(10)
        elif Target == 'web':
            # 等待主帳戶餘額更新
            time.sleep(10)
        else:
            pass
        account_balance = self.find_element(*Xpath.account_balance).text.replace('元', "")
        return [account_balance]

    def switch_finance_option(self, option):
        if option == 'deposit':
            option = self.find_element(*Xpath.finance_option_deposit)
        elif option == 'withdraw':
            option = self.find_element(*Xpath.finance_option_withdraw)
        elif option == 'transfer':
            option = self.find_element(*Xpath.finance_option_transfer)
        elif option == 'withdraw_account':
            if Project in ['sta']:
                option = self.find_element(*Xpath.finance_option_withdraw_account)
            elif Project in ['vt']:
                option = self.find_element(*Xpath.finance_option_withdraw_account_vt)
        option.click()

    def close_CS_window(self):
        if Project in ['sta'] and Target == 'h5':
            try:
                close_button = self.find_element(*Xpath.close_button_comm100)
                close_button.click()
            except Exception as e:
                print(e)
        else:
            pass

    def trigger_deposit(self, channel):
        time.sleep(1)  # 等待主帳戶餘額更新
        # 關閉客服視窗
        self.close_CS_window()
        # 選擇充值渠道(越南站目前無第三方渠道, 故需另外判斷)
        option = None
        if channel == 'bank':
            if Project in ['vt']:
                option = self.find_element(*Xpath.ch_bank_vt)
            else:
                option = self.find_element(*Xpath.ch_bank)
        elif channel == 'thirdParty':
            option = self.find_element(*Xpath.ch_thirdParty)
        elif channel == 'USDT':
            if Project in ['vt']:
                option = self.find_element(*Xpath.ch_USDT_vt)
            else:
                option = self.find_element(*Xpath.ch_USDT)
        option.click()
        # 輸入充值金額及確認
        if channel == 'USDT':
            deposit_value = "100"  # USDT僅有充值金額輸入框, 無快捷選項(先預設為100, 後續視情況修改)
            self.input(*Xpath.amount_input_field, contents=deposit_value)
            if Platform == 'iOS' and Target == 'app':  # 需多點擊一次讓button enabled
                confirm_button = self.find_element(*Xpath.confirm_button_deposit)
                confirm_button.click()
            elif Target == 'web':
                balance_reflash_button = self.find_element(*Xpath.balance_reflash)
                balance_reflash_button.click()
        else:
            deposit_value = self.find_element(*Xpath.amount_input_option).text
            amount_input_option = self.find_element(*Xpath.amount_input_option)
            amount_input_option.click()
        confirm_button = self.find_element(*Xpath.confirm_button_deposit)
        confirm_button.click()

        return deposit_value

    def check_deposit_info(self, channel):
        try:
            if channel == 'bank':
                value_sn = self.find_element(*Xpath.bank_sn).text
                value_amount = self.find_element(*Xpath.bank_amount).text
                value_fee = self.find_element(*Xpath.bank_fee).text
                bank_name = self.find_element(*Xpath.bank_name).text
                bank_account_name = self.find_element(*Xpath.bank_account_name).text
                bank_account = self.find_element(*Xpath.bank_account).text
                bank_currency = self.find_element(*Xpath.bank_currency).text
                bank_ratio = self.find_element(*Xpath.bank_ratio).text
                bank_comment = self.find_element(*Xpath.bank_comment).text
                return [value_sn, value_amount, value_fee, bank_name, bank_account_name, bank_account, bank_currency,
                        bank_ratio, bank_comment]
            elif channel == 'thirdParty':
                value_sn = self.find_element(*Xpath.thirdParty_sn).text
                value_amount = self.find_element(*Xpath.thirdParty_amount).text
                value_fee = self.find_element(*Xpath.thirdParty_fee).text
                thirdParty_method = self.find_element(*Xpath.thirdParty_method).text
                return [value_sn, value_amount, value_fee, thirdParty_method]
            elif channel == 'USDT':
                value_sn = self.find_element(*Xpath.usdt_sn).text
                value_amount = self.find_element(*Xpath.usdt_amount).text
                value_fee = self.find_element(*Xpath.usdt_fee).text
                usdt_name = self.find_element(*Xpath.usdt_name).text
                usdt_protocol = self.find_element(*Xpath.usdt_protocol).text
                usdt_address = self.find_element(*Xpath.usdt_address).text
                usdt_currency = self.find_element(*Xpath.usdt_currency).text
                usdt_ratio = self.find_element(*Xpath.usdt_ratio).text
                usdt_actualAmount = self.find_element(*Xpath.usdt_actualAmount).text
                return [value_sn, value_amount, value_fee, usdt_name, usdt_protocol, usdt_address, usdt_currency,
                        usdt_ratio, usdt_actualAmount]

        except Exception as e:
            print(e)

    def close_deposit_page(self):
        time.sleep(3)  # AT/Fin確認訂單後, 等待餘額更新時間
        if Target == 'web':
            pass
        else:
            try:
                back_button = self.find_element(*Xpath.back_button_deposit)
                back_button.click()
                done_button = self.find_element(*Xpath.done_button_deposit)
                done_button.click()
                if Target == 'h5':  # 需多點一次回個人中心頁
                    self.back_to_UserPage()

            except Exception as e:
                print(e)
                self.back_to_UserPage()

    def input_pin_code(self):
        pin_code = JsonLoader('CMDArgs').get_cmd_args('PinCode')
        if Platform == 'Android' and Target == 'app':
            self.input(*Xpath.pin_input_field, contents=pin_code)
        else:
            pin_list = list(pin_code)
            if Target in ['h5', 'web']:
                time.sleep(1)  # 避免速度過快抓錯元件值
            input_field = self.find_elements(*Xpath.pin_input_field)
            count = 0
            while count < len(pin_list):
                input_field[count].send_keys(int(pin_list[count]))
                count += 1
        if Target in ['h5', 'web']:  # 需多點一次確認button
            confirm_button = self.find_element(*Xpath.confirm_button_pin)
            confirm_button.click()

    def switch_withdraw_account(self, option):
        if option == 'bankcard':
            option = self.find_element(*Xpath.withdrawOption_bankcard)
        elif option == 'USDT':
            option = self.find_element(*Xpath.withdrawOption_USDT)
        option.click()

    def check_bankcard_info(self):
        if Target == 'web':
            time.sleep(4)
        bankName = self.find_element(*Xpath.bankcard_bankName).text
        value_cardNumber = self.find_element(*Xpath.bankcard_cardNumber).text.replace(' ', "")
        cardNumber = DataExtractor.extract_text("(\d{4})", value_cardNumber)
        accountName = self.find_element(*Xpath.bankcard_accountName).text
        return [bankName, cardNumber, accountName]

    def check_usdt_info(self):
        walletName = self.find_element(*Xpath.usdt_walletName).text
        value_walletAddress = self.find_element(*Xpath.usdt_walletAddress).text.replace(' ', "")
        walletAddress = DataExtractor.extract_text("(\d{4})", value_walletAddress)
        walletProtocol = self.find_element(*Xpath.usdt_walletProtocol).text
        return [walletName, walletAddress, walletProtocol]

    def trigger_withdraw(self, option, amount):
        time.sleep(1)  # 等待主帳戶餘額更新
        # 選擇提現帳戶
        self.switch_withdraw_account(option)
        # 獲取提現帳戶資訊
        withdraw_account_info = None
        if option == 'bankcard':
            withdraw_account_info = self.check_bankcard_info()
        elif option == 'USDT':
            withdraw_account_info = self.check_usdt_info()
        # 輸入提現金額及確認
        self.input(*Xpath.withdraw_input_field, contents=amount)
        next_button = self.find_element(*Xpath.next_button_withdraw)
        next_button.click()
        # 檢查是否已達免手續費次數
        self.check_fee_notice()

        return withdraw_account_info

    def check_fee_notice(self):
        try:
            confirm_button = WebDriverWait(self.driver, 3).until(ec.presence_of_element_located(Xpath.confirm_button_feeNotice))
            confirm_button.click()
        except TimeoutException as e:
            print(e)

    def check_withdraw_info(self):
        try:
            bankName = self.find_element(*Xpath.order_bankcard_BankName).text
            value_cardNumber = self.find_element(*Xpath.order_bankcard_Last4Number).text.replace(' ', "")
            cardNumber = DataExtractor.extract_text("(\d{4})", value_cardNumber)
            apply_amount = self.find_element(*Xpath.order_apply_amount).text
            admin_fee = self.find_element(*Xpath.order_admin_fee).text
            discount_amount = self.find_element(*Xpath.order_discount_amount).text
            handling_fee = self.find_element(*Xpath.order_handling_fee).text
            final_amount = self.find_element(*Xpath.order_final_amount).text
            return [bankName, cardNumber, apply_amount, admin_fee, discount_amount, handling_fee, final_amount]

        except Exception as e:
            print(e)

    def close_withdraw_page(self):
        try:
            confirm_button = self.find_element(*Xpath.confirm_button_withdraw)
            confirm_button.click()
            done_button = self.find_element(*Xpath.done_button_withdraw)
            done_button.click()
            if Target == 'h5':  # 需多點一次OK button
                ok_button = self.find_element(*Xpath.done_button_withdraw)
                ok_button.click()

        except Exception as e:  # 避免因流水審核未過而造成error
            print(e)
            back_button = self.find_element(*Xpath.navigationBar_button_back)
            back_button.click()
            self.back_to_UserPage()

    def check_transfer_info(self, target):
        time.sleep(3)  # 等待轉賬頁面餘額更新
        try:
            if target == 'Center':
                if Target == 'web':
                    balance_refresh_button = self.find_element(*Xpath.balance_reflash)
                    balance_refresh_button.click()
                target_name = "Center"
                target_balance = self.find_element(*Xpath.balance_Center).text
            else:
                if Target == 'web':
                    if Project in ['vt']:
                        sortOrder = {'IM1': 'im', 'IBC': 'onebook', 'TF': 'tf', 'DG': 'dg', 'WM': 'wm',
                                     'Sexy': 'aesexy', 'CMD': 'cmd',
                                     'SBO': 'sbo', 'CQ9': 'cq9', 'CG': 'cg2', 'LC': 'lc', 'BBIN': 'bbin'}
                    else:
                        sortOrder = {'LEG': 'leg', 'IM1': 'im', 'IM3': 'im3', 'IBC': 'onebook', 'BG': 'bg', 'KY': 'ky',
                                     'TF': 'tf',
                                     'DG': 'dg'}
                    sort = sortOrder[target]
                    target_name = target
                    target_balance = self.find_element(*(By.XPATH, Xpath.info_thirdParty + str(sort) + "')]/following::p[1]")).text
                else:
                    if Project in ['vt']:
                        sortOrder = {'IM1': 2, 'IBC': 3, 'TF': 6, 'DG': 7, 'WM': 8, 'Sexy': 9, 'CMD': 10,
                                     'SBO': 11, 'CQ9': 12, 'CG': 13, 'LC': 14, 'BBIN': 15}
                    else:
                        sortOrder = {'LEG': 2, 'IM1': 3, 'IM3': 4, 'IBC': 5, 'BG': 6, 'KY': 9, 'TF': 11,
                                     'DG': 12}
                    sort = sortOrder[target]
                    if Platform == 'iOS' and Target == 'app':
                        target_info = self.find_elements(
                            *(By.XPATH, Xpath.info_thirdParty + "[" + str(sort) + "]//*[@class='UIAStaticText']"))
                    else:
                        target_info = self.find_elements(*(By.XPATH, Xpath.info_thirdParty + "[" + str(sort) + "]/*"))
                    target_name = target_info[0].text
                    target_balance = target_info[1].text
            print("target_name", target_name, "target_balance", target_balance)
            return target_balance

        except Exception as e:
            print(e)
            if Platform == 'Android' and Target == 'app':  # 避免操作無效button遮蔽
                error_button = self.find_element(*Xpath.error_button_transfer)
                error_button.click()
            elif Target == 'h5':
                self.back_to_UserPage()

    def select_thirdParty_option(self, third_party):
        print("所有環境", self.driver.contexts)
        print("目前環境", self.driver.current_context)
        webview = self.driver.contexts[1]
        button_dropDown = self.find_element(*Xpath.button_dropDown)
        button_dropDown.click()
        time.sleep(1)  # 避免速度過快抓錯元件值
        target = None
        if Project in ['vt']:
            if Platform == 'Android' and Target == 'app':
                dropDownList = self.find_elements(*Xpath.dropDownList)
                if third_party in ['IM1', 'IBC', 'TF', 'DG', 'WM', 'Sexy', 'CMD', 'SBO', 'CQ9', 'CG']:
                    sortOrder = {'IM1': 1, 'IBC': 2, 'TF': 5, 'DG': 6, 'WM': 7, 'Sexy': 8, 'CMD': 9,
                                 'SBO': 10, 'CQ9': 11, 'CG': 12}
                    sort = sortOrder[third_party]
                    target = dropDownList[sort]
                else:
                    start_location = self.find_element(*Xpath.dropDownList_last).location
                    end_location = self.find_element(*Xpath.dropDownList_first).location
                    self.swipe(start_location, end_location, y2scale=1)
                    time.sleep(1)  # 避免速度過快抓錯元件值
                    dropDownList = self.find_elements(*Xpath.dropDownList)  # 需再找一次, 否則會跳error
                    if third_party in ['LC', 'BBIN']:
                        sortOrder = {'LC': 13, 'BBIN': 14}
                        sort = sortOrder[third_party]
                        target = dropDownList[sort]

            elif Platform == 'iOS' and Target == 'app':
                dropDownList = self.find_elements(*Xpath.dropDownList)
                if third_party in ['IM1', 'IBC', 'TF']:
                    sortOrder = {'IM1': 1, 'IBC': 2, 'TF': 5}
                    sort = sortOrder[third_party]
                    target = dropDownList[sort]
                else:
                    start_location = self.find_element(*Xpath.dropDownList_last).location
                    end_location = self.find_element(*Xpath.dropDownList_first).location
                    self.swipe(start_location, end_location, y2scale=1)
                    time.sleep(1)  # 避免速度過快抓錯元件值
                    if third_party in ['DG', 'WM', 'Sexy', 'CMD', 'SBO', 'CQ9']:
                        sortOrder = {'DG': 6, 'WM': 7, 'Sexy': 8, 'CMD': 9, 'SBO': 10, 'CQ9': 11}
                        sort = sortOrder[third_party]
                        target = dropDownList[sort]
                    else:
                        start_location = self.find_element(*Xpath.dropDownList_last2).location
                        end_location = self.find_element(*Xpath.dropDownList_first2).location
                        self.swipe(start_location, end_location, y2scale=0.8, duration=1500)
                        time.sleep(1)  # 避免速度過快抓錯元件值
                        if third_party in ['CG', 'LC', 'BBIN']:
                            sortOrder = {'CG': 12, 'LC': 13, 'BBIN': 14}
                            sort = sortOrder[third_party]
                            target = dropDownList[sort]

            elif Target == 'h5':  # H5元件會有固定index, 調整須注意
                print("切換環境")
                self.driver.switch_to.context('NATIVE_APP')
                print("目前環境", self.driver.current_context)
                if third_party in ['IM1', 'IBC', 'TF', 'DG', 'WM']:
                    sortOrder = {'IM1': 2, 'IBC': 3, 'TF': 6, 'DG': 7, 'WM': 8}
                    sort = sortOrder[third_party]
                    target = self.find_element(*(By.XPATH, Xpath.dropDownList + "[" + str(sort) + "]"))
                else:
                    start_location = self.find_element(*Xpath.dropDownList_last).location
                    end_location = self.find_element(*Xpath.dropDownList_first).location
                    self.swipe(start_location, end_location, y2scale=1)
                    time.sleep(1)  # 避免速度過快抓錯元件值
                    if third_party in ['Sexy', 'CMD', 'SBO', 'CQ9', 'CG', 'LC', 'BBIN']:
                        sortOrder = {'Sexy': 3, 'CMD': 4, 'SBO': 5, 'CQ9': 6, 'CG': 7, 'LC': 8, 'BBIN': 9}
                        sort = sortOrder[third_party]
                        target = self.find_element(*(By.XPATH, Xpath.dropDownList + "[" + str(sort) + "]"))

            elif Target == 'web':
                self.execute_script("window.scrollBy(0,600)", "")
                dropDownList = self.find_elements(*Xpath.dropDownList)
                if third_party in ['IM1', 'IBC', 'TF', 'DG', 'WM', 'Sexy', 'CMD']:
                    sortOrder = {'IM1': 1, 'IBC': 2, 'TF': 5, 'DG': 6, 'WM': 7, 'Sexy': 8, 'CMD': 9}
                    sort = sortOrder[third_party]
                    target = dropDownList[sort]
                else:
                    time.sleep(1)  # 避免速度過快抓錯元件值
                    scrollbars = self.find_element(*Xpath.scrollbars)
                    scrollbars.click()
                    self.execute_script("window.scrollBy(0,600)", "")
                    if third_party in ['SBO', 'CQ9', 'CG', 'CG', 'LC', 'BBIN']:
                        sortOrder = {'SBO': 10, 'CQ9': 11, 'CG': 12, 'LC': 13, 'BBIN': 14}
                        sort = sortOrder[third_party]
                        target = dropDownList[sort]

        else:
            if Platform == 'Android' and Target == 'app':
                dropDownList = self.find_elements(*Xpath.dropDownList)
                if third_party in ['LEG', 'IM1', 'IM3', 'IBC', 'BG', 'KY']:
                    sortOrder = {'LEG': 1, 'IM1': 2, 'IM3': 3, 'IBC': 4, 'BG': 5, 'KY': 8}
                    sort = sortOrder[third_party]
                    target = dropDownList[sort]
                else:
                    start_location = self.find_element(*Xpath.dropDownList_last).location
                    end_location = self.find_element(*Xpath.dropDownList_first).location
                    self.swipe(start_location, end_location, y2scale=1)
                    time.sleep(1)  # 避免速度過快抓錯元件值
                    dropDownList = self.find_elements(*Xpath.dropDownList)  # 需再找一次, 否則會跳error
                    if third_party in ['TF', 'DG']:
                        sortOrder = {'TF': 7, 'DG': 8}
                        sort = sortOrder[third_party]
                        target = dropDownList[sort]

            elif Platform == 'iOS' and Target == 'app':
                dropDownList = self.find_elements(*Xpath.dropDownList)
                if third_party in ['LEG', 'IM1', 'IM3', 'IBC', 'BG']:
                    sortOrder = {'LEG': 1, 'IM1': 2, 'IM3': 3, 'IBC': 4, 'BG': 5}
                    sort = sortOrder[third_party]
                    target = dropDownList[sort]
                else:
                    start_location = self.find_element(*Xpath.dropDownList_last).location
                    end_location = self.find_element(*Xpath.dropDownList_first).location
                    self.swipe(start_location, end_location, y2scale=1)
                    time.sleep(1)  # 避免速度過快抓錯元件值
                    if third_party in ['KY', 'TF', 'DG']:
                        sortOrder = {'KY': 8, 'TF': 10, 'DG': 11}
                        sort = sortOrder[third_party]
                        target = dropDownList[sort]

            elif Target == 'h5':
                print("切換環境")
                self.driver.switch_to.context('NATIVE_APP')
                print("目前環境", self.driver.current_context)
                if third_party in ['LEG', 'IM1', 'IM3', 'IBC', 'BG']:
                    sortOrder = {'LEG': 2, 'IM1': 3, 'IM3': 4, 'IBC': 5, 'BG': 6}  # H5元件會有固定index, 調整須注意
                    sort = sortOrder[third_party]
                    target = self.find_element(*(By.XPATH, Xpath.dropDownList + "[" + str(sort) + "]"))
                else:
                    start_location = self.find_element(*Xpath.dropDownList_last).location
                    end_location = self.find_element(*Xpath.dropDownList_first).location
                    self.swipe(start_location, end_location, y2scale=1)
                    time.sleep(1)  # 避免速度過快抓錯元件值
                    if third_party in ['KY', 'TF', 'DG']:
                        sortOrder = {'KY': 9, 'TF': 11, 'DG': 12}
                        sort = sortOrder[third_party]
                        target = self.find_element(*(By.XPATH, Xpath.dropDownList + "[" + str(sort) + "]"))

            elif Target == 'web':
                self.execute_script("window.scrollBy(0,600)", "")
                dropDownList = self.find_elements(*Xpath.dropDownList)
                if third_party in ['LEG', 'IM1', 'IM3', 'IBC', 'BG']:
                    sortOrder = {'LEG': 1, 'IM1': 2, 'IM3': 3, 'IBC': 4, 'BG': 5}
                    sort = sortOrder[third_party]
                    target = dropDownList[sort]
                else:
                    time.sleep(1)  # 避免速度過快抓錯元件值
                    scrollbars = self.find_element(*Xpath.scrollbars)
                    scrollbars.click()
                    self.execute_script("window.scrollBy(0,600)", "")
                    if third_party in ['KY', 'TF', 'DG']:
                        sortOrder = {'KY': 8, 'TF': 10, 'DG': 11}
                        sort = sortOrder[third_party]
                        target = dropDownList[sort]

        option_name = target.text
        print("option_name", option_name)
        target.click()

        if Target == 'h5':
            print("點擊完成, 切換回原本環境")
            self.driver.switch_to.context(webview)
            print("目前環境", self.driver.current_context)

    def trigger_transfer(self, direction, transfer_amount):
        if direction == 'toThirdParty':
            pass
        elif direction == 'toCenter':
            transfer_switch_button = self.find_element(*Xpath.transfer_switch_button)
            transfer_switch_button.click()
        # 因Android客製化鍵盤影響, 改為點擊快捷選項(暫時固定為100)
        if transfer_amount == '100':
            if Target == 'web':
                self.input(*Xpath.transfer_input_field, contents=transfer_amount)
            else:
                transfer_amount = self.find_element(*Xpath.transfer_amount_100)
                transfer_amount.click()
        # 越南站和H5的轉帳頁面需先滑動避免元件被遮蔽
        if Project in ['vt'] or Target == 'h5':
            if Target == 'web':
                pass
            else:
                start_location = self.find_element(*Xpath.transfer_amount_title).location
                end_location = self.find_element(*Xpath.navigationBar_button_back).location
                self.swipe(start_location, end_location, y2scale=1)

        confirm_button = self.find_element(*Xpath.confirm_button_transfer)
        confirm_button.click()
        if Target in ['web']:  # 需多點一次OK button
            try:
                ok_button = self.find_element(*Xpath.done_button_transfer)
                ok_button.click()
            except Exception as e:  # 避免第三方錢包代理餘額不足導致無法轉帳問題
                print(e)
        elif Target in ['h5']:  # response的時間不一致，且只有toast提示轉帳結果
            try:
                time.sleep(10)
                self.driver.refresh()
                time.sleep(5)
            except Exception as e:  # 避免第三方錢包代理餘額不足導致無法轉帳問題
                print(e)

        # 越南站和H5的轉帳頁面需先滑動避免元件被遮蔽
        if Project in ['vt']:
            if Target == 'web':
                pass
            else:
                start_location = self.find_element(*Xpath.auto_transfer_tips).location
                end_location = self.find_element(*Xpath.transfer_amount_title).location
                self.swipe(start_location, end_location, y2scale=1)

    def switch_report_option(self, option, wait_time=5):
        print("Wait status sync, time(Sec):", wait_time)
        time.sleep(wait_time)
        if option == 'deposit':
            if Target == 'web':
                self.driver.refresh()
                time.sleep(5)
                if Project in ['vt']:
                    record_list = self.find_element(*Xpath.button_record_open)
                    record_list.click()
            option = self.find_element(*Xpath.report_option_deposit)
        elif option == 'withdraw':
            if Project in ['vt']:
                if Target == 'web':
                    self.driver.refresh()
                    time.sleep(5)
                    record_list = self.find_element(*Xpath.button_record_open)
                    record_list.click()
                option = self.find_element(*Xpath.report_option_withdraw_vt)
            else:
                if Target == 'web':
                    self.driver.refresh()
                    time.sleep(5)
                option = self.find_element(*Xpath.report_option_withdraw)
        elif option == 'transfer':
            if Project in ['vt']:
                option = self.find_element(*Xpath.report_option_transfer_vt)
            else:
                option = self.find_element(*Xpath.report_option_transfer)
        option.click()

    def check_depositReport_info(self):  # TODO: 待補申請時間/到賬時間
        depositAmount = self.find_element(*Xpath.info_depositAmount).text
        depositNo = self.find_element(*Xpath.info_depositNo).text
        depositStatus = self.find_element(*Xpath.info_depositStatus).text
        if Target == 'web':
            pass
        else:
            self.back_to_UserPage()
        return [depositAmount, depositNo, depositStatus]

    def check_withdrawReport_info(self):  # TODO: 待補申請時間
        withdrawAmount = self.find_element(*Xpath.info_withdrawAmount).text
        withdrawNo = self.find_element(*Xpath.info_withdrawNo).text
        withdrawStatus = self.find_element(*Xpath.info_withdrawStatus).text
        if Target == 'web':
            pass
        else:
            self.back_to_UserPage()
        return [withdrawAmount, withdrawNo, withdrawStatus]

    def check_transferReport_info(self):  # TODO: 待補轉賬時間
        value_transferAmount = self.find_element(*Xpath.info_transferAmount).text
        transferAmount = value_transferAmount.replace(" ", "")
        transferNo = self.find_element(*Xpath.info_transferNo).text
        transferType = self.find_element(*Xpath.info_transferType).text
        if Target == 'web':
            pass
        else:
            self.back_to_UserPage()
        return [transferAmount, transferNo, transferType]

    def back_to_UserPage(self):
        if Target == 'web':
            pass
        else:
            time.sleep(5)
            back_button = self.find_element(*Xpath.navigationBar_button_back)
            back_button.click()

    def click_logout(self):
        if Target in ['web', 'h5']:
            pass
        else:
            if Project in ['vt'] or Target == 'app':  # 越南站的個人中心頁面需先滑動避免元件被遮蔽
                start_location = self.find_element(*Xpath.button_logout).location
                end_location = self.find_element(*Xpath.account_balance).location
                self.swipe(start_location, end_location, y2scale=1)
            logout_button = self.find_element(*Xpath.button_logout)
            logout_button.click()

    def switch_setting_option(self, option):
        time.sleep(5)
        if option == 'setting_info':
            if Project == 'vt':
                option = self.find_element(*Xpath.button_user_setting_vt)
            else:
                option = self.find_element(*Xpath.button_user_setting)
        option.click()
        time.sleep(5)

    def data_setting_info_nick_name(self):
        time.sleep(5)
        setting_info_nick_name = self.find_element(*Xpath.setting_info_nick_name)
        return setting_info_nick_name

    def data_user_page_nick_name(self):
        time.sleep(10)
        user_page_nick_name = self.find_element(*Xpath.user_page_nick_name)
        return user_page_nick_name

    def click_setting_info_nick_name(self):
        time.sleep(5)
        nick_name = self.find_element(*Xpath.setting_info_nick_name)
        nick_name.click()

    def click_button_back(self):
        time.sleep(3)
        button_back = self.find_element(*Xpath.button_back)
        button_back.click()

    def click_button_confirm(self):
        time.sleep(5)
        button_confirm_nick_name = self.find_element(*Xpath.button_confirm)
        button_confirm_nick_name.click()

    def edit_setting_info_nick_name(self):
        dt = datetime.datetime.today()  # 獲得當地時間
        dt_str = dt.strftime("%d%H%M")  # 格式化日期
        nick_name = "qa" + dt_str
        self.click_setting_info_nick_name()
        time.sleep(3)
        self.find_element(*Xpath.common_input_field_01).clear()
        self.input(*Xpath.common_input_field_01, contents=nick_name)
        self.click_button_submit()
        self.click_button_confirm()
        return nick_name

    def edit_setting_info_nick_name_to_account_name(self, expect_nick_name = None):
        self.click_setting_info_nick_name()
        time.sleep(10)
        self.find_element(*Xpath.common_input_field_01).clear()
        self.input(*Xpath.common_input_field_01, contents=expect_nick_name)
        self.click_button_submit()
        self.click_button_confirm()
        return expect_nick_name

    def click_button_edit_pin_code(self):
        time.sleep(3)
        if Project == 'vt':
            button_edit_pin_code = self.find_element(*Xpath.button_edit_pin_code_vt)
        else:
            button_edit_pin_code = self.find_element(*Xpath.button_edit_pin_code)
        button_edit_pin_code.click()

    def click_button_next_step(self):
        time.sleep(10)
        button_next_step = self.find_element(*Xpath.button_next_step)
        button_next_step.click()

    def click_button_submit(self):
        button_submit_pin_code = self.find_element(*Xpath.button_submit)
        button_submit_pin_code.click()

    def click_button_show_hide_pwds(self):
        time.sleep(3)
        button_show_hide_pwds = self.find_elements(*Xpath.button_show_hide_pwd)
        for button_show_hide_pwd in button_show_hide_pwds:
            button_show_hide_pwd.click()
            time.sleep(1)

    def input_verify_pin_code(self, pin_code=None):
        time.sleep(3)
        self.input(*Xpath.common_input_field_01, contents=pin_code)

    def input_new_pin_code(self, pin_code=None):
        time.sleep(10)
        self.input(*Xpath.common_input_field_01, contents=pin_code)
        self.input(*Xpath.common_input_field_02, contents=pin_code)

    def data_common_input_field_01(self):
        time.sleep(5)
        input_box = self.find_element(*Xpath.common_input_field_01)
        return input_box

    def data_common_input_field_02(self):
        time.sleep(1)
        input_box2 = self.find_element(*Xpath.common_input_field_02)
        return input_box2

    def input_verify_ping_code(self, pin_code=None):
        self.click_button_edit_pin_code()
        self.click_button_show_hide_pwds()
        self.input_verify_pin_code(pin_code)
        input_box_ping_code = self.data_common_input_field_01().get_attribute("value")
        self.click_button_next_step()

        return input_box_ping_code

    def edit_ping_code(self, pin_code=None):
        self.click_button_show_hide_pwds()
        self.input_new_pin_code(pin_code)
        input_box_ping_code = self.data_common_input_field_01().get_attribute("value")
        input_box2_ping_code = self.data_common_input_field_02().get_attribute("value")
        input_box_edit_ping_code = [input_box_ping_code, input_box2_ping_code]
        self.click_button_submit()
        self.click_button_confirm()

        return input_box_edit_ping_code

    def click_button_edit_password(self):
        time.sleep(3)
        if Project == 'vt':
            button_edit_password = self.find_element(*Xpath.button_edit_password_vt)
        else:
            button_edit_password = self.find_element(*Xpath.button_edit_password)
        button_edit_password.click()

    def input_verify_login_password(self, password=None):
        self.click_button_edit_password()
        self.click_button_show_hide_pwds()
        self.input_verify_pin_code(password)
        input_box_ping_code = self.data_common_input_field_01().get_attribute("value")
        self.click_button_next_step()

        return input_box_ping_code

    def edit_login_password(self, password=None):
        self.click_button_show_hide_pwds()
        self.input_new_pin_code(password)
        input_box_ping_code = self.data_common_input_field_01().get_attribute("value")
        input_box2_ping_code = self.data_common_input_field_02().get_attribute("value")
        input_box_edit_ping_code = [input_box_ping_code, input_box2_ping_code]
        self.click_button_submit()
        self.click_button_confirm()

        return input_box_edit_ping_code

    def input_wrong_password(self, password=None):
        self.find_element(*Xpath.common_input_field_01).clear()
        self.input_verify_pin_code(password)
        self.click_button_submit()
        self.click_button_confirm()

    def input_wrong_verify_login_password(self, password=None):
        self.click_button_edit_password()
        self.click_button_show_hide_pwds()
        self.input_wrong_password(password)
        self.input_wrong_password(password)
        self.input_wrong_password(password)

    def click_button_edit_phone_number(self):
        self.driver.refresh()
        time.sleep(3)
        button_edit_phone_number = self.find_element(*Xpath.button_edit_phone_number)
        button_edit_phone_number.click()

    def input_phone_captcha(self, phoneCaptcha):
        time.sleep(10)
        self.input(*Xpath.common_input_field_01, contents=phoneCaptcha)
        self.click_button_submit()
        self.click_button_confirm()

    def new_phone_number(self):
        dt = datetime.datetime.today()  # 獲得當地時間
        dt_str = dt.strftime("%y%d%H%M")  # 格式化日期
        phone_number = "101" + dt_str
        print('phone_number')
        print(phone_number)
        time.sleep(5)
        self.click_button_edit_phone_number()
        time.sleep(5)
        self.find_element(*Xpath.common_input_field_01).clear()
        self.input(*Xpath.common_input_field_01, contents=phone_number)
        self.click_button_submit()
        time.sleep(5)

        return phone_number

    def click_button_edit_security_email(self):
        time.sleep(3)
        button_edit_security_email = self.find_element(*Xpath.button_edit_security_email)
        button_edit_security_email.click()

    def new_security_email(self):
        dt = datetime.datetime.today()  # 獲得當地時間
        dt_str = dt.strftime("%m%d%H%M")  # 格式化日期
        new_security_email = dt_str + "@gmail.com"
        print('new_security_email')
        print(new_security_email)
        return new_security_email

    def input_security_email(self, security_email):
        self.click_button_edit_security_email()
        time.sleep(5)
        self.find_element(*Xpath.common_input_field_01).clear()
        self.input(*Xpath.common_input_field_01, contents=security_email)
        input_box_security_email = self.data_common_input_field_01().get_attribute("value")
        self.click_button_submit()
        self.click_button_confirm()
        # time.sleep(10)
        return input_box_security_email

    def click_tab_bank_card(self):
        time.sleep(2)
        tab_bank_card = self.find_element(*Xpath.tab_bank_card)
        tab_bank_card.click()

    def click_tab_crypto_wallet(self):
        time.sleep(2)
        tab_crypto_wallet = self.find_element(*Xpath.tab_crypto_wallet)
        tab_crypto_wallet.click()

    def switch_withdraw_account_type(self, account_type):
        if account_type == "bank":
            self.click_tab_bank_card()
        elif account_type == "crypto":
            self.click_tab_crypto_wallet()

    def click_button_add_bank_card(self):
        time.sleep(2)
        button_add_bank_card = self.find_element(*Xpath.button_add_bank_card)
        button_add_bank_card.click()

    def click_button_add_crypto_wallet(self):
        time.sleep(2)
        button_add_crypto_wallet = self.find_element(*Xpath.button_add_crypto_wallet)
        button_add_crypto_wallet.click()

    def store_bank_card_name(self):
        input_bank_card_name = self.find_element(*Xpath.field_input_bank_card_name).get_attribute("value")
        return input_bank_card_name

    def input_bank_card_num(self, num):
        time.sleep(2)
        self.input(*Xpath.field_input_bank_card_num, contents=num)

    def click_button_add_bank_card_next(self):
        time.sleep(2)
        button_add_bank_card_next = self.find_element(*Xpath.button_add_bank_card_next)
        button_add_bank_card_next.click()

    def store_confirm_bank_card_name(self):
        confirm_bank_card_name = self.find_element(*Xpath.confirm_bank_card_name).text
        return confirm_bank_card_name

    def store_confirm_bank_card_num(self):
        confirm_bank_card_num = self.find_element(*Xpath.confirm_bank_card_num).text
        return confirm_bank_card_num

    def click_dropdown_bank_list(self):
        time.sleep(3)
        dropdown_bank_list = self.find_element(*Xpath.dropdown_bank_list)
        dropdown_bank_list.click()

    def select_dropdown_bank_first(self):
        time.sleep(2)
        if Target == 'h5':
            print("所有環境", self.driver.contexts)
            print("目前環境", self.driver.current_context)
            webview = self.driver.contexts[1]
            self.driver.switch_to.context('NATIVE_APP')
            print("目前環境", self.driver.current_context)
            dropdown_bank_first = self.find_element(*Xpath.dropdown_bank_first)
            dropdown_bank_first.click()
            self.driver.switch_to.context(webview)
            print("目前環境", self.driver.current_context)
        else:
            time.sleep(2)
            dropdown_bank_first = self.find_element(*Xpath.dropdown_bank_first)
            dropdown_bank_first.click()

    def click_button_add_bank_card_confirm(self):
        time.sleep(2)
        button_add_bank_card_confirm = self.find_element(*Xpath.button_add_bank_card_confirm)
        button_add_bank_card_confirm.click()

    def click_wallet_protocol(self, protocol):
        time.sleep(2)
        wallet_protocol = None
        if protocol == 'erc':
            wallet_protocol = self.find_element(*Xpath.wallet_protocol_erc)
        elif protocol == 'trc':
            wallet_protocol = self.find_element(*Xpath.wallet_protocol_trc)
        elif protocol == 'omni':
            wallet_protocol = self.find_element(*Xpath.wallet_protocol_omni)
        wallet_protocol.click()

    def input_field_wallet_address(self, address):
        time.sleep(2)
        self.input(*Xpath.field_input_wallet_address, contents=address)

    def click_button_add_wallet_address_next(self):
        time.sleep(2)
        button_add_wallet_address_next = self.find_element(*Xpath.button_add_wallet_address_next)
        button_add_wallet_address_next.click()

    def input_field_input_wallet_nickname(self, nickname):
        time.sleep(2)
        self.input(*Xpath.field_input_wallet_nickname, contents=nickname)

    def store_confirm_wallet_protocol(self):
        confirm_wallet_protocol = self.find_element(*Xpath.confirm_wallet_protocol).text
        return confirm_wallet_protocol

    def store_confirm_wallet_address(self):
        confirm_wallet_address = self.find_element(*Xpath.confirm_wallet_address).text
        return confirm_wallet_address

    def click_button_add_wallet_confirm(self):
        time.sleep(2)
        button_add_wallet_confirm = self.find_element(*Xpath.button_add_wallet_confirm)
        button_add_wallet_confirm.click()

    def click_button_OTP_request(self):
        time.sleep(5)
        button_OTP_request = self.find_element(*Xpath.button_OTP_request)
        button_OTP_request.click()
        time.sleep(5)

    def input_field_OTP(self, num):
        time.sleep(2)
        self.input(*Xpath.field_input_OTP, contents=num)

    def click_button_OTP_submit(self):
        time.sleep(2)
        button_OTP_submit = self.find_element(*Xpath.button_OTP_submit)
        button_OTP_submit.click()

    def click_button_OTP_confirm(self):
        time.sleep(2)
        button_OTP_confirm = self.find_element(*Xpath.button_OTP_confirm)
        button_OTP_confirm.click()

    def generate_bank_card_num(self):
        dt = datetime.datetime.today()  # 獲得當地時間
        dt_str = dt.strftime("%Y%m%d%H%M%S")  # 格式化日期
        card_num = dt_str + "00"
        return card_num

    def generate_crypto_wallet_address(self, protocol):
        dt = datetime.datetime.today()  # 獲得當地時間
        dt_str = dt.strftime("%Y%m%d%H%M%S")  # 格式化日期

        code = ''
        address = dt_str
        if protocol.lower() == 'erc':
            code = '0x'
        elif protocol.lower() == 'trc':
            code = 'T'
        elif protocol.lower() == 'omni':
            code = '1'
        print(protocol, code)
        crypto_wallet_address = code + address
        return crypto_wallet_address

    def complete_input_bank_card_num(self, card_num):
        self.input_bank_card_num(card_num)
        self.click_button_add_bank_card_next()
        self.click_dropdown_bank_list()
        self.select_dropdown_bank_first()
        self.click_button_add_bank_card_confirm()

    def complete_input_crypto_wallet_address(self, protocol, CryptoCurrencyAddress):
        self.click_wallet_protocol(protocol)
        self.input_field_wallet_address(CryptoCurrencyAddress)
        self.click_button_add_wallet_address_next()
        self.input_field_input_wallet_nickname(CryptoCurrencyAddress)
        self.click_button_add_wallet_confirm()

    def complete_input_otp(self, otp):
        time.sleep(5)
        self.input_field_OTP(otp[1])
        self.click_button_OTP_submit()
        self.click_button_OTP_confirm()

    def click_button_member_data_vip_level(self):
        time.sleep(2)
        button_member_data_vip_level = self.find_element(*Xpath.button_name_member_data_level)
        button_member_data_vip_level.click()

    def click_navigationBar_button_vip(self):
        time.sleep(2)
        button_navigationBar_button_vip = self.find_element(*Xpath.navigationBar_button_vip)
        button_navigationBar_button_vip.click()

    def get_vip_level(self):
        time.sleep(5)
        vip_level_name = self.find_element(*Xpath.page_vip_level_name).text
        return vip_level_name

    def check_my_vip_interest(self):
        time.sleep(5)
        my_vip_interest = self.find_elements(*Xpath.my_vip_interest)
        row = len(my_vip_interest)
        num = 0
        my_vip_interest_list = []

        while row > num:
            try:
                my_vip_interest = self.find_elements(*Xpath.my_vip_interest)
                interest_list = my_vip_interest[num].text.replace('0%', "0.0%").replace(',', "").replace('\n会员特权',
                                                                                                         "").replace(
                    '\nĐặc quyền hội viên', "").replace(' ', "").replace('\n返水优惠', "").replace('\nĐặc quyền hội viên',
                                                                                               "").replace('%', "")
                my_vip_interest_list.append(interest_list)
                num += 1
            except Exception as e:
                print(e)
        if Target == 'web':
            self.execute_script("window.scrollBy(0,-400)", "")
        elif Target == 'h5':
            self.driver.execute_script("mobile: scroll", {'direction': 'up'})
        return my_vip_interest_list

    def click_button_more_vip_interest(self):
        time.sleep(2)
        button_more_vip_interest = self.find_element(*Xpath.button_more_vip_interest)
        button_more_vip_interest.click()

    def total_tab_len(self):
        time.sleep(5)
        total_tab_len = len(self.find_elements(*Xpath.button_tab_vip))
        return total_tab_len

    def total_tab_vip(self):
        time.sleep(2)
        tab_vips = self.find_elements(*Xpath.button_tab_vip)
        num = 0
        check_my_vip_interest_all = []
        for tab_vip in tab_vips:
            time.sleep(2)
            tab_vip.click()
            time.sleep(2)
            tab_vip.click()
            time.sleep(5)
            if num == 5:
                start_location = tab_vip.location
                end_location = tab_vips[0].location
                self.swipe(start_location, end_location, x1scale=1)
                print("========================================================")
            num += 1
            print(num)

            check_my_vip_interest = self.check_my_vip_interest()
            print('check_my_vip_interest')
            print(check_my_vip_interest)
            check_my_vip_interest_all.append(check_my_vip_interest)
            time.sleep(1)
        return check_my_vip_interest_all

    def click_button_tab_vip(self, vip_level=None):
        self.click_button_member_interest()
        tab_vip = self.find_elements(*Xpath.button_tab_vip)
        start_location = tab_vip[vip_level].location
        end_location = tab_vip[10].location
        # self.swipe(start_location, end_location, y1scale=2, y2scale=1)
        self.swipe(start_location, end_location)
        time.sleep(1)
        button_tab_vip = tab_vip[vip_level]
        button_tab_vip.click()
        time.sleep(1)
        print('1')
        button_tab_vip.click()
        time.sleep(1)
        print('2')
        button_tab_vip.click()
        vip = tab_vip[vip_level].text
        print('Now vip_level')
        print(vip_level)
        print(vip)

    def click_button_member_interest(self):
        time.sleep(3)
        button_member_interest = self.find_element(*Xpath.button_member_interest)
        button_member_interest.click()

    def click_button_member_return(self):
        time.sleep(3)
        button_member_return = self.find_element(*Xpath.button_member_return)
        button_member_return.click()

    def click_button_cs_nav(self):
        time.sleep(2)
        button_cs_nav = self.find_element(*Xpath.button_cs_nav)
        button_cs_nav.click()

    def click_button_cs_mine(self):
        time.sleep(2)
        button_cs_mine = self.find_element(*Xpath.button_cs_mine)
        button_cs_mine.click()

    def confirm_cs_loading_complete(self):
        time.sleep(5)
        try:
            self.driver.find_element_by_xpath(Xpath.button_cs_title)
            return True
        except Exception as e:
            print(e)
            return False

    def click_button_promo(self):
        time.sleep(2)
        button_promo = self.find_element(*Xpath.button_promo)
        button_promo.click()

    def click_button_promo_cs(self):
        time.sleep(2)
        button_promo_cs = self.find_element(*Xpath.button_promo_cs)
        button_promo_cs.click()

    def click_button_promo_download(self):
        time.sleep(2)
        button_promo_download = self.find_element(*Xpath.button_promo_download)
        button_promo_download.click()

    def click_button_promo_qr_code(self):
        time.sleep(2)
        button_promo_qr_code = self.find_element(*Xpath.button_promo_qr_code)
        button_promo_qr_code.click()

    def click_button_register_with_promo_code(self):
        time.sleep(2)
        button_register_with_promo_code = self.find_element(*Xpath.button_register_with_promo_code)
        button_register_with_promo_code.click()

    def click_button_download_promo_qr_code(self):
        time.sleep(2)
        button_download_promo_qr_code = self.find_element(*Xpath.button_download_promo_qr_code)
        button_download_promo_qr_code.click()

    def store_copy_promo_code(self):
        button_copy_promo_code = self.find_element(*Xpath.button_copy_promo_code).text
        return button_copy_promo_code

    def store_current_url(self):
        time.sleep(3)
        current_url = self.get_current_url()
        return current_url

    def check_keyword_in_string(self, keyword, string):
        if keyword in string:
            return True
        else:
            return False

    def store_clipboard_text_content(self):
        time.sleep(5)
        content = self.store_clipboard_text()
        return content

    def get_download_file_from_device(self, filepath):
        time.sleep(6)
        content = self.get_file_from_device(filepath)
        if content == "":
            return False
        else:
            return True

    def delete_download_file_from_device(self, filepath):
        time.sleep(3)
        self.delete_file_from_device(filepath)

    def click_button_activity(self):
        time.sleep(2)
        button_activity = self.find_element(*Xpath.button_activity)
        button_activity.click()

    def activity_total_count(self):
        time.sleep(2)
        total_count = len(self.find_elements(*Xpath.activity_total_count))
        return total_count

    def click_button_notice_board(self):
        time.sleep(2)
        buttton_notice_board = self.find_element(*Xpath.buttton_notice_board)
        buttton_notice_board.click()

    def notice_board_total_count(self):
        time.sleep(2)
        total_count = len(self.find_elements(*Xpath.notice_board_total_count))
        return total_count

    def click_button_user_page_download_app(self):
        time.sleep(3)
        button_user_page_download_app = self.find_element(*Xpath.button_user_page_download_app)
        button_user_page_download_app.click()

    def click_button_ios_tab(self):
        time.sleep(3)
        button_ios_tab = self.find_element(*Xpath.button_ios_tab)
        button_ios_tab.click()
        button_ios_tab.click()

    def click_button_android_tab(self):
        time.sleep(3)
        button_android_tab = self.find_element(*Xpath.button_android_tab)
        button_android_tab.click()
        button_android_tab.click()

    def get_download_page_app_version(self):
        time.sleep(3)
        if Project in ['vt']:
            app_version_info = self.find_element(*Xpath.app_version_info).text.replace('Phiên bản mới nhất', "").replace('Ngày cập nhật', "").replace('Hỗ trợ hệ thống', "").replace(' ', "").split("：")
        else:
            app_version_info = self.find_element(*Xpath.app_version_info).text.replace('最新版本', "").replace('更新日期',"").replace('支持系统', "").replace(' ', "").split("：")
        app_version = app_version_info[1]
        return app_version

    def click_download_page_app_version(self):
        time.sleep(3)
        app_version_info = self.find_element(*Xpath.app_version_info)
        app_version_info.click()

    def click_button_user_page_logout(self):
        time.sleep(3)
        button_user_page_download_app = self.find_element(*Xpath.button_user_page_download_app)
        user_page_nick_name = self.find_element(*Xpath.user_page_nick_name)
        start_location = button_user_page_download_app.location
        end_location = user_page_nick_name.location
        self.swipe(start_location, end_location)
        time.sleep(3)
        button_user_page_logout = self.find_element(*Xpath.button_user_page_logout)
        time.sleep(3)
        button_user_page_logout.click()

    def click_button_confirm_logout(self):
        time.sleep(3)
        button_confirm_logout = self.find_element(*Xpath.button_confirm_logout)
        button_confirm_logout.click()
        # time.sleep(5)

if __name__ == '__main__':
    pass
