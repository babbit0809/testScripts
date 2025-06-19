from selenium.webdriver.common.by import By
from config.SetUIConfig import Platform, Target
from test_UI.common import BasePage


class Xpath(BasePage.BasePage):
    # Locators
    if Platform == 'Android' and Target == 'app':
        pass

    elif Platform == 'Android' and Target == 'h5':
        button_transfer_window_open = (By.XPATH, "//*[contains(@data-testid,'navigation-bar')]/div/div[3]/button[1]")
        button_transfer_window_close = (By.XPATH, "//*[@aria-label='core-dialog']//*[contains(@class,'right-2')]")
        button_fullScreen = (By.XPATH, "//*[contains(@data-testid,'navigation-bar')]/div/div[3]/button[2]")
        button_popup_window = (By.XPATH, "//*[contains(@data-testid,'navigation-bar')]/div/div[3]/button[3]")
        field_center_money = (By.XPATH, "(//*[contains(@class, 'title-8')]"
                                        "/following-sibling::*[contains(@class, 'body-6')])[1]")
        field_thirdParty_money = (By.XPATH, "(//*[contains(@class, 'title-8')]"
                                            "/following-sibling::*[contains(@class, 'body-6')])[2]")
        button_transfer_100 = (By.XPATH, "//button[contains(@class, 'p-2')][1]")
        button_transfer_300 = (By.XPATH, "//button[contains(@class, 'p-2')][2]")
        button_transfer_500 = (By.XPATH, "//button[contains(@class, 'p-2')][3]")
        button_transfer_1000 = (By.XPATH, "//button[contains(@class, 'p-2')][4]")
        button_transfer_max = (By.XPATH, "//button[contains(@class, 'p-2')][5]")
        button_transfer_submit = (By.XPATH, "//button[@type='submit']")
        button_transfer_confirm = (By.XPATH, "//*[contains(@class,'core-dialog-footer')]//button")
        error_transfer = (By.XPATH, "//*[contains(@class,'error-message')]")
        html_body = (By.XPATH, "//body")
        slots_first_game = (By.XPATH, "//*[contains(@class,'flex-wrap')]/div[1]")

    elif Platform == 'iOS' and Target == 'app':
        button_transfer_window_open = (By.ID, "id_UIButton_navBtn_transfer")
        button_transfer_window_close = (By.XPATH, "//*[@label='icon cancel']")
        button_popup_window = (By.ID, "id_UIButton_navBtn_openSafari")
        button_refresh_thirdParty_game = (By.ID, "id_UIButton_navBtn_refresh")
        field_center_money = (By.XPATH, "//*[@label='icon cancel']/following-sibling::*[@class='UIAView'][1]"
                                        "//*[@class='UIAStaticText'][3]")
        field_thirdParty_money = (By.XPATH, "//*[@label='icon cancel']/following-sibling::*[@class='UIAView'][2]"
                                            "//*[@class='UIAStaticText'][3]")
        button_transfer_100 = (By.XPATH, "//*[@label='icon cancel']/following-sibling::*[@class='UIAView'][3]"
                                         "//*[@name='id_UIButton_100']")
        button_transfer_300 = (By.XPATH, "//*[@label='icon cancel']/following-sibling::*[@class='UIAView'][3]"
                                         "//*[@name='id_UIButton_300']")
        button_transfer_500 = (By.XPATH, "//*[@label='icon cancel']/following-sibling::*[@class='UIAView'][3]"
                                         "//*[@name='id_UIButton_500']")
        button_transfer_1000 = (By.XPATH, "//*[@label='icon cancel']/following-sibling::*[@class='UIAView'][3]"
                                          "//*[@name='id_UIButton_1000']")
        button_transfer_max = (By.XPATH, "//*[@label='icon cancel']/following-sibling::*[@class='UIAView'][3]"
                                         "//*[@class='UIAButton'][5]")
        button_transfer_submit = (By.XPATH, "//*[@accessibilityLabel='id_UITextField_']/following-sibling::*[@class='UIAButton']")
        slots_first_game = (By.XPATH, "//*[@knownSuperClass='UICollectionViewCell'][1]")

    elif Platform == 'iOS' and Target == 'h5':
        pass


if __name__ == '__main__':
    pass
