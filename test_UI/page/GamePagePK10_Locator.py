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
        # 雙面盤玩法
        twoSide_game_name_All = (By.XPATH, "//*[@id='left_recycler_view']/*")
        # 投注相關 for 盤面需要swipe時, end_location定位用
        history_button = (By.ID, "historyToggleBtn")
        # 投注相關 for 官方盤/常規 猜冠軍/猜冠亞軍/猜前三 & 官方盤/趣味 吃冠軍/投三甲/吃三甲/位置Q/連贏
        betting_all_button = (By.XPATH, "//*[@id='quickBtnContainer']/*[1]")
        # 投注相關 for 官方盤/常規 定位膽
        next_title = (By.XPATH, "(//*[@id='titleTextView'])[2]")  # 官方盤/常規 定位膽 & 雙面盤 兩面/1-10名 定位用
        betting_firstToTenth = (By.ID, "squareContainer")
        # 投注相關 for 雙面盤 兩面/猜冠亞/1-10名
        button_row2 = (By.XPATH, "(//*[@id='squareContainer'])[5]")  # 猜冠亞 定位用
        betting_twoSide_all_buttons = (By.ID, "squareContainer")
        # 投注相關 for 雙面盤 冠亞和
        button_row1 = (By.XPATH, "(//*[@id='squareContainer'])[1]")  # 定位用
        betting_sum1and2 = (By.ID, "squareContainer")

    elif Platform == 'Android' and Target == 'h5':
        # 官方盤玩法
        pro_game_type_normal = (By.XPATH, "//*[@nodeName='SECTION']/*[2]/*[@nodeName='BUTTON'][1]")
        pro_game_type_fun = (By.XPATH, "//*[@nodeName='SECTION']/*[2]/*[@nodeName='BUTTON'][2]")
        pro_game_name_All = (By.XPATH, "//*[@nodeName='SECTION']/*[3]/*/*/*/*[contains(@class, 'select-button')]")
        button_pro_game_confirm = (By.XPATH, "//*[@nodeName='MAIN']/*[@nodeName='MAIN']/*[@nodeName='DIV']"
                                             "/*[@nodeName='BUTTON']")
        # 雙面盤玩法
        twoSide_game_name_All = (By.XPATH, "//*[contains(@class, 'tabs-list')]/*")
        # 投注相關 for 盤面需要swipe時, end_location定位用
        history_button = (By.XPATH, "//*[@nodeName='BUTTON' and ./parent::*[@nodeName='SECTION']]")
        # 投注相關 for 官方盤/常規 猜冠軍/猜冠亞軍/猜前三 & 官方盤/趣味 吃冠軍/投三甲/吃三甲/位置Q/連贏
        betting_all_button = (By.XPATH, "//*[@class='bet_quick']/*/*/*[1]")
        # 投注相關 for 官方盤/常規 定位膽
        title_first = "//*[@nodeName='MAIN']/*[@nodeName='SECTION'][3]/*[2]/*[contains(@class, 'display-name')]"
        title_second = "//*[@nodeName='MAIN']/*[@nodeName='SECTION'][3]/*[3]/*[contains(@class, 'display-name')]"
        title_third = "//*[@nodeName='MAIN']/*[@nodeName='SECTION'][3]/*[4]/*[contains(@class, 'display-name')]"
        title_fourth = "//*[@nodeName='MAIN']/*[@nodeName='SECTION'][3]/*[5]/*[contains(@class, 'display-name')]"
        title_fifth = "//*[@nodeName='MAIN']/*[@nodeName='SECTION'][3]/*[6]/*[contains(@class, 'display-name')]"
        title_sixth = "//*[@nodeName='MAIN']/*[@nodeName='SECTION'][3]/*[7]/*[contains(@class, 'display-name')]"
        title_seventh = "//*[@nodeName='MAIN']/*[@nodeName='SECTION'][3]/*[8]/*[contains(@class, 'display-name')]"
        title_eighth = "//*[@nodeName='MAIN']/*[@nodeName='SECTION'][3]/*[9]/*[contains(@class, 'display-name')]"
        title_ninth = "//*[@nodeName='MAIN']/*[@nodeName='SECTION'][3]/*[10]/*[contains(@class, 'display-name')]"
        title_tenth = "//*[@nodeName='MAIN']/*[@nodeName='SECTION'][3]/*[11]/*[contains(@class, 'display-name')]"
        betting_first = "(((//*[@nodeName='MAIN']/*[@nodeName='SECTION'])[3]/*[@nodeName='DIV'])[2]/*/*[@nodeName='BUTTON'])"
        betting_second = "(((//*[@nodeName='MAIN']/*[@nodeName='SECTION'])[3]/*[@nodeName='DIV'])[3]/*/*[@nodeName='BUTTON'])"
        betting_third = "(((//*[@nodeName='MAIN']/*[@nodeName='SECTION'])[3]/*[@nodeName='DIV'])[4]/*/*[@nodeName='BUTTON'])"
        betting_fourth = "(((//*[@nodeName='MAIN']/*[@nodeName='SECTION'])[3]/*[@nodeName='DIV'])[5]/*/*[@nodeName='BUTTON'])"
        betting_fifth = "(((//*[@nodeName='MAIN']/*[@nodeName='SECTION'])[3]/*[@nodeName='DIV'])[6]/*/*[@nodeName='BUTTON'])"
        betting_sixth = "(((//*[@nodeName='MAIN']/*[@nodeName='SECTION'])[3]/*[@nodeName='DIV'])[7]/*/*[@nodeName='BUTTON'])"
        betting_seventh = "(((//*[@nodeName='MAIN']/*[@nodeName='SECTION'])[3]/*[@nodeName='DIV'])[8]/*/*[@nodeName='BUTTON'])"
        betting_eighth = "(((//*[@nodeName='MAIN']/*[@nodeName='SECTION'])[3]/*[@nodeName='DIV'])[9]/*/*[@nodeName='BUTTON'])"
        betting_ninth = "(((//*[@nodeName='MAIN']/*[@nodeName='SECTION'])[3]/*[@nodeName='DIV'])[10]/*/*[@nodeName='BUTTON'])"
        betting_tenth = "(((//*[@nodeName='MAIN']/*[@nodeName='SECTION'])[3]/*[@nodeName='DIV'])[11]/*/*[@nodeName='BUTTON'])"
        # 投注相關 for 雙面盤 兩面/1-10名
        twoSide_title_first = "(//*[contains(@class, 'bet-buttons')]//*[contains(@class, 'display-name')])[1]"
        twoSide_title_second = "(//*[contains(@class, 'bet-buttons')]//*[contains(@class, 'display-name')])[2]"
        twoSide_title_third = "(//*[contains(@class, 'bet-buttons')]//*[contains(@class, 'display-name')])[3]"
        twoSide_title_fourth = "(//*[contains(@class, 'bet-buttons')]//*[contains(@class, 'display-name')])[4]"
        twoSide_title_fifth = "(//*[contains(@class, 'bet-buttons')]//*[contains(@class, 'display-name')])[5]"
        twoSide_title_sixth = "(//*[contains(@class, 'bet-buttons')]//*[contains(@class, 'display-name')])[6]"
        twoSide_title_seventh = "(//*[contains(@class, 'bet-buttons')]//*[contains(@class, 'display-name')])[7]"
        twoSide_title_eighth = "(//*[contains(@class, 'bet-buttons')]//*[contains(@class, 'display-name')])[8]"
        twoSide_title_ninth = "(//*[contains(@class, 'bet-buttons')]//*[contains(@class, 'display-name')])[9]"
        twoSide_title_tenth = "(//*[contains(@class, 'bet-buttons')]//*[contains(@class, 'display-name')])[10]"
        betting_twoSide_first = "//*[@nodeName='DIV'][3]/*/*[@nodeName='BUTTON']"
        betting_twoSide_second = "//*[@nodeName='DIV'][4]/*/*[@nodeName='BUTTON']"
        betting_twoSide_third = "//*[@nodeName='DIV'][5]/*/*[@nodeName='BUTTON']"
        betting_twoSide_fourth = "//*[@nodeName='DIV'][6]/*/*[@nodeName='BUTTON']"
        betting_twoSide_fifth = "//*[@nodeName='DIV'][7]/*/*[@nodeName='BUTTON']"
        betting_twoSide_sixth = "//*[@nodeName='DIV'][8]/*/*[@nodeName='BUTTON']"
        betting_twoSide_seventh = "//*[@nodeName='DIV'][9]/*/*[@nodeName='BUTTON']"
        betting_twoSide_eighth = "//*[@nodeName='DIV'][10]/*/*[@nodeName='BUTTON']"
        betting_twoSide_ninth = "//*[@nodeName='DIV'][11]/*/*[@nodeName='BUTTON']"
        betting_twoSide_tenth = "//*[@nodeName='DIV'][12]/*/*[@nodeName='BUTTON']"
        # 投注相關 for 雙面盤 猜冠亞
        betting_1 = "//*[contains(@value,'1-')]"
        betting_2 = "//*[contains(@value,'2-')]"
        betting_3 = "//*[contains(@value,'3-')]"
        betting_4 = "//*[contains(@value,'4-')]"
        betting_5 = "//*[contains(@value,'5-')]"
        betting_6 = "//*[contains(@value,'6-')]"
        betting_7 = "//*[contains(@value,'7-')]"
        betting_8 = "//*[contains(@value,'8-')]"
        betting_9 = "//*[contains(@value,'9-')]"
        # 投注相關 for 雙面盤 冠亞和
        button_row1 = (By.XPATH, "(//*[@data-testid='pk10_BtnTestId'])[1]")  # 定位用
        betting_sum1and2 = (By.XPATH, "//*[@nodeName='SECTION'][3]/*/*/*[@nodeName='DIV'][3]/*[@nodeName='DIV']")

    elif Platform == 'iOS' and Target == 'app':
        # 官方盤玩法
        pro_game_type_normal = (By.XPATH, "//*[@class='UIAScrollView']//*[@class='UIASegmentedControl']/*[1]")
        pro_game_type_fun = (By.XPATH, "//*[@class='UIAScrollView']//*[@class='UIASegmentedControl']/*[2]")
        pro_game_name_All = (By.XPATH, "//*[@class='UIAView'][2]/*[@class='UIACollectionView']"
                                       "/*[@knownSuperClass='UICollectionViewCell']")
        # 雙面盤玩法
        twoSide_game_name_All = (By.XPATH, "//*[@class='UIATable']/*[@XCElementType='XCUIElementTypeCell']")
        # 投注相關 for 盤面需要swipe時, end_location定位用
        history_button = (By.XPATH, "//*[@knownSuperClass='UINavigationTransitionView']/*/*/*[@class='UIAButton'][2]")
        # 投注相關 for 官方盤/常規 猜冠軍/猜冠亞軍/猜前三 & 趣味 吃冠軍/投三甲/吃三甲/位置Q/連贏
        betting_all_button = (By.XPATH, "//*[@knownSuperClass='UIScrollView']/*/*/*/*[@class='UIAView'][1]/*[1]")
        # 投注相關 for 官方盤/常規 定位膽
        next_title = "(//*[@class='UIAScrollView']//*[@class='UIAScrollView']/*/*/*/*[@id='id_UILabel_'])"  # 定位用
        betting_first = "//*[@knownSuperClass='UIScrollView']/*/*/*[1]/*[2]//*[contains(@id,'id_UIButton')]"
        betting_second = "//*[@knownSuperClass='UIScrollView']/*/*/*[2]/*[2]//*[contains(@id,'id_UIButton')]"
        betting_third = "//*[@knownSuperClass='UIScrollView']/*/*/*[3]/*[2]//*[contains(@id,'id_UIButton')]"
        betting_fourth = "//*[@knownSuperClass='UIScrollView']/*/*/*[4]/*[2]//*[contains(@id,'id_UIButton')]"
        betting_fifth = "//*[@knownSuperClass='UIScrollView']/*/*/*[5]/*[2]//*[contains(@id,'id_UIButton')]"
        betting_sixth = "//*[@knownSuperClass='UIScrollView']/*/*/*[6]/*[2]//*[contains(@id,'id_UIButton')]"
        betting_seventh = "//*[@knownSuperClass='UIScrollView']/*/*/*[7]/*[2]//*[contains(@id,'id_UIButton')]"
        betting_eighth = "//*[@knownSuperClass='UIScrollView']/*/*/*[8]/*[2]//*[contains(@id,'id_UIButton')]"
        betting_ninth = "//*[@knownSuperClass='UIScrollView']/*/*/*[9]/*[2]//*[contains(@id,'id_UIButton')]"
        betting_tenth = "//*[@knownSuperClass='UIScrollView']/*/*/*[10]/*[2]//*[contains(@id,'id_UIButton')]"
        # 投注相關 for 雙面盤 兩面/1-10名
        next_title_twoSide = "(//*[@class='UIAScrollView']//*[@class='UIAScrollView']/*/*/*[@id='id_UILabel_'])"  # 定位用
        betting_first_twoSide = "//*[@knownSuperClass='UIScrollView']/*/*[@class='UIAView'][1]//*[@class='UIAButton']"
        betting_second_twoSide = "//*[@knownSuperClass='UIScrollView']/*/*[@class='UIAView'][2]//*[@class='UIAButton']"
        betting_third_twoSide = "//*[@knownSuperClass='UIScrollView']/*/*[@class='UIAView'][3]//*[@class='UIAButton']"
        betting_fourth_twoSide = "//*[@knownSuperClass='UIScrollView']/*/*[@class='UIAView'][4]//*[@class='UIAButton']"
        betting_fifth_twoSide = "//*[@knownSuperClass='UIScrollView']/*/*[@class='UIAView'][5]//*[@class='UIAButton']"
        betting_sixth_twoSide = "//*[@knownSuperClass='UIScrollView']/*/*[@class='UIAView'][6]//*[@class='UIAButton']"
        betting_seventh_twoSide = "//*[@knownSuperClass='UIScrollView']/*/*[@class='UIAView'][7]//*[@class='UIAButton']"
        betting_eighth_twoSide = "//*[@knownSuperClass='UIScrollView']/*/*[@class='UIAView'][8]//*[@class='UIAButton']"
        betting_ninth_twoSide = "//*[@knownSuperClass='UIScrollView']/*/*[@class='UIAView'][9]//*[@class='UIAButton']"
        betting_tenth_twoSide = "//*[@knownSuperClass='UIScrollView']/*/*[@class='UIAView'][10]//*[@class='UIAButton']"
        # 投注相關 for 雙面盤 猜冠亞
        betting_1 = "(//*[@class='UIAScrollView']//*[contains(@value,'id_UIButton__1-') " \
                    "and contains(@id,'id_UIButton__1-')])"
        betting_2 = "(//*[@class='UIAScrollView']//*[contains(@value,'id_UIButton__2-') " \
                    "and contains(@id,'id_UIButton__2-')])"
        betting_3 = "(//*[@class='UIAScrollView']//*[contains(@value,'id_UIButton__3-') " \
                    "and contains(@id,'id_UIButton__3-')])"
        betting_4 = "(//*[@class='UIAScrollView']//*[contains(@value,'id_UIButton__4-') " \
                    "and contains(@id,'id_UIButton__4-')])"
        betting_5 = "(//*[@class='UIAScrollView']//*[contains(@value,'id_UIButton__5-') " \
                    "and contains(@id,'id_UIButton__5-')])"
        betting_6 = "(//*[@class='UIAScrollView']//*[contains(@value,'id_UIButton__6-') " \
                    "and contains(@id,'id_UIButton__6-')])"
        betting_7 = "(//*[@class='UIAScrollView']//*[contains(@value,'id_UIButton__7-') " \
                    "and contains(@id,'id_UIButton__7-')])"
        betting_8 = "(//*[@class='UIAScrollView']//*[contains(@value,'id_UIButton__8-') " \
                    "and contains(@id,'id_UIButton__8-')])"
        betting_9 = "(//*[@class='UIAScrollView']//*[contains(@value,'id_UIButton__9-') " \
                    "and contains(@id,'id_UIButton__9-')])"
        # 投注相關 for 雙面盤 冠亞和
        button_row1 = (By.XPATH, "//*[@knownSuperClass='UIScrollView']/*/*[3]/*/*[1]/*[@class='UIAButton']")  # 定位用
        betting_sum1and2 = (By.XPATH, "(//*[@class='UIAScrollView']//*[contains(@value,'id_UIButton_')"
                                      " and contains(@id,'id_UIButton_')])")

    elif Platform == 'iOS' and Target == 'h5':
        pass

    elif Target == 'web':
        # 切換官方盤玩法
        pro_game_type_normal = (By.XPATH, "//button[@id='game_type_btn-normalgame']")
        pro_game_type_fun = (By.XPATH, "//button[@id='game_type_btn-funnygame']")
        normal_guess1 = (By.XPATH, "//button[@id='game-nav_guess1']")
        normal_guess12 = (By.XPATH, "//button[@id='game-nav_guess12']")
        normal_guess123 = (By.XPATH, "//button[@id='game-nav_guess123']")
        normal_firstToTenth = (By.XPATH, "//button[@id='game-nav_firstToTenth']")
        fun_eat1 = (By.XPATH, "//button[@id='game-nav_eat1']")
        fun_bet3 = (By.XPATH, "//button[@id='game-nav_bet3']")
        fun_eat3 = (By.XPATH, "//button[@id='game-nav_eat3']")
        fun_positionQ = (By.XPATH, "//button[@id='game-nav_positionQ']")
        fun_winningStreak = (By.XPATH, "//button[@id='game-nav_winningStreak']")
        betting_all_button = (By.XPATH, "(//*[contains(@id,'bet_btn_all')])")
        # 切換雙面盤玩法
        two_side_twoface = (By.XPATH, "//button[@id='game-nav_twoface']")
        two_side_combination1and2 = (By.XPATH, "//button[@id='game-nav_combination1and2']")
        two_side_sum1and2 = (By.XPATH, "//button[@id='game-nav_sum1and2']")
        two_side_firsttotenth = (By.XPATH, "//button[@id='game-nav_firsttotenth']")
        # 投注相關 for 官方盤/常規 定位膽
        subgame_firsttotenth = "//*[contains(@id, 'subgame-nav')]"
        betting_items = "//*[@class='not-number']//button"


if __name__ == '__main__':
    pass
