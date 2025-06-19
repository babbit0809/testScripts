import time

import pyperclip as pyperclip
import requests
import subprocess
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.keys import Keys


from config.SetUIConfig import Platform, Target


class BasePage(object):  # 原WebDriverWait()在PK10-官方/常規/定位膽及雙面/猜冠亞會跳error, 故改用新寫法

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *loc):
        count = 0
        check = False
        element = None

        while count < 15 and check is False:
            try:
                element = self.driver.find_element(*loc)
                check = True

            except Exception as e:
                time.sleep(1)
                count += 1
                print(count, e)

        return element

    def find_elements(self, *loc):
        count = 0
        check = False
        elements = []

        while count < 15 and check is False:
            try:
                elements = self.driver.find_elements(*loc)
                check = True

            except Exception as e:
                time.sleep(1)
                count += 1
                print(count, e)

        return elements

    def execute_script(self, js, *loc):
        return self.driver.execute_script(js, *loc)

    def swipe(self, start_location, end_location, x1scale=1, y1scale=1, x2scale=1, y2scale=1, duration=1000):
        start_x = start_location["x"]
        start_y = start_location["y"]
        end_x = end_location["x"]
        end_y = end_location["y"]
        self.driver.swipe(int(start_x) * x1scale, int(start_y) * y1scale, int(end_x) * x2scale, int(end_y) * y2scale,
                          duration)

    def tap(self, tap_location, offset_x=0, offset_y=0):  # Android/iOS所能使用指令不同, 故分開判別
        action = TouchAction(self.driver)
        if Platform == 'Android':
            action.tap(tap_location, offset_x, offset_y).perform()

        elif Platform == 'iOS':
            tap_location = tap_location.location
            location_x = tap_location["x"] + offset_x
            location_y = tap_location["y"] + offset_y
            action_chain = action.press(x=location_x, y=location_y).release()
            action_chain.perform()

    def input(self, *loc, contents):
        if Target == 'app':
            input_field = self.find_element(*loc)
            input_field.click()
            input_field.send_keys(contents)
            self.driver.hide_keyboard()

        elif Target == 'h5':
            # Following is the workaround for "H5 input value will not save" issue.
            # unpkg is a fast, global content delivery network for everything on npm, hence keep use requests.
            precondition = requests.get('https://unpkg.com/react-trigger-change/dist/react-trigger-change.js')
            self.execute_script(precondition.text)
            input_field = self.find_element(*loc)
            input_field.click()
            time.sleep(5)  # 避免部分裝置操作過快噴錯
            input_field.send_keys(contents)
            self.execute_script("reactTriggerChange(arguments[0]);", input_field)
            self.driver.hide_keyboard()

        elif Target in ['web', 'admintool']:
            input_field = self.find_element(*loc)
            input_field.send_keys(Keys.CONTROL, 'a')
            input_field.send_keys(Keys.DELETE)
            time.sleep(1)
            input_field.click()
            input_field.send_keys(contents)

    def back_prev_page(self):
        self.driver.press_keycode(4)

    def switch_to_frame(self, frame):
        self.driver.switch_to.frame(frame)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url

    def store_clipboard_text(self):
        content = self.driver.get_clipboard_text()
        return content

    def get_file_from_device(self, filepath):
        file = self.driver.pull_file(filepath)
        return file

    def delete_file_from_device(self, filepath):
        print("delete file from device: " + filepath)
        subprocess.call("adb shell rm " + filepath, shell=True)


if __name__ == '__main__':
    pass
