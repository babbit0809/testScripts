import time
from config.SetUIConfig import Platform, Target
from test_UI.common import BasePage
from test_UI.page.GamePage11x5_Locator import Xpath
from test_UI.common.GamePageCommon import GamePageCommon


class GamePage11x5(BasePage.BasePage):
    # Actions
    def switch_pro_game(self, game_type, game_name, subGame_name=None):
        # 切換官方盤/雙面盤
        GamePageCommon(self.driver).switch_bet_category('pro')
        # 點擊官方盤玩法選單
        GamePageCommon(self.driver).click_pro_game_option()
        # 避免被盈虧視窗擋住的檢查機制
        GamePageCommon(self.driver).check_pro_game_option_showing()
        # 切換常規/趣味
        if Target in ['app', 'h5', 'web']:
            option = None
            if game_type == 'normal':
                option = self.find_element(*Xpath.pro_game_type_normal)
            elif game_type == 'fun':
                option = self.find_element(*Xpath.pro_game_type_fun)
            option.click()
        # 切換主玩法
        if Target in ['app', 'h5']:
            pro_game_name_All = self.find_elements(*Xpath.pro_game_name_All)
            if game_name in ['r2', 'sum']:
                game_name = pro_game_name_All[0]
            elif game_name in ['r3', 'crossDegree']:
                game_name = pro_game_name_All[1]
            elif game_name in ['r4', 'cowcow']:
                game_name = pro_game_name_All[2]
            elif game_name in ['r5', 'cardPoint']:
                game_name = pro_game_name_All[3]
            elif game_name in ['r6', 'dragonTiger']:
                game_name = pro_game_name_All[4]
            elif game_name in ['r7', 'alwaysGuess']:
                game_name = pro_game_name_All[5]
            elif game_name == 'r8':
                game_name = pro_game_name_All[6]
            elif game_name == 'front1':
                game_name = pro_game_name_All[7]
            elif game_name == 'front2':
                game_name = pro_game_name_All[8]
            elif game_name == 'front3':
                game_name = pro_game_name_All[9]
            game_name.click()

        elif Target == 'web':
            time.sleep(2)
            if game_name in 'r2':
                game_name = self.find_element(*Xpath.normal_r2)
            elif game_name in 'r3':
                game_name = self.find_element(*Xpath.normal_r3)
            elif game_name in 'r4':
                game_name = self.find_element(*Xpath.normal_r4)
            elif game_name in 'r5':
                game_name = self.find_element(*Xpath.normal_r5)
            elif game_name in 'r6':
                game_name = self.find_element(*Xpath.normal_r6)
            elif game_name in 'r7':
                game_name = self.find_element(*Xpath.normal_r7)
            elif game_name == 'r8':
                game_name = self.find_element(*Xpath.normal_r8)
            elif game_name == 'front1':
                game_name = self.find_element(*Xpath.normal_front1)
            elif game_name == 'front2':
                game_name = self.find_element(*Xpath.normal_front2)
            elif game_name == 'front3':
                game_name = self.find_element(*Xpath.normal_front3)
            elif game_name == 'sum':
                game_name = self.find_element(*Xpath.fun_sum)
            elif game_name == 'crossDegree':
                game_name = self.find_element(*Xpath.fun_crossDegree)
            elif game_name == 'cowcow':
                game_name = self.find_element(*Xpath.fun_cowcow)
            elif game_name == 'cardPoint':
                game_name = self.find_element(*Xpath.fun_cardPoint)
            elif game_name == 'dragonTiger':
                game_name = self.find_element(*Xpath.fun_dragontiger)
            elif game_name == 'alwaysGuess':
                game_name = self.find_element(*Xpath.fun_alwaysGuess)
            game_name.click()
        # 切換子玩法(常規-前二/前三的單式以及趣味-跨度的前中後三和趣味-龍虎的前中後三前後二要另外判斷)
        if Target in ['app', 'h5']:
            if subGame_name:
                pro_subGame_name_All = self.find_elements(*Xpath.pro_subGame_name_All)
                if subGame_name in ['standard', 'directStandard', 'front3', 'all5']:
                    subGame_name = pro_subGame_name_All[0]
                elif subGame_name in ['order', 'directOrder', 'groupSelect', 'middle3', 'crossDegree_front3',
                                      'dragonTiger_front3']:
                    subGame_name = pro_subGame_name_All[1]
                elif subGame_name in ['front2_directOrder', 'front3_directOrder', 'back3', 'crossDegree_middle3',
                                      'dragonTiger_middle3']:
                    subGame_name = pro_subGame_name_All[2]
                elif subGame_name in ['front2', 'crossDegree_back3', 'dragonTiger_back3']:
                    subGame_name = pro_subGame_name_All[3]
                elif subGame_name in ['back2', 'dragonTiger_front2']:
                    subGame_name = pro_subGame_name_All[4]
                elif subGame_name in ['dragonTiger_back2']:
                    subGame_name = pro_subGame_name_All[5]
                subGame_name.click()

        # H5需多點擊確認按鈕
        if Target == 'h5':
            confirm_button = self.find_element(*Xpath.button_pro_game_confirm)
            confirm_button.click()

        elif Target == 'web':
            if subGame_name:
                if subGame_name in ['standard', 'directStandard', 'front3', 'crossDegree_front3', 'dragonTiger_front3']:
                    if game_type == 'fun':
                        subGame_name = self.find_element(*Xpath.fun_sum_front3)
                    else:
                        subGame_name = self.find_element(*Xpath.pro_game_sandard)
                elif subGame_name in ['order', 'directOrder', 'front2_directOrder', 'front3_directOrder']:
                    subGame_name = self.find_element(*Xpath.pro_game_order)
                elif subGame_name in ['groupSelect']:
                    subGame_name = self.find_element(*Xpath.pro_game_group)
                elif subGame_name in ['front2', "dragonTiger_front2"]:
                    subGame_name = self.find_element(*Xpath.fun_sum_front2)
                elif subGame_name in ['back2', "dragonTiger_back2"]:
                    subGame_name = self.find_element(*Xpath.fun_sum_back2)
                elif subGame_name in ['middle3', 'crossDegree_middle3', 'dragonTiger_middle3']:
                    subGame_name = self.find_element(*Xpath.fun_sum_middle3)
                elif subGame_name in ['back3', 'crossDegree_back3', "dragonTiger_back3"]:
                    subGame_name = self.find_element(*Xpath.fun_sum_back3)
                elif subGame_name in ['all5']:
                    subGame_name = self.find_element(*Xpath.fun_crossDegree_all5)
                subGame_name.click()

    def switch_twoSide_game(self, game_name):
        # 切換官方盤/雙面盤
        GamePageCommon(self.driver).switch_bet_category('twoSide')
        # 切換主玩法
        if Target in ['app', 'h5']:
            twoSide_game_name_All = self.find_elements(*Xpath.twoSide_game_name_All)
            if game_name == 'firstBall':
                game_name = twoSide_game_name_All[0]
            elif game_name == 'secondBall':
                game_name = twoSide_game_name_All[1]
            elif game_name == 'thirdBall':
                game_name = twoSide_game_name_All[2]
            elif game_name == 'fourthBall':
                game_name = twoSide_game_name_All[3]
            elif game_name == 'fifthBall':
                game_name = twoSide_game_name_All[4]
            elif game_name == 'total':
                game_name = twoSide_game_name_All[5]
            elif game_name == 'dragon':
                game_name = twoSide_game_name_All[6]
            elif game_name == 'tiger':
                game_name = twoSide_game_name_All[7]
            game_name.click()

        elif Target == 'web':
            if game_name == 'firstBall':
                game_name = self.find_element(*Xpath.two_side_firstBall)
            elif game_name == 'secondBall':
                game_name = self.find_element(*Xpath.two_side_secondBall)
            elif game_name == 'thirdBall':
                game_name = self.find_element(*Xpath.two_side_thirdBall)
            elif game_name == 'fourthBall':
                game_name = self.find_element(*Xpath.two_side_fourthBall)
            elif game_name == 'fifthBall':
                game_name = self.find_element(*Xpath.two_side_fifthBall)
            elif game_name == 'total':
                game_name = self.find_element(*Xpath.two_side_total)
            elif game_name == 'dragon':
                dragontiger_icon = self.find_element(*Xpath.two_side_dragontiger)
                dragontiger_icon.click()
                game_name = self.find_element(*Xpath.two_side_dragon)
            elif game_name == 'tiger':
                dragontiger_icon = self.find_element(*Xpath.two_side_dragontiger)
                dragontiger_icon.click()
                game_name = self.find_element(*Xpath.two_side_tiger)
            game_name.click()

    def bet_pro_all(self, type_name, subtype_name=None, bet_number=None):
        if type_name in ['r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'front1', 'front2', 'front3', 'alwaysGuess']:
            if subtype_name in ['order', 'directOrder']:  # 單式系列
                if Platform == 'Android' and Target == 'app':
                    GamePageCommon(self.driver).check_countdown_time()
                    self.input(*Xpath.betting_input_field, contents=bet_number)
                    tap_location = self.find_element(*Xpath.betting_info)
                    self.tap(tap_location, offset_x=-100, offset_y=30)

                elif Platform == 'iOS' and Target == 'app':
                    GamePageCommon(self.driver).check_countdown_time()
                    self.input(*Xpath.betting_input_field, contents=bet_number)
                    tap_location = self.find_element(*Xpath.betting_info)
                    tap_location.click()
                    order_format_confirm = self.find_element(*Xpath.order_format_verified)
                    order_format_confirm.click()

                else:
                    GamePageCommon(self.driver).check_countdown_time()
                    self.input(*Xpath.betting_input_field, contents=bet_number)

            else:
                GamePageCommon(self.driver).check_countdown_time()
                all_buttons = self.find_elements(*Xpath.betting_all_button)
                for buttons in all_buttons:
                    buttons.click()

        elif type_name in ['sum']:
            if Platform == 'Android' and Target == 'app':  # 因UI關係需另外判斷
                if subtype_name in ['front3', 'middle3', 'back3']:
                    GamePageCommon(self.driver).check_countdown_time()
                    button_big_to_25 = self.find_elements(*Xpath.betting_sumtodragonTiger)
                    count = 0
                    for buttons in button_big_to_25[:24]:
                        if count < 24:
                            if count % 5 == 0:
                                GamePageCommon(self.driver).check_countdown_time()
                            buttons.click()
                        count += 1

                    GamePageCommon(self.driver).check_countdown_time()
                    start_location = self.find_element(*Xpath.betting_button_22).location
                    end_location = self.find_element(*Xpath.history_button).location
                    self.swipe(start_location, end_location, y2scale=1)

                    GamePageCommon(self.driver).check_countdown_time()
                    button_26_to_29 = self.find_elements(*Xpath.betting_sumtodragonTiger)
                    count = 0
                    for buttons in button_26_to_29[-5:]:
                        if count % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                        buttons.click()
                        count += 1

                else:
                    GamePageCommon(self.driver).check_countdown_time()
                    all_buttons = self.find_elements(*Xpath.betting_sumtodragonTiger)
                    count = 0
                    for buttons in all_buttons:
                        if count % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                        buttons.click()
                        count += 1

            elif Platform == 'Android' and Target == 'h5':
                if subtype_name in ['front3', 'middle3', 'back3']:
                    GamePageCommon(self.driver).check_countdown_time()
                    button_before_numbers = self.find_elements(*Xpath.betting_before_numbers)
                    button_numbers1x = self.find_elements(*Xpath.betting_numbers1x)
                    button_beforeTo1x = [button_before_numbers, button_numbers1x]
                    count = 0
                    while count < 2:
                        num = 0
                        GamePageCommon(self.driver).check_countdown_time()
                        for buttons in button_beforeTo1x[count]:
                            buttons.click()
                            num += 1
                            if num % 5 == 0:
                                GamePageCommon(self.driver).check_countdown_time()
                        count += 1

                    GamePageCommon(self.driver).check_countdown_time()
                    start_location = self.find_element(*Xpath.button_18).location
                    end_location = self.find_element(*Xpath.history_button).location
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

                else:
                    GamePageCommon(self.driver).check_countdown_time()
                    all_buttons = self.find_elements(*Xpath.betting_sumtodragonTiger)
                    self.execute_script("return arguments[0].scrollIntoView(true);", all_buttons[0])
                    count = 0
                    for buttons in all_buttons:
                        if count % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                        if count == 20:
                            GamePageCommon(self.driver).check_countdown_time()
                            start_location = buttons.location
                            end_location = self.find_element(*Xpath.history_button).location
                            self.swipe(start_location, end_location, y2scale=1.1)
                        buttons.click()
                        count += 1

            elif Platform == 'iOS' and Target == 'app':
                if subtype_name in ['front3', 'middle3', 'back3']:
                    GamePageCommon(self.driver).check_countdown_time()
                    button_big_to_25 = self.find_elements(*Xpath.betting_sumtodragonTiger)
                    count = 0
                    for buttons in button_big_to_25[:24]:
                        if count < 24:
                            if count % 5 == 0:
                                GamePageCommon(self.driver).check_countdown_time()
                            buttons.click()
                        count += 1

                    GamePageCommon(self.driver).check_countdown_time()
                    start_location = self.find_element(*Xpath.betting_button_22).location
                    end_location = self.find_element(*Xpath.history_button).location
                    self.swipe(start_location, end_location, y2scale=1)

                    GamePageCommon(self.driver).check_countdown_time()
                    button_26_to_29 = self.find_elements(*Xpath.betting_sumtodragonTiger)
                    count = 0
                    for buttons in button_26_to_29[-5:]:
                        if count % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                        buttons.click()
                        count += 1

                else:
                    GamePageCommon(self.driver).check_countdown_time()
                    all_buttons = self.find_elements(*Xpath.betting_sumtodragonTiger)
                    count = 0
                    for buttons in all_buttons:
                        if count % 5 == 0:
                            GamePageCommon(self.driver).check_countdown_time()
                        buttons.click()
                        count += 1

            elif Target == 'web':
                # if subtype_name in ['front3', 'middle3', 'back3']:
                GamePageCommon(self.driver).check_countdown_time()
                all_buttons = self.find_elements(*Xpath.betting_sumtodragonTiger)
                count = 0
                for buttons in all_buttons:
                    if count % 10 == 0:
                        GamePageCommon(self.driver).check_countdown_time()
                    buttons.click()
                    count += 1

        elif type_name in ['crossDegree', 'cowcow', 'cardPoint', 'dragonTiger']:
            GamePageCommon(self.driver).check_countdown_time()
            all_buttons = self.find_elements(*Xpath.betting_sumtodragonTiger)
            count = 0
            for buttons in all_buttons:
                if count % 5 == 0:
                    GamePageCommon(self.driver).check_countdown_time()
                buttons.click()
                count += 1

    def bet_twoSide_all(self, type_name):
        if type_name in ['firstBall', 'secondBall', 'thirdBall', 'fourthBall', 'fifthBall', 'total', 'dragon', 'tiger']:
            GamePageCommon(self.driver).check_countdown_time()
            all_buttons = self.find_elements(*Xpath.betting_twoSide_all_buttons)
            # H5的第一球~第五球需先滑動避免元件被遮蔽
            if Target == 'h5' and type_name in ['firstBall', 'secondBall', 'thirdBall', 'fourthBall', 'fifthBall']:
                GamePageCommon(self.driver).check_countdown_time()
                start_location = all_buttons[1].location
                end_location = self.find_element(*Xpath.history_button).location
                self.swipe(start_location, end_location, y2scale=1)

            count = 0
            for buttons in all_buttons:
                buttons.click()
                count += 1
                if count % 5 == 0:
                    GamePageCommon(self.driver).check_countdown_time()

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
