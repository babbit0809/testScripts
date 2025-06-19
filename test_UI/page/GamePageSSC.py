import time
from config.SetUIConfig import Platform, Target
from test_UI.common import BasePage
from test_UI.page.GamePageSSC_Locator import Xpath
from test_UI.common.GamePageCommon import GamePageCommon


class GamePageSSC(BasePage.BasePage):
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
            if game_name == 'fiveStar':
                game_name = pro_game_name_All[0]
            elif game_name == 'threeStar':
                game_name = pro_game_name_All[1]
            elif game_name == 'threeStarGroup3':
                game_name = pro_game_name_All[2]
            elif game_name == 'threeStarGroup6':
                game_name = pro_game_name_All[3]
            elif game_name == 'twoStar':
                game_name = pro_game_name_All[4]
            elif game_name == 'dingweidan':
                game_name = pro_game_name_All[5]
            elif game_name == 'budingweidan':
                game_name = pro_game_name_All[6]
            elif game_name == 'bigSmallOddEven':
                game_name = pro_game_name_All[7]
            elif game_name == 'freeSelection':
                game_name = pro_game_name_All[8]
            game_name.click()

        elif Target == 'web':
            if game_name == 'fiveStar':
                game_name = self.find_element(*Xpath.normal_fiveStar)
            elif game_name in 'threeStar':
                game_name = self.find_element(*Xpath.normal_threeStar)
            elif game_name in 'threeStarGroup3':
                game_name = self.find_element(*Xpath.normal_threeStarGroup3)
            elif game_name in 'threeStarGroup6':
                game_name = self.find_element(*Xpath.normal_threeStarGroup6)
            elif game_name in 'twoStar':
                game_name = self.find_element(*Xpath.normal_twoStar)
            elif game_name in 'dingweidan':
                game_name = self.find_element(*Xpath.normal_dingweidan)
            elif game_name in 'budingweidan':
                game_name = self.find_element(*Xpath.normal_budingweidan)
            elif game_name in 'bigSmallOddEven':
                game_name = self.find_element(*Xpath.normal_bigSmallOddEven)
            elif game_name in 'freeSelection':
                game_name = self.find_element(*Xpath.normal_freeSelection)
            game_name.click()
        # 切換子玩法
        if Target in ['app', 'h5']:
            if subGame_name:
                pro_subGame_name_All = self.find_elements(*Xpath.pro_subGame_name_All)
                if subGame_name in ['fiveStarDirectSelection', 'front3Choice', 'front3Group3', 'front3Group6',
                                    'frontDirect',
                                    'front3', 'twoDirect']:
                    subGame_name = pro_subGame_name_All[0]
                elif subGame_name in ['fiveStarOrder', 'front3Order', 'middle3Group3', 'middle3Group6', 'frontGroup',
                                      'middle3', 'twoGroup']:
                    subGame_name = pro_subGame_name_All[1]
                elif subGame_name in ['selection120', 'middle3Choice', 'back3Group3', 'back3Group6', 'frontOrder',
                                      'back3', 'twoOrder']:
                    subGame_name = pro_subGame_name_All[2]
                elif subGame_name in ['selection60', 'middle3Order', 'backDirect', 'threeDirect']:
                    subGame_name = pro_subGame_name_All[3]
                elif subGame_name in ['selection30', 'back3Choice', 'backGroup', 'threeGroup3']:
                    subGame_name = pro_subGame_name_All[4]
                elif subGame_name in ['selection20', 'back3Order', 'backOrder', 'threeGroup6']:
                    subGame_name = pro_subGame_name_All[5]
                elif subGame_name in ['selection10', 'front3Mix', 'threeOrder']:
                    subGame_name = pro_subGame_name_All[6]
                elif subGame_name in ['selection5', 'middle3Mix', 'fourDirect']:
                    subGame_name = pro_subGame_name_All[7]
                elif subGame_name in ['back3Mix', 'fourOrder']:
                    subGame_name = pro_subGame_name_All[8]
                subGame_name.click()
        # H5需多點擊確認按鈕
        if Target == 'h5':
            confirm_button = self.find_element(*Xpath.button_pro_game_confirm)
            confirm_button.click()

        elif Target == 'web':
            if subGame_name:
                if subGame_name in ['fiveStarOrder', 'front3Order', 'frontOrder']:
                    pro_subGame_name_All = self.find_elements(*Xpath.pro_game_order)
                    subGame_name = pro_subGame_name_All[0]
                elif subGame_name in ['middle3Order', 'backOrder']:
                    pro_subGame_name_All = self.find_elements(*Xpath.pro_game_order)
                    subGame_name = pro_subGame_name_All[1]
                elif subGame_name in ['back3Order']:
                    pro_subGame_name_All = self.find_elements(*Xpath.pro_game_order)
                    subGame_name = pro_subGame_name_All[2]
                elif subGame_name in ['front3Choice', 'front3Group3', 'front3Group6', 'frontDirect', 'front3']:
                    pro_subGame_name_All = self.find_elements(*Xpath.normal_game_front)
                    subGame_name = pro_subGame_name_All[0]
                elif subGame_name in ['frontGroup']:
                    pro_subGame_name_All = self.find_elements(*Xpath.normal_game_front)
                    subGame_name = pro_subGame_name_All[1]
                elif subGame_name in ['middle3Choice', 'middle3Group3', 'middle3Group6', 'middle3']:
                    pro_subGame_name_All = self.find_elements(*Xpath.normal_game_middle)
                    subGame_name = pro_subGame_name_All[0]
                elif subGame_name in ['back3Choice', 'back3Group3', 'back3Group6', 'backDirect', 'back3']:
                    pro_subGame_name_All = self.find_elements(*Xpath.normal_game_back)
                    subGame_name = pro_subGame_name_All[0]
                elif subGame_name in ['backGroup']:
                    pro_subGame_name_All = self.find_elements(*Xpath.normal_game_back)
                    subGame_name = pro_subGame_name_All[1]
                elif subGame_name in 'front3Mix':
                    pro_subGame_name_All = self.find_elements(*Xpath.normal_game_mix)
                    subGame_name = pro_subGame_name_All[0]
                elif subGame_name in 'middle3Mix':
                    pro_subGame_name_All = self.find_elements(*Xpath.normal_game_mix)
                    subGame_name = pro_subGame_name_All[1]
                elif subGame_name in 'back3Mix':
                    pro_subGame_name_All = self.find_elements(*Xpath.normal_game_mix)
                    subGame_name = pro_subGame_name_All[2]
                elif subGame_name in ['fiveStarDirectSelection']:
                    subGame_name = self.find_element(*Xpath.normal_fiveStar_fiveStarDirectSelection)
                elif subGame_name in 'selection120':
                    subGame_name = self.find_element(*Xpath.normal_fiveStar_selection120)
                elif subGame_name in 'selection60':
                    subGame_name = self.find_element(*Xpath.normal_fiveStar_selection60)
                elif subGame_name in 'selection30':
                    subGame_name = self.find_element(*Xpath.normal_fiveStar_selection30)
                elif subGame_name in 'selection20':
                    subGame_name = self.find_element(*Xpath.normal_fiveStar_selection20)
                elif subGame_name in 'selection10':
                    subGame_name = self.find_element(*Xpath.normal_fiveStar_selection10)
                elif subGame_name in 'selection5':
                    subGame_name = self.find_element(*Xpath.normal_fiveStar_selection5)
                elif subGame_name in 'twoDirect':
                    subGame_name = self.find_element(*Xpath.normal_freeSelection_twoDirect)
                elif subGame_name in 'twoGroup':
                    subGame_name = self.find_element(*Xpath.normal_freeSelection_twoGroup)
                elif subGame_name in 'twoOrder':
                    subGame_name = self.find_element(*Xpath.normal_freeSelection_twoOrder)
                elif subGame_name in 'threeDirect':
                    subGame_name = self.find_element(*Xpath.normal_freeSelection_threeDirect)
                elif subGame_name in 'threeGroup3':
                    subGame_name = self.find_element(*Xpath.normal_freeSelection_threeGroup3)
                elif subGame_name in 'threeGroup6':
                    subGame_name = self.find_element(*Xpath.normal_freeSelection_threeGroup6)
                elif subGame_name in 'threeOrder':
                    subGame_name = self.find_element(*Xpath.normal_freeSelection_threeOrder)
                elif subGame_name in 'fourDirect':
                    subGame_name = self.find_element(*Xpath.normal_freeSelection_fourDirect)
                elif subGame_name in 'fourOrder':
                    subGame_name = self.find_element(*Xpath.normal_freeSelection_fourOrder)

                subGame_name.click()

    def switch_twoSide_game(self, game_name):
        # 切換官方盤/雙面盤
        GamePageCommon(self.driver).switch_bet_category('twoSide')
        # 切換主玩法
        if Target in ['app', 'h5']:
            time.sleep(3)
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
            elif game_name == 'front3':
                game_name = twoSide_game_name_All[6]
            elif game_name == 'middle3':
                game_name = twoSide_game_name_All[7]
            elif game_name == 'back3':
                game_name = twoSide_game_name_All[8]
            elif game_name == 'dragon':
                game_name = twoSide_game_name_All[9]
            elif game_name == 'tiger':
                game_name = twoSide_game_name_All[10]
            elif game_name == 'equal':
                game_name = twoSide_game_name_All[11]
            game_name.click()

        elif Target == 'web':
            main_type = None
            if game_name in ['firstBall', 'secondBall', 'thirdBall', 'fourthBall', 'fifthBall']:
                main_type = self.find_element(*Xpath.two_side_firstToFifth)
            elif game_name in ['front3', 'middle3', 'back3']:
                main_type = self.find_element(*Xpath.two_side_frontMiddleBack3)
            elif game_name in ['dragon', 'tiger', 'equal']:
                main_type = self.find_element(*Xpath.two_side_dragonTigerEqual)
            elif game_name in ['total']:
                main_type = self.find_element(*Xpath.two_side_total)
            main_type.click()
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
            elif game_name == 'front3':
                game_name = self.find_element(*Xpath.two_side_front3)
            elif game_name == 'middle3':
                game_name = self.find_element(*Xpath.two_side_middle3)
            elif game_name == 'back3':
                game_name = self.find_element(*Xpath.two_side_back3)
            elif game_name == 'dragon':
                game_name = self.find_element(*Xpath.two_side_dragon)
            elif game_name == 'tiger':
                game_name = self.find_element(*Xpath.two_side_tiger)
            elif game_name == 'equal':
                game_name = self.find_element(*Xpath.two_side_equal)
            game_name.click()

    def bet_pro_all(self, type_name, subtype_name=None, betting_number=None):
        if type_name in ['fiveStar', 'threeStar', 'threeStarGroup3', 'threeStarGroup6', 'twoStar', 'budingweidan']:
            if subtype_name in ['fiveStarOrder', 'front3Order', 'middle3Order', 'back3Order', 'front3Mix', 'middle3Mix',
                                'back3Mix', 'frontOrder', 'backOrder']:  # 單式系列(任選不在此列)
                if Platform == 'Android' and Target == 'app':
                    GamePageCommon(self.driver).check_countdown_time()
                    self.input(*Xpath.betting_input_field, contents=betting_number)
                    tap_location = self.find_element(*Xpath.betting_info)
                    self.tap(tap_location, offset_x=-100, offset_y=30)

                elif Platform == 'Android' and Target == 'h5':
                    GamePageCommon(self.driver).check_countdown_time()
                    self.input(*Xpath.betting_input_field, contents=betting_number)

                elif Platform == 'iOS' and Target == 'app':
                    GamePageCommon(self.driver).check_countdown_time(check_time=20)
                    self.input(*Xpath.betting_input_field, contents=betting_number)
                    tap_location = self.find_element(*Xpath.betting_info)
                    tap_location.click()
                    order_format_confirm = self.find_element(*Xpath.order_format_verified)
                    order_format_confirm.click()

                elif Target == 'web':
                    GamePageCommon(self.driver).check_countdown_time()
                    input_field = self.find_element(*Xpath.betting_input_field)
                    input_field.click()
                    input_field.send_keys(betting_number)

            elif subtype_name == 'fiveStarDirectSelection':
                if Platform == 'Android' and Target == 'app':
                    GamePageCommon(self.driver).check_countdown_time()
                    all_buttons = self.find_elements(*Xpath.betting_all_button)
                    for buttons in all_buttons:
                        buttons.click()

                    GamePageCommon(self.driver).check_countdown_time()
                    start_location = self.find_element(*Xpath.title_hundred).location
                    end_location = self.find_element(*Xpath.history_button).location
                    self.swipe(start_location, end_location, y2scale=1.1)

                    GamePageCommon(self.driver).check_countdown_time()
                    all_buttons = self.find_elements(*Xpath.betting_all_button)
                    for buttons in all_buttons:
                        buttons.click()

                elif Platform == 'Android' and Target == 'h5':  # 此處微調swipe()座標避免觸發網頁搜尋機制及crash
                    GamePageCommon(self.driver).check_countdown_time()
                    million_all_button = self.find_element(*Xpath.betting_million_all_button)
                    thousand_all_button = self.find_element(*Xpath.betting_thousand_all_button)
                    hundred_all_button = self.find_element(*Xpath.betting_hundred_all_button)
                    for buttons in [million_all_button, thousand_all_button, hundred_all_button]:
                        buttons.click()

                    GamePageCommon(self.driver).check_countdown_time()
                    start_location = self.find_element(*Xpath.title_hundred).location
                    end_location = self.find_element(*Xpath.history_button).location
                    self.swipe(start_location, end_location, y1scale=0.8, y2scale=0.6)

                    GamePageCommon(self.driver).check_countdown_time()
                    ten_all_button = self.find_element(*Xpath.betting_ten_all_button)
                    digit_all_button = self.find_element(*Xpath.betting_digit_all_button)
                    for buttons in [ten_all_button, digit_all_button]:
                        buttons.click()

                elif Platform == 'iOS' and Target == 'app':
                    GamePageCommon(self.driver).check_countdown_time()
                    count = 0
                    all_buttons = self.find_elements(*Xpath.betting_all_button)
                    for buttons in all_buttons:
                        if count == 3:
                            GamePageCommon(self.driver).check_countdown_time()
                            start_location = self.find_element(*Xpath.title_hundred).location
                            end_location = self.find_element(*Xpath.history_button).location
                            self.swipe(start_location, end_location, y2scale=1.1)
                        buttons.click()
                        count += 1

                elif Target == 'web':
                    GamePageCommon(self.driver).check_countdown_time()
                    self.find_elements(*Xpath.betting_all_button)
                    all_buttons = self.find_elements(*Xpath.betting_all_button)
                    for buttons in all_buttons:
                        buttons.click()

            else:
                GamePageCommon(self.driver).check_countdown_time()
                all_buttons = self.find_elements(*Xpath.betting_all_button)
                for buttons in all_buttons:
                    buttons.click()

        elif type_name == 'dingweidan':  # 玩法與五星直選"fiveStarDirectSelection"相同
            if Platform == 'Android' and Target == 'app':
                GamePageCommon(self.driver).check_countdown_time()
                all_buttons = self.find_elements(*Xpath.betting_all_button)
                for buttons in all_buttons:
                    buttons.click()

                GamePageCommon(self.driver).check_countdown_time()
                start_location = self.find_element(*Xpath.title_hundred).location
                end_location = self.find_element(*Xpath.history_button).location
                self.swipe(start_location, end_location, y2scale=1.1)

                GamePageCommon(self.driver).check_countdown_time()
                all_buttons = self.find_elements(*Xpath.betting_all_button)
                for buttons in all_buttons:
                    buttons.click()

            elif Platform == 'Android' and Target == 'h5':
                GamePageCommon(self.driver).check_countdown_time()
                million_all_button = self.find_element(*Xpath.betting_million_all_button)
                thousand_all_button = self.find_element(*Xpath.betting_thousand_all_button)
                hundred_all_button = self.find_element(*Xpath.betting_hundred_all_button)
                for buttons in [million_all_button, thousand_all_button, hundred_all_button]:
                    buttons.click()

                GamePageCommon(self.driver).check_countdown_time()
                start_location = self.find_element(*Xpath.title_hundred).location
                end_location = self.find_element(*Xpath.history_button).location
                self.swipe(start_location, end_location, y2scale=1)

                GamePageCommon(self.driver).check_countdown_time()
                ten_all_button = self.find_element(*Xpath.betting_ten_all_button)
                digit_all_button = self.find_element(*Xpath.betting_digit_all_button)
                for buttons in [ten_all_button, digit_all_button]:
                    buttons.click()

            elif Platform == 'iOS' and Target == 'app':
                GamePageCommon(self.driver).check_countdown_time()
                all_buttons = self.find_elements(*Xpath.betting_all_button)
                count = 0
                for buttons in all_buttons:
                    if count == 3:
                        GamePageCommon(self.driver).check_countdown_time()
                        start_location = self.find_element(*Xpath.title_hundred).location
                        end_location = self.find_element(*Xpath.history_button).location
                        self.swipe(start_location, end_location, y2scale=1.1)
                    buttons.click()
                    count += 1

            elif Target == 'web':
                GamePageCommon(self.driver).check_countdown_time()
                all_buttons = self.find_elements(*Xpath.betting_all_button)
                count = 0
                for buttons in all_buttons:
                    buttons.click()
                    count += 1

        elif type_name == 'bigSmallOddEven':
            GamePageCommon(self.driver).check_countdown_time()
            all_buttons = self.find_elements(*Xpath.betting_bigSmallOddEven)
            count = 0
            for buttons in all_buttons:
                if count % 5 == 0:
                    GamePageCommon(self.driver).check_countdown_time()
                buttons.click()
                count += 1

        elif type_name == 'freeSelection':
            if subtype_name in ['twoDirect', 'twoGroup', 'threeGroup3', 'threeGroup6']:
                GamePageCommon(self.driver).check_countdown_time()
                all_buttons = self.find_elements(*Xpath.betting_freeSelection)
                for buttons in all_buttons:
                    buttons.click()

                GamePageCommon(self.driver).check_countdown_time()
                all_buttons = self.find_elements(*Xpath.betting_all_button)
                for buttons in all_buttons:
                    buttons.click()

            elif subtype_name in ['twoOrder', 'threeOrder', 'fourOrder']:
                if Platform == 'Android':
                    GamePageCommon(self.driver).check_countdown_time()
                    all_buttons = self.find_elements(*Xpath.betting_freeSelection_order)
                    for buttons in all_buttons:
                        buttons.click()
                    self.input(*Xpath.betting_input_field, contents=betting_number)
                    if Target == 'app':
                        GamePageCommon(self.driver).check_countdown_time()
                        tap_location = self.find_element(*Xpath.betting_info)
                        self.tap(tap_location, offset_x=-100, offset_y=30)

                elif Platform == 'iOS' and Target == 'app':
                    GamePageCommon(self.driver).check_countdown_time(check_time=20)
                    all_buttons = self.find_elements(*Xpath.betting_freeSelection_order)
                    for buttons in all_buttons:
                        buttons.click()

                    GamePageCommon(self.driver).check_countdown_time(check_time=20)
                    self.input(*Xpath.betting_input_field, contents=betting_number)
                    tap_location = self.find_element(*Xpath.betting_info)
                    tap_location.click()
                    order_format_confirm = self.find_element(*Xpath.order_format_verified)
                    order_format_confirm.click()

                elif Target == 'web':
                    GamePageCommon(self.driver).check_countdown_time()
                    all_buttons = self.find_elements(*Xpath.betting_freeSelection)
                    for buttons in all_buttons:
                        buttons.click()

                    GamePageCommon(self.driver).check_countdown_time()
                    input_field = self.find_element(*Xpath.betting_input_field)
                    input_field.click()
                    input_field.send_keys(betting_number)

            elif subtype_name == 'threeDirect':
                if Target == 'h5':
                    GamePageCommon(self.driver).check_countdown_time()
                    all_buttons = self.find_elements(*Xpath.betting_freeSelection)
                    for buttons in all_buttons:
                        buttons.click()

                    GamePageCommon(self.driver).check_countdown_time()
                    first_all_button = self.find_element(*Xpath.betting_first_all_button)
                    second_all_button = self.find_element(*Xpath.betting_second_all_button)
                    for buttons in [first_all_button, second_all_button, ]:
                        buttons.click()

                    GamePageCommon(self.driver).check_countdown_time()
                    start_location = self.find_element(*Xpath.title_second).location
                    end_location = self.find_element(*Xpath.history_button).location
                    self.swipe(start_location, end_location, y2scale=1.2)

                    GamePageCommon(self.driver).check_countdown_time()
                    third_all_button = self.find_element(*Xpath.betting_third_all_button)
                    third_all_button.click()

                else:
                    GamePageCommon(self.driver).check_countdown_time()
                    all_buttons = self.find_elements(*Xpath.betting_freeSelection)
                    for buttons in all_buttons:
                        buttons.click()

                    GamePageCommon(self.driver).check_countdown_time()
                    all_buttons = self.find_elements(*Xpath.betting_all_button)
                    for buttons in all_buttons:
                        buttons.click()

            elif subtype_name == 'fourDirect':
                if Platform == 'Android' and Target == 'app':
                    GamePageCommon(self.driver).check_countdown_time()
                    all_buttons = self.find_elements(*Xpath.betting_freeSelection)
                    for buttons in all_buttons:
                        buttons.click()

                    GamePageCommon(self.driver).check_countdown_time()
                    all_buttons = self.find_elements(*Xpath.betting_all_button)
                    for buttons in all_buttons:
                        buttons.click()

                    GamePageCommon(self.driver).check_countdown_time()
                    start_location = self.find_element(*Xpath.title_second).location
                    end_location = self.find_element(*Xpath.history_button).location
                    self.swipe(start_location, end_location, y2scale=1.1)

                    GamePageCommon(self.driver).check_countdown_time()
                    all_buttons = self.find_elements(*Xpath.betting_all_button)
                    for buttons in all_buttons:
                        buttons.click()

                elif Platform == 'Android' and Target == 'h5':
                    GamePageCommon(self.driver).check_countdown_time()
                    all_buttons = self.find_elements(*Xpath.betting_freeSelection)
                    for buttons in all_buttons:
                        buttons.click()

                    GamePageCommon(self.driver).check_countdown_time()
                    first_all_button = self.find_element(*Xpath.betting_first_all_button)
                    second_all_button = self.find_element(*Xpath.betting_second_all_button)
                    for buttons in [first_all_button, second_all_button, ]:
                        buttons.click()

                    GamePageCommon(self.driver).check_countdown_time()
                    start_location = self.find_element(*Xpath.title_second).location
                    end_location = self.find_element(*Xpath.history_button).location
                    self.swipe(start_location, end_location, y2scale=1.2)

                    GamePageCommon(self.driver).check_countdown_time()
                    third_all_button = self.find_element(*Xpath.betting_third_all_button)
                    fourth_all_button = self.find_element(*Xpath.betting_fourth_all_button)
                    for buttons in [third_all_button, fourth_all_button]:
                        buttons.click()

                elif Platform == 'iOS' and Target == 'app':
                    GamePageCommon(self.driver).check_countdown_time()
                    all_buttons = self.find_elements(*Xpath.betting_freeSelection)
                    for buttons in all_buttons:
                        buttons.click()

                    GamePageCommon(self.driver).check_countdown_time()
                    all_buttons = self.find_elements(*Xpath.betting_all_button)
                    count = 0
                    for buttons in all_buttons:
                        if count == 3:
                            GamePageCommon(self.driver).check_countdown_time()
                            start_location = self.find_element(*Xpath.title_second).location
                            end_location = self.find_element(*Xpath.history_button).location
                            self.swipe(start_location, end_location, y2scale=1.1)
                        buttons.click()
                        count += 1

                elif Target == 'web':
                    GamePageCommon(self.driver).check_countdown_time()
                    all_buttons = self.find_elements(*Xpath.betting_freeSelection)
                    for buttons in all_buttons:
                        buttons.click()

                    GamePageCommon(self.driver).check_countdown_time()
                    all_buttons = self.find_elements(*Xpath.betting_all_button)
                    count = 0
                    for buttons in all_buttons:
                        buttons.click()
                        count += 1

    def bet_twoSide_all(self, type_name):
        if type_name in ['firstBall', 'secondBall', 'thirdBall', 'fourthBall', 'fifthBall', 'total', 'front3',
                         'middle3', 'back3', 'dragon', 'tiger', 'equal']:
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
