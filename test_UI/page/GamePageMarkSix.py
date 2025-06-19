from selenium.webdriver.common.by import By
from config.SetUIConfig import Platform, Target
from test_UI.common import BasePage
from test_UI.page.GamePageMarkSix_Locator import Xpath
from test_UI.common.GamePageCommon import GamePageCommon


class GamePageMarkSix(BasePage.BasePage):  # 六合彩無盤面之分(亦無常規/趣味之分)
    # Actions
    def switch_pro_game(self, game_name, subGame_name=None):
        # 點擊官方盤玩法選單
        if Target == 'web':
            pass
        else:
            GamePageCommon(self.driver).click_pro_game_option()
        # 避免被盈虧視窗擋住的檢查機制
        GamePageCommon(self.driver).check_pro_game_option_showing()
        # 切換主玩法
        if Target in ['app', 'h5']:
            pro_game_name_All = self.find_elements(*Xpath.pro_game_name_All)
            if game_name == 'specialNo':
                game_name = pro_game_name_All[0]
            elif game_name == 'mainNo':
                game_name = pro_game_name_All[1]
            elif game_name == 'main1to6':
                game_name = pro_game_name_All[2]
            elif game_name == 'mainSpecial':
                game_name = pro_game_name_All[3]
            elif game_name == 'halfBall':
                game_name = pro_game_name_All[4]
            elif game_name == 'tailNo':
                game_name = pro_game_name_All[5]
            elif game_name == 'zodiac1':
                game_name = pro_game_name_All[6]
            elif game_name == 'specialZodiac':
                game_name = pro_game_name_All[7]
            elif game_name == 'dt16':
                game_name = pro_game_name_All[8]
            game_name.click()

        elif Target == 'web':
            if game_name == 'specialNo':
                game_name = self.find_element(*Xpath.normal_specialNo)
            elif game_name == 'mainNo':
                game_name = self.find_element(*Xpath.normal_mainNo)
            elif game_name == 'main1to6':
                game_name = self.find_element(*Xpath.normal_main1to6)
            elif game_name == 'mainSpecial':
                game_name = self.find_element(*Xpath.normal_mainSpecial)
            elif game_name == 'halfBall':
                game_name = self.find_element(*Xpath.normal_halfBall)
            elif game_name == 'tailNo':
                game_name = self.find_element(*Xpath.normal_tailNo)
            elif game_name == 'zodiac1':
                game_name = self.find_element(*Xpath.normal_zodiac1)
            elif game_name == 'specialZodiac':
                game_name = self.find_element(*Xpath.normal_specialZodiac)
            elif game_name == 'dt16':
                game_name = self.find_element(*Xpath.normal_dt16)
            game_name.click()
        # 切換子玩法
        if Target in ['app', 'h5']:
            if subGame_name:
                pro_subGame_name_All = self.find_elements(*Xpath.pro_subGame_name_All)
                if subGame_name in ['main1st', 'main1Special']:
                    subGame_name = pro_subGame_name_All[0]
                elif subGame_name in ['main2nd', 'main2Special']:
                    subGame_name = pro_subGame_name_All[1]
                elif subGame_name in ['main3rd', 'main3Special']:
                    subGame_name = pro_subGame_name_All[2]
                elif subGame_name in ['main4th', 'main4Special']:
                    subGame_name = pro_subGame_name_All[3]
                elif subGame_name in ['main5th', 'main5Special']:
                    subGame_name = pro_subGame_name_All[4]
                elif subGame_name in ['main6th', 'main6Special']:
                    subGame_name = pro_subGame_name_All[5]
                subGame_name.click()
        # H5需多點擊確認按鈕
        if Target == 'h5':
            confirm_button = self.find_element(*Xpath.button_pro_game_confirm)
            confirm_button.click()

        elif Target == 'web':
            if subGame_name:
                if subGame_name in 'main1st':
                    subGame_name = self.find_element(*Xpath.normal_main1to6_main1st)
                elif subGame_name in 'main2nd':
                    subGame_name = self.find_element(*Xpath.normal_main1to6_main2nd)
                elif subGame_name in 'main3rd':
                    subGame_name = self.find_element(*Xpath.normal_main1to6_main3rd)
                elif subGame_name in 'main4th':
                    subGame_name = self.find_element(*Xpath.normal_main1to6_main4th)
                elif subGame_name in 'main5th':
                    subGame_name = self.find_element(*Xpath.normal_main1to6_main5th)
                elif subGame_name in 'main6th':
                    subGame_name = self.find_element(*Xpath.normal_main1to6_main6th)
                elif subGame_name in 'main1Special':
                    subGame_name = self.find_element(*Xpath.normal_mainSpecial_main1Special)
                elif subGame_name in 'main2Special':
                    subGame_name = self.find_element(*Xpath.normal_mainSpecial_main2Special)
                elif subGame_name in 'main3Special':
                    subGame_name = self.find_element(*Xpath.normal_mainSpecial_main3Special)
                elif subGame_name in 'main4Special':
                    subGame_name = self.find_element(*Xpath.normal_mainSpecial_main4Special)
                elif subGame_name in 'main5Special':
                    subGame_name = self.find_element(*Xpath.normal_mainSpecial_main5Special)
                elif subGame_name in 'main6Special':
                    subGame_name = self.find_element(*Xpath.normal_mainSpecial_main6Special)
                elif subGame_name in 'main2nd':
                    subGame_name = self.find_element(*Xpath.normal_main1to6_main2nd)
                elif subGame_name in 'main3rd':
                    subGame_name = self.find_element(*Xpath.normal_main1to6_main3rd)
                elif subGame_name in 'main2nd':
                    subGame_name = self.find_element(*Xpath.normal_main1to6_main2nd)
                elif subGame_name in 'main3rd':
                    subGame_name = self.find_element(*Xpath.normal_main1to6_main3rd)
                subGame_name.click()

    def bet_pro_all(self, type_name, subtype_name=None, bet_case=None):
        if type_name in ['specialNo']:
            if Platform == 'Android' and Target == 'app':
                GamePageCommon(self.driver).check_countdown_time()
                end_location = self.find_element(*Xpath.history_button).location
                button_01_to_49 = self.find_elements(*Xpath.betting_numbers)
                count = 0
                while count < 3:
                    num = 0
                    if count == 2:
                        GamePageCommon(self.driver).check_countdown_time()
                        rest_buttons = self.find_elements(*Xpath.betting_squares)
                        for buttons in rest_buttons:
                            if num % 5 == 0:
                                GamePageCommon(self.driver).check_countdown_time()
                            buttons.click()
                            num += 1
                    elif count == 1:
                        GamePageCommon(self.driver).check_countdown_time()
                        for buttons in button_01_to_49[:24]:
                            if num % 5 == 0:
                                GamePageCommon(self.driver).check_countdown_time()
                            buttons.click()
                            num += 1
                    else:
                        for buttons in button_01_to_49[:25]:
                            if num % 5 == 0:
                                GamePageCommon(self.driver).check_countdown_time()
                            buttons.click()
                            num += 1

                    if count < 2:
                        GamePageCommon(self.driver).check_countdown_time()
                        start_location = self.find_element(*Xpath.button_row5).location
                        self.swipe(start_location, end_location, y2scale=0.4)
                    count += 1

            elif Platform == 'Android' and Target == 'h5':
                GamePageCommon(self.driver).check_countdown_time()
                end_location = self.find_element(*Xpath.history_button).location
                button_numbers0x = self.find_elements(*Xpath.betting_numbers0x)
                button_numbers1x = self.find_elements(*Xpath.betting_numbers1x)
                button_0xto1x = [button_numbers0x, button_numbers1x]
                count = 0
                while count < 2:
                    num = 0
                    GamePageCommon(self.driver).check_countdown_time()
                    for buttons in button_0xto1x[count]:
                        buttons.click()
                        num += 1
                        if num % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                    count += 1

                GamePageCommon(self.driver).check_countdown_time()
                start_location = self.find_element(*Xpath.button_16).location
                self.swipe(start_location, end_location, y2scale=1)

                GamePageCommon(self.driver).check_countdown_time()
                button_numbers2x = self.find_elements(*Xpath.betting_numbers2x)
                button_numbers3x = self.find_elements(*Xpath.betting_numbers3x)
                button_2xto3x = [button_numbers2x, button_numbers3x]
                count = 0
                while count < 2:
                    num = 0
                    for buttons in button_2xto3x[count]:
                        buttons.click()
                        num += 1
                        if num % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                    count += 1

                GamePageCommon(self.driver).check_countdown_time()
                start_location = self.find_element(*Xpath.button_36).location
                self.swipe(start_location, end_location, y2scale=1)

                GamePageCommon(self.driver).check_countdown_time()
                button_numbers4x = self.find_elements(*Xpath.betting_numbers4x)
                count = 0
                for buttons in button_numbers4x:
                    if count % 5 == 0:
                        GamePageCommon(self.driver).check_countdown_time()
                    buttons.click()
                    count += 1

                GamePageCommon(self.driver).check_countdown_time()
                start_location = self.find_element(*Xpath.button_46).location
                self.swipe(start_location, end_location, y2scale=0.4)

                GamePageCommon(self.driver).check_countdown_time()
                button_numbers_combo = self.find_elements(*Xpath.betting_numbers_combo)
                button_squares_set = self.find_elements(*Xpath.betting_squares_set)
                button_squares_color = self.find_elements(*Xpath.betting_squares_color)
                rest_buttons = [button_numbers_combo, button_squares_set, button_squares_color]
                count = 0
                while count < 3:
                    num = 0
                    for buttons in rest_buttons[count]:
                        buttons.click()
                        num += 1
                        if num % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                    count += 1

            elif Platform == 'iOS' and Target == 'app':
                GamePageCommon(self.driver).check_countdown_time()
                end_location = self.find_element(*Xpath.history_button).location
                button_numbers0x = self.find_elements(*Xpath.betting_numbers0x)
                button_numbers1x = self.find_elements(*Xpath.betting_numbers1x)
                button_0xto1x = [button_numbers0x, button_numbers1x]
                count = 0
                while count < 2:
                    GamePageCommon(self.driver).check_countdown_time(check_time=60)
                    for buttons in button_0xto1x[count]:
                        buttons.click()
                    count += 1

                GamePageCommon(self.driver).check_countdown_time()
                start_location = self.find_element(*Xpath.button_16).location
                self.swipe(start_location, end_location, y2scale=1.2, duration=1500)

                GamePageCommon(self.driver).check_countdown_time()
                button_numbers2x = self.find_elements(*Xpath.betting_numbers2x)
                button_numbers3x = self.find_elements(*Xpath.betting_numbers3x)
                button_2xto3x = [button_numbers2x, button_numbers3x]
                count = 0
                while count < 2:
                    GamePageCommon(self.driver).check_countdown_time(check_time=60)
                    for buttons in button_2xto3x[count]:
                        buttons.click()
                    count += 1

                GamePageCommon(self.driver).check_countdown_time()
                start_location = self.find_element(*Xpath.button_36).location
                self.swipe(start_location, end_location, y2scale=1.2, duration=1500)

                GamePageCommon(self.driver).check_countdown_time()
                button_numbers4x = self.find_elements(*Xpath.betting_numbers4x)
                count = 0
                GamePageCommon(self.driver).check_countdown_time(check_time=60)
                for buttons in button_numbers4x:
                    buttons.click()
                    count += 1

                GamePageCommon(self.driver).check_countdown_time()
                start_location = self.find_element(*Xpath.button_46).location
                self.swipe(start_location, end_location, y2scale=0.6, duration=1500)

                GamePageCommon(self.driver).check_countdown_time()
                rest_buttons = self.find_elements(*Xpath.betting_squares)
                count = 0
                GamePageCommon(self.driver).check_countdown_time(check_time=60)
                for buttons in rest_buttons:
                    buttons.click()
                    count += 1
                    if count % 10 == 0:
                        GamePageCommon(self.driver).check_countdown_time(check_time=60)

            elif Target == 'web':
                GamePageCommon(self.driver).check_countdown_time()
                button_numbers0x = self.find_elements(*Xpath.betting_numbers0x)
                button_numbers1x = self.find_elements(*Xpath.betting_numbers1x)
                button_0xto1x = [button_numbers0x, button_numbers1x]
                count = 0
                while count < 2:
                    num = 0
                    GamePageCommon(self.driver).check_countdown_time()
                    for buttons in button_0xto1x[count]:
                        buttons.click()
                        num += 1
                        if num % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                    count += 1
                GamePageCommon(self.driver).check_countdown_time()
                button_numbers2x = self.find_elements(*Xpath.betting_numbers2x)
                button_numbers3x = self.find_elements(*Xpath.betting_numbers3x)
                button_2xto3x = [button_numbers2x, button_numbers3x]
                count = 0
                while count < 2:
                    num = 0
                    for buttons in button_2xto3x[count]:
                        buttons.click()
                        num += 1
                        if num % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                    count += 1
                GamePageCommon(self.driver).check_countdown_time()
                button_numbers4x = self.find_elements(*Xpath.betting_numbers4x)
                count = 0
                for buttons in button_numbers4x:
                    if count % 10 == 0:
                        GamePageCommon(self.driver).check_countdown_time()
                    buttons.click()
                    count += 1
                GamePageCommon(self.driver).check_countdown_time()
                all_buttons = self.find_elements(*Xpath.betting_not_number)
                count = 0
                for buttons in all_buttons:
                    if count % 10 == 0:
                        GamePageCommon(self.driver).check_countdown_time()
                    buttons.click()
                    count += 1

        elif type_name in ['mainNo']:
            if Platform == 'Android' and Target == 'app':  # 避免click到Back To Top button, 故另外判斷
                GamePageCommon(self.driver).check_countdown_time()
                end_location = self.find_element(*Xpath.history_button).location
                button_01_to_49 = self.find_elements(*Xpath.betting_numbers)
                count = 0
                while count < 3:
                    num = 0
                    if count == 2:
                        GamePageCommon(self.driver).check_countdown_time()
                        rest_buttons = self.find_elements(*Xpath.betting_squares)
                        for buttons in rest_buttons[:7]:
                            if num % 5 == 0:
                                GamePageCommon(self.driver).check_countdown_time()
                            buttons.click()
                            num += 1
                        tap_location = self.find_element(*Xpath.text_dragon)
                        self.tap(tap_location, offset_x=200)
                    elif count == 1:
                        GamePageCommon(self.driver).check_countdown_time()
                        for buttons in button_01_to_49[:24]:
                            if num % 5 == 0:
                                GamePageCommon(self.driver).check_countdown_time()
                            buttons.click()
                            num += 1
                    else:
                        for buttons in button_01_to_49[:25]:
                            if num % 5 == 0:
                                GamePageCommon(self.driver).check_countdown_time()
                            buttons.click()
                            num += 1

                    if count < 2:
                        GamePageCommon(self.driver).check_countdown_time()
                        start_location = self.find_element(*Xpath.button_row5).location
                        self.swipe(start_location, end_location, y2scale=0.5)
                    count += 1

            elif Platform == 'Android' and Target == 'h5':
                GamePageCommon(self.driver).check_countdown_time()
                end_location = self.find_element(*Xpath.history_button).location
                button_numbers0x = self.find_elements(*Xpath.betting_numbers0x)
                button_numbers1x = self.find_elements(*Xpath.betting_numbers1x)
                button_0xto1x = [button_numbers0x, button_numbers1x]
                count = 0
                while count < 2:
                    num = 0
                    GamePageCommon(self.driver).check_countdown_time()
                    for buttons in button_0xto1x[count]:
                        buttons.click()
                        num += 1
                        if num % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                    count += 1

                GamePageCommon(self.driver).check_countdown_time()
                start_location = self.find_element(*Xpath.button_16).location
                self.swipe(start_location, end_location, y2scale=1)

                GamePageCommon(self.driver).check_countdown_time()
                button_numbers2x = self.find_elements(*Xpath.betting_numbers2x)
                button_numbers3x = self.find_elements(*Xpath.betting_numbers3x)
                button_2xto3x = [button_numbers2x, button_numbers3x]
                count = 0
                while count < 2:
                    num = 0
                    for buttons in button_2xto3x[count]:
                        buttons.click()
                        num += 1
                        if num % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                    count += 1

                GamePageCommon(self.driver).check_countdown_time()
                start_location = self.find_element(*Xpath.button_36).location
                self.swipe(start_location, end_location, y2scale=1)

                GamePageCommon(self.driver).check_countdown_time()
                button_numbers4x = self.find_elements(*Xpath.betting_numbers4x)
                button_squares_set = self.find_elements(*Xpath.betting_squares_set)
                button_4xtoSet = [button_numbers4x, button_squares_set]
                count = 0
                while count < 2:
                    num = 0
                    for buttons in button_4xtoSet[count]:
                        buttons.click()
                        num += 1
                        if num % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                    count += 1

            elif Platform == 'iOS' and Target == 'app':  # 避免click到Back To Top button, 故另外判斷
                GamePageCommon(self.driver).check_countdown_time()
                end_location = self.find_element(*Xpath.history_button).location
                button_numbers0x = self.find_elements(*Xpath.betting_numbers0x)
                button_numbers1x = self.find_elements(*Xpath.betting_numbers1x)
                button_0xto1x = [button_numbers0x, button_numbers1x]
                count = 0
                while count < 2:
                    num = 0
                    for buttons in button_0xto1x[count]:
                        buttons.click()
                        num += 1
                        if num % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                    count += 1

                GamePageCommon(self.driver).check_countdown_time()
                start_location = self.find_element(*Xpath.button_16).location
                self.swipe(start_location, end_location, y2scale=1.2, duration=1500)

                GamePageCommon(self.driver).check_countdown_time()
                button_numbers2x = self.find_elements(*Xpath.betting_numbers2x)
                button_numbers3x = self.find_elements(*Xpath.betting_numbers3x)
                button_2xto3x = [button_numbers2x, button_numbers3x]
                count = 0
                while count < 2:
                    num = 0
                    for buttons in button_2xto3x[count]:
                        buttons.click()
                        num += 1
                        if num % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                    count += 1

                GamePageCommon(self.driver).check_countdown_time()
                start_location = self.find_element(*Xpath.button_36).location
                self.swipe(start_location, end_location, y2scale=1.2, duration=1500)

                GamePageCommon(self.driver).check_countdown_time()
                button_numbers4x = self.find_elements(*Xpath.betting_numbers4x)
                count = 0
                for buttons in button_numbers4x:
                    buttons.click()
                    count += 1
                    if count % 5 == 0:
                        GamePageCommon(self.driver).check_countdown_time()

                GamePageCommon(self.driver).check_countdown_time()
                start_location = self.find_element(*Xpath.button_46).location
                self.swipe(start_location, end_location, y2scale=1.2, duration=1500)

                GamePageCommon(self.driver).check_countdown_time()
                rest_buttons = self.find_elements(*Xpath.betting_squares)
                count = 0
                for buttons in rest_buttons[:7]:
                    buttons.click()
                    count += 1
                    if count % 5 == 0:
                        GamePageCommon(self.driver).check_countdown_time()

                GamePageCommon(self.driver).check_countdown_time()
                tap_location = self.find_element(*Xpath.text_dragon)
                self.tap(tap_location, offset_x=300)

            elif Target == 'web':
                GamePageCommon(self.driver).check_countdown_time()
                button_numbers0x = self.find_elements(*Xpath.betting_numbers0x)
                button_numbers1x = self.find_elements(*Xpath.betting_numbers1x)
                button_0xto1x = [button_numbers0x, button_numbers1x]
                count = 0
                while count < 2:
                    num = 0
                    GamePageCommon(self.driver).check_countdown_time()
                    for buttons in button_0xto1x[count]:
                        buttons.click()
                        num += 1
                        if num % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                    count += 1
                GamePageCommon(self.driver).check_countdown_time()
                button_numbers2x = self.find_elements(*Xpath.betting_numbers2x)
                button_numbers3x = self.find_elements(*Xpath.betting_numbers3x)
                button_2xto3x = [button_numbers2x, button_numbers3x]
                count = 0
                while count < 2:
                    num = 0
                    for buttons in button_2xto3x[count]:
                        buttons.click()
                        num += 1
                        if num % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                    count += 1
                GamePageCommon(self.driver).check_countdown_time()
                button_numbers4x = self.find_elements(*Xpath.betting_numbers4x)
                count = 0
                for buttons in button_numbers4x:
                    if count % 10 == 0:
                        GamePageCommon(self.driver).check_countdown_time()
                    buttons.click()
                    count += 1
                GamePageCommon(self.driver).check_countdown_time()
                all_buttons = self.find_elements(*Xpath.betting_not_number)
                count = 0
                for buttons in all_buttons:
                    if count % 10 == 0:
                        GamePageCommon(self.driver).check_countdown_time()
                    buttons.click()
                    count += 1

        elif type_name in ['main1to6']:
            if Target == 'app':
                GamePageCommon(self.driver).check_countdown_time()
                all_buttons = self.find_elements(*Xpath.betting_squares)
                count = 0
                for buttons in all_buttons:
                    if count % 5 == 0:
                        GamePageCommon(self.driver).check_countdown_time()
                    buttons.click()
                    count += 1

            elif Target == 'h5':
                GamePageCommon(self.driver).check_countdown_time()
                button_squares_set = self.find_elements(*Xpath.betting_squares_set)
                button_squares_color = self.find_elements(*Xpath.betting_squares_color)
                button_SetToColor = [button_squares_set, button_squares_color]
                count = 0
                while count < 2:
                    num = 0
                    GamePageCommon(self.driver).check_countdown_time()
                    for buttons in button_SetToColor[count]:
                        buttons.click()
                        num += 1
                        if num % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                    count += 1

            elif Target == 'web':
                GamePageCommon(self.driver).check_countdown_time()
                all_buttons = self.find_elements(*Xpath.betting_not_number)
                count = 0
                for buttons in all_buttons:
                    if count % 5 == 0:
                        GamePageCommon(self.driver).check_countdown_time()
                    buttons.click()
                    count += 1

        elif type_name in ['mainSpecial']:
            if Platform == 'Android' and Target == 'app':
                GamePageCommon(self.driver).check_countdown_time()
                end_location = self.find_element(*Xpath.history_button).location
                button_01_to_49 = self.find_elements(*Xpath.betting_numbers)
                count = 0
                while count < 3:
                    num = 0
                    if count == 2:
                        GamePageCommon(self.driver).check_countdown_time()
                        rest_buttons = self.find_elements(*Xpath.betting_squares)
                        for buttons in rest_buttons:
                            if num % 5 == 0:
                                GamePageCommon(self.driver).check_countdown_time()
                            buttons.click()
                            num += 1
                    elif count == 1:
                        GamePageCommon(self.driver).check_countdown_time()
                        for buttons in button_01_to_49[:24]:
                            if num % 5 == 0:
                                GamePageCommon(self.driver).check_countdown_time()
                            buttons.click()
                            num += 1
                    else:
                        for buttons in button_01_to_49[:25]:
                            if num % 5 == 0:
                                GamePageCommon(self.driver).check_countdown_time()
                            buttons.click()
                            num += 1

                    if count < 2:
                        GamePageCommon(self.driver).check_countdown_time()
                        start_location = self.find_element(*Xpath.button_row5).location
                        self.swipe(start_location, end_location, y2scale=0.4)
                    count += 1

            elif Platform == 'Android' and Target == 'h5':
                GamePageCommon(self.driver).check_countdown_time()
                end_location = self.find_element(*Xpath.history_button).location
                button_numbers0x = self.find_elements(*Xpath.betting_numbers0x)
                button_numbers1x = self.find_elements(*Xpath.betting_numbers1x)
                button_0xto1x = [button_numbers0x, button_numbers1x]
                count = 0
                while count < 2:
                    num = 0
                    GamePageCommon(self.driver).check_countdown_time()
                    for buttons in button_0xto1x[count]:
                        buttons.click()
                        num += 1
                        if num % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                    count += 1

                GamePageCommon(self.driver).check_countdown_time()
                start_location = self.find_element(*Xpath.button_16).location
                self.swipe(start_location, end_location, y2scale=1)

                GamePageCommon(self.driver).check_countdown_time()
                button_numbers2x = self.find_elements(*Xpath.betting_numbers2x)
                button_numbers3x = self.find_elements(*Xpath.betting_numbers3x)
                button_2xto3x = [button_numbers2x, button_numbers3x]
                count = 0
                while count < 2:
                    num = 0
                    for buttons in button_2xto3x[count]:
                        buttons.click()
                        num += 1
                        if num % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                    count += 1

                GamePageCommon(self.driver).check_countdown_time()
                start_location = self.find_element(*Xpath.button_36).location
                self.swipe(start_location, end_location, y2scale=1)

                GamePageCommon(self.driver).check_countdown_time()
                button_numbers4x = self.find_elements(*Xpath.betting_numbers4x)
                count = 0
                for buttons in button_numbers4x:
                    if count % 5 == 0:
                        GamePageCommon(self.driver).check_countdown_time()
                    buttons.click()
                    count += 1

                GamePageCommon(self.driver).check_countdown_time()
                start_location = self.find_element(*Xpath.button_46).location
                self.swipe(start_location, end_location, y2scale=0.6)

                GamePageCommon(self.driver).check_countdown_time()
                button_squares_set = self.find_elements(*Xpath.betting_squares_set)
                button_squares_color = self.find_elements(*Xpath.betting_squares_color)
                rest_buttons = [button_squares_set, button_squares_color]
                count = 0
                while count < 2:
                    num = 0
                    for buttons in rest_buttons[count]:
                        buttons.click()
                        num += 1
                        if num % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                    count += 1

            elif Platform == 'iOS' and Target == 'app':
                GamePageCommon(self.driver).check_countdown_time()
                end_location = self.find_element(*Xpath.history_button).location
                button_numbers0x = self.find_elements(*Xpath.betting_numbers0x)
                button_numbers1x = self.find_elements(*Xpath.betting_numbers1x)
                button_0xto1x = [button_numbers0x, button_numbers1x]
                count = 0
                while count < 2:
                    GamePageCommon(self.driver).check_countdown_time(check_time=60)
                    for buttons in button_0xto1x[count]:
                        buttons.click()
                    count += 1

                GamePageCommon(self.driver).check_countdown_time()
                start_location = self.find_element(*Xpath.button_16).location
                self.swipe(start_location, end_location, y2scale=1.2, duration=1500)

                GamePageCommon(self.driver).check_countdown_time()
                button_numbers2x = self.find_elements(*Xpath.betting_numbers2x)
                button_numbers3x = self.find_elements(*Xpath.betting_numbers3x)
                button_2xto3x = [button_numbers2x, button_numbers3x]
                count = 0
                while count < 2:
                    GamePageCommon(self.driver).check_countdown_time(check_time=60)
                    for buttons in button_2xto3x[count]:
                        buttons.click()
                    count += 1

                GamePageCommon(self.driver).check_countdown_time()
                start_location = self.find_element(*Xpath.button_36).location
                self.swipe(start_location, end_location, y2scale=1.2, duration=1500)

                GamePageCommon(self.driver).check_countdown_time()
                button_numbers4x = self.find_elements(*Xpath.betting_numbers4x)
                GamePageCommon(self.driver).check_countdown_time(check_time=60)
                for buttons in button_numbers4x:
                    buttons.click()

                GamePageCommon(self.driver).check_countdown_time()
                start_location = self.find_element(*Xpath.button_46).location
                self.swipe(start_location, end_location, y2scale=0.6, duration=1500)

                GamePageCommon(self.driver).check_countdown_time()
                rest_buttons = self.find_elements(*Xpath.betting_squares)
                GamePageCommon(self.driver).check_countdown_time(check_time=60)
                for buttons in rest_buttons:
                    buttons.click()

            elif Target == 'web':
                GamePageCommon(self.driver).check_countdown_time()
                button_numbers0x = self.find_elements(*Xpath.betting_numbers0x)
                button_numbers1x = self.find_elements(*Xpath.betting_numbers1x)
                button_0xto1x = [button_numbers0x, button_numbers1x]
                count = 0
                while count < 2:
                    num = 0
                    GamePageCommon(self.driver).check_countdown_time()
                    for buttons in button_0xto1x[count]:
                        buttons.click()
                        num += 1
                        if num % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                    count += 1
                GamePageCommon(self.driver).check_countdown_time()
                button_numbers2x = self.find_elements(*Xpath.betting_numbers2x)
                button_numbers3x = self.find_elements(*Xpath.betting_numbers3x)
                button_2xto3x = [button_numbers2x, button_numbers3x]
                count = 0
                while count < 2:
                    num = 0
                    for buttons in button_2xto3x[count]:
                        buttons.click()
                        num += 1
                        if num % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                    count += 1
                GamePageCommon(self.driver).check_countdown_time()
                button_numbers4x = self.find_elements(*Xpath.betting_numbers4x)
                count = 0
                for buttons in button_numbers4x:
                    if count % 10 == 0:
                        GamePageCommon(self.driver).check_countdown_time()
                    buttons.click()
                    count += 1
                GamePageCommon(self.driver).check_countdown_time()
                all_buttons = self.find_elements(*Xpath.betting_not_number)
                count = 0
                for buttons in all_buttons:
                    if count % 10 == 0:
                        GamePageCommon(self.driver).check_countdown_time()
                    buttons.click()
                    count += 1

        elif type_name in ['multiNo', 'notWinning']:
            if subtype_name in ['notWinning5', 'notWinning6']:
                if bet_case == 'notWinningCase1':  # 1-8
                    GamePageCommon(self.driver).check_countdown_time()
                    button_01_to_49 = self.find_elements(*Xpath.betting_numbers)
                    count = 0
                    for buttons in button_01_to_49[:8]:
                        if count % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                        buttons.click()
                        count += 1

                elif bet_case == 'notWinningCase2':  # 9-16
                    GamePageCommon(self.driver).check_countdown_time()
                    button_01_to_49 = self.find_elements(*Xpath.betting_numbers)
                    count = 0
                    for buttons in button_01_to_49[8:16]:
                        if count % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                        buttons.click()
                        count += 1

                elif bet_case == 'notWinningCase3':  # 17-24
                    GamePageCommon(self.driver).check_countdown_time()
                    button_01_to_49 = self.find_elements(*Xpath.betting_numbers)
                    count = 0
                    for buttons in button_01_to_49[16:24]:
                        if count % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                        buttons.click()
                        count += 1

                elif bet_case == 'notWinningCase4':  # 25-32
                    GamePageCommon(self.driver).check_countdown_time()
                    start_location = self.find_element(*Xpath.button_row5).location
                    end_location = self.find_element(*Xpath.history_button).location
                    self.swipe(start_location, end_location, y2scale=1)

                    GamePageCommon(self.driver).check_countdown_time()
                    button_01_to_49 = self.find_elements(*Xpath.betting_numbers)
                    count = 0
                    for buttons in button_01_to_49[4:12]:
                        if count % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                        buttons.click()
                        count += 1

                elif bet_case == 'notWinningCase5':  # 33-40
                    GamePageCommon(self.driver).check_countdown_time()
                    start_location = self.find_element(*Xpath.button_row5).location
                    end_location = self.find_element(*Xpath.history_button).location
                    self.swipe(start_location, end_location, y2scale=1)

                    GamePageCommon(self.driver).check_countdown_time()
                    button_01_to_49 = self.find_elements(*Xpath.betting_numbers)
                    count = 0
                    for buttons in button_01_to_49[12:20]:
                        if count % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                        buttons.click()
                        count += 1

                elif bet_case == 'notWinningCase6':  # 41-48
                    GamePageCommon(self.driver).check_countdown_time()
                    start_location = self.find_element(*Xpath.button_row5).location
                    end_location = self.find_element(*Xpath.history_button).location
                    self.swipe(start_location, end_location, y2scale=1)

                    GamePageCommon(self.driver).check_countdown_time()
                    button_01_to_49 = self.find_elements(*Xpath.betting_numbers)
                    count = 0
                    for buttons in button_01_to_49[20:28]:
                        if count % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                        buttons.click()
                        count += 1

                elif bet_case == 'notWinningCase7':  # 42-49
                    GamePageCommon(self.driver).check_countdown_time()
                    start_location = self.find_element(*Xpath.button_row5).location
                    end_location = self.find_element(*Xpath.history_button).location
                    self.swipe(start_location, end_location, y2scale=1)

                    GamePageCommon(self.driver).check_countdown_time()
                    button_01_to_49 = self.find_elements(*Xpath.betting_numbers)
                    count = 0
                    for buttons in button_01_to_49[-8:]:
                        if count % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                        buttons.click()
                        count += 1

            else:  # 連碼/不中(七不中/八不中/九不中/十不中)
                if bet_case in ['multiNoCase1', 'notWinningCase1']:  # 1-10
                    GamePageCommon(self.driver).check_countdown_time()
                    button_01_to_49 = self.find_elements(*Xpath.betting_numbers)
                    count = 0
                    for buttons in button_01_to_49[:10]:
                        if count % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                        buttons.click()
                        count += 1

                elif bet_case in ['multiNoCase2', 'notWinningCase2']:  # 11-20
                    GamePageCommon(self.driver).check_countdown_time()
                    button_01_to_49 = self.find_elements(*Xpath.betting_numbers)
                    count = 0
                    for buttons in button_01_to_49[10:20]:
                        if count % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                        buttons.click()
                        count += 1

                elif bet_case in ['multiNoCase3', 'notWinningCase3']:  # 21-30
                    GamePageCommon(self.driver).check_countdown_time()
                    start_location = self.find_element(*Xpath.button_row5).location
                    end_location = self.find_element(*Xpath.history_button).location
                    self.swipe(start_location, end_location, y2scale=0.9)

                    GamePageCommon(self.driver).check_countdown_time()
                    button_01_to_49 = self.find_elements(*Xpath.betting_numbers)
                    count = 0
                    for buttons in button_01_to_49[:10]:
                        if count % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                        buttons.click()
                        count += 1

                elif bet_case in ['multiNoCase4', 'notWinningCase4']:  # 31-40
                    GamePageCommon(self.driver).check_countdown_time()
                    start_location = self.find_element(*Xpath.button_row5).location
                    end_location = self.find_element(*Xpath.history_button).location
                    self.swipe(start_location, end_location, y2scale=0.9)

                    GamePageCommon(self.driver).check_countdown_time()
                    button_01_to_49 = self.find_elements(*Xpath.betting_numbers)
                    count = 0
                    for buttons in button_01_to_49[10:20]:
                        if count % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                        buttons.click()
                        count += 1

                elif bet_case in ['multiNoCase5', 'notWinningCase5']:  # 40-49
                    GamePageCommon(self.driver).check_countdown_time()
                    start_location = self.find_element(*Xpath.button_row5).location
                    end_location = self.find_element(*Xpath.history_button).location
                    self.swipe(start_location, end_location, y2scale=0.9)

                    GamePageCommon(self.driver).check_countdown_time()
                    button_01_to_49 = self.find_elements(*Xpath.betting_numbers)
                    count = 0
                    for buttons in button_01_to_49[-10:]:
                        if count % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                        buttons.click()
                        count += 1

        elif type_name in ['halfBall']:
            if Platform == 'Android' and Target == 'app':
                GamePageCommon(self.driver).check_countdown_time()
                end_location = self.find_element(*Xpath.history_button).location
                all_buttons = self.find_elements(*Xpath.betting_sets)
                count = 0
                while count < 5:
                    num = 0
                    if count == 4:
                        GamePageCommon(self.driver).check_countdown_time()
                        for buttons in all_buttons[-2:]:
                            if num % 5 == 0:
                                GamePageCommon(self.driver).check_countdown_time()
                            buttons.click()
                            num += 1
                    else:
                        for buttons in all_buttons[:4]:
                            if num % 5 == 0:
                                GamePageCommon(self.driver).check_countdown_time()
                            buttons.click()
                            num += 1

                    if count < 4:
                        GamePageCommon(self.driver).check_countdown_time()
                        start_location = self.find_element(*Xpath.button_row4).location
                        self.swipe(start_location, end_location, y2scale=0.2)
                    count += 1

            elif Platform == 'Android' and Target == 'h5':
                count = 1
                while count < 19:
                    GamePageCommon(self.driver).check_countdown_time()
                    button = self.find_element(*(By.XPATH, Xpath.betting_halfBall + "[" + str(count) + "]"))
                    button.click()
                    count += 1
                    if count % 4 == 0:
                        GamePageCommon(self.driver).check_countdown_time()
                        button_forth = self.find_element(*(By.XPATH, Xpath.betting_halfBall + "[" + str(count) + "]"))
                        start_location = button_forth.location
                        end_location = self.find_element(*Xpath.history_button).location
                        self.swipe(start_location, end_location, y2scale=1)

            elif Platform == 'iOS' and Target == 'app':
                GamePageCommon(self.driver).check_countdown_time()
                end_location = self.find_element(*Xpath.history_button).location
                betting_halfBall = self.find_elements(*Xpath.betting_halfBall)
                for buttons in betting_halfBall[:4]:
                    buttons.click()

                GamePageCommon(self.driver).check_countdown_time()
                start_location = self.find_element(*Xpath.button_red_even).location
                self.swipe(start_location, end_location, y2scale=1.2, duration=2000)

                GamePageCommon(self.driver).check_countdown_time()
                betting_halfBall = self.find_elements(*Xpath.betting_halfBall)
                for buttons in betting_halfBall[4:8]:
                    buttons.click()

                GamePageCommon(self.driver).check_countdown_time()
                start_location = self.find_element(*Xpath.button_blue_small).location
                self.swipe(start_location, end_location, y2scale=1.2, duration=2000)

                GamePageCommon(self.driver).check_countdown_time()
                betting_halfBall = self.find_elements(*Xpath.betting_halfBall)
                for buttons in betting_halfBall[8:12]:
                    buttons.click()

                GamePageCommon(self.driver).check_countdown_time()
                start_location = self.find_element(*Xpath.button_blue_total_even).location
                self.swipe(start_location, end_location, y2scale=1.2, duration=2000)

                GamePageCommon(self.driver).check_countdown_time()
                betting_halfBall = self.find_elements(*Xpath.betting_halfBall)
                for buttons in betting_halfBall[12:16]:
                    buttons.click()

                GamePageCommon(self.driver).check_countdown_time()
                start_location = self.find_element(*Xpath.button_green_even).location
                self.swipe(start_location, end_location, y2scale=1.2, duration=2000)

                GamePageCommon(self.driver).check_countdown_time()
                betting_halfBall = self.find_elements(*Xpath.betting_halfBall)
                for buttons in betting_halfBall[-2:]:
                    buttons.click()

            elif Target == 'web':
                GamePageCommon(self.driver).check_countdown_time()
                all_buttons = self.find_elements(*Xpath.betting_sets)
                count = 0
                for buttons in all_buttons:
                    if count % 5 == 0:
                        GamePageCommon(self.driver).check_countdown_time()
                    buttons.click()
                    count += 1

        elif type_name in ['tailNo']:
            if Platform == 'Android' and Target == 'app':
                GamePageCommon(self.driver).check_countdown_time()
                end_location = self.find_element(*Xpath.history_button).location
                all_buttons = self.find_elements(*Xpath.betting_sets)
                count = 0
                while count < 3:
                    num = 0
                    if count == 2:
                        GamePageCommon(self.driver).check_countdown_time()
                        for buttons in all_buttons[-2:]:
                            if num % 5 == 0:
                                GamePageCommon(self.driver).check_countdown_time()
                            buttons.click()
                            num += 1
                    else:
                        for buttons in all_buttons[:4]:
                            if num % 5 == 0:
                                GamePageCommon(self.driver).check_countdown_time()
                            buttons.click()
                            num += 1

                    if count < 1:
                        GamePageCommon(self.driver).check_countdown_time()
                        start_location = self.find_element(*Xpath.button_row4).location
                        self.swipe(start_location, end_location, y2scale=0.2)
                    count += 1

            elif Platform == 'Android' and Target == 'h5':
                count = 1
                while count < 11:
                    GamePageCommon(self.driver).check_countdown_time()
                    button = self.find_element(*(By.XPATH, Xpath.betting_tailNo + "[" + str(count) + "]"))
                    button.click()
                    count += 1
                    if count % 4 == 0:
                        GamePageCommon(self.driver).check_countdown_time()
                        button_forth = self.find_element(*(By.XPATH, Xpath.betting_tailNo + "[" + str(count) + "]"))
                        start_location = button_forth.location
                        end_location = self.find_element(*Xpath.history_button).location
                        self.swipe(start_location, end_location, y2scale=1)

            elif Platform == 'iOS' and Target == 'app':
                GamePageCommon(self.driver).check_countdown_time()
                end_location = self.find_element(*Xpath.history_button).location
                betting_tailNo = self.find_elements(*Xpath.betting_tailNo)
                for buttons in betting_tailNo[:5]:
                    buttons.click()

                GamePageCommon(self.driver).check_countdown_time()
                start_location = self.find_element(*Xpath.button_tail4).location
                self.swipe(start_location, end_location, y2scale=1)

                GamePageCommon(self.driver).check_countdown_time()
                betting_tailNo = self.find_elements(*Xpath.betting_tailNo)
                for buttons in betting_tailNo[-5:]:
                    buttons.click()

            elif Target == 'web':
                GamePageCommon(self.driver).check_countdown_time()
                all_buttons = self.find_elements(*Xpath.betting_tailNo_zodiac1_specialZodiac_betting_sets)
                count = 0
                for buttons in all_buttons:
                    if count % 5 == 0:
                        GamePageCommon(self.driver).check_countdown_time()
                    buttons.click()
                    count += 1

        elif type_name in ['zodiac1', 'specialZodiac']:
            if Platform == 'Android' and Target == 'app':
                GamePageCommon(self.driver).check_countdown_time()
                end_location = self.find_element(*Xpath.history_button).location
                all_buttons = self.find_elements(*Xpath.betting_sets)
                count = 0
                while count < 2:
                    num = 0
                    for buttons in all_buttons[:6]:
                        if num % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                        buttons.click()
                        num += 1

                    if count < 1:
                        GamePageCommon(self.driver).check_countdown_time()
                        start_location = self.find_element(*Xpath.button_row6).location
                        self.swipe(start_location, end_location, y2scale=0.2)
                    count += 1

            elif Platform == 'Android' and Target == 'h5':
                count = 1
                while count < 13:
                    GamePageCommon(self.driver).check_countdown_time()
                    button = self.find_element(*(By.XPATH, Xpath.betting_zodiac + "[" + str(count) + "]"))
                    button.click()
                    count += 1
                    if count % 4 == 0:
                        GamePageCommon(self.driver).check_countdown_time()
                        button_forth = self.find_element(*(By.XPATH, Xpath.betting_zodiac + "[" + str(count) + "]"))
                        start_location = button_forth.location
                        end_location = self.find_element(*Xpath.history_button).location
                        self.swipe(start_location, end_location, y2scale=1)

            elif Platform == 'iOS' and Target == 'app':
                GamePageCommon(self.driver).check_countdown_time()
                end_location = self.find_element(*Xpath.history_button).location
                betting_zodiac = self.find_elements(*Xpath.betting_zodiac)
                for buttons in betting_zodiac[:4]:
                    buttons.click()

                GamePageCommon(self.driver).check_countdown_time()
                start_location = self.find_element(*Xpath.button_rabbit).location
                self.swipe(start_location, end_location, y2scale=1.2)

                GamePageCommon(self.driver).check_countdown_time()
                betting_zodiac = self.find_elements(*Xpath.betting_zodiac)
                for buttons in betting_zodiac[4:8]:
                    buttons.click()

                GamePageCommon(self.driver).check_countdown_time()
                start_location = self.find_element(*Xpath.button_sheep).location
                self.swipe(start_location, end_location, y2scale=1.2)

                GamePageCommon(self.driver).check_countdown_time()
                betting_zodiac = self.find_elements(*Xpath.betting_zodiac)
                for buttons in betting_zodiac[-4:]:
                    buttons.click()

            elif Target == 'web':
                GamePageCommon(self.driver).check_countdown_time()
                all_buttons = self.find_elements(*Xpath.betting_tailNo_zodiac1_specialZodiac_betting_sets)
                count = 0
                for buttons in all_buttons:
                    if count % 5 == 0:
                        GamePageCommon(self.driver).check_countdown_time()
                    buttons.click()
                    count += 1

        elif type_name in ['zodiac6', 'zodiacs']:
            if bet_case in ['zodiac6Case1', 'zodiacsCase1']:  # 鼠-蛇
                GamePageCommon(self.driver).check_countdown_time()
                all_buttons = self.find_elements(*Xpath.betting_sets)
                count = 0
                for buttons in all_buttons[:6]:
                    if count % 5 == 0:
                        GamePageCommon(self.driver).check_countdown_time()
                    buttons.click()
                    count += 1

            elif bet_case in ['zodiac6Case2', 'zodiacsCase2']:  # 馬-豬
                GamePageCommon(self.driver).check_countdown_time()
                start_location = self.find_element(*Xpath.button_row6).location
                end_location = self.find_element(*Xpath.history_button).location
                self.swipe(start_location, end_location, y2scale=0.2)

                GamePageCommon(self.driver).check_countdown_time()
                all_buttons = self.find_elements(*Xpath.betting_sets)
                count = 0
                for buttons in all_buttons[:6]:
                    if count % 5 == 0:
                        GamePageCommon(self.driver).check_countdown_time()
                    buttons.click()
                    count += 1

        elif type_name in ['tails']:
            if bet_case == 'tailsCase1':  # 0尾-4尾
                GamePageCommon(self.driver).check_countdown_time()
                all_buttons = self.find_elements(*Xpath.betting_sets)
                count = 0
                for buttons in all_buttons[:5]:
                    if count % 5 == 0:
                        GamePageCommon(self.driver).check_countdown_time()
                    buttons.click()
                    count += 1

            elif bet_case == 'tailsCase2':  # 5尾-9尾
                GamePageCommon(self.driver).check_countdown_time()
                start_location = self.find_element(*Xpath.button_row6).location
                end_location = self.find_element(*Xpath.history_button).location
                self.swipe(start_location, end_location, y2scale=1)

                GamePageCommon(self.driver).check_countdown_time()
                all_buttons = self.find_elements(*Xpath.betting_sets)
                count = 0
                for buttons in all_buttons[-5:]:
                    if count % 5 == 0:
                        GamePageCommon(self.driver).check_countdown_time()
                    buttons.click()
                    count += 1

        elif type_name in ['dt16']:
            if Platform == 'Android' and Target == 'app':
                GamePageCommon(self.driver).check_countdown_time()
                all_buttons = self.find_elements(*Xpath.betting_squares)
                count = 0
                for buttons in all_buttons[:15]:
                    if count % 5 == 0:
                        GamePageCommon(self.driver).check_countdown_time()
                    buttons.click()
                    count += 1

                GamePageCommon(self.driver).check_countdown_time()
                start_location = self.find_element(*Xpath.title_tiger).location
                end_location = self.find_element(*Xpath.history_button).location
                self.swipe(start_location, end_location, y2scale=1)

                GamePageCommon(self.driver).check_countdown_time()
                all_buttons = self.find_elements(*Xpath.betting_squares)
                count = 0
                for buttons in all_buttons[-15:]:
                    if count % 5 == 0:
                        GamePageCommon(self.driver).check_countdown_time()
                    buttons.click()
                    count += 1

            elif Platform == 'Android' and Target == 'h5':
                GamePageCommon(self.driver).check_countdown_time()
                button_dt16_dragon = self.find_elements(*Xpath.betting_dt16_dragon)
                count = 0
                for buttons in button_dt16_dragon:
                    if count % 5 == 0:
                        GamePageCommon(self.driver).check_countdown_time()
                    buttons.click()
                    count += 1

                GamePageCommon(self.driver).check_countdown_time()
                start_location = self.find_element(*Xpath.title_tiger).location
                end_location = self.find_element(*Xpath.history_button).location
                self.swipe(start_location, end_location, y2scale=1)

                GamePageCommon(self.driver).check_countdown_time()
                button_dt16_tiger = self.find_elements(*Xpath.betting_dt16_tiger)
                count = 0
                for buttons in button_dt16_tiger:
                    if count % 5 == 0:
                        GamePageCommon(self.driver).check_countdown_time()
                    buttons.click()
                    count += 1

            elif Platform == 'iOS' and Target == 'app':
                GamePageCommon(self.driver).check_countdown_time()
                button_dt16_dragon = self.find_elements(*Xpath.betting_dt16_dragon)
                count = 0
                for buttons in button_dt16_dragon:
                    if count % 5 == 0:
                        GamePageCommon(self.driver).check_countdown_time()
                    buttons.click()
                    count += 1

                GamePageCommon(self.driver).check_countdown_time()
                start_location = self.find_element(*Xpath.title_tiger).location
                end_location = self.find_element(*Xpath.history_button).location
                self.swipe(start_location, end_location, y2scale=0.9)

                GamePageCommon(self.driver).check_countdown_time()
                button_dt16_tiger = self.find_elements(*Xpath.betting_dt16_tiger)
                count = 0
                for buttons in button_dt16_tiger:
                    if count % 5 == 0:
                        GamePageCommon(self.driver).check_countdown_time()
                    buttons.click()
                    count += 1

            elif Target == 'web':
                GamePageCommon(self.driver).check_countdown_time()
                all_buttons = self.find_elements(*Xpath.betting_not_number)
                count = 0
                for buttons in all_buttons:
                    if count % 10 == 0:
                        GamePageCommon(self.driver).check_countdown_time()
                    buttons.click()
                    count += 1


if __name__ == '__main__':
    pass
