import time
import math
from decimal import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from config.SetUIConfig import Driver, Platform, Target, Project
from test_UI.common import BasePage
from test_UI.common.GamePageCommon_Locator import Xpath
from test_UI.page.HomePage import HomePage
from utils import DataExtractor, Localization


class GamePageCommon(BasePage.BasePage):
    # Actions
    def get_countdown_time(self):
        info_countdown = self.find_element(*Xpath.info_countdown_all_page).text
        (h, m, s) = info_countdown.split(':')
        countdown_time = int(h) * 3600 + int(m) * 60 + int(s)
        return countdown_time

    def close_endgame_button(self, countdown_time, check_time=15):
        if Target == 'app':
            count = 0
            status = False
            if countdown_time < check_time:
                while count < check_time and status is False:
                    try:
                        endgame_button = self.find_element(*Xpath.button_endgame)
                        endgame_button.click()
                        status = True

                    except Exception as e:
                        print(e)
                        time.sleep(1)
                        count += 1

            else:
                pass
        # H5如點擊過快會出錯且視窗5秒左右會自動關閉, 故改為等待countdown_time + 6秒
        elif Target in ['h5', 'web']:
            wait_time = {'h5': 6, 'web': 10}
            if countdown_time < check_time:
                time.sleep(countdown_time + wait_time[Target])
            else:
                pass

    def check_countdown_time(self, check_time=15):
        try:
            if Platform == 'iOS' and Target == 'app':
                try:
                    endgame_button = WebDriverWait(Driver, 1).until(ec.visibility_of_element_located(Xpath.button_endgame))
                    endgame_button.click()
                except TimeoutException:
                    pass

            countdown_time = self.get_countdown_time()
            self.close_endgame_button(countdown_time, check_time)
        except Exception as e:
            print(e)
            if Platform == 'Android' and Target == 'app':
                endgame_button = WebDriverWait(Driver, 1).until(ec.visibility_of_element_located(Xpath.button_endgame))
                endgame_button.click()
            elif Target in ['h5', 'web']:
                time.sleep(6)

        return True

    def switch_bet_category(self, bet_category):
        if Project in ['vt']:  # 越南無官方盤/雙面盤之分, 故另外判斷
            time.sleep(3)  # 避免切換過快造成error

        else:
            self.check_countdown_time()

            if bet_category == 'pro':
                bet_category = self.find_element(*Xpath.bet_category_pro)
            elif bet_category == 'twoSide':
                bet_category = self.find_element(*Xpath.bet_category_twoSide)
            bet_category.click()

    def click_pro_game_option(self):
        self.check_countdown_time(check_time=25)

        pro_game_type_option = self.find_element(*Xpath.option_pro_game_type)
        pro_game_type_option.click()

    def check_pro_game_option_showing(self):  # 避免盈虧通知視窗(2秒左右會自動關閉)擋住玩法選單造成error
        if Target == 'web':
            pass
        else:
            try:
                WebDriverWait(Driver, 3).until(ec.presence_of_element_located(Xpath.option_level1_title))
            except TimeoutException as e:
                print(e, "click_pro_game_option again.")
                self.click_pro_game_option()

    def set_pro_bet_setting(self, bet_currency):  # 倍數暫定使用預設值"1", 後續視情況新增
        self.check_countdown_time()

        if bet_currency == 'dollar':
            bet_currency = self.find_element(*Xpath.bet_currency_dollar)
        elif bet_currency == 'dime':
            bet_currency = self.find_element(*Xpath.bet_currency_dime)
        elif bet_currency == 'cent':
            bet_currency = self.find_element(*Xpath.bet_currency_cent)
        bet_currency.click()

    def set_twoSide_bet_setting(self, bet_chip):  # 最小投注額為2, 自訂金額部分後續視情況新增
        self.check_countdown_time()

        if bet_chip == '2':
            bet_chip = self.find_element(*Xpath.bet_chip_2)
        elif bet_chip == '50':
            bet_chip = self.find_element(*Xpath.bet_chip_50)
        elif bet_chip == '100':
            bet_chip = self.find_element(*Xpath.bet_chip_100)
        elif bet_chip == '500':
            bet_chip = self.find_element(*Xpath.bet_chip_500)
        elif bet_chip == '1000':
            bet_chip = self.find_element(*Xpath.bet_chip_1000)
        bet_chip.click()

    def click_bet_basket(self):  # 購彩籃icon, 官方盤 only
        bet_basket_button = self.find_element(*Xpath.button_bet_basket)
        bet_basket_button.click()

    def click_payment(self, bet_category):
        self.check_countdown_time(check_time=25)  # 避免抓取訂單資訊過慢而導致error

        payment_button = None
        if bet_category == 'pro':
            payment_button = self.find_element(*Xpath.button_payment_pro)
        elif bet_category == 'twoSide':
            payment_button = self.find_element(*Xpath.button_payment_twoSide)
        elif bet_category == 'tracing_bet':
            payment_button = self.find_element(*Xpath.tracing_bet_button)
        payment_button.click()

    def check_order_info(self):  # 因訂單資訊各端顯示方式不一, 暫時分開判斷
        value_game = None
        value_sn = None
        value_amount = None
        value_track = None
        value_number = None
        value_count = None

        if Platform == 'Android' and Target == 'app':
            order_info = self.find_elements(*Xpath.order_info)
            order_info_game = order_info[0].text
            order_info_sn = order_info[1].text
            order_info_amount = order_info[2].text
            order_info_track = order_info[3].text
            order_info_number = order_info[4].text
            order_info_count = order_info[5].text

            if Project in ['vt']:
                value_game = DataExtractor.extract_text("Loại xổ số:\s(.+)", order_info_game)
                value_sn = DataExtractor.extract_text("Kỳ số:\s(.+)", order_info_sn)
                value_amount = DataExtractor.extract_text("Tổng cược:\s(.+)", order_info_amount)
                value_track = DataExtractor.extract_text("Đuổi số:\s(.+)", order_info_track)
                value_number = DataExtractor.extract_text("Hạng mục đặt cược:\s(.+)", order_info_number)
                value_count = DataExtractor.extract_text("Số lượng vé cược:\s(.+)\své", order_info_count)
            else:
                value_game = DataExtractor.extract_text("彩种:\s(.+)", order_info_game)
                value_sn = DataExtractor.extract_text("期号:\s(.+)", order_info_sn)
                value_amount = DataExtractor.extract_text("投注总额:\s(.+)", order_info_amount)
                value_track = DataExtractor.extract_text("追号:\s(.+)", order_info_track)
                value_number = DataExtractor.extract_text("投注项:\s(.+)", order_info_number)
                value_count = DataExtractor.extract_text("注数:\s(.+)注", order_info_count)

        elif Platform == 'iOS' and Target == 'app':
            order_info = self.find_element(*Xpath.order_info).text

            if Project in ['vt']:
                value_game = DataExtractor.extract_text("Loại xổ số:\s(.+)", order_info)
                value_sn = DataExtractor.extract_text("Kỳ số:\s(.+)", order_info)
                value_amount = DataExtractor.extract_text("Tổng cược:\s(.+)", order_info)
                value_track = DataExtractor.extract_text("Đuổi số:\s(.+)", order_info)
                value_number = DataExtractor.extract_text("Hạng mục đặt cược:\s(.+)", order_info)
                value_count = DataExtractor.extract_text("Số lượng cược :(.+)\slần", order_info)
            else:
                value_game = DataExtractor.extract_text("彩种: (.+)", order_info)
                value_sn = DataExtractor.extract_text("期号: (.+)", order_info)
                value_amount = DataExtractor.extract_text("投注总额: (.+)", order_info)
                value_track = DataExtractor.extract_text("追号: (.+)", order_info)
                value_number = DataExtractor.extract_text("投注项: (.+)", order_info)
                value_count = DataExtractor.extract_text("注数: (.+)\s注", order_info)

        elif Target == 'h5':
            order_info = self.find_element(*Xpath.order_info).text

            if Project in ['vt']:
                value_game = DataExtractor.extract_text("Loại xổ số:\s(.+)", order_info)
                value_sn = DataExtractor.extract_text("Số kỳ:\s(.+)", order_info)
                value_amount = DataExtractor.extract_text("Tổng tiền đặt cược:\s(.+)", order_info)
                value_track = DataExtractor.extract_text("Đuổi số:\s(.+)", order_info)
                value_number = DataExtractor.extract_text("Hạng mục đặt cược:\s(.+)", order_info)
                value_count = DataExtractor.extract_text("Số lượng cược:\s(.+)\sVé cược", order_info)
            else:
                value_game = DataExtractor.extract_text("彩种: (.+)", order_info)
                value_sn = DataExtractor.extract_text("期号: (.+)", order_info)
                value_amount = DataExtractor.extract_text("投注总额: (.+)", order_info)
                value_track = DataExtractor.extract_text("追号: (.+)", order_info)
                value_number = DataExtractor.extract_text("投注项: (.+)", order_info)
                value_count = DataExtractor.extract_text("注数: (.+) 注", order_info)

        elif Target == 'web':
            # web 因執行速度較快，訂單未顯示完全，故需加 time.sleep
            time.sleep(4)
            order_info_all = self.find_elements(*Xpath.order_info_all)
            if Project in ['vt']:
                value_game = order_info_all[1].text
                value_sn = order_info_all[5].text
                value_amount = DataExtractor.extract_text("(.+)₫", order_info_all[9].text)
                value_track = order_info_all[3].text
                value_number = order_info_all[7].text
                value_count = DataExtractor.extract_text("(.+)vé cược", order_info_all[11].text)
            else:
                value_game = order_info_all[1].text
                value_sn = order_info_all[5].text
                value_amount = DataExtractor.extract_text("(.+)元", order_info_all[9].text)
                value_track = order_info_all[3].text
                value_number = order_info_all[7].text
                value_count = DataExtractor.extract_text("(.+)注", order_info_all[11].text)

        return [value_game, value_sn, value_amount, value_track, value_number, value_count]

    # 避免訂單視窗前後資訊不一致, 故相關func不呼叫check_countdown, 而在前面的時間點視情況呼叫
    def click_order_confirm(self):
        order_confirm_button = self.find_element(*Xpath.button_order_confirm)
        order_confirm_button.click()

    def click_order_done(self):
        order_done_button = self.find_element(*Xpath.button_order_done)
        if Target == 'web':
            self.check_countdown_time()
        order_done_button.click()
        if Target == 'web':
            self.execute_script("window.scrollBy(0,-600)", "")

    def back_to_homepage(self):
        self.check_countdown_time()
        if Target == 'web':
            pass
        else:
            try:
                back_button = self.find_element(*Xpath.button_back)
                back_button.click()
                home_page = HomePage(self.driver)
                home_page.switch_category("home")
            except Exception as e:
                print(e)
                # 避免當期截止視窗遮蔽元件
                if Target == 'app':
                    try:
                        endgame_button = WebDriverWait(Driver, 1).until(ec.visibility_of_element_located(Xpath.button_endgame))
                        endgame_button.click()
                    except TimeoutException:
                        pass
                back_button = self.find_element(*Xpath.button_back)
                back_button.click()
                home_page = HomePage(self.driver)
                home_page.switch_category("home")

    def click_back_button(self):
        try:
            back_button = self.find_element(*Xpath.button_back)
            back_button.click()
            home_page = HomePage(self.driver)
            home_page.switch_category("home")
        except Exception as e:
            print(e)

    def check_homepage_showing(self):  # 避免盈虧通知視窗(2秒左右會自動關閉)擋住玩法選單造成error
        try:
            WebDriverWait(Driver, 3).until(ec.presence_of_element_located(HomePage.tab_game))

        except TimeoutException as e:
            print(e, "back_to_homepage again.")
            self.back_to_homepage()

    def get_thirdParty_title(self):
        time.sleep(5)
        thirdParty_title = self.find_element(*Xpath.thirdParty_title).text
        return thirdParty_title

    # Following Functions for 追號
    def click_tracking_tab(self, tracking_category, tracing_times):  # 點擊追號分頁
        time.sleep(2)
        self.check_countdown_time()
        if tracking_category == 'double_tracking':
            self.find_element(*Xpath.button_double_tracking)
            tracking_tab_button = self.find_element(*Xpath.button_double_tracking)
            tracking_tab_button.click()
            self.input_total_tracing_value('double_tracking', tracing_times)  # 輸入追號期數
            self.input_total_tracing_value('double_tracking', tracing_times)  # 輸入追號期數

        elif tracking_category == 'smart_tracking':
            self.find_element(*Xpath.button_smart_tracking)
            tracking_tab_button = self.find_element(*Xpath.button_smart_tracking)
            tracking_tab_button.click()
            self.input_tracing_profitability_value('10')  # 预期盈利
            self.input_total_tracing_value('smart_tracking', tracing_times)  # 輸入追號期數
            self.input_total_tracing_value('smart_tracking', tracing_times)  # 輸入追號期數

        self.find_element(*Xpath.button_add_tracing)
        add_tracing = self.find_element(*Xpath.button_add_tracing)
        add_tracing.click()  # 生成追號方案
        time.sleep(6)
        end_of_winning = self.find_element(*Xpath.button_end_of_winning)
        end_of_winning.click()

    def click_tracing_category(self, tracing_category, tracing_times):  # 追號類別
        self.check_countdown_time()
        if tracing_category == 'double_tracking':
            self.find_element(*Xpath.button_tracing)
            tracing_button = self.find_element(*Xpath.button_tracing)
            tracing_button.click()
            self.click_tracking_tab('double_tracking', tracing_times)

        elif tracing_category == 'smart_tracking':
            self.find_element(*Xpath.button_tracing)
            tracing_button = self.find_element(*Xpath.button_tracing)
            tracing_button.click()
            self.click_tracking_tab('smart_tracking', tracing_times)

    def input_total_tracing_value(self, tracking_category, tracing_times):  # 輸入追號期數
        self.check_countdown_time()
        input_total_tracing_value = self.find_elements(*Xpath.input_tracing_number)
        time.sleep(2)
        if tracking_category == 'double_tracking':
            input_total_tracing_value = input_total_tracing_value[3]

        elif tracking_category == 'smart_tracking':
            input_total_tracing_value = input_total_tracing_value[1]
        self.check_countdown_time()
        input_total_tracing_value.send_keys(Keys.CONTROL, 'a')
        input_total_tracing_value.send_keys(Keys.DELETE)
        input_total_tracing_value.send_keys(tracing_times)

    def input_tracing_profitability_value(self, value):  # 追號_智能追號_輸入预期盈利
        self.check_countdown_time()
        self.input(*Xpath.input_profitability, contents=value)

    def default_tracking_data_of_current(self):  # 預設翻倍追號資料
        tracing_bet_info_of_current = self.check_tracing_bet_info_of_current()
        tracing_bet_info_of_accumulation = self.check_tracing_bet_info_of_accumulation()
        tracing_bet_info_of_win_profit = self.check_tracing_bet_info_of_win_profit()
        tracing_bet_info_of_profitability = self.check_tracing_bet_info_of_profitability()
        time.sleep(2)
        return [tracing_bet_info_of_current, tracing_bet_info_of_accumulation, tracing_bet_info_of_win_profit,
                tracing_bet_info_of_profitability]

    def check_tracing_bet_info_of_current(self):  # 追號_介面当前投入
        input_multiples_of_tracing = self.find_elements(*Xpath.input_multiples_of_tracing)
        row = len(input_multiples_of_tracing)
        num = 1
        tracing_bet_info_current_list = []

        # 如果此部分作法個平台都一致的話  就把tracing_bet系列 if Target == 'web': 這移除
        if Target == 'web':
            while row >= num:
                try:
                    tracing_bet_info_current = self.find_elements(*Xpath.tracing_bet_info_of_current)
                    tracing_list = tracing_bet_info_current[num].text
                    tracing_bet_info_current_list.append(tracing_list)
                    num += 1

                except Exception as e:
                    print(e)

        return [tracing_bet_info_current_list]

    def check_tracing_bet_info_of_accumulation(self):  # 追號_介面累积投入
        input_multiples_of_tracing = self.find_elements(*Xpath.input_multiples_of_tracing)
        row = len(input_multiples_of_tracing)
        num = 1
        tracing_bet_info_of_accumulation_list = []

        if Target == 'web':
            while row >= num:
                try:
                    tracing_bet_info_accumulation = self.find_elements(*Xpath.tracing_bet_info_of_accumulation)
                    tracing_list = tracing_bet_info_accumulation[num].text
                    tracing_bet_info_of_accumulation_list.append(tracing_list)
                    num += 1

                except Exception as e:
                    print(e)

        return [tracing_bet_info_of_accumulation_list]

    def check_tracing_bet_info_of_win_profit(self):  # 追號_介面盈利
        input_multiples_of_tracing = self.find_elements(*Xpath.input_multiples_of_tracing)
        row = len(input_multiples_of_tracing)
        num = 1
        tracing_bet_info_of_win_profit_list = []

        if Target == 'web':
            while row >= num:
                try:
                    self.check_countdown_time()
                    tracing_bet_info_win_profit = self.find_elements(*Xpath.tracing_bet_info_of_win_profit)
                    tracing_list = Decimal(tracing_bet_info_win_profit[num].text.replace(',', "")).quantize(
                        Decimal('0'), rounding=ROUND_DOWN)
                    tracing_bet_info_of_win_profit_list.append(str(tracing_list))
                    num += 1

                except Exception as e:
                    print(e)

        return [tracing_bet_info_of_win_profit_list]

    def check_tracing_bet_info_of_profitability(self):  # 追號_介面盈利率
        input_multiples_of_tracing = self.find_elements(*Xpath.input_multiples_of_tracing)
        row = len(input_multiples_of_tracing)
        num = 1
        tracing_bet_info_of_profitability = []

        if Target == 'web':
            while row >= num:
                try:
                    self.check_countdown_time()
                    tracing_bet_info_profitability = self.find_elements(*Xpath.tracing_bet_info_of_profitability)
                    tracing_list = Decimal(
                        tracing_bet_info_profitability[num].text.replace(',', "").replace('%', "")).quantize(
                        Decimal('0'), rounding=ROUND_DOWN)
                    tracing_bet_info_of_profitability.append(str(tracing_list))
                    num += 1

                except Exception as e:
                    print(e)

        return [tracing_bet_info_of_profitability]

    def default_tracking_data_of_expect(self, tracking_type):  # 計算預設追號資料
        expect_data_of_current = self.default_data_of_current(tracking_type)
        expect_data_of_accumulation = self.default_data_of_accumulation(tracking_type)
        expect_data_of_win_profit = self.default_data_of_win_profit(tracking_type)
        expect_data_of_profitability = self.default_data_of_profitability(tracking_type)
        time.sleep(2)
        return [expect_data_of_current, expect_data_of_accumulation, expect_data_of_win_profit,
                expect_data_of_profitability]

    def default_data_of_current(self, bet_category):  # 計算預設当前投入
        input_multiples_of_tracing = self.find_elements(*Xpath.input_multiples_of_tracing)
        row = len(input_multiples_of_tracing)
        num = 0
        value = 0.02
        default_data_of_current_list = []

        if Target == 'web':
            if bet_category == 'double_tracking':
                while row > num:
                    try:
                        tracing_list = value
                        default_data_of_current_list.append(str(tracing_list))
                        num += 1
                        value = value * 2

                    except Exception as e:
                        print(e)
            elif bet_category == 'smart_tracking':
                while row > num:
                    try:
                        tracing_list = value
                        default_data_of_current_list.append(str(tracing_list))
                        num += 1
                        value = value

                    except Exception as e:
                        print(e)

        return [default_data_of_current_list]

    def default_data_of_accumulation(self, bet_category):  # 計算預設累积投入
        input_multiples_of_tracing = self.find_elements(*Xpath.input_multiples_of_tracing)
        row = len(input_multiples_of_tracing)
        num = 0
        value = 0.02
        default_data_of_accumulation_list = []

        if Target == 'web':
            if bet_category == 'double_tracking':
                while row > num:
                    try:
                        tracing_list = Decimal(value).quantize(Decimal('.01'), ROUND_HALF_UP)
                        default_data_of_accumulation_list.append(str(tracing_list))
                        num += 1
                        value = (value * 2) + 0.02

                    except Exception as e:
                        print(e)
            elif bet_category == 'smart_tracking':
                while row > num:
                    try:
                        tracing_list = Decimal(value).quantize(Decimal('.01'), ROUND_HALF_UP)
                        default_data_of_accumulation_list.append(str(tracing_list))
                        num += 1
                        value = value + 0.02

                    except Exception as e:
                        print(e)

        return [default_data_of_accumulation_list]

    def default_data_of_win_profit(self, bet_category):  # 計算預設盈利（元）：每一期最高中獎金額－累計投入
        time.sleep(6)
        bet_bonus = Decimal(self.find_element(*Xpath.bonus_odd).text.replace(',', "")) * Decimal(0.01)
        input_multiples_of_tracing = self.find_elements(*Xpath.input_multiples_of_tracing)
        row = len(input_multiples_of_tracing)
        num = 0
        value = Decimal(0.02)
        profit_value = bet_bonus - value
        default_data_of_win_profit_list = []

        if Target == 'web':
            if bet_category == 'double_tracking':
                while row > num:
                    try:
                        tracing_list = Decimal(profit_value).quantize(Decimal('0'), rounding=ROUND_DOWN)
                        default_data_of_win_profit_list.append(str(tracing_list))
                        num += 1
                        profit_value = ((profit_value * 2) - Decimal(0.02)).quantize(Decimal('.00001'),
                                                                                     rounding=ROUND_DOWN)

                    except Exception as e:
                        print(e)
            elif bet_category == 'smart_tracking':
                while row > num:
                    try:
                        tracing_list = Decimal(profit_value).quantize(Decimal('0'), rounding=ROUND_DOWN)
                        default_data_of_win_profit_list.append(str(tracing_list))
                        num += 1
                        profit_value = profit_value - value

                    except Exception as e:
                        print(e)

        return [default_data_of_win_profit_list]

    def default_data_of_profitability(self, bet_category):  # 計算預設盈利率：盈利（元）÷累計投入   測試加入 self.check_countdown_time()
        bet_bonus = Decimal(self.find_element(*Xpath.bonus_odd).text.replace(',', "")) * Decimal(0.01)
        input_multiples_of_tracing = self.find_elements(*Xpath.input_multiples_of_tracing)
        row = len(input_multiples_of_tracing)
        num = 0
        value = Decimal(0.02)
        accumulation_value = Decimal(0.02)
        profit_value = bet_bonus - accumulation_value  # 盈利（元）
        default_data_of_profitability_list = []

        if Target == 'web':
            if bet_category == 'double_tracking':
                while row > num:
                    try:
                        profitability_value = (profit_value / accumulation_value) * 100
                        tracing_list = profitability_value.quantize(Decimal('.0001'), ROUND_HALF_UP).quantize(
                            Decimal('0'), rounding=ROUND_DOWN)
                        default_data_of_profitability_list.append(str(tracing_list))
                        num += 1
                        accumulation_value = (accumulation_value * 2) + value
                        profit_value = ((profit_value * 2) - value)
                        self.check_countdown_time()
                    except Exception as e:
                        print(e)
            elif bet_category == 'smart_tracking':
                while row > num:
                    try:
                        profitability_value = profit_value / accumulation_value
                        tracing_list = (profitability_value * 100).quantize(Decimal('.0001'), ROUND_HALF_UP).quantize(
                            Decimal('0'), rounding=ROUND_DOWN)
                        default_data_of_profitability_list.append(str(tracing_list))
                        num += 1
                        accumulation_value = accumulation_value + value
                        profit_value = profit_value - value
                        self.check_countdown_time()
                    except Exception as e:
                        print(e)

        return [default_data_of_profitability_list]

    def input_multiples_of_tracing_value(self):  # 輸入追號列表倍數
        input_multiples_of_tracing = self.find_elements(*Xpath.input_multiples_of_tracing)
        row = len(input_multiples_of_tracing)
        num = 0
        value = int(math.pow(2, row) / 2)

        while row > num:
            try:
                self.check_countdown_time()
                input_time = input_multiples_of_tracing[num]
                input_time.click()
                input_time.send_keys(Keys.CONTROL, 'a')
                input_time.send_keys(value)

                num += 1
                value = int(value / 2)

            except Exception as e:
                print(e)
        time.sleep(6)

    def expect_tracking_data_of_current(self):  # 修改倍數後翻倍追號資料
        time.sleep(2)
        tracing_bet_info_of_current = self.check_tracing_bet_info_of_current()
        tracing_bet_info_of_accumulation = self.check_tracing_bet_info_of_accumulation()
        tracing_bet_info_of_win_profit = self.check_tracing_bet_info_of_win_profit()
        tracing_bet_info_of_profitability = self.check_tracing_bet_info_of_profitability()
        time.sleep(2)
        return [tracing_bet_info_of_current, tracing_bet_info_of_accumulation, tracing_bet_info_of_win_profit,
                tracing_bet_info_of_profitability]

    def expect_tracking_data(self, tracking_type):  # 修改倍數後預期翻倍追號資料
        time.sleep(2)
        expect_data_of_current = self.expect_data_of_current(tracking_type)
        expect_data_of_accumulation = self.expect_data_of_accumulation(tracking_type)
        expect_data_of_win_profit = self.expect_data_of_win_profit(tracking_type)
        expect_data_of_profitability = self.expect_data_of_profitability(tracking_type)
        time.sleep(2)
        return [expect_data_of_current, expect_data_of_accumulation, expect_data_of_win_profit,
                expect_data_of_profitability]

    def expect_data_of_current(self, bet_category):  # 計算修改倍數後預期当前投入
        input_multiples_of_tracing = self.find_elements(*Xpath.input_multiples_of_tracing)
        row = len(input_multiples_of_tracing)
        num = 0
        value = Decimal((math.pow(2, row) * 0.02) / 2).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
        expect_data_of_current_list = []

        if Target == 'web':
            if bet_category == 'double_tracking':
                while row > num:
                    try:
                        tracing_list = value
                        expect_data_of_current_list.append(str(tracing_list))
                        num += 1
                        value = value / 2

                    except Exception as e:
                        print(e)
            elif bet_category == 'smart_tracking':
                while row > num:
                    try:
                        tracing_list = value
                        expect_data_of_current_list.append(str(tracing_list))
                        num += 1
                        value = value / 2

                    except Exception as e:
                        print(e)

        return [expect_data_of_current_list]

    def expect_data_of_accumulation(self, bet_category):  # 計算修改倍數後預期累积投入
        input_multiples_of_tracing = self.find_elements(*Xpath.input_multiples_of_tracing)
        row = len(input_multiples_of_tracing)
        num = 0
        value = Decimal((math.pow(2, row) * 0.02) / 2).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
        expect_data_of_current_value = Decimal((math.pow(2, row) * 0.02) / 2).quantize(Decimal('0.01'),
                                                                                       rounding=ROUND_DOWN)
        expect_data_of_accumulation_list = []

        if Target == 'web':
            if bet_category == 'double_tracking':
                while row > num:
                    try:
                        tracing_list = Decimal(value).quantize(Decimal('.01'), ROUND_HALF_UP)
                        expect_data_of_accumulation_list.append(str(tracing_list))
                        num += 1
                        expect_data_of_current_value = expect_data_of_current_value / 2
                        value = value + expect_data_of_current_value

                    except Exception as e:
                        print(e)

            elif bet_category == 'smart_tracking':
                while row > num:
                    try:
                        tracing_list = Decimal(value).quantize(Decimal('.01'), ROUND_HALF_UP)
                        expect_data_of_accumulation_list.append(str(tracing_list))
                        num += 1
                        expect_data_of_current_value = expect_data_of_current_value / 2
                        value = value + expect_data_of_current_value

                    except Exception as e:
                        print(e)

        return [expect_data_of_accumulation_list]

    def expect_data_of_win_profit(self, bet_category):  # 計算修改倍數後預期盈利_盈利（元）：每一期最高中獎金額－累計投入
        time.sleep(6)
        bet_bonus = Decimal(self.find_element(*Xpath.bonus_odd).text.replace(',', "")) * Decimal(0.01)
        input_multiples_of_tracing = self.find_elements(*Xpath.input_multiples_of_tracing)
        row = len(input_multiples_of_tracing)
        num = 0
        n = row
        value = Decimal((math.pow(2, n) * 0.02) / 2).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
        expect_data_of_current_value = Decimal((math.pow(2, row) * 0.02) / 2).quantize(Decimal('0.01'),
                                                                                       rounding=ROUND_DOWN)
        profit_value = (bet_bonus * Decimal(math.pow(2, n) / 2)) - value
        expect_data_of_win_profit_list = []

        if Target == 'web':
            if bet_category == 'double_tracking':
                while row > num:
                    try:
                        tracing_list = Decimal(profit_value).quantize(Decimal('0'), rounding=ROUND_DOWN)
                        expect_data_of_win_profit_list.append(str(tracing_list))
                        num += 1
                        n -= 1
                        expect_data_of_current_value = expect_data_of_current_value / 2
                        value = value + expect_data_of_current_value
                        profit_value = (bet_bonus * Decimal(math.pow(2, n) / 2)) - value

                    except Exception as e:
                        print(e)
            elif bet_category == 'smart_tracking':
                while row > num:
                    try:
                        tracing_list = Decimal(profit_value).quantize(Decimal('0'), rounding=ROUND_DOWN)
                        expect_data_of_win_profit_list.append(str(tracing_list))
                        num += 1
                        n -= 1
                        expect_data_of_current_value = expect_data_of_current_value / 2
                        value = value + expect_data_of_current_value
                        profit_value = (bet_bonus * Decimal(math.pow(2, n) / 2)) - value

                    except Exception as e:
                        print(e)

        return [expect_data_of_win_profit_list]

    def expect_data_of_profitability(self, bet_category):  # 計算修改倍數後盈利率：盈利（元）÷累計投入
        bet_bonus = Decimal(self.find_element(*Xpath.bonus_odd).text.replace(',', "")) * Decimal(0.01)
        input_multiples_of_tracing = self.find_elements(*Xpath.input_multiples_of_tracing)
        row = len(input_multiples_of_tracing)
        num = 0
        n = row
        value = Decimal((math.pow(2, n) * 0.02) / 2).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
        expect_data_of_current_value = Decimal((math.pow(2, row) * 0.02) / 2).quantize(Decimal('0.01'),
                                                                                       rounding=ROUND_DOWN)
        profit_value = (bet_bonus * Decimal(math.pow(2, n) / 2)) - value
        expect_data_of_profitability_list = []

        if Target == 'web':
            if bet_category == 'double_tracking':
                while row > num:
                    try:
                        profitability_value = profit_value / value
                        tracing_list = (Decimal(profitability_value).quantize(Decimal('.0001'),
                                                                              ROUND_HALF_UP) * 100).quantize(
                            Decimal('0'), rounding=ROUND_DOWN)
                        expect_data_of_profitability_list.append(str(tracing_list))
                        num += 1
                        n -= 1
                        expect_data_of_current_value = expect_data_of_current_value / 2
                        value = value + expect_data_of_current_value
                        profit_value = (bet_bonus * Decimal(math.pow(2, n) / 2)) - value

                    except Exception as e:
                        print(e)

            elif bet_category == 'smart_tracking':
                while row > num:
                    try:
                        profitability_value = profit_value / value
                        tracing_list = (Decimal(profitability_value).quantize(Decimal('.0001'),
                                                                              ROUND_HALF_UP) * 100).quantize(
                            Decimal('0'), rounding=ROUND_DOWN)
                        expect_data_of_profitability_list.append(str(tracing_list))
                        num += 1
                        n -= 1
                        expect_data_of_current_value = expect_data_of_current_value / 2
                        value = value + expect_data_of_current_value
                        profit_value = (bet_bonus * Decimal(math.pow(2, n) / 2)) - value

                    except Exception as e:
                        print(e)

        return [expect_data_of_profitability_list]

    def click_tracking_order_confirm(self):
        order_confirm_button = self.find_element(*Xpath.button_order_confirm)
        if Target == 'web':
            self.check_countdown_time()
        order_confirm_button.click()

    def click_tracing_order_done(self):
        tracing_order_done_button = self.find_element(*Xpath.button_tracing_order_done)
        if Target == 'web':
            self.check_countdown_time()
        tracing_order_done_button.click()

    def OrderInfoTrace_Yes(self, tracing_times):
        OrderInfoTrace_Yes = Localization.get_loc("GamePage_Common", 'OrderInfoTrace_Yes').replace('4', tracing_times)
        return OrderInfoTrace_Yes

    def bet_tracing(self):
        self.check_countdown_time()
        # 因web有清空購物車步驟，估要確認畫面有在購採籃
        if Target == 'web':
            try:
                shop_car_button = self.find_element(*Xpath.shop_car_button)
                shop_car_button.click()
                time.sleep(1)
                self.find_element(*Xpath.shop_car_active_button)
            except Exception as e:
                print(e)
                shop_car_button = self.find_element(*Xpath.shop_car_button)
                shop_car_button.click()
        else:
            pass
        GamePageCommon(self.driver).check_countdown_time()
        del_bet_buttons = self.find_element(*Xpath.del_bet_buttons)
        del_bet_buttons.click()
        random_button = self.find_element(*Xpath.random_bet_buttons)
        random_button.click()


if __name__ == '__main__':
    pass
