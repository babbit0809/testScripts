from selenium.webdriver.common.by import By
from config.SetUIConfig import Platform, Target
from test_UI.common import BasePage


class Xpath(BasePage.BasePage):
    # Locators
    if Platform == 'Android' and Target == 'app':
        # 官方盤玩法
        pro_game_type_normal = (By.XPATH, "//*[@id='radioToggleGroup']/*[1]")
        pro_game_type_fun = (By.XPATH, "//*[@id='radioToggleGroup']/*[2]")
        pro_game_name_All = (By.XPATH, "//*[@id='mainGameRecyclerView']/*")
        pro_subGame_name_All = (By.XPATH, "//*[@id='subGameRecyclerView']/*")
        # 雙面盤玩法
        twoSide_game_name_All = (By.XPATH, "//*[@id='left_recycler_view']/*")
        # 投注相關 for 盤面需要swipe時, end_location定位用
        history_button = (By.ID, "historyToggleBtn")
        # 投注相關 for 官方盤/常規 五星玩法(五星直選/組選120/組選60/組選30/組選20/組選10/組選5)
        #                        三星玩法(前三直選/中三直選/後三直選)
        #                        三星組三(前三組三/中三組三/後三組三)
        #                        三星組六(前三組六/中三組六/後三組六)
        #                        二星玩法(前二直選/前二組選/後二直選/後二組選)
        #                        定位膽/不定位膽(前三/中三/後三)
        #                        任選(任二直選/任二組選)
        title_hundred = (By.XPATH, "//*[@id='recyclerView']/*[@class='android.widget.RelativeLayout'][4]"
                                   "/*[@class='android.widget.TextView']")  # 五星直選/定位膽 定位用
        betting_all_button = (By.XPATH, "//*[@id='quickBtnContainer']/*[1]")
        # 投注相關 for 官方盤/常規 五星玩法(五星單式)
        #                        三星玩法(前三單式/中三單式/後三單式/前三混選/中三混選/後三混選)
        #                        二星玩法(前二單式/後二單式)
        #                        任選(任二單式/任三單式/任四單式)
        betting_info = (By.ID, "bettingCount")  # 單式鍵盤確認鍵 定位用
        betting_input_field = (By.ID, "orderInputEditText")
        # 投注相關 for 官方盤/常規 大小單雙
        betting_bigSmallOddEven = (By.ID, "squareContainer")
        # 投注相關 for 官方盤/常規 任選(任二直選/任二組選/任三直選/任三組三/任三組六/任四直選), 需同時搭配betting_all_button
        title_second = (By.XPATH, "//*[@id='recyclerView']/*[@class='android.widget.RelativeLayout'][7]"
                                  "/*[@class='android.widget.TextView']")  # 任選(任四直選) 定位用
        betting_freeSelection = (By.ID, "positBtn")
        # 投注相關 for 官方盤/常規 任選(任二單式/任三單式/任四單式), 需同時搭配betting_input_field
        betting_freeSelection_order = (By.XPATH, "//*[@id='positSection']/*[@class='android.widget.TextView']")
        # 投注相關 for 雙面盤 第一球~第五球/總和/前三~後三/龍~和
        betting_twoSide_all_buttons = (By.XPATH, "(//*[@id='recycler_view']/*/*/*"
                                                 "[@class='android.widget.LinearLayout'])")

    elif Platform == 'Android' and Target == 'h5':
        # 官方盤玩法(尚未分常規/趣味)
        pro_game_name_All = (By.XPATH, "//*[@nodeName='SECTION']/*[1]/*/*/*/*[contains(@class, 'select-button')]")
        pro_subGame_name_All = (By.XPATH, "//*[@nodeName='SECTION']/*[2]/*/*/*/*[contains(@class, 'select-button')]")
        button_pro_game_confirm = (By.XPATH, "//*[@nodeName='MAIN']/*/*[@nodeName='DIV']/*[@nodeName='BUTTON']")
        # 雙面盤玩法
        twoSide_game_name_All = (By.XPATH, "//*[contains(@class, 'tabs-list')]/*")
        # 投注相關 for 盤面需要swipe時, end_location定位用
        history_button = (By.XPATH, "//*[@nodeName='BUTTON' and ./parent::*[@nodeName='SECTION']]")
        # 投注相關 for 官方盤/常規 五星玩法(五星直選/組選120/組選60/組選30/組選20/組選10/組選5)
        #                        三星玩法(前三直選/中三直選/後三直選)
        #                        三星組三(前三組三/中三組三/後三組三)
        #                        三星組六(前三組六/中三組六/後三組六)
        #                        二星玩法(前二直選/前二組選/後二直選/後二組選)
        #                        定位膽/不定位膽(前三/中三/後三)
        #                        任選(任二直選/任二組選)
        title_hundred = (By.XPATH, "//*[@nodeName='MAIN']/*[@nodeName='SECTION'][2]/*[2]/*/*/*[3]"
                                   "//*[@class='unit_title']")  # 五星直選/定位膽 定位用
        betting_million_all_button = (By.XPATH, "(//*[@class='bet_quick']//li[1])[1]")
        betting_thousand_all_button = (By.XPATH, "(//*[@class='bet_quick']//li[1])[2]")
        betting_hundred_all_button = (By.XPATH, "(//*[@class='bet_quick']//li[1])[3]")
        betting_ten_all_button = (By.XPATH, "(//*[@class='bet_quick']//li[1])[4]")
        betting_digit_all_button = (By.XPATH, "(//*[@class='bet_quick']//li[1])[5]")
        betting_all_button = (By.XPATH, "//*[@class='bet_quick']/*/*/*[1]")
        # 投注相關 for 官方盤/常規 五星玩法(五星單式)
        #                        三星玩法(前三單式/中三單式/後三單式/前三混選/中三混選/後三混選)
        #                        二星玩法(前二單式/後二單式)
        #                        任選(任二單式)
        betting_input_field = (By.XPATH, "//*[@nodeName='TEXTAREA']")
        # 投注相關 for 官方盤/常規 大小單雙
        betting_bigSmallOddEven = (By.XPATH, "(((//*[@nodeName='MAIN']/*/*/*[@nodeName='DIV' and "
                                             "./parent::*[@nodeName='DIV' and "
                                             "./parent::*[@nodeName='SECTION']]])[3]/*[@nodeName='DIV'])"
                                             "/*/*[@nodeName='BUTTON'])")
        # 投注相關 for 官方盤/常規 任選(任二直選/任二組選/任三直選/任三組三/任三組六/任四直選), 需同時搭配betting_all_button
        title_second = (By.XPATH, "//*[@nodeName='MAIN']/*[@nodeName='SECTION'][2]/*[2]/*/*"
                                  "/*[3]//*[@class='unit_title']")  # 任選(任三直選/任四直選) 定位用
        betting_freeSelection = (By.XPATH, "//*[contains(@class,'input-checkbox')]")
        betting_first_all_button = (
            By.XPATH, "//*[@nodeName='SECTION'][2]/*[2]/*/*/*[2]/*[1]/*[2]/*/*[@nodeName='UL']/*[1]")
        betting_second_all_button = (
            By.XPATH, "//*[@nodeName='SECTION'][2]/*[2]/*/*/*[3]/*[1]/*[2]/*/*[@nodeName='UL']/*[1]")
        betting_third_all_button = (
            By.XPATH, "//*[@nodeName='SECTION'][2]/*[2]/*/*/*[4]/*[1]/*[2]/*/*[@nodeName='UL']/*[1]")
        betting_fourth_all_button = (
            By.XPATH, "//*[@nodeName='SECTION'][2]/*[2]/*/*/*[5]/*[1]/*[2]/*/*[@nodeName='UL']/*[1]")
        # 投注相關 for 官方盤/常規 任選(任二單式/任三單式/任四單式), 需同時搭配betting_input_field
        betting_freeSelection_order = (By.XPATH, "//*[@class='checkmark label-start']")
        # 投注相關 for 雙面盤 第一球~第五球/總和/前三~後三/龍~和
        betting_twoSide_all_buttons = (By.XPATH, "//*[@nodeName='SECTION' and ./*[./*[@nodeName='ASIDE']]]"
                                                 "//*[@nodeName='DIV']/*[@nodeName='DIV']/*/*[@nodeName='BUTTON']")

    elif Platform == 'iOS' and Target == 'app':
        # 官方盤玩法
        pro_game_type_normal = (By.XPATH, "//*[@class='UIAScrollView']//*[@class='UIASegmentedControl']/*[1]")
        pro_game_type_fun = (By.XPATH, "//*[@class='UIAScrollView']//*[@class='UIASegmentedControl']/*[2]")
        pro_game_name_All = (By.XPATH, "//*[@class='UIAView'][2]/*[@class='UIACollectionView']"
                                       "/*[@knownSuperClass='UICollectionViewCell']")
        pro_subGame_name_All = (By.XPATH, "//*[@class='UIAView'][3]/*[@class='UIACollectionView']"
                                          "/*[@knownSuperClass='UICollectionViewCell']")
        # 雙面盤玩法
        twoSide_game_name_All = (By.XPATH, "//*[@class='UIATable']/*[@XCElementType='XCUIElementTypeCell']")
        # 投注相關 for 盤面需要swipe時, end_location定位用
        history_button = (By.XPATH, "//*[@knownSuperClass='UINavigationTransitionView']/*/*/*[@class='UIAButton'][2]")
        # 投注相關 for 官方盤/常規 五星玩法(五星直選/組選120/組選60/組選30/組選20/組選10/組選5)
        #                        三星玩法(前三直選/中三直選/後三直選)
        #                        三星組三(前三組三/中三組三/後三組三)
        #                        三星組六(前三組六/中三組六/後三組六)
        #                        二星玩法(前二直選/前二組選/後二直選/後二組選)
        #                        定位膽/不定位膽(前三/中三/後三)
        #                        任選(任二直選/任二組選)
        title_hundred = (By.XPATH, "//*[@knownSuperClass='UIScrollView']/*/*/*[3]/*[@id='id_UILabel_']")  # 五星直選/定位膽 定位用
        betting_all_button = (By.XPATH, "//*[@knownSuperClass='UIScrollView']/*/*/*/*[2]/*[1]/*[@class='UIAButton']")
        # 投注相關 for 官方盤/常規 五星玩法(五星單式)
        #                        三星玩法(前三單式/中三單式/後三單式/前三混選/中三混選/後三混選)
        #                        二星玩法(前二單式/後二單式)
        #                        任選(任二單式/任三單式/任四單式)
        betting_info = (By.XPATH, "//*[@knownSuperClass='UIStackView'][4]/*[@class='UIAButton'][1]")  # 單式鍵盤確認鍵 定位用
        betting_input_field = (By.XPATH, "//*[contains(@id,'id_UITextView_')]")
        order_format_verified = (By.XPATH, "//*[@knownSuperClass='UIStackView']")
        # 投注相關 for 官方盤/常規 大小單雙
        betting_bigSmallOddEven = (By.XPATH, "(//*[@class='UIAScrollView']//*[contains(@value,'id_UIButton_')"
                                             " and contains(@id,'id_UIButton_')])")
        # 投注相關 for 官方盤/常規 任選(任二直選/任二組選/任三直選/任三組三/任三組六/任四直選), 需同時搭配betting_all_button
        title_second = (By.XPATH, "//*[@knownSuperClass='UIScrollView']/*/*/*[3]/*[@id='id_UILabel_']")  # 任選(任四直選) 定位用
        betting_freeSelection = (By.XPATH, "//*[@knownSuperClass='UIScrollView']/*/*/*[1]/*[@class='UIAButton']")
        # 投注相關 for 官方盤/常規 任選(任二單式/任三單式/任四單式), 需同時搭配betting_input_field
        betting_freeSelection_order = (By.XPATH, "//*[@knownSuperClass='UIScrollView']/*/*/*[1]/*[@class='UIAButton']")
        # 投注相關 for 雙面盤 第一球~第五球/總和/前三~後三/龍~和
        betting_twoSide_all_buttons = (By.XPATH, "(//*[@class='UIAScrollView']//*[contains(@value,'id_UIButton_')"
                                                 " and contains(@id,'id_UIButton_')])")

    elif Platform == 'iOS' and Target == 'h5':  # 尚未分常規/趣味
        pass

    elif Target == 'web':
        # 切換官方盤玩法
        pro_game_type_normal = (By.XPATH, "//button[@id='game_type_btn-normalgame']")
        pro_game_type_fun = (By.XPATH, "//button[@id='game_type_btn-funnygame']")

        # 投注相關 for 官方盤/常規 五星玩法(五星單式)
        #                        三星玩法(前三單式/中三單式/後三單式/前三混選/中三混選/後三混選)
        #                        二星玩法(前二單式/後二單式)
        pro_game_order = (By.XPATH, "(//*[contains(@id,'rder')])")  # 單式
        normal_game_front = (By.XPATH, "(//*[contains(@id,'subgame-nav_front')])")  # 前
        normal_game_middle = (By.XPATH, "(//*[contains(@id,'subgame-nav_middle')])")  # 中
        normal_game_back = (By.XPATH, "(//*[contains(@id,'subgame-nav_back')])")  # 後
        normal_game_mix = (By.XPATH, "(//*[contains(@id,'Mix')])")  # 混選
        betting_input_field = (By.XPATH, "//textarea")
        shop_car_button = (By.XPATH, "//button[@id='tab-bet_basket']")  # 購彩籃
        shop_car_active_button = (By.XPATH, "//button[@id='tab-bet_basket'][@class='active']")  # 購彩籃啟用
        del_bet_buttons = (By.XPATH, "//button[@class='clean-bet-list']")  # 清空購彩籃
        random_bet_buttons = (By.XPATH, "//*[@id='btn-random_bet']")  # 機選一注

        # 投注相關 for 官方盤/常規 五星玩法(五星直選/組選120/組選60/組選30/組選20/組選10/組選5)
        #                         三星玩法/三星组三/三星组六/二星玩法/定位胆/不定位胆/大小单双
        normal_fiveStar = (By.XPATH, "//button[@id='game-nav_fiveStar']")
        normal_fiveStar_fiveStarDirectSelection = (By.XPATH, "//button[@id='subgame-nav_fiveStarDirectSelection']")
        normal_fiveStar_selection120 = (By.XPATH, "//button[@id='subgame-nav_selection120']")
        normal_fiveStar_selection60 = (By.XPATH, "//button[@id='subgame-nav_selection60']")
        normal_fiveStar_selection30 = (By.XPATH, "//button[@id='subgame-nav_selection30']")
        normal_fiveStar_selection20 = (By.XPATH, "//button[@id='subgame-nav_selection20']")
        normal_fiveStar_selection10 = (By.XPATH, "//button[@id='subgame-nav_selection10']")
        normal_fiveStar_selection5 = (By.XPATH, "//button[@id='subgame-nav_selection5']")
        normal_threeStar = (By.XPATH, "//button[@id='game-nav_threeStar']")
        normal_threeStarGroup3 = (By.XPATH, "//button[@id='game-nav_threeStarGroup3']")
        normal_threeStarGroup6 = (By.XPATH, "//button[@id='game-nav_threeStarGroup6']")
        normal_twoStar = (By.XPATH, "//button[@id='game-nav_twoStar']")
        normal_dingweidan = (By.XPATH, "//button[@id='game-nav_dingweidan']")
        normal_budingweidan = (By.XPATH, "//button[@id='game-nav_budingweidan']")
        normal_bigSmallOddEven = (By.XPATH, "//button[@id='game-nav_bigSmallOddEven']")

        betting_freeSelection = (By.XPATH, "//label[contains(@for,'id_')]")
        betting_freeSelection_order = (By.XPATH, "//label[contains(@for,'id_')]")
        betting_all_button = (By.XPATH, "(//*[contains(@id,'bet_btn_all')])")  # 全
        normal_freeSelection = (By.XPATH, "//button[@id='game-nav_freeSelection']")
        normal_freeSelection_twoDirect = (By.XPATH, "//button[@id='subgame-nav_twoDirect']")
        normal_freeSelection_twoGroup = (By.XPATH, "//button[@id='subgame-nav_twoGroup']")
        normal_freeSelection_twoOrder = (By.XPATH, "//button[@id='subgame-nav_twoOrder']")
        normal_freeSelection_threeDirect = (By.XPATH, "//button[@id='subgame-nav_threeDirect']")
        normal_freeSelection_threeGroup3 = (By.XPATH, "//button[@id='subgame-nav_threeGroup3']")
        normal_freeSelection_threeGroup6 = (By.XPATH, "//button[@id='subgame-nav_threeGroup6']")
        normal_freeSelection_threeOrder = (By.XPATH, "//button[@id='subgame-nav_threeOrder']")
        normal_freeSelection_fourDirect = (By.XPATH, "//button[@id='subgame-nav_fourDirect']")
        normal_freeSelection_fourOrder = (By.XPATH, "//button[@id='subgame-nav_fourOrder']")
        # 投注相關 for 官方盤/常規 大小单双
        betting_bigSmallOddEven = (By.XPATH, "(//*[contains(@id,'bet-btn')])")

        # 切換雙面盤玩法
        two_side_firstToFifth = (By.XPATH, "//button[@id='game-nav_firstToFifth']")
        two_side_firstBall = (By.XPATH, "//button[@id='subgame-nav_firstBall']")
        two_side_secondBall = (By.XPATH, "//button[@id='subgame-nav_secondBall']")
        two_side_thirdBall = (By.XPATH, "//button[@id='subgame-nav_thirdBall']")
        two_side_fourthBall = (By.XPATH, "//button[@id='subgame-nav_fourthBall']")
        two_side_fifthBall = (By.XPATH, "//button[@id='subgame-nav_fifthBall']")
        two_side_frontMiddleBack3 = (By.XPATH, "//button[@id='game-nav_frontMiddleBack3']")
        two_side_front3 = (By.XPATH, "//button[@id='subgame-nav_front3']")
        two_side_middle3 = (By.XPATH, "//button[@id='subgame-nav_middle3']")
        two_side_back3 = (By.XPATH, "//button[@id='subgame-nav_back3']")
        two_side_total = (By.XPATH, "//*[@id='game-nav_total']")
        two_side_dragonTigerEqual = (By.XPATH, "//button[@id='game-nav_dragonTigerEqual']")
        two_side_dragon = (By.XPATH, "//button[@id='subgame-nav_dragon']")
        two_side_tiger = (By.XPATH, "//button[@id='subgame-nav_tiger']")
        two_side_equal = (By.XPATH, "//button[@id='subgame-nav_equal']")

        # 投注相關 for 雙面
        betting_twoSide_all_buttons = (By.XPATH, "(//*[contains(@class,'bet-btn')])")


if __name__ == '__main__':
    pass
