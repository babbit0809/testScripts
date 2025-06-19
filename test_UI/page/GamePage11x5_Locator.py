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
        # 投注相關 for 官方盤/常規 任二/任三/任四/任五/任六/任七/任八/前一/前二/前三(標準/組選) & 趣味 猜必出號碼
        betting_all_button = (By.XPATH, "//*[@id='quickBtnContainer']/*[1]")
        # 投注相關 for 官方盤/常規 任二/任三/任四/任五/任六/任七/任八/前一/前二/前三(單式)
        betting_info = (By.ID, "bettingCount")  # 單式鍵盤確認鍵 定位用
        betting_input_field = (By.ID, "orderInputEditText")
        # 投注相關 for 官方盤/趣味 和值(前三~後二)/跨度(全五~後三)/牛牛/牌點(前三~後三)/龍虎(全五~後二)
        betting_button_22 = (By.XPATH, "//*[@class='android.widget.RelativeLayout'][21]/*[@id='squareContainer']")  # 定位用
        betting_sumtodragonTiger = (By.ID, "squareContainer")
        # 投注相關 for 雙面盤 第一球~第五球/總和/龍/虎
        betting_twoSide_all_buttons = (By.ID, "squareContainer")

    elif Platform == 'Android' and Target == 'h5':
        # 官方盤玩法
        pro_game_type_normal = (By.XPATH, "//*[@nodeName='SECTION']/*[2]/*[@nodeName='BUTTON'][1]")
        pro_game_type_fun = (By.XPATH, "//*[@nodeName='SECTION']/*[2]/*[@nodeName='BUTTON'][2]")
        pro_game_name_All = (By.XPATH, "//*[@nodeName='SECTION']/*[3]/*/*/*/*[contains(@class, 'select-button')]")
        pro_subGame_name_All = (By.XPATH, "//*[@nodeName='SECTION']/*[4]/*/*/*/*[contains(@class, 'select-button')]")
        button_pro_game_confirm = (By.XPATH, "//*[@nodeName='MAIN']/*[@nodeName='MAIN']/*[@nodeName='DIV']"
                                             "/*[@nodeName='BUTTON']")
        # 雙面盤玩法
        twoSide_game_name_All = (By.XPATH, "//*[contains(@class, 'tabs-list')]/*")
        # 投注相關 for 盤面需要swipe時, end_location定位用
        history_button = (By.XPATH, "//*[@nodeName='BUTTON' and ./parent::*[@nodeName='SECTION']]")
        # 投注相關 for 官方盤/常規 任二/任三/任四/任五/任六/任七/任八/前一/前二/前三(標準/組選) & 趣味 猜必出號碼
        betting_all_button = (By.XPATH, "//*[@class='bet_quick']/*/*/*[1]")
        # 投注相關 for 官方盤/常規 任二/任三/任四/任五/任六/任七/任八/前一/前二/前三(單式)
        betting_input_field = (By.XPATH, "//*[@nodeName='TEXTAREA']")
        # 投注相關 for 官方盤/趣味 和值(前三~後三)
        betting_before_numbers = (By.XPATH, "//*[@nodeName='SECTION'][2]/*[2]/*/*/*[9]/preceding-sibling::*")
        betting_numbers1x = (By.XPATH, "//*[@class='center' and starts-with(@text, '1')]")
        betting_numbers2x = (By.XPATH, "//*[@class='center' and starts-with(@text, '2')]")
        betting_numbers3x = (By.XPATH, "//*[@class='center' and starts-with(@text, '3')]")
        button_18 = (By.XPATH, "//*[@class='center' and (@text='18')]")  # 定位用
        # 投注相關 for 官方盤/趣味 和值(前二~後二)/跨度(全五~後三)/牛牛/牌點(前三~後三)/龍虎(全五~後二)
        betting_sumtodragonTiger = (By.XPATH, "//*[@data-testid='betButton']")
        # 投注相關 for 雙面盤 第一球~第五球/總和/龍/虎
        betting_twoSide_all_buttons = (By.XPATH, "//*[contains(@data-testid,'TestId')]")

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
        # 投注相關 for 官方盤/常規 任二/任三/任四/任五/任六/任七/任八/前一/前二/前三(標準/組選) & 趣味 猜必出號碼
        betting_all_button = (By.XPATH, "//*[@knownSuperClass='UIScrollView']/*/*/*/*[@class='UIAView'][1]/*[1]")
        # 投注相關 for 官方盤/常規 任二/任三/任四/任五/任六/任七/任八/前一/前二/前三(單式)
        betting_info = (By.XPATH, "//*[@knownSuperClass='UIStackView']/*[4]/*[1]")  # 單式鍵盤確認鍵 定位用
        betting_input_field = (By.XPATH, "//*[contains(@id,'id_UITextView_')]")
        order_format_verified = (By.XPATH, "//*[@knownSuperClass='_UIAlertControllerActionView']")
        # 投注相關 for 官方盤/趣味 和值(前三~後二)/跨度(全五~後三)/牛牛/牌點(前三~後三)/龍虎(全五~後二)
        betting_button_22 = (By.ID, "id_UIButton__22")  # 定位用
        betting_sumtodragonTiger = (By.XPATH, "(//*[@class='UIAScrollView']//*[contains(@value,'id_UIButton_')"
                                              " and contains(@id,'id_UIButton_')])")
        # 投注相關 for 雙面盤 第一球~第五球/總和/龍/虎
        betting_twoSide_all_buttons = (By.XPATH, "(//*[@class='UIAScrollView']//*[contains(@value,'id_UIButton_')"
                                                 " and contains(@id,'id_UIButton_')])")

    elif Platform == 'iOS' and Target == 'h5':
        pass

    elif Target == 'web':
        # 玩法切換
        bet_category_pro = (By.XPATH, "//*[@id='profession']")
        bet_category_twoSide = (By.XPATH, "//*[@id='twoface']")
        # 切換官方盤玩法
        pro_game_type_normal = (By.XPATH, "//button[@id='game_type_btn-normalgame']")  # 常規_20200811
        pro_game_type_fun = (By.XPATH, "//button[@id='game_type_btn-funnygame']")  # 趣味_20200811
        pro_game_sandard = (By.XPATH, "//*[contains(@id,'andard')]")  # 標準_20200818
        pro_game_order = (By.XPATH, "//*[contains(@id,'rder')]")  # 單式_20200818
        pro_game_group = (By.XPATH, "//*[contains(@id,'group')]")  # 組選_20200818
        normal_r2 = (By.XPATH, "//button[@id='game-nav_r2']")  # 任二
        normal_r3 = (By.XPATH, "//button[@id='game-nav_r3']")  # 任三
        normal_r4 = (By.XPATH, "//button[@id='game-nav_r4']")  # 任四
        normal_r5 = (By.XPATH, "//button[@id='game-nav_r5']")  # 任五
        normal_r6 = (By.XPATH, "//button[@id='game-nav_r6']")  # 任六
        normal_r7 = (By.XPATH, "//button[@id='game-nav_r7']")  # 任七
        normal_r8 = (By.XPATH, "//button[@id='game-nav_r8']")  # 任八
        normal_front1 = (By.XPATH, "//button[@id='game-nav_front1']")  # 前一
        normal_front2 = (By.XPATH, "//button[@id='game-nav_front2']")  # 前二
        normal_front3 = (By.XPATH, "//button[@id='game-nav_front3']")  # 前三
        shop_car_button = (By.XPATH, "//button[@id='tab-bet_basket']")  # 購彩籃
        shop_car_active_button = (By.XPATH, "//button[@id='tab-bet_basket'][@class='active']")  # 購彩籃啟用
        del_bet_buttons = (By.XPATH, "//button[@class='clean-bet-list']")  # 清空購彩籃
        random_bet_buttons = (By.XPATH, "//*[@id='btn-random_bet']")  # 機選一注
        fun_sum = (By.XPATH, "//button[@id='game-nav_sum']")  # 和值
        fun_crossDegree = (By.XPATH, "//button[@id='game-nav_crossDegree']")  # 跨度
        fun_cowcow = (By.XPATH, "//button[@id='game-nav_cowcow']")  # 牛牛
        fun_cardPoint = (By.XPATH, "//button[@id='game-nav_cardPoint']")  # 牌点
        fun_dragontiger = (By.XPATH, "//button[@id='game-nav_dragonTiger']")  # 龙虎
        fun_alwaysGuess = (By.XPATH, "//button[@id='game-nav_alwaysGuess']")  # 猜必出号码
        fun_crossDegree_all5 = (By.XPATH, "//*[contains(@id,'subgame-nav_all5')]")  # 全五
        fun_sum_front3 = (By.XPATH, "//*[contains(@id,'subgame-nav_front3')]")  # 前三
        fun_sum_middle3 = (By.XPATH, "//*[contains(@id,'subgame-nav_middle3')]")  # 中三
        fun_sum_back3 = (By.XPATH, "//*[contains(@id,'subgame-nav_back3')]")  # 中三
        fun_sum_front2 = (By.XPATH, "//*[contains(@id,'subgame-nav_front2')]")  # 前二
        fun_sum_back2 = (By.XPATH, "//*[contains(@id,'subgame-nav_back2')]")  # 后二
        # 投注相關 for 官方盤/常規 任二/任三/任四/任五/任六/任七/任八/前一/前二/前三(標準/組選) & 趣味 猜必出號碼
        betting_all_button = (By.XPATH, "(//*[contains(@id,'bet_btn_all')])")  # 全
        # 投注相關 for 官方盤/趣味 和值(前三~後二)/跨度(全五~後三)/牛牛/牌點(前三~後三)/龍虎(全五~後二)
        # (使用find_elements, 視UI呈現分組)
        betting_sumtodragonTiger = (By.XPATH, "//*[@class='bet-btn']//button")  # 20200819_Adam
        # 切換雙面盤玩法
        two_side_firstToFifth = (By.XPATH, "//button[@id='game-nav_firstToFifth']")  # 第一球~第五球
        two_side_firstBall = (By.XPATH, "//button[@id='subgame-nav_firstBall']")  # 第一球
        two_side_secondBall = (By.XPATH, "//button[@id='subgame-nav_secondBall']")  # 第二球
        two_side_thirdBall = (By.XPATH, "//button[@id='subgame-nav_thirdBall']")  # 第三球
        two_side_fourthBall = (By.XPATH, "//button[@id='subgame-nav_fourthBall']")  # 第四球
        two_side_fifthBall = (By.XPATH, "//button[@id='subgame-nav_fifthBall']")  # 第五球
        two_side_total = (By.XPATH, "//button[@id='game-nav_total']")  # 总和
        two_side_dragontiger = (By.XPATH, "//button[@id='game-nav_dragontiger']")  # 龙虎
        two_side_dragon = (By.XPATH, "//button[@id='subgame-nav_dragon']")  # 龙
        two_side_tiger = (By.XPATH, "//button[@id='subgame-nav_tiger']")  # 虎
        # 投注相關 for 官方盤/常規 任二/任三/任四/任五/任六/任七/任八(單式)
        #                        前一/前二/前三(直选单式)
        betting_input_field = (By.XPATH, "//textarea")
        # 投注相關 for 雙面盤 第一球~第五球/總和/龍/虎 (使用find_elements, 視UI呈現分組)
        betting_twoSide_all_buttons = (By.XPATH, "//*[@class='not-number']//button")


if __name__ == '__main__':
    pass
