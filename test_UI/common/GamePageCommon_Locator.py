from selenium.webdriver.common.by import By
from config.SetUIConfig import Platform, Target
from test_UI.common import BasePage


class Xpath(BasePage.BasePage):
    # Locators
    if Platform == 'Android' and Target == 'app':
        # 當期截止視窗相關
        info_countdown_all_page = (By.ID, "currentIssueCountdownTextView")
        button_endgame = (By.ID, "button1")
        # 盤面切換
        bet_category_pro = (By.XPATH, "//*[@id='radio_pro']")
        bet_category_twoSide = (By.XPATH, "//*[@id='radio_two_side']")
        # 切換官方盤玩法 (option_level1_title為避免高頻彩的盈虧通知視窗擋住玩法選單造成error)
        option_pro_game_type = (By.ID, "toolbar_title")
        option_level1_title = (By.ID, "mainGameTextView")
        # 投注相關(官方盤)
        bet_currency_dollar = (By.ID, "radio_dollar")
        bet_currency_dime = (By.ID, "radio_dime")
        bet_currency_cent = (By.ID, "radio_cent")
        button_bet_basket = (By.ID, "confirmBtn")
        # 投注相關(雙面盤)
        bet_chip_2 = (By.ID, "chip2")
        bet_chip_50 = (By.ID, "chip50")
        bet_chip_100 = (By.ID, "chip100")
        bet_chip_500 = (By.ID, "chip500")
        bet_chip_1000 = (By.ID, "chip1000")
        # 訂單相關(訂單確認/訂單成立視窗欄位元件一致)
        button_payment_pro = (By.ID, "submitBtn")
        button_payment_twoSide = (By.ID, "submitBtn")
        order_info = (By.XPATH, "//*[@id='custom']/*/*[@class='android.widget.LinearLayout']//*[@class='android.widget.TextView']")
        button_order_confirm = (By.ID, "okBtn")
        button_order_done = (By.ID, "okBtn")
        # 彩票投注tearDown相關
        button_back = (By.ID, "toolbar_nav_btn")
        # For 越南tearDown用
        lottery_banner_Hot = (By.XPATH, "//*[@id='gameRecyclerView']/*[@class='android.widget.FrameLayout'][1]")

    elif Platform == 'Android' and Target == 'h5':
        # 當期截止視窗相關
        info_countdown_all_page = (By.XPATH, "//*[@class='status-bottom']/*[1]")
        button_endgame = (By.CLASS_NAME, "swal2-confirm swal2-styled")
        # 盤面切換
        bet_category_pro = (By.XPATH, "//*[contains(@class,'switch')]//button[1]")
        bet_category_twoSide = (By.XPATH, "//*[contains(@class,'switch')]//button[2]")
        # 切換官方盤玩法 (option_level1_title為避免高頻彩的盈虧通知視窗擋住玩法選單造成error)
        option_pro_game_type = (By.CLASS_NAME, "tringle")
        option_level1_title = (By.XPATH, "//*[@nodeName='H2']")
        # 投注相關(官方盤)
        bet_currency_dollar = (By.XPATH, "//*[@nodeName='FOOTER']/*/*[1]/*[@nodeName='BUTTON'][1]")
        bet_currency_dime = (By.XPATH, "//*[@nodeName='FOOTER']/*/*[1]/*[@nodeName='BUTTON'][2]")
        bet_currency_cent = (By.XPATH, "//*[@nodeName='FOOTER']/*/*[1]/*[@nodeName='BUTTON'][3]")
        button_bet_basket = (By.XPATH, "//*[contains(@class,'cart-button')]")
        # 投注相關(雙面盤)
        bet_chip_2 = (By.XPATH, "//*[@nodeName='FOOTER']//*[@id='chip2']")
        bet_chip_50 = (By.XPATH, "//*[@nodeName='FOOTER']//*[@id='chip50']")
        bet_chip_100 = (By.XPATH, "//*[@nodeName='FOOTER']//*[@id='chip100']")
        bet_chip_500 = (By.XPATH, "//*[@nodeName='FOOTER']//*[@id='chip500']")
        bet_chip_1000 = (By.XPATH, "//*[@nodeName='FOOTER']//*[@id='chip1000']")
        # 訂單相關(訂單確認/訂單成立視窗欄位元件一致)
        button_payment_pro = (By.XPATH, "//*[contains(@class,'checkout-button')]")
        button_payment_twoSide = (By.XPATH, "//*[contains(@class,'etButton')]")
        order_info = (By.XPATH, "//*[@class='swal2-content']//*[@id='swal2-content']/*[1]")
        button_order_confirm = (By.XPATH, "//*[contains(@class,'confirm')]")
        button_order_done = (By.XPATH, "//*[contains(@class,'confirm')]")
        # 彩票投注tearDown相關
        button_back = (By.XPATH, "//*[contains(@data-testid,'navigation-bar')]/div/div[1]")
        # For 越南tearDown用
        lottery_banner_Hot = (By.XPATH, "//*[contains(@class,'PanelSummary')][@id='panel1d-header']")
        # 第三方遊戲標題
        thirdParty_title = (By.XPATH, "//*[contains(@data-testid,'navigation-bar')]/div/div[2]/div")

    elif Platform == 'iOS' and Target == 'app':
        # 當期截止視窗相關
        info_countdown_all_page = (By.XPATH, "//*[@class='UIAView']/*[@class='UIAStaticText'][5]")
        button_endgame = (By.XPATH, "//*[@knownSuperClass='UITransitionView'][2]/*/*/*[3]/*[@class='UIAButton']")
        # 盤面切換
        bet_category_pro = (By.XPATH, "//*[@class='UIASegmentedControl']/*[1]")
        bet_category_twoSide = (By.XPATH, "//*[@class='UIASegmentedControl']/*[2]")
        # 切換官方盤玩法 (option_level1_title為避免高頻彩的盈虧通知視窗擋住玩法選單造成error)
        option_pro_game_type = (By.XPATH, "//*[@class='UIANavigationBar']//*[@id='id_UILabel_']")
        option_level1_title = (By.XPATH, "//*[@class='UIAScrollView']/*/*[@id='id_UILabel_'][1]")
        # 投注相關(官方盤)
        bet_currency_dollar = (By.XPATH, "(//*[@class='UIAScrollView'])[1]/*/*/*[last()]/*/*[@class='UIAButton'][1]")
        bet_currency_dime = (By.XPATH, "(//*[@class='UIAScrollView'])[1]/*/*/*[last()]/*/*[@class='UIAButton'][2]")
        bet_currency_cent = (By.XPATH, "(//*[@class='UIAScrollView'])[1]/*/*/*[last()]/*/*[@class='UIAButton'][3]")
        button_bet_basket = (By.XPATH, "(//*[@class='UIAScrollView'])[1]/*/*/*[last()]/*/*//*[@class='UIAButton']")
        # 投注相關(雙面盤)
        bet_chip_2 = (By.ID, "icon chip02")
        bet_chip_50 = (By.ID, "icon chip50")
        bet_chip_100 = (By.ID, "icon chip100")
        bet_chip_500 = (By.ID, "icon chip500")
        bet_chip_1000 = (By.ID, "icon chip1000")
        # 訂單相關(訂單確認/訂單成立視窗欄位元件一致)
        button_payment_pro = (By.ID, "id_UIButton_cartVC_semSubmitBtn")
        button_payment_twoSide = (By.XPATH, "//*[@knownSuperClass='_UIQueuingScrollView']/*/*/*[3]/*[2]/*[3]")
        order_info = (By.XPATH, "(//*[@knownSuperClass='UITransitionView'])[2]/*/*/*[2]")
        button_order_confirm = (By.XPATH, "(//*[@knownSuperClass='UITransitionView'])[2]/*/*/*[4]//*[@class='UIAButton'][2]")
        button_order_done = (By.XPATH, "(//*[@knownSuperClass='UITransitionView'])[2]/*/*/*[4]//*[@class='UIAButton']")
        # 彩票投注tearDown相關
        button_back = (By.ID, "id_UIButton_navBtn_back")
        # For 越南tearDown用
        lottery_banner_Hot = (By.XPATH, "//*[@XCElementType='XCUIElementTypeTable']/*[2]/*[@label='Game Hot']")
        lottery_banner_SSC = (By.XPATH, "//*[@class='UIATable']/*[3]/*[@class='UIAButton'][2]")  # 定位用
        tab_home = (By.XPATH, "//*[@class='UIATabBar']/*[@class='UIAButton'][1]")  # 定位用
        # 第三方遊戲標題
        thirdParty_title = (By.XPATH, "//*[@class='UIANavigationBar']//*[@class='UIAStaticText' and @knownSuperClass='UILabel']")

    elif Platform == 'iOS' and Target == 'h5':
        pass

    elif Target == 'web':
        # 當期截止視窗相關
        info_countdown_all_page = (By.CSS_SELECTOR, "#counter")
        info_countdown_basket_page = (By.CSS_SELECTOR, "#counter")
        # button_endgame = (By.XPATH, "//*[@text='确认' and @nodeName='BUTTON']")
        button_endgame = (By.XPATH, "//button[contains(@class,'close')]")
        # 盤面切換
        option_pro_game_type = (By.XPATH, "//*[@id='profession']")
        bet_category_pro = (By.XPATH, "//*[@id='profession']")  # 官方
        bet_category_twoSide = (By.XPATH, "//*[@id='twoface']")  # 雙面
        # 投注相關 for pro_bet_setting & enter 購彩籃頁面
        bet_currency_dollar = (By.XPATH, "//button[@id='currency-btn-dollar']")
        bet_currency_dime = (By.XPATH, "//button[@id='currency-btn-dime']")
        bet_currency_cent = (By.XPATH, "//button[@id='currency-btn-cent']")
        button_bet_basket = (By.XPATH, "//button[@id='btn-add_to_card']")
        # 投注相關 for two_side_bet_setting
        bet_chip_2 = (By.XPATH, "//*[@id='chip2']")
        bet_chip_50 = (By.XPATH, "//*[@id='chip50']")
        bet_chip_100 = (By.XPATH, "//*[@id='chip100']")
        bet_chip_500 = (By.XPATH, "//*[@id='chip500']")
        bet_chip_1000 = (By.XPATH, "//*[@id='chip1000']")
        # 訂單相關(訂單確認/訂單成立視窗欄位元件一致)
        button_payment_pro = (By.XPATH, "//button[@id='btn-bet']")
        button_payment_twoSide = (By.XPATH, "//button[@id='btn-pay_immediately']")
        order_info_all = (By.XPATH, "//tr/td")
        button_order_confirm = (By.XPATH, "//button[contains(@class,'betting')]")
        button_order_done = (By.XPATH, "//*[contains(@src,'ic_circle_ok')]/following::*[@type='submit']")
        button_tracing_order_done = (By.XPATH, "(//div[@class='footer']//button)[2]")
        # 追號
        bonus_odd = (By.XPATH, "//*[@disabled]//*[@class='bonus-odd']")  # 當前彩種獎金
        button_tracing = (By.XPATH, "//*[@id='btn-tracing_number']")  # 追號按鈕
        button_double_tracking = (By.XPATH, "//*[@class='tabMenu']/div[1]")  # 翻倍追號
        button_smart_tracking = (By.XPATH, "//*[@class='tabMenu']/div[2]")  # 智能追號
        button_add_tracing = (
            By.XPATH, "//*[@mode='BUTTON_MODE_DEFAULT']//*[contains(@class,'icon-ic_add')]")  # 生成追號方案
        button_end_of_winning = (By.XPATH, "//*[@for='StopTrace']")  # 中奖后停止追号
        tracing_bet_button = (By.XPATH, "//div[@class='right']//button[@type='button']")  # 投注
        input_tracing_number = (By.XPATH, "//*[contains(@class,'head inputSmall')]//*[@type='text']")  # 追号期数
        input_profitability = (By.XPATH, "//*[contains(@for,'profitability')]//*[@type='text']")  # 预期盈利
        input_multiples_of_tracing = (By.XPATH, "(//div[@class='chase_td times']//input[@value])")  # 輸入倍数
        tracing_bet_info_of_current = (By.XPATH, "//*[contains(@class,'current')]")  # 当前投入
        tracing_bet_info_of_accumulation = (By.XPATH, "//*[contains(@class,'accumulation')]")  # 累积投入
        tracing_bet_info_of_win_profit = (By.XPATH, "//*[contains(@class,'winProfit')]")  # 盈利
        tracing_bet_info_of_profitability = (By.XPATH, "//*[contains(@class,'profitability')]")  # 盈利率
        shop_car_button = (By.XPATH, "//button[@id='tab-bet_basket']")  # 購彩籃
        shop_car_active_button = (By.XPATH, "//button[@id='tab-bet_basket'][@class='active']")  # 購彩籃啟用
        del_bet_buttons = (By.XPATH, "//button[@class='clean-bet-list']")  # 清空購彩籃
        random_bet_buttons = (By.XPATH, "//*[@id='btn-random_bet']")  # 機選一注


if __name__ == '__main__':
    pass
