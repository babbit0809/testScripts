import time
from selenium.webdriver.common.by import By
from config.SetUIConfig import Platform, Target
from test_UI.common import BasePage
from test_UI.page.GamePagePK10_Locator import Xpath
from test_UI.common.GamePageCommon import GamePageCommon


class GamePagePK10(BasePage.BasePage):
    # Actions
    def switch_pro_game(self, game_type, game_name):  # PK10無子玩法階層
        # 切換官方盤/雙面盤
        GamePageCommon(self.driver).switch_bet_category('pro')
        # 點擊官方盤玩法選單
        GamePageCommon(self.driver).click_pro_game_option()
        # 避免被盈虧視窗擋住的檢查機制
        GamePageCommon(self.driver).check_pro_game_option_showing()
        # 切換常規/趣味
        if Target in ['app', 'h5', 'web']:
            if game_type == 'normal':
                game_type = self.find_element(*Xpath.pro_game_type_normal)
            elif game_type == 'fun':
                game_type = self.find_element(*Xpath.pro_game_type_fun)
            game_type.click()
        # 切換主玩法
        if Target in ['app', 'h5']:
            pro_game_name_All = self.find_elements(*Xpath.pro_game_name_All)
            if game_name in ['guess1', 'eat1']:
                game_name = pro_game_name_All[0]
            elif game_name in ['guess12', 'bet3']:
                game_name = pro_game_name_All[1]
            elif game_name in ['guess123', 'eat3']:
                game_name = pro_game_name_All[2]
            elif game_name in ['firstToTenth', 'positionQ']:
                game_name = pro_game_name_All[3]
            elif game_name == 'winningStreak':
                game_name = pro_game_name_All[4]
            game_name.click()
        # H5需多點擊確認按鈕
        if Target == 'h5':
            confirm_button = self.find_element(*Xpath.button_pro_game_confirm)
            confirm_button.click()

        elif Target == 'web':
            if game_name == 'guess1':
                game_name = self.find_element(*Xpath.normal_guess1)
            elif game_name == 'guess12':
                game_name = self.find_element(*Xpath.normal_guess12)
            elif game_name == 'guess123':
                game_name = self.find_element(*Xpath.normal_guess123)
            elif game_name == 'firstToTenth':
                game_name = self.find_element(*Xpath.normal_firstToTenth)
            elif game_name == 'eat1':
                game_name = self.find_element(*Xpath.fun_eat1)
            elif game_name == 'bet3':
                game_name = self.find_element(*Xpath.fun_bet3)
            elif game_name == 'eat3':
                game_name = self.find_element(*Xpath.fun_eat3)
            elif game_name == 'positionQ':
                game_name = self.find_element(*Xpath.fun_positionQ)
            elif game_name == 'winningStreak':
                game_name = self.find_element(*Xpath.fun_winningStreak)
            game_name.click()

    def switch_twoSide_game(self, game_name):
        if Target == 'h5':  # 避免H5因UI遮蔽玩法選單出錯
            self.driver.refresh()
            time.sleep(5)
        # 切換官方盤/雙面盤
        GamePageCommon(self.driver).switch_bet_category('twoSide')
        # 切換主玩法
        if Target in ['app', 'h5']:
            time.sleep(3)
            twoSide_game_name_All = self.find_elements(*Xpath.twoSide_game_name_All)
            if game_name == 'twoface':
                game_name = twoSide_game_name_All[0]
            elif game_name == 'combination1and2':
                game_name = twoSide_game_name_All[1]
            elif game_name == 'sum1and2':
                game_name = twoSide_game_name_All[2]
            elif game_name == 'firsttotenth':
                game_name = twoSide_game_name_All[3]
            game_name.click()

        elif Target == 'web':
            if game_name == 'twoface':
                game_name = self.find_element(*Xpath.two_side_twoface)
            elif game_name == 'combination1and2':
                game_name = self.find_element(*Xpath.two_side_combination1and2)
            elif game_name == 'sum1and2':
                game_name = self.find_element(*Xpath.two_side_sum1and2)
            elif game_name == 'firsttotenth':
                game_name = self.find_element(*Xpath.two_side_firsttotenth)
            game_name.click()

    def bet_pro_all(self, type_name):
        if type_name in ['guess1', 'guess12', 'guess123', 'eat1', 'bet3', 'eat3', 'positionQ', 'winningStreak']:
            GamePageCommon(self.driver).check_countdown_time()
            all_button = self.find_elements(*Xpath.betting_all_button)
            for buttons in all_button:
                buttons.click()

        elif type_name == 'firstToTenth':
            if Platform == 'Android' and Target == 'app':
                GamePageCommon(self.driver).check_countdown_time()
                end_location = self.find_element(*Xpath.history_button).location
                first_to_eight = self.find_elements(*Xpath.betting_firstToTenth)
                count = 0
                while count < 9:
                    num = 0
                    if count == 8:
                        GamePageCommon(self.driver).check_countdown_time()
                        ninth_to_tenth = self.find_elements(*Xpath.betting_firstToTenth)
                        for buttons in ninth_to_tenth[-20:]:
                            buttons.click()
                            num += 1
                            if num % 5 == 0:
                                GamePageCommon(self.driver).check_countdown_time()
                    else:
                        for buttons in first_to_eight[:10]:
                            buttons.click()
                            num += 1
                            if num % 5 == 0:
                                GamePageCommon(self.driver).check_countdown_time()

                    if count < 8:
                        GamePageCommon(self.driver).check_countdown_time()
                        start_location = self.find_element(*Xpath.next_title).location
                        self.swipe(start_location, end_location, y2scale=1)
                    count += 1

            elif Platform == 'Android' and Target == 'h5':
                buttons_first_to_tenth = [Xpath.betting_first, Xpath.betting_second,
                                          Xpath.betting_third, Xpath.betting_fourth,
                                          Xpath.betting_fifth, Xpath.betting_sixth,
                                          Xpath.betting_seventh, Xpath.betting_eighth,
                                          Xpath.betting_ninth, Xpath.betting_tenth]
                title_first_to_tenth = [Xpath.title_first, Xpath.title_second,
                                        Xpath.title_third, Xpath.title_fourth,
                                        Xpath.title_fifth, Xpath.title_sixth,
                                        Xpath.title_seventh, Xpath.title_eighth,
                                        Xpath.title_ninth, Xpath.title_tenth]
                GamePageCommon(self.driver).check_countdown_time()
                end_location = self.find_element(*Xpath.history_button).location
                count = 0
                while count < 10:
                    GamePageCommon(self.driver).check_countdown_time()
                    next_title = self.find_element(*(By.XPATH, title_first_to_tenth[count]))
                    start_location = next_title.location
                    self.swipe(start_location, end_location, y2scale=1)

                    GamePageCommon(self.driver).check_countdown_time()
                    buttons = self.find_elements(*(By.XPATH, buttons_first_to_tenth[count]))
                    num = 0
                    for button in buttons:
                        button.click()
                        num += 1
                        if num % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                    count += 1

            elif Platform == 'iOS' and Target == 'app':
                first_to_tenth = [Xpath.betting_first, Xpath.betting_second, Xpath.betting_third, Xpath.betting_fourth,
                                  Xpath.betting_fifth, Xpath.betting_sixth, Xpath.betting_seventh, Xpath.betting_eighth,
                                  Xpath.betting_ninth, Xpath.betting_tenth]
                GamePageCommon(self.driver).check_countdown_time()
                end_location = self.find_element(*Xpath.history_button).location
                count = 0
                while count < 10:
                    GamePageCommon(self.driver).check_countdown_time(check_time=60)
                    buttons = self.find_elements(*(By.XPATH, first_to_tenth[count]))
                    for button in buttons:
                        button.click()
                    count += 1
                    if count < 9:
                        GamePageCommon(self.driver).check_countdown_time()
                        next_title = self.find_element(*(By.XPATH, Xpath.next_title + "[" + str(count + 1) + "]"))
                        start_location = next_title.location
                        self.swipe(start_location, end_location, y2scale=1)

            elif Target == 'web':
                GamePageCommon(self.driver).check_countdown_time()
                subgames = self.find_elements(*(By.XPATH, Xpath.subgame_firsttotenth))
                for subgame in subgames:
                    subgame.click()
                    count = 0
                    num = 0
                    bet_flow = GamePageCommon(self.driver)
                    bet_flow.set_pro_bet_setting("cent")
                    buttons = self.find_elements(*(By.XPATH, Xpath.betting_items))
                    for button in buttons:
                        button.click()
                        num += 1
                        if num % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                    if count < 9:
                        bet_flow.click_bet_basket()
                        count += 1

    def bet_twoSide_all(self, type_name):
        if type_name == 'twoface':
            if Platform == 'Android' and Target == 'app':
                GamePageCommon(self.driver).check_countdown_time()
                end_location = self.find_element(*Xpath.history_button).location
                first_to_fifth = self.find_elements(*Xpath.betting_twoSide_all_buttons)
                count = 0
                while count < 8:
                    if count == 7:
                        GamePageCommon(self.driver).check_countdown_time()
                        eighth_to_tenth = self.find_elements(*Xpath.betting_twoSide_all_buttons)
                        num = 0
                        for buttons in eighth_to_tenth[-12:]:
                            buttons.click()
                            num += 1
                            if num % 5 == 0:
                                GamePageCommon(self.driver).check_countdown_time()
                    elif count in [5, 6]:
                        GamePageCommon(self.driver).check_countdown_time()
                        sixth_to_seventh = self.find_elements(*Xpath.betting_twoSide_all_buttons)
                        for buttons in sixth_to_seventh[:4]:
                            buttons.click()
                    else:
                        for buttons in first_to_fifth[:6]:
                            buttons.click()

                    if count < 7:
                        GamePageCommon(self.driver).check_countdown_time()
                        start_location = self.find_element(*Xpath.next_title).location
                        self.swipe(start_location, end_location, y2scale=0.9)
                    count += 1

            elif Platform == 'Android' and Target == 'h5':
                buttons_first_to_tenth = [Xpath.betting_twoSide_first, Xpath.betting_twoSide_second,
                                          Xpath.betting_twoSide_third, Xpath.betting_twoSide_fourth,
                                          Xpath.betting_twoSide_fifth, Xpath.betting_twoSide_sixth,
                                          Xpath.betting_twoSide_seventh, Xpath.betting_twoSide_eighth,
                                          Xpath.betting_twoSide_ninth, Xpath.betting_twoSide_tenth]
                title_second_to_tenth = [Xpath.twoSide_title_second, Xpath.twoSide_title_third,
                                         Xpath.twoSide_title_fourth, Xpath.twoSide_title_fifth,
                                         Xpath.twoSide_title_sixth, Xpath.twoSide_title_seventh,
                                         Xpath.twoSide_title_eighth, Xpath.twoSide_title_ninth,
                                         Xpath.twoSide_title_tenth]
                GamePageCommon(self.driver).check_countdown_time()
                end_location = self.find_element(*Xpath.history_button).location
                count = 0
                while count < 10:
                    GamePageCommon(self.driver).check_countdown_time()
                    buttons = self.find_elements(*(By.XPATH, buttons_first_to_tenth[count]))
                    num = 0
                    for button in buttons:
                        button.click()
                        num += 1
                        if num % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                    count += 1
                    if count < 9:
                        GamePageCommon(self.driver).check_countdown_time()
                        next_title = self.find_element(*(By.XPATH, title_second_to_tenth[count]))
                        start_location = next_title.location
                        self.swipe(start_location, end_location, y2scale=1)

            elif Platform == 'iOS' and Target == 'app':
                first_to_tenth = [Xpath.betting_first_twoSide, Xpath.betting_second_twoSide, Xpath.betting_third_twoSide,
                                  Xpath.betting_fourth_twoSide, Xpath.betting_fifth_twoSide, Xpath.betting_sixth_twoSide,
                                  Xpath.betting_seventh_twoSide, Xpath.betting_eighth_twoSide, Xpath.betting_ninth_twoSide,
                                  Xpath.betting_tenth_twoSide]
                GamePageCommon(self.driver).check_countdown_time()
                end_location = self.find_element(*Xpath.history_button).location
                count = 0
                while count < 10:
                    GamePageCommon(self.driver).check_countdown_time(check_time=60)
                    buttons = self.find_elements(*(By.XPATH, first_to_tenth[count]))
                    for button in buttons:
                        button.click()
                    count += 1
                    if count < 9:
                        GamePageCommon(self.driver).check_countdown_time()
                        next_title = self.find_element(*(By.XPATH, Xpath.next_title_twoSide + "[" + str(count + 1) + "]"))
                        start_location = next_title.location
                        self.swipe(start_location, end_location, y2scale=0.9, duration=1500)

            elif Target == 'web':
                GamePageCommon(self.driver).check_countdown_time()
                subgames = self.find_elements(*(By.XPATH, Xpath.subgame_firsttotenth))
                for subgame in subgames:
                    subgame.click()
                    num = 0
                    buttons = self.find_elements(*(By.XPATH, Xpath.betting_items))
                    for button in buttons:
                        button.click()
                        num += 1
                        if num % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()

        elif type_name == 'combination1and2':
            if Platform == 'Android' and Target == 'app':
                GamePageCommon(self.driver).check_countdown_time()
                end_location = self.find_element(*Xpath.history_button).location
                first = self.find_elements(*Xpath.betting_twoSide_all_buttons)
                count = 0
                while count < 7:
                    if count == 6:
                        GamePageCommon(self.driver).check_countdown_time()
                        first = self.find_elements(*Xpath.betting_twoSide_all_buttons)
                        num = 0
                        for buttons in first[-21:]:
                            buttons.click()
                            num += 1
                            if num % 5 == 0:
                                GamePageCommon(self.driver).check_countdown_time()
                    else:
                        for buttons in first[:4]:
                            buttons.click()

                    if count < 6:
                        GamePageCommon(self.driver).check_countdown_time()
                        start_location = self.find_element(*Xpath.button_row2).location
                        self.swipe(start_location, end_location, y2scale=0.9)
                    count += 1

            elif Platform == 'Android' and Target == 'h5':
                buttons_1_to_9 = [Xpath.betting_1, Xpath.betting_2, Xpath.betting_3, Xpath.betting_4,
                                  Xpath.betting_5, Xpath.betting_6, Xpath.betting_7, Xpath.betting_8,
                                  Xpath.betting_9]
                GamePageCommon(self.driver).check_countdown_time()
                end_location = self.find_element(*Xpath.history_button).location
                count = 0
                while count < 9:
                    GamePageCommon(self.driver).check_countdown_time()
                    buttons = self.find_elements(*(By.XPATH, buttons_1_to_9[count]))
                    num = 0
                    for button in buttons:
                        button.click()
                        num += 1
                        if num % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                    count += 1
                    if count % 2 == 0 and count < 5:
                        GamePageCommon(self.driver).check_countdown_time()
                        start_location = buttons[4].location
                        self.swipe(start_location, end_location, y2scale=1)

            elif Platform == 'iOS' and Target == 'app':
                betting_1to9 = [Xpath.betting_1, Xpath.betting_2, Xpath.betting_3, Xpath.betting_4, Xpath.betting_5,
                                Xpath.betting_6, Xpath.betting_7, Xpath.betting_8, Xpath.betting_9]
                GamePageCommon(self.driver).check_countdown_time()
                end_location = self.find_element(*Xpath.history_button).location
                count = 0
                while count < 9:
                    GamePageCommon(self.driver).check_countdown_time()
                    buttons = self.find_elements(*(By.XPATH, betting_1to9[count]))
                    GamePageCommon(self.driver).check_countdown_time(check_time=60)
                    for button in buttons:
                        button.click()
                    count += 1
                    if count % 2 == 0 and count < 5:
                        start_location = buttons[4].location
                        self.swipe(start_location, end_location, y2scale=1.2)

            elif Target == 'web':
                GamePageCommon(self.driver).check_countdown_time()
                num = 0
                buttons = self.find_elements(*(By.XPATH, Xpath.betting_items))
                for button in buttons:
                    button.click()
                    num += 1
                    if num % 5 == 0:
                        GamePageCommon(self.driver).check_countdown_time()

        elif type_name == 'sum1and2':
            if Target == 'web':
                GamePageCommon(self.driver).check_countdown_time()
                num = 0
                buttons = self.find_elements(*(By.XPATH, Xpath.betting_items))
                for button in buttons:
                    button.click()
                    num += 1
                    if num % 5 == 0:
                        GamePageCommon(self.driver).check_countdown_time()
            else:
                GamePageCommon(self.driver).check_countdown_time()
                start_location = self.find_element(*Xpath.button_row1).location
                end_location = self.find_element(*Xpath.history_button).location
                self.swipe(start_location, end_location, y2scale=0.9)

                GamePageCommon(self.driver).check_countdown_time()
                all_buttons = self.find_elements(*Xpath.betting_sum1and2)
                count = 0
                for buttons in all_buttons:
                    buttons.click()
                    count += 1
                    if count % 5 == 0:
                        GamePageCommon(self.driver).check_countdown_time()

        elif type_name == 'firsttotenth':
            if Platform == 'Android' and Target == 'app':
                GamePageCommon(self.driver).check_countdown_time()
                end_location = self.find_element(*Xpath.history_button).location
                first_to_eight = self.find_elements(*Xpath.betting_twoSide_all_buttons)
                count = 0
                while count < 9:
                    num = 0
                    if count == 8:
                        GamePageCommon(self.driver).check_countdown_time()
                        ninth_to_tenth = self.find_elements(*Xpath.betting_twoSide_all_buttons)
                        for buttons in ninth_to_tenth[-20:]:
                            buttons.click()
                            num += 1
                            if num % 5 == 0:
                                GamePageCommon(self.driver).check_countdown_time()
                    else:
                        for buttons in first_to_eight[:10]:
                            buttons.click()
                            num += 1
                            if num % 5 == 0:
                                GamePageCommon(self.driver).check_countdown_time()

                    if count < 8:
                        GamePageCommon(self.driver).check_countdown_time()
                        start_location = self.find_element(*Xpath.next_title).location
                        self.swipe(start_location, end_location, y2scale=0.9)
                    count += 1

            elif Platform == 'Android' and Target == 'h5':
                buttons_first_to_tenth = [Xpath.betting_twoSide_first, Xpath.betting_twoSide_second,
                                          Xpath.betting_twoSide_third, Xpath.betting_twoSide_fourth,
                                          Xpath.betting_twoSide_fifth, Xpath.betting_twoSide_sixth,
                                          Xpath.betting_twoSide_seventh, Xpath.betting_twoSide_eighth,
                                          Xpath.betting_twoSide_ninth, Xpath.betting_twoSide_tenth]
                title_first_to_tenth = [Xpath.twoSide_title_first, Xpath.twoSide_title_second,
                                        Xpath.twoSide_title_third, Xpath.twoSide_title_fourth,
                                        Xpath.twoSide_title_fifth, Xpath.twoSide_title_sixth,
                                        Xpath.twoSide_title_seventh, Xpath.twoSide_title_eighth,
                                        Xpath.twoSide_title_ninth, Xpath.twoSide_title_tenth]
                GamePageCommon(self.driver).check_countdown_time()
                end_location = self.find_element(*Xpath.history_button).location
                count = 0
                while count < 10:
                    GamePageCommon(self.driver).check_countdown_time()
                    next_title = self.find_element(*(By.XPATH, title_first_to_tenth[count]))
                    start_location = next_title.location
                    self.swipe(start_location, end_location, y2scale=1)

                    GamePageCommon(self.driver).check_countdown_time()
                    buttons = self.find_elements(*(By.XPATH, buttons_first_to_tenth[count]))
                    num = 0
                    for button in buttons:
                        button.click()
                        num += 1
                        if num % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                    count += 1

            elif Platform == 'iOS' and Target == 'app':
                first_to_tenth = [Xpath.betting_first_twoSide, Xpath.betting_second_twoSide, Xpath.betting_third_twoSide,
                                  Xpath.betting_fourth_twoSide, Xpath.betting_fifth_twoSide, Xpath.betting_sixth_twoSide,
                                  Xpath.betting_seventh_twoSide, Xpath.betting_eighth_twoSide, Xpath.betting_ninth_twoSide,
                                  Xpath.betting_tenth_twoSide]
                GamePageCommon(self.driver).check_countdown_time()
                end_location = self.find_element(*Xpath.history_button).location
                count = 0
                while count < 10:
                    GamePageCommon(self.driver).check_countdown_time(check_time=60)
                    buttons = self.find_elements(*(By.XPATH, first_to_tenth[count]))
                    for button in buttons:
                        button.click()
                    count += 1
                    if count < 9:
                        GamePageCommon(self.driver).check_countdown_time()
                        next_title = self.find_element(*(By.XPATH, Xpath.next_title_twoSide + "[" + str(count + 1) + "]"))
                        start_location = next_title.location
                        self.swipe(start_location, end_location, y2scale=1, duration=1500)

            elif Target == 'web':
                GamePageCommon(self.driver).check_countdown_time()
                subgames = self.find_elements(*(By.XPATH, Xpath.subgame_firsttotenth))
                for subgame in subgames:
                    subgame.click()
                    num = 0
                    buttons = self.find_elements(*(By.XPATH, Xpath.betting_items))
                    for button in buttons:
                        button.click()
                        num += 1
                        if num % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()


if __name__ == '__main__':
    pass
