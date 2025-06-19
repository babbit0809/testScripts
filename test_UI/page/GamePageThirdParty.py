import time
import unittest
from config.SetUIConfig import Platform, Target, Project
from test_UI.common import BasePage
from utils.DataLoader import JsonLoader
from test_UI.page.GamePageThirdParty_Locator import Xpath


class GamePageThirdParty(BasePage.BasePage):
    # Actions
    def click_button_transfer_window_open(self):
        button_transfer_window = self.find_element(*Xpath.button_transfer_window_open)
        button_transfer_window.click()
        time.sleep(3)

    def click_button_transfer_window_close(self):
        button_transfer_window_close = self.find_element(*Xpath.button_transfer_window_close)
        button_transfer_window_close.click()
        time.sleep(5)

    def click_button_popup_window(self):
        button_popup_window = self.find_element(*Xpath.button_popup_window)
        button_popup_window.click()
        time.sleep(5)

    def click_button_transfer_100(self):
        button_transfer_100 = self.find_element(*Xpath.button_transfer_100)
        button_transfer_100.click()
        time.sleep(1)

    def click_button_transfer_submit(self):
        button_transfer_submit = self.find_element(*Xpath.button_transfer_submit)
        button_transfer_submit.click()
        time.sleep(3)

    def click_button_transfer_confirm(self):
        button_transfer_confirm = self.find_element(*Xpath.button_transfer_confirm)
        button_transfer_confirm.click()
        time.sleep(3)

    def click_button_refresh_thirdParty_game(self):
        button_refresh_thirdParty_game = self.find_element(*Xpath.button_refresh_thirdParty_game)
        button_refresh_thirdParty_game.click()
        time.sleep(3)

    def click_slots_first_game(self):
        slots_first_game = self.find_element(*Xpath.slots_first_game)
        slots_first_game.click()
        time.sleep(3)

    def store_field_center_money(self):
        field_center_money = self.find_element(*Xpath.field_center_money).text
        return field_center_money

    def store_field_thirdParty_money(self):
        field_thirdParty_money = self.find_element(*Xpath.field_thirdParty_money).text
        return field_thirdParty_money

    def back_to_previous_page(self):
        time.sleep(10)
        self.back_prev_page()
        time.sleep(5)

    def check_thirdParty_response(self, thirdParty_money):
        count = 0
        while thirdParty_money == "-" and count < 21:
            self.click_button_transfer_window_close()
            if Target in ["h5"]:
                self.click_button_popup_window()
                self.back_to_previous_page()
            else:
                self.click_button_refresh_thirdParty_game()
            self.click_button_transfer_window_open()
            thirdParty_money = self.store_field_thirdParty_money()
            count += 1
        return count

    def store_transfer_info(self):
        thirdParty_money = self.store_field_thirdParty_money()
        count = self.check_thirdParty_response(thirdParty_money)
        center_money = self.store_field_center_money()
        thirdParty_money = self.store_field_thirdParty_money()
        if count == 21:
            self.click_button_transfer_window_close()
        return float(center_money.replace(",", "")), float(thirdParty_money.replace(",", ""))

    def execute_transfer_to_thirdParty_100(self):
        self.click_button_transfer_100()
        if Target in ["h5"]:
            if self.find_element(*Xpath.error_transfer):
                pass
            else:
                self.click_button_transfer_submit()
                self.click_button_transfer_confirm()
                self.click_button_transfer_window_open()
                thirdParty_money_change = self.store_field_thirdParty_money()
                self.check_thirdParty_response(thirdParty_money_change)
        else:
            self.click_button_transfer_submit()
            time.sleep(5)
            self.click_button_transfer_window_open()
        center_money_change = self.store_field_center_money()
        thirdParty_money_change = self.store_field_thirdParty_money()
        self.click_button_transfer_window_close()
        self.driver.swipe(start_x=-0, start_y=300, end_x=500, end_y=300, duration=100)
        return float(center_money_change.replace(",", "")), float(thirdParty_money_change.replace(",", ""))


if __name__ == '__main__':
    pass
