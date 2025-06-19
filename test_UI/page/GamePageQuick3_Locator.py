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
        # 投注相關 for 官方盤/常規 和值/三連號/三同號/三不同號/二同號(單選/複選)/二不同號
        betting_SumToDiffer2 = (By.ID, "squareContainer")
        # 投注相關 for 雙面盤 三軍/總和/點數/圍骰/長牌/短牌/魚蝦蟹
        betting_twoSide_all_buttons = (By.ID, "squareContainer")

    elif Platform == 'Android' and Target == 'h5':
        # 官方盤玩法(尚未分常規/趣味)
        pro_game_name_All = (By.XPATH, "//*[@nodeName='SECTION']/*[1]/*/*/*/*[contains(@class, 'select-button')]")
        pro_subGame_name_All = (By.XPATH, "//*[@nodeName='SECTION']/*[2]/*/*/*/*[contains(@class, 'select-button')]")
        button_pro_game_confirm = (By.XPATH, "//*[@nodeName='MAIN']/*/*[@nodeName='DIV']/*[@nodeName='BUTTON']")
        # 雙面盤玩法
        twoSide_game_name_All = (By.XPATH, "//*[contains(@class, 'tabs-list')]/*")
        # 投注相關 for 盤面需要swipe時, end_location定位用
        history_button = (By.XPATH, "//*[@nodeName='BUTTON' and ./parent::*[@nodeName='SECTION']]")
        # 投注相關 for 官方盤/常規 和值/三連號/三同號/三不同號/二同號(複選)/二不同號
        button_line4_sum = (By.XPATH, "//*[@nodeName='SECTION'][2]/*[2]/*/*/*[13]/*[@nodeName='BUTTON']")  # 定位用
        betting_SumToDiffer2 = (By.XPATH, "//*[@nodeName='SECTION'][2]//*[@nodeName='BUTTON']")
        # 投注相關 for 官方盤/常規 二同號(單選)
        title_differ = (By.XPATH, "//*[contains(@class, 'margin-top')]")  # 二同號(單選) 定位用
        betting_same2single_11toAll = (By.XPATH, "(((//*[@nodeName='MAIN']/*/*/*[@nodeName='DIV' and "
                                                 "./parent::*[@nodeName='DIV' and "
                                                 "./parent::*[@nodeName='SECTION']]])[3]/*[@nodeName='DIV'])[2]"
                                                 "/*/*[@nodeName='BUTTON'])")
        betting_same2single_1to6 = (By.XPATH, "(((//*[@nodeName='MAIN']/*/*/*[@nodeName='DIV' and "
                                              "./parent::*[@nodeName='DIV' and "
                                              "./parent::*[@nodeName='SECTION']]])[3]/*[@nodeName='DIV'])[4]"
                                              "/*/*[@nodeName='BUTTON'])")
        # 投注相關 for 雙面盤 三軍/總和/點數/圍骰/長牌/短牌/魚蝦蟹
        button_line1_long = (By.XPATH, "(//*[@data-testid='k3LongBetTestId'])[1]")  # 定位用
        betting_twoSide_all_buttons = (By.XPATH, "(//*[@nodeName='DIV' and ./parent::*[@nodeName='DIV' and "
                                                 "./parent::*[@nodeName='DIV' and "
                                                 "./parent::*[@nodeName='DIV']]]]/*/*[@nodeName='BUTTON'])")

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
        # 投注相關 for 官方盤/常規 和值/三連號/三同號/三不同號/二同號(單選/複選)/二不同號
        betting_SumToDiffer2 = (By.XPATH, "(//*[@class='UIAScrollView']//*[contains(@value,'id_UIButton_')"
                                          " and contains(@id,'id_UIButton_')])")
        # 投注相關 for 雙面盤 三軍/總和/點數/圍骰/長牌/短牌/魚蝦蟹
        betting_twoSide_all_buttons = (By.XPATH, "(//*[@class='UIAScrollView']//*[contains(@value,'id_UIButton_')"
                                                 " and contains(@id,'id_UIButton_')])")

    elif Platform == 'iOS' and Target == 'h5':  # 尚未分常規/趣味
        pass

    elif Target == 'web':
        # 切換官方盤玩法
        pro_game_type_normal = (By.XPATH, "//button[@id='game_type_btn-normalgame']")
        pro_game_type_fun = (By.XPATH, "//button[@id='game_type_btn-funnygame']")
        normal_sum = (By.XPATH, "//button[@id='game-nav_sum']")
        normal_continuous3 = (By.XPATH, "//button[@id='game-nav_continuous3']")
        normal_same3 = (By.XPATH, "//button[@id='game-nav_same3']")
        normal_differ3 = (By.XPATH, "//button[@id='game-nav_differ3']")
        normal_same2 = (By.XPATH, "//button[@id='game-nav_same2']")
        normal_same2_singleChoice = (By.XPATH, "//button[@id='subgame-nav_singleChoice']")
        normal_same2_multiChoices = (By.XPATH, "//button[@id='subgame-nav_multiChoices']")
        normal_differ2 = (By.XPATH, "//button[@id='game-nav_differ2']")
        shop_car_button = (By.XPATH, "//button[@id='tab-bet_basket']")  # 購彩籃
        shop_car_active_button = (By.XPATH, "//button[@id='tab-bet_basket'][@class='active']")  # 購彩籃啟用
        del_bet_buttons = (By.XPATH, "//button[@class='clean-bet-list']")  # 清空購彩籃
        random_bet_buttons = (By.XPATH, "//*[@id='btn-random_bet']")  # 機選一注

        # 切換雙面盤玩法
        two_side_army3 = (By.XPATH, "//button[@id='game-nav_army3']")
        two_side_fast3Sum = (By.XPATH, "//button[@id='game-nav_fast3Sum']")
        two_side_point = (By.XPATH, "//button[@id='game-nav_point']")
        two_side_triple = (By.XPATH, "//button[@id='game-nav_triple']")
        two_side_long = (By.XPATH, "//button[@id='game-nav_long']")
        two_side_short = (By.XPATH, "//button[@id='game-nav_short']")
        two_side_fishShrimpCrab = (By.XPATH, "//button[@id='game-nav_fishShrimpCrab']")

        # 投注相關 for 官方盤/常規 和值/三連號/三同號/三不同號/二同號(複選)/二不同號
        betting_SumToDiffer2 = (By.XPATH, "//*[@class='bet-btn']//button")
        betting_SumToDifferAll = (By.XPATH, "//*[@class='all']//button")

        # 投注相關 for 官方盤/常規 二同號(單選)
        betting_same2single_11toAll = (By.XPATH, "//*[@class='betLabel']")

        # 投注相關 for 雙面盤 三軍/總和/點數/圍骰/長牌/短牌/魚蝦蟹
        betting_twoSide_all_buttons = (By.XPATH, "//*[@class='bet-btn']//button")


if __name__ == '__main__':
    pass
