import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from config.SetUIConfig import Driver, Platform, Env, Target
from config.PathConfig import Config_TMP
from config.RequestData import get_payload_AT
from test_UI.common import BasePage
from test_UI.page.HomePage import HomePage
from utils.DataLoader import JsonLoader
from utils import DataExtractor


class LoginPage(BasePage.BasePage):
    # Locators
    if Platform == 'Android' and Target == 'app':
        field_account = (By.ID, "edittext_account")
        field_password = (By.ID, "edittext_pw")
        button_login = (By.ID, "button_login")
        text_version = (By.ID, "txtVersion")

    elif Platform == 'Android' and Target == 'h5':
        button_download_banner = (By.XPATH, "//*[contains(@class,'CloseIcon')]")
        field_account = (By.XPATH, "//*[@name='accountId']")
        field_password = (By.XPATH, "//*[@name='password']")
        button_login = (By.XPATH, "//button[@type='submit']")
        button_download_app = (By.XPATH, "(//*[@class='text-body-8 font-semibold'])[1]")

    elif Platform == 'iOS' and Target == 'app':
        field_account = (By.CLASS_NAME, "XCUIElementTypeTextField")
        field_password = (By.CLASS_NAME, "XCUIElementTypeSecureTextField")
        button_login = (By.XPATH, "//*[@class='UIATable']/*[@XCElementType='XCUIElementTypeCell'][last()-1]")
        text_version = (By.XPATH, "//*[@knownSuperClass='UIViewControllerWrapperView']/*/*[last()]")

    elif Platform == 'iOS' and Target == 'h5':
        pass

    elif Target == 'web':
        field_account = (By.XPATH, "//*[@class='input']//*[@type='text']")
        field_password = (By.XPATH, "//*[@type='password']")
        button_login = (By.XPATH, "//button[@type='submit']")
        text_version = (By.XPATH, "//div[@id='root']/div[1]")

    elif Target == 'admintool':
        field_account = (By.XPATH, "//input[@name='account']")
        field_password = (By.XPATH, "//input[@name='password']")
        field_OTP = (By.XPATH, "//input[@name='verifyCode']")
        button_login = (By.XPATH, "//*[contains(@class,'login-form-button')]")

    # Actions
    def close_download_banner(self):  # for H5
        try:
            close_button = WebDriverWait(Driver, 3).until(ec.presence_of_element_located(self.button_download_banner))
            close_button.click()
        except TimeoutException as e:
            print(e)

    def input_account(self, account):
        self.input(*self.field_account, contents=account)

    def input_password(self, password):
        self.input(*self.field_password, contents=password)

    def input_otp(self, verifyCode):
        self.input(*self.field_OTP, contents=verifyCode)

    def click_login(self):
        login_button = self.find_element(*self.button_login)
        login_button.click()

    def check_version(self):
        try:
            version_info = WebDriverWait(Driver, 3).until(ec.presence_of_element_located(self.text_version))
            version = DataExtractor.extract_text("ver\s(.+)", version_info.text)
            return version
        except TimeoutException as e:
            print(e)

    def record_version(self):
        version = self.check_version()
        with open(Config_TMP, 'r+') as f:
            data = json.load(f)
            data[Platform]['version_' + Env] = version
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()

    def execute_login(self):
        if Target == 'admintool':
            data = get_payload_AT("User", "Login")
            account = data['account']
            password = data['password']
            otp = data['verifyCode']
            self.input_account(account)
            self.input_password(password)
            self.input_otp(otp)
            self.click_login()
        else:
            try:
                # 確認是否在登入頁面
                WebDriverWait(Driver, 10).until(ec.presence_of_element_located(self.button_login))
                if Target == 'h5':
                    self.close_download_banner()
                if Target == 'app':
                    self.record_version()
                account = JsonLoader('CMDArgs').get_cmd_args('Account')
                password = JsonLoader('CMDArgs').get_cmd_args('Password')
                self.input_account(account)
                self.input_password(password)
                self.click_login()
            except Exception as e:
                print(e)
            home_page = HomePage(self)
            home_page.close_announcement()

    def click_button_download_app(self):
        download_app_button = self.find_element(*self.button_download_app)
        download_app_button.click()

if __name__ == '__main__':
    pass
