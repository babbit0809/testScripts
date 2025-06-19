from selenium.webdriver.common.by import By
from config.SetUIConfig import Platform, Target
from test_UI.common import BasePage


class Xpath(BasePage.BasePage):  # 六合彩沒有分官方盤/雙面盤(亦無常規/趣味之分)
    # Locators
    if Platform == 'Android' and Target == 'app':
        # 官方盤玩法
        pro_game_name_All = (By.XPATH, "//*[@id='mainGameRecyclerView']/*")
        pro_subGame_name_All = (By.XPATH, "//*[@id='subGameRecyclerView']/*")
        # 投注相關 for 盤面需要swipe時, end_location定位用
        history_button = (By.ID, "historyToggleBtn")
        # 投注相關 for 官方盤 特碼/正碼/正特/連碼/不中 (部分玩法需搭配下方"betting_squares")
        betting_numbers = (By.XPATH, "(//*[@id='recyclerView']/*/*/*[@class='android.view.ViewGroup'])")
        button_row5 = (By.XPATH, "(//*[@id='recyclerView']/*/*/*[@class='android.view.ViewGroup'])[21]")  # 定位用
        # 投注相關 for 官方盤 正碼1-6/1-6龍虎
        betting_squares = (By.ID, "squareContainer")
        text_dragon = (By.XPATH, "//*[@class='android.widget.RelativeLayout'][7]/*[@id='squareContainer']")  # 正碼 定位用
        title_tiger = (By.XPATH, "//*[@id='recyclerView']/*[@class='android.widget.RelativeLayout'][17]"
                                 "//*[@id='titleTextView']")  # 1-6龍虎 定位用
        # 投注相關 for 官方盤 半波/尾數/一肖/特肖/六肖/連肖/連尾
        betting_sets = (By.XPATH, "(//*[@id='recyclerView']/*[./*])")
        button_row4 = (By.XPATH, "(//*[@id='recyclerView']/*[./*])[4]")  # 半波/尾數 定位用
        button_row6 = (By.XPATH, "(//*[@id='recyclerView']/*[./*])[6]")  # 一肖/特肖/六肖/連肖/連尾 定位用

    elif Platform == 'Android' and Target == 'h5':
        # 官方盤玩法
        pro_game_name_All = (By.XPATH, "//*[@nodeName='SECTION']/*[1]/*/*/*/*[contains(@class, 'select-button')]")
        pro_subGame_name_All = (By.XPATH, "//*[@nodeName='SECTION']/*[2]/*/*/*/*[contains(@class, 'select-button')]")
        button_pro_game_confirm = (By.XPATH, "//*[@nodeName='MAIN']/*/*[@nodeName='DIV']/*[@nodeName='BUTTON']")
        # 投注相關 for 盤面需要swipe時, end_location定位用
        history_button = (By.XPATH, "//*[@nodeName='BUTTON' and ./parent::*[@nodeName='SECTION']]")
        # 投注相關 for 官方盤 特碼/正碼/正碼1-6/正特
        betting_numbers0x = (By.XPATH, "//*[contains(@data-testid,'mark6Button') and starts-with(@value,'0')]")
        betting_numbers1x = (By.XPATH, "//*[contains(@data-testid,'mark6Button') and starts-with(@value,'1')]")
        betting_numbers2x = (By.XPATH, "//*[contains(@data-testid,'mark6Button') and starts-with(@value,'2')]")
        betting_numbers3x = (By.XPATH, "//*[contains(@data-testid,'mark6Button') and starts-with(@value,'3')]")
        betting_numbers4x = (By.XPATH, "//*[contains(@data-testid,'mark6Button') and starts-with(@value,'4')]")
        betting_numbers_combo = (By.XPATH, "//*[@nodeName='DIV']/*[contains(@data-testid,'1-49Button')]")
        button_16 = (By.XPATH, "//*[@nodeName='DIV' and ./*[@text='16']]")  # 定位用
        button_36 = (By.XPATH, "//*[@nodeName='DIV' and ./*[@text='36']]")  # 定位用
        button_46 = (By.XPATH, "//*[@nodeName='DIV' and ./*[@text='46']]")  # 定位用
        betting_squares_set = (By.XPATH, "//*[@nodeName='DIV']/*[contains(@data-testid,'optionsButton')]")
        betting_squares_color = (By.XPATH, "//*[@nodeName='DIV']/*[contains(@data-testid,'betButton')]")
        # 投注相關 for 官方盤 半波
        betting_halfBall = "(//*[@data-testid='mark6HalfBallButton'])"
        # 投注相關 for 官方盤 尾數
        betting_tailNo = "(//*[@data-testid='mark6TailNoButton'])"
        # 投注相關 for 官方盤 一肖/特肖
        betting_zodiac = "(//*[@data-testid='mark6ZodiacButton'])"
        # 投注相關 for 官方盤 1-6龍虎
        betting_dt16_dragon = (By.XPATH, "//*[@nodeName='SECTION']/*[2]/*/*[2]//*[@nodeName='BUTTON']")
        betting_dt16_tiger = (By.XPATH, "//*[@nodeName='SECTION']/*[2]/*/*[4]//*[@nodeName='BUTTON']")
        title_tiger = (By.XPATH, "//*[@nodeName='SECTION']/*[2]/*/*[3]")  # 定位用

    elif Platform == 'iOS' and Target == 'app':
        # 官方盤玩法
        pro_game_name_All = (By.XPATH, "(//*[@class='UIACollectionView'])[1]/*[@knownSuperClass='UICollectionViewCell']")
        pro_subGame_name_All = (By.XPATH, "(//*[@class='UIACollectionView'])[2]/*[@knownSuperClass='UICollectionViewCell']")
        # 投注相關 for 盤面需要swipe時, end_location定位用
        history_button = (By.XPATH, "//*[@knownSuperClass='UINavigationTransitionView']/*/*/*[@class='UIAButton'][2]")
        # 投注相關 for 官方盤 特碼/正碼/正碼1-6/正特
        betting_numbers0x = (By.XPATH, "//*[@class='UIAScrollView']//*[contains(@id,'UILabel') and "
                                       "starts-with(@text,'0') and not (contains(@text, '-')) and not (contains(@text, '.'))]")
        betting_numbers1x = (By.XPATH, "//*[@class='UIAScrollView']//*[contains(@id,'UILabel') and "
                                       "starts-with(@text,'1') and not (contains(@text, '-')) and not (contains(@text, '.'))]")
        betting_numbers2x = (By.XPATH, "//*[@class='UIAScrollView']//*[contains(@id,'UILabel') and "
                                       "starts-with(@text,'2') and not (contains(@text, '-')) and not (contains(@text, '.'))]")
        betting_numbers3x = (By.XPATH, "//*[@class='UIAScrollView']//*[contains(@id,'UILabel') and "
                                       "starts-with(@text,'3') and not (contains(@text, '-')) and not (contains(@text, '.'))]")
        betting_numbers4x = (By.XPATH, "//*[@class='UIAScrollView']//*[contains(@id,'UILabel') and "
                                       "starts-with(@text,'4') and not (contains(@text, '-')) and not (contains(@text, '.'))]")
        button_16 = (By.XPATH, "//*[@accessibilityLabel='id_UILabel_' and @text='16']")  # 定位用
        button_36 = (By.XPATH, "//*[@accessibilityLabel='id_UILabel_' and @text='36']")  # 定位用
        button_46 = (By.XPATH, "//*[@accessibilityLabel='id_UILabel_' and @text='46']")  # 定位用
        betting_squares = (By.XPATH, "//*[contains(@id, 'id_UIButton__')]")
        text_dragon = (By.XPATH, "(//*[contains(@id, 'id_UIButton__')])[7]")  # 正碼 定位用
        # 投注相關 for 官方盤 半波
        betting_halfBall = (By.XPATH, "//*[@knownSuperClass='UIScrollView']/*/*/*/*")
        button_red_even = (By.XPATH, "//*[@knownSuperClass='UIScrollView']/*/*/*/*[4]")  # 定位用
        button_blue_small = (By.XPATH, "//*[@knownSuperClass='UIScrollView']/*/*/*/*[8]")  # 定位用
        button_blue_total_even = (By.XPATH, "//*[@knownSuperClass='UIScrollView']/*/*/*/*[12]")  # 定位用
        button_green_even = (By.XPATH, "//*[@knownSuperClass='UIScrollView']/*/*/*/*[16]")  # 定位用
        # 投注相關 for 官方盤 尾數
        betting_tailNo = (By.XPATH, "//*[@knownSuperClass='UIScrollView']/*/*/*/*")
        button_tail4 = (By.XPATH, "//*[@knownSuperClass='UIScrollView']/*/*/*/*[5]")  # 定位用
        # 投注相關 for 官方盤 一肖/特肖
        betting_zodiac = (By.XPATH, "//*[@knownSuperClass='UIScrollView']/*/*/*/*")
        button_rabbit = (By.XPATH, "//*[@knownSuperClass='UIScrollView']/*/*/*/*[4]")  # 定位用
        button_sheep = (By.XPATH, "//*[@knownSuperClass='UIScrollView']/*/*/*/*[8]")  # 定位用
        # 投注相關 for 官方盤 1-6龍虎
        betting_dt16_dragon = (By.XPATH, "//*[@knownSuperClass='UIScrollView']/*/*/*[1]/*/*/*[2]")
        betting_dt16_tiger = (By.XPATH, "//*[@knownSuperClass='UIScrollView']/*/*/*[2]/*/*/*[2]")
        title_tiger = (By.XPATH, "//*[@knownSuperClass='UIScrollView']/*/*/*[2]/*[1]")  # 定位用

    elif Platform == 'iOS' and Target == 'h5':
        pass

    elif Target == 'web':
        # 官方盤玩法
        normal_specialNo = (By.XPATH, "//*[@id='game-nav_specialNo']")  # 特码
        normal_mainNo = (By.XPATH, "//*[@id='game-nav_mainNo']")  # 正码
        normal_main1to6 = (By.XPATH, "//*[@id='game-nav_main1to6']")  # 正码1-6
        normal_main1to6_main1st = (By.XPATH, "//*[@id='subgame-nav_main1st']")  # 正码1
        normal_main1to6_main2nd = (By.XPATH, "//*[@id='subgame-nav_main2nd']")  # 正码2
        normal_main1to6_main3rd = (By.XPATH, "//*[@id='subgame-nav_main3th']")  # 正码3
        normal_main1to6_main4th = (By.XPATH, "//*[@id='subgame-nav_main4th']")  # 正码4
        normal_main1to6_main5th = (By.XPATH, "//*[@id='subgame-nav_main5th']")  # 正码5
        normal_main1to6_main6th = (By.XPATH, "//*[@id='subgame-nav_main6th']")  # 正码6
        normal_mainSpecial = (By.XPATH, "//*[@id='game-nav_mainSpecial']")  # 正特
        normal_mainSpecial_main1Special = (By.XPATH, "//*[@id='subgame-nav_main1Special']")  # 正一特
        normal_mainSpecial_main2Special = (By.XPATH, "//*[@id='subgame-nav_main2Special']")  # 正二特
        normal_mainSpecial_main3Special = (By.XPATH, "//*[@id='subgame-nav_main3Special']")  # 正三特
        normal_mainSpecial_main4Special = (By.XPATH, "//*[@id='subgame-nav_main4Special']")  # 正四特
        normal_mainSpecial_main5Special = (By.XPATH, "//*[@id='subgame-nav_main5Special']")  # 正五特
        normal_mainSpecial_main6Special = (By.XPATH, "//*[@id='subgame-nav_main6Special']")  # 正六特
        normal_halfBall = (By.XPATH, "//*[@id='game-nav_halfBall']")  # 半波
        normal_tailNo = (By.XPATH, "//*[@id='game-nav_tailNo']")  # 尾数
        normal_zodiac1 = (By.XPATH, "//*[@id='game-nav_zodiac1']")  # 一肖
        normal_specialZodiac = (By.XPATH, "//*[@id='game-nav_specialZodiac']")  # 特肖

        # 投注相關 for 官方盤 特碼/正碼/正碼1-6/正特
        betting_numbers0x = (By.XPATH, "//button[starts-with(text(),'0')]")  # 六合彩_數字01~49，0開頭的數字
        betting_numbers1x = (By.XPATH, "//button[starts-with(text(),'1')]")  # 六合彩_數字01~49，1開頭的數字
        betting_numbers2x = (By.XPATH, "//button[starts-with(text(),'2')]")  # 六合彩_數字01~49，2開頭的數字
        betting_numbers3x = (By.XPATH, "//button[starts-with(text(),'3')]")  # 六合彩_數字01~49，3開頭的數字
        betting_numbers4x = (By.XPATH, "//button[starts-with(text(),'4')]")  # 六合彩_數字01~49，4開頭的數字
        betting_not_number = (By.XPATH, "//*[@class='not-number']")  # 投注相關 for 官方盤 特码 正码 正码1-6 正特 1-6龙虎 組合按鈕
        betting_numbers_combo = (By.XPATH, "//*[@nodeName='DIV']/*[contains(@data-testid,'1-49Button')]")
        button_16 = (By.XPATH, "//*[@nodeName='DIV' and ./*[@text='16']]")  # 定位用
        button_36 = (By.XPATH, "//*[@nodeName='DIV' and ./*[@text='36']]")  # 定位用
        button_46 = (By.XPATH, "//*[@nodeName='DIV' and ./*[@text='46']]")  # 定位用
        betting_squares_set = (By.XPATH, "//*[@nodeName='DIV']/*[contains(@data-testid,'optionsButton')]")
        betting_squares_color = (By.XPATH, "//*[@nodeName='DIV']/*[contains(@data-testid,'betButton')]")
        # 投注相關 for 官方盤 半波
        betting_sets = (By.XPATH, "//*[@class='left']")

        # 投注相關 for 官方盤 尾數 一肖/特肖
        betting_tailNo_zodiac1_specialZodiac_betting_sets = (By.XPATH, "//*[@class='nums']")

        # 投注相關 for 官方盤 一肖/特肖
        betting_zodiac1_set1 = (By.XPATH, "//*[text()='鼠' or text()='牛' or text()='虎' or text()='兔']")
        betting_zodiac1_set2 = (By.XPATH, "//*[text()='龙' or text()='蛇' or text()='马' or text()='羊']")
        betting_zodiac1_set3 = (By.XPATH, "//*[text()='猴' or text()='鸡' or text()='狗' or text()='猪']")
        button_rabbit = (By.XPATH, "//*[text()='兔']")  # 定位用
        button_sheep = (By.XPATH, "//*[text()='羊']")  # 定位用
        normal_dt16 = (By.XPATH, "//*[@id='game-nav_dt16']")  # 1-6龙虎


if __name__ == '__main__':
    pass
