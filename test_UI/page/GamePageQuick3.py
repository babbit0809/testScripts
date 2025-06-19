import time
from config.SetUIConfig import Target
from test_UI.common import BasePage
from test_UI.page.GamePageQuick3_Locator import Xpath
from test_UI.common.GamePageCommon import GamePageCommon


class GamePageQuick3(BasePage.BasePage):
    # Actions
    def switch_pro_game(self, game_type, game_name, subGame_name=None):
        # 切換官方盤/雙面盤
        GamePageCommon(self.driver).switch_bet_category('pro')
        # 點擊官方盤玩法選單
        GamePageCommon(self.driver).click_pro_game_option()
        # 避免被盈虧視窗擋住的檢查機制
        GamePageCommon(self.driver).check_pro_game_option_showing()
        # 切換常規/趣味
        if Target in ['app', 'web']:
            if game_type == 'normal':
                game_type = self.find_element(*Xpath.pro_game_type_normal)
            elif game_type == 'fun':
                game_type = self.find_element(*Xpath.pro_game_type_fun)
            game_type.click()
        # 切換主玩法
        if Target in ['app', 'h5']:
            pro_game_name_All = self.find_elements(*Xpath.pro_game_name_All)
            if game_name == 'sum':
                game_name = pro_game_name_All[0]
            elif game_name == 'continuous3':
                game_name = pro_game_name_All[1]
            elif game_name == 'same3':
                game_name = pro_game_name_All[2]
            elif game_name == 'differ3':
                game_name = pro_game_name_All[3]
            elif game_name == 'same2':
                game_name = pro_game_name_All[4]
            elif game_name == 'differ2':
                game_name = pro_game_name_All[5]
            game_name.click()

        elif Target == 'web':
            if game_name == 'sum':
                game_name = self.find_element(*Xpath.normal_sum)
            elif game_name == 'continuous3':
                game_name = self.find_element(*Xpath.normal_continuous3)
            elif game_name == 'same3':
                game_name = self.find_element(*Xpath.normal_same3)
            elif game_name == 'differ3':
                game_name = self.find_element(*Xpath.normal_differ3)
            elif game_name == 'same2':
                game_name = self.find_element(*Xpath.normal_same2)
            elif game_name == 'differ2':
                game_name = self.find_element(*Xpath.normal_differ2)
            game_name.click()

        # 切換子玩法
        if Target in ['app', 'h5']:
            if subGame_name:
                pro_subGame_name_All = self.find_elements(*Xpath.pro_subGame_name_All)
                if subGame_name == 'singleChoice':
                    subGame_name = pro_subGame_name_All[0]
                elif subGame_name == 'multiChoices':
                    subGame_name = pro_subGame_name_All[1]
                subGame_name.click()

        elif Target == 'web':
            if subGame_name:
                if subGame_name == 'singleChoice':
                    subGame_name = self.find_element(*Xpath.normal_same2_singleChoice)
                elif subGame_name == 'multiChoices':
                    subGame_name = self.find_element(*Xpath.normal_same2_multiChoices)
                subGame_name.click()
        # H5需多點擊確認按鈕
        if Target == 'h5':
            confirm_button = self.find_element(*Xpath.button_pro_game_confirm)
            confirm_button.click()

    def switch_twoSide_game(self, game_name):
        # 切換官方盤/雙面盤
        GamePageCommon(self.driver).switch_bet_category('twoSide')
        # 切換主玩法
        if Target == 'app' or Target == 'h5':
            twoSide_game_name_All = self.find_elements(*Xpath.twoSide_game_name_All)
            if game_name == 'army3':
                game_name = twoSide_game_name_All[0]
            elif game_name == 'fast3Sum':
                game_name = twoSide_game_name_All[1]
            elif game_name == 'point':
                game_name = twoSide_game_name_All[2]
            elif game_name == 'triple':
                game_name = twoSide_game_name_All[3]
            elif game_name == 'long':
                game_name = twoSide_game_name_All[4]
            elif game_name == 'short':
                game_name = twoSide_game_name_All[5]
            elif game_name == 'fishShrimpCrab':
                game_name = twoSide_game_name_All[6]
            game_name.click()

        elif Target == 'web':
            if game_name == 'army3':
                game_name = self.find_element(*Xpath.two_side_army3)
            elif game_name == 'fast3Sum':
                game_name = self.find_element(*Xpath.two_side_fast3Sum)
            elif game_name == 'point':
                game_name = self.find_element(*Xpath.two_side_point)
            elif game_name == 'triple':
                game_name = self.find_element(*Xpath.two_side_triple)
            elif game_name == 'long':
                game_name = self.find_element(*Xpath.two_side_long)
            elif game_name == 'short':
                game_name = self.find_element(*Xpath.two_side_short)
            elif game_name == 'fishShrimpCrab':
                game_name = self.find_element(*Xpath.two_side_fishShrimpCrab)
            game_name.click()

    def bet_pro_all(self, type_name, subtype_name=None, bet_case=None):
        if type_name == 'sum':
            if Target == 'h5':
                GamePageCommon(self.driver).check_countdown_time()
                start_location = self.find_element(*Xpath.button_line4_sum).location
                end_location = self.find_element(*Xpath.history_button).location
                self.swipe(start_location, end_location, y2scale=1)

                GamePageCommon(self.driver).check_countdown_time()
                all_buttons = self.find_elements(*Xpath.betting_SumToDiffer2)
                count = 0
                for buttons in all_buttons:
                    if count % 5 == 0:
                        GamePageCommon(self.driver).check_countdown_time()
                    buttons.click()
                    count += 1

            else:
                GamePageCommon(self.driver).check_countdown_time()
                all_buttons = self.find_elements(*Xpath.betting_SumToDiffer2)
                count = 0
                for buttons in all_buttons:
                    if count % 5 == 0:
                        GamePageCommon(self.driver).check_countdown_time()
                    buttons.click()
                    count += 1

        elif type_name in ['continuous3', 'same3', 'differ3', 'differ2']:
            GamePageCommon(self.driver).check_countdown_time()
            all_buttons = self.find_elements(*Xpath.betting_SumToDiffer2)
            count = 0
            for buttons in all_buttons:
                if count % 5 == 0:
                    GamePageCommon(self.driver).check_countdown_time()
                buttons.click()
                count += 1

            if Target == 'web':
                if type_name in ['continuous3', 'same3', 'differ3']:
                    GamePageCommon(self.driver).check_countdown_time()
                    button_all = self.find_element(*Xpath.betting_SumToDifferAll)
                    button_all.click()

        elif type_name == 'same2':
            if subtype_name == 'singleChoice':
                if bet_case == 'same2case1':  # 同號: 1 + 二同號通選 + 不同號: 2-6
                    if Target == 'app':
                        GamePageCommon(self.driver).check_countdown_time()
                        same2single_all_buttons = self.find_elements(*Xpath.betting_SumToDiffer2)
                        betting_11 = same2single_all_buttons[0]
                        betting_all = same2single_all_buttons[6]
                        betting_2 = same2single_all_buttons[8]
                        betting_3 = same2single_all_buttons[9]
                        betting_4 = same2single_all_buttons[10]
                        betting_5 = same2single_all_buttons[11]
                        betting_6 = same2single_all_buttons[12]
                        for buttons in [betting_11, betting_all, betting_2, betting_3, betting_4, betting_5, betting_6]:
                            buttons.click()

                    elif Target == 'h5':
                        GamePageCommon(self.driver).check_countdown_time()
                        same2single_11toAll_buttons = self.find_elements(*Xpath.betting_same2single_11toAll)
                        betting_11 = same2single_11toAll_buttons[0]
                        betting_all = same2single_11toAll_buttons[6]
                        for buttons in [betting_11, betting_all]:
                            buttons.click()

                        GamePageCommon(self.driver).check_countdown_time()
                        start_location = self.find_element(*Xpath.title_differ).location
                        end_location = self.find_element(*Xpath.history_button).location
                        self.swipe(start_location, end_location, y2scale=1)

                        GamePageCommon(self.driver).check_countdown_time()
                        same2single_1to6_buttons = self.find_elements(*Xpath.betting_same2single_1to6)
                        betting_2 = same2single_1to6_buttons[1]
                        betting_3 = same2single_1to6_buttons[2]
                        betting_4 = same2single_1to6_buttons[3]
                        betting_5 = same2single_1to6_buttons[4]
                        betting_6 = same2single_1to6_buttons[5]
                        for buttons in [betting_2, betting_3, betting_4, betting_5, betting_6]:
                            buttons.click()

                    elif Target == 'web':
                        GamePageCommon(self.driver).check_countdown_time()
                        same2single_11toAll_buttons = self.find_elements(*Xpath.betting_same2single_11toAll)
                        betting_11 = same2single_11toAll_buttons[1]
                        betting_all = same2single_11toAll_buttons[0]
                        for buttons in [betting_11, betting_all]:
                            buttons.click()

                        GamePageCommon(self.driver).check_countdown_time()
                        betting_2 = same2single_11toAll_buttons[8]
                        betting_3 = same2single_11toAll_buttons[9]
                        betting_4 = same2single_11toAll_buttons[10]
                        betting_5 = same2single_11toAll_buttons[11]
                        betting_6 = same2single_11toAll_buttons[12]
                        for buttons in [betting_2, betting_3, betting_4, betting_5, betting_6]:
                            buttons.click()

                elif bet_case == 'same2case2':  # 同號: 2-6 + 二同號通選 + 不同號: 1'
                    if Target == 'app':
                        GamePageCommon(self.driver).check_countdown_time()
                        same2single_all_buttons = self.find_elements(*Xpath.betting_SumToDiffer2)
                        betting_22 = same2single_all_buttons[1]
                        betting_33 = same2single_all_buttons[2]
                        betting_44 = same2single_all_buttons[3]
                        betting_55 = same2single_all_buttons[4]
                        betting_66 = same2single_all_buttons[5]
                        betting_all = same2single_all_buttons[6]
                        betting_1 = same2single_all_buttons[7]
                        for buttons in [betting_22, betting_33, betting_44, betting_55, betting_66, betting_all,
                                        betting_1]:
                            buttons.click()

                    elif Target == 'h5':
                        GamePageCommon(self.driver).check_countdown_time()
                        same2single_11toAll_buttons = self.find_elements(*Xpath.betting_same2single_11toAll)
                        betting_22 = same2single_11toAll_buttons[1]
                        betting_33 = same2single_11toAll_buttons[2]
                        betting_44 = same2single_11toAll_buttons[3]
                        betting_55 = same2single_11toAll_buttons[4]
                        betting_66 = same2single_11toAll_buttons[5]
                        betting_all = same2single_11toAll_buttons[6]
                        for buttons in [betting_22, betting_33, betting_44, betting_55, betting_66, betting_all]:
                            buttons.click()

                        GamePageCommon(self.driver).check_countdown_time()
                        start_location = self.find_element(*Xpath.title_differ).location
                        end_location = self.find_element(*Xpath.history_button).location
                        self.swipe(start_location, end_location, y2scale=1)

                        GamePageCommon(self.driver).check_countdown_time()
                        same2single_1to6_buttons = self.find_elements(*Xpath.betting_same2single_1to6)
                        betting_1 = same2single_1to6_buttons[0]
                        betting_1.click()

                    elif Target == 'web':
                        GamePageCommon(self.driver).check_countdown_time()
                        same2single_11toAll_buttons = self.find_elements(*Xpath.betting_same2single_11toAll)
                        betting_22 = same2single_11toAll_buttons[2]
                        betting_33 = same2single_11toAll_buttons[3]
                        betting_44 = same2single_11toAll_buttons[4]
                        betting_55 = same2single_11toAll_buttons[5]
                        betting_66 = same2single_11toAll_buttons[6]
                        betting_all = same2single_11toAll_buttons[0]
                        for buttons in [betting_22, betting_33, betting_44, betting_55, betting_66, betting_all]:
                            buttons.click()

                        GamePageCommon(self.driver).check_countdown_time()
                        betting_1 = same2single_11toAll_buttons[7]
                        betting_1.click()

            elif subtype_name == 'multiChoices':
                GamePageCommon(self.driver).check_countdown_time()
                all_buttons = self.find_elements(*Xpath.betting_SumToDiffer2)
                for buttons in all_buttons:
                    buttons.click()

    def bet_twoSide_all(self, type_name):
        if type_name in ['army3', 'fast3Sum', 'point', 'triple', 'short', 'fishShrimpCrab']:
            GamePageCommon(self.driver).check_countdown_time()
            all_buttons = self.find_elements(*Xpath.betting_twoSide_all_buttons)
            count = 0
            for buttons in all_buttons:
                if count % 5 == 0:
                    GamePageCommon(self.driver).check_countdown_time()
                buttons.click()
                count += 1

        elif type_name == 'long':
            if Target == 'h5':
                GamePageCommon(self.driver).check_countdown_time()
                start_location = self.find_element(*Xpath.button_line1_long).location
                end_location = self.find_element(*Xpath.history_button).location
                self.swipe(start_location, end_location, y2scale=1)

                GamePageCommon(self.driver).check_countdown_time()
                all_buttons = self.find_elements(*Xpath.betting_twoSide_all_buttons)
                count = 0
                for buttons in all_buttons:
                    if count % 5 == 0:
                        GamePageCommon(self.driver).check_countdown_time()
                    buttons.click()
                    count += 1

            else:
                GamePageCommon(self.driver).check_countdown_time()
                all_buttons = self.find_elements(*Xpath.betting_twoSide_all_buttons)
                count = 0
                for buttons in all_buttons:
                    if count % 5 == 0:
                        GamePageCommon(self.driver).check_countdown_time()
                    buttons.click()
                    count += 1

    def click_random_button(self):
        GamePageCommon(self.driver).check_countdown_time()
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
        del_bet_buttons = self.find_element(*Xpath.del_bet_buttons)
        del_bet_buttons.click()
        random_button = self.find_element(*Xpath.random_bet_buttons)
        random_button.click()


if __name__ == '__main__':
    pass
