import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from config.SetUIConfig import Driver, Platform, Target, Project
from test_UI.common import BasePage


class HomePage(BasePage.BasePage):
    # Locators
    if Platform == 'Android' and Target == 'app':
        icon_announcement = (By.ID, "ivIcon")
        tab_home = (By.ID, "tab_home")
        tab_game = (By.ID, "tab_game_lobby")
        game_option_lottery = (By.XPATH, "//*[@id='gameTabLayout']/*/*[3]")
        tab_user = (By.ID, "tab_mine")

    elif Platform == 'Android' and Target == 'h5':
        button_announcement = (By.XPATH, "//*[@aria-label='core-dialog']//*[contains(@class,'right-2')]")
        tab_home = (By.XPATH, "//*[contains(@class,'flex py-2')]/div[1]")
        tab_game = (By.XPATH, "//*[contains(@class,'flex py-2')]/div[1]")
        game_option_lottery = (By.XPATH, "//*[contains(@class,'LobbyNav')][2]")
        game_button_lottery = (By.XPATH, "//*[@class='gamebutton' and @id='lottery']")
        tab_user = (By.XPATH, "(//*[@class='flex-1'])[4]")
        tab_activity = (By.XPATH, "//*[contains(@class,'flex py-2')]/div[3]")
        home_page_nick_name = (By.XPATH, "//*[contains(@class,'text-body-5')]")

    elif Platform == 'iOS' and Target == 'app':
        button_announcement = (By.XPATH, "//*[@label='icon announce cancel']")
        tab_home = (By.XPATH, "//*[@class='UIATabBar']/*[@class='UIAButton'][1]")
        tab_game = (By.XPATH, "//*[@class='UIATabBar']/*[@class='UIAButton'][3]")
        game_option_lottery = (By.XPATH, "//*[@class='UIAScrollView']/*/*[3]")
        tab_user = (By.XPATH, "//*[@class='UIATabBar']/*[@class='UIAButton'][5]")

    elif Platform == 'iOS' and Target == 'h5':
        pass

    elif Target == 'web':
        button_announcement = (By.XPATH, "//*[@class='inner-box']//*[@class='icon-ic_close']")
        tab_home = (By.XPATH, "//*[@class='category-menu']/descendant::*[contains(@src,'images')][1]")
        game_option_lottery = (By.XPATH, "//*[contains(@src,'ic-lottery')]")
        tab_game = (By.XPATH, "//*[@class='category-menu']/descendant::*[contains(@src,'images')][2]")
        tab_user = (By.XPATH, "(//*[contains(@href,'/user')])[2]")
        game_option_lottery_sme_vt = (By.XPATH, "(//*[contains(@class,'category-menu')]//li)[1]")  # Web SME & VT999 彩票

    # Actions
    def close_announcement(self):
        # Android App在公告視窗UI調整後抓取不到原Close Button, 需另外判斷
        try:
            if Platform == 'Android' and Target == 'app':
                tap_location = WebDriverWait(Driver, 10).until(ec.visibility_of_element_located(self.icon_announcement))
                self.driver.tap(tap_location, offset_y=-350)
            else:
                close_button = WebDriverWait(Driver, 20).until(ec.visibility_of_element_located(self.button_announcement))
                close_button.click()
        except TimeoutException as e:  # 避免未設定公告跳error的情況
            print(e, "\nNo announcement.")

    def switch_category(self, category):
        tab = None
        if category == 'home':
            tab = self.find_element(*self.tab_home)
        elif category == 'game':
            if Target == 'web':
                if Project in ['vt']:
                    tab = self.find_element(*self.game_option_lottery_sme_vt)  # Web SME & VT999 彩票
                else:
                    tab = self.find_element(*self.game_option_lottery)
            else:
                # 越南的遊戲會取代首頁位置
                if Project in ['vt']:
                    tab = self.find_element(*self.tab_home)
                else:
                    tab = self.find_element(*self.tab_game)
        elif category == 'user':
            tab = self.find_element(*self.tab_user)
        elif category == 'activity':
            tab = self.find_element(*self.tab_activity)
        tab.click()
        # 星輝因遊戲預設為體育分類, 需多一步切換
        if category == 'game' and Project in ['sta']:
            game_option_lottery = self.find_element(*self.game_option_lottery)
            game_option_lottery.click()

    def data_home_page_nick_name(self):
        time.sleep(5)
        home_page_nick_name = self.find_element(*self.home_page_nick_name)
        return home_page_nick_name

if __name__ == '__main__':
    pass
