import time

from selenium.webdriver.common.by import By
from config.SetUIConfig import Platform, Target, Project
from test_UI.common import BasePage
from utils.DataLoader import JsonLoader


class GamePage(BasePage.BasePage):  # TODO: 加入新的澳洲彩種(codeName需存暫存檔方便之後判斷)
    # Locators
    if Platform == 'Android' and Target == 'app':
        # For 星輝
        game_option_home = (By.XPATH, "//*[@id='gameTabLayout']//*[@class='android.widget.TextView'][1]")
        first_title = (By.XPATH, "//*[@id='epoxy_recycler_view']/*[@class='android.widget.LinearLayout'][1]")
        next_title = (By.XPATH, "//*[@id='epoxy_recycler_view']/*[@class='android.widget.LinearLayout'][2]")
        gameNameList_All = (By.XPATH, "//*[@class='android.view.ViewGroup']//*[@class='android.widget.TextView']")
        # For 越南(快3/PK10在越南站順序有變)
        switch_to_gamepage = (By.XPATH, "(//*[@id='game_name'])[1]")
        lottery_banner_Hot = (By.XPATH, "//*[@id='gameRecyclerView']/*[@class='android.widget.FrameLayout'][1]")
        lottery_banner_SSC = (By.XPATH, "//*[@id='gameRecyclerView']/*[@class='android.widget.FrameLayout'][2]")
        lottery_banner_11x5 = (By.XPATH, "//*[@id='gameRecyclerView']/*[@class='android.widget.FrameLayout'][3]")
        lottery_banner_PK10 = (By.XPATH, "//*[@id='gameRecyclerView']/*[@class='android.widget.FrameLayout'][4]")
        lottery_banner_Quick3 = (By.XPATH, "//*[@id='gameRecyclerView']/*[@class='android.widget.FrameLayout'][5]")
        gameNameBanner_All = (By.ID, "layoutGame")

    elif Platform == 'Android' and Target == 'h5':
        banner_carousell = (By.XPATH, "//*[contains(@class,'slick-list')]")
        # For 星輝
        game_option_home = (By.XPATH, "//*[@nodeName='UL']/*[@id='tab_0']")
        title_SSC = (By.XPATH, "//*[@nodeName='SECTION']/*[@nodeName='SPAN'][1]")
        title_11x5 = (By.XPATH, "//*[@nodeName='SECTION']/*[@nodeName='SPAN'][2]")
        title_Quick3 = (By.XPATH, "//*[@nodeName='SECTION']/*[@nodeName='SPAN'][3]")
        gameNameList_SSC = (By.XPATH, "//*[@nodeName='SECTION'][1]/*/*[contains(@class, 'GridItem')]")
        gameNameList_11x5 = (By.XPATH, "//*[@nodeName='SECTION'][2]/*/*[contains(@class, 'GridItem')]")
        gameNameList_Quick3 = (By.XPATH, "//*[@nodeName='SECTION'][3]/*/*[contains(@class, 'GridItem')]")
        gameNameList_PK10 = (By.XPATH, "//*[@nodeName='SECTION'][4]/*/*[contains(@class, 'GridItem')]")
        gameNameList_MarkSix = (By.XPATH, "//*[@nodeName='SECTION'][5]/*/*[contains(@class, 'GridItem')]")
        # For 越南(快3/PK10在越南站順序有變)
        switch_to_gamepage = (By.XPATH, "(//*[@nodeName='SECTION'])[3]/*[1]")
        game_type_nav = (By.XPATH, "//*[@class='quickLink']/following::div/UL")
        lottery_banner_Hot = (By.XPATH, "//*[contains(@class,'PanelSummary')][@id='panel1d-header']")
        lottery_banner_SSC = (By.XPATH, "//*[contains(@class,'PanelSummary')][@id='panel2d-header']")
        lottery_banner_11x5 = (By.XPATH, "//*[contains(@class,'PanelSummary')][@id='panel3d-header']")
        lottery_banner_PK10 = (By.XPATH, "//*[contains(@class,'PanelSummary')][@id='panel4d-header']")
        lottery_banner_Quick3 = (By.XPATH, "//*[contains(@class,'PanelSummary')][@id='panel5d-header']")
        gameNameBanner_Hot = (By.XPATH, "(//*[@nodeName='SECTION'])[3]//*[contains(@class,'MuiGrid-item')]")
        gameNameBanner_SSC = "(//*[@nodeName='SECTION'])[4]//*[contains(@class,'MuiGrid-item')]"
        gameNameBanner_11x5 = "(//*[@nodeName='SECTION'])[5]//*[contains(@class,'MuiGrid-item')]"
        gameNameBanner_PK10 = "(//*[@nodeName='SECTION'])[6]//*[contains(@class,'MuiGrid-item')]"
        gameNameBanner_Quick3 = "(//*[@nodeName='SECTION'])[7]//*[contains(@class,'MuiGrid-item')]"
        # For 第三方
        thirdParty_Nav = (By.XPATH, "//*[contains(@class,'items-start')]/div[1]//*[contains(@class,'LobbyNav')]")
        thirdParty_cmd = (By.XPATH, "//*[contains(@class,'items-start')]/div[2]//*[@id='Sport']")
        thirdParty_Sport = (By.XPATH, "//*[contains(@class,'items-start')]/div[2]//*[@id='Sport']/following::*[contains(@class,'sc-')]")
        thirdParty_ok368 = (By.XPATH, "//*[contains(@class,'items-start')]/div[2]//*[@id='Lottery']")
        thirdParty_Lottery = (By.XPATH, "//*[contains(@class,'items-start')]/div[2]//*[@id='Lottery']/following::*[contains(@class,'sc-')]")
        thirdParty_agCasino = (By.XPATH, "//*[contains(@class,'items-start')]/div[2]//*[@id='LiveDealer']")
        thirdParty_wmCasino = (By.XPATH, "//*[contains(@class,'items-start')]/div[2]//*[@id='LiveDealer']")
        thirdParty_LiveDealer = (By.XPATH, "//*[contains(@class,'items-start')]/div[2]//*[@id='LiveDealer']/following::*[contains(@class,'sc-')]")
        thirdParty_CockFight = (By.XPATH, "//*[contains(@class,'items-start')]/div[2]//*[@id='CockFight']")
        thirdParty_kyPoker = (By.XPATH, "//*[contains(@class,'items-start')]/div[2]//*[@id='Poker']")
        thirdParty_v8Poker = (By.XPATH, "//*[contains(@class,'items-start')]/div[2]//*[@id='Poker']")
        thirdParty_Poker = (By.XPATH, "//*[contains(@class,'items-start')]/div[2]//*[@id='Poker']/following::*[contains(@class,'sc-')]")
        thirdParty_mgSlot = (By.XPATH, "//*[contains(@class,'items-start')]/div[2]//*[@id='Slot']")
        thirdParty_cq9Slot = (By.XPATH, "//*[contains(@class,'items-start')]/div[2]//*[@id='Slot']")
        thirdParty_Slot = (By.XPATH, "//*[contains(@class,'items-start')]/div[2]//*[@id='Slot']/following::*[contains(@class,'sc-')]")
        thirdParty_bgFishingMaster = (By.XPATH, "//*[contains(@class,'items-start')]/div[2]//*[@id='Fishing']")
        thirdParty_Fishing = (By.XPATH, "//*[contains(@class,'items-start')]/div[2]//*[@id='Fishing']/following::*[contains(@class,'sc-')]")

    elif Platform == 'iOS' and Target == 'app':
        # For 星輝
        game_option_home = (By.XPATH, "//*[@class='UIAScrollView']/*/*[@class='UIAButton'][1]")
        first_title = (By.XPATH, "//*[@class='UIACollectionView']/*[@knownSuperClass='UICollectionReusableView'][1]")
        next_title = (By.XPATH, "//*[@class='UIACollectionView']/*[@knownSuperClass='UICollectionReusableView'][2]")
        gameNameList_SSC11x5 = (By.XPATH, "//*[@knownSuperClass='UICollectionReusableView'][1]/following::*//*[@id='id_UILabel_']")
        gameNameList_Quick3 = (By.XPATH, "//*[@knownSuperClass='UICollectionReusableView'][1]/following::*//*[@id='id_UILabel_']")
        gameNameList_PK10 = (By.XPATH, "//*[@knownSuperClass='UICollectionReusableView'][2]/following::*//*[@id='id_UILabel_']")
        gameNameList_MarkSix = (By.XPATH, "//*[@knownSuperClass='UICollectionReusableView'][3]/following::*//*[@id='id_UILabel_']")
        # For 越南(快3/PK10在越南站順序有變)
        switch_to_gamepage = (By.XPATH, "(//*[@XCElementType='XCUIElementTypeCell']//*[@accessibilityLabel='id_UILabel_'])[1]")
        lottery_banner_Hot = (By.XPATH, "//*[@XCElementType='XCUIElementTypeTable']/*[2]/*[@label='Game Hot']")
        lottery_banner_SSC = (By.XPATH, "//*[@XCElementType='XCUIElementTypeTable']/*[3]/*[@class='UIAButton'][2]")
        lottery_banner_11x5 = (By.XPATH, "//*[@XCElementType='XCUIElementTypeTable']/*[4]/*[@class='UIAButton'][2]")
        lottery_banner_PK10 = (By.XPATH, "//*[@XCElementType='XCUIElementTypeTable']/*[5]/*[@class='UIAButton'][2]")
        lottery_banner_Quick3 = (By.XPATH, "//*[@XCElementType='XCUIElementTypeTable']/*[6]/*[@class='UIAButton'][2]")
        gameNameBanner_All = (By.XPATH, "//*[@class='UIATable']//*[@knownSuperClass='UIStackView']/*//*[@knownSuperClass='UIButton']")
        # For 第三方
        thirdParty_Nav_vt = (By.XPATH, "//*[@class='UIAScrollView']//*[@class='UIAButton']")
        thirdParty_Entrance_vt = (By.XPATH, "//*[@class='UIATable']//*[@XCElementType='XCUIElementTypeCell']")

    elif Platform == 'iOS' and Target == 'h5':
        pass

    elif Target == 'web':
        """for VT"""  # SSC (因應命名規則需要)
        switch_to_gamepage = (By.XPATH, "(//*[contains(@src,'menu')])[1]")
        """時時彩"""  # SSC (因應命名規則需要)
        game_tjc = (By.XPATH, "//*[contains(@href,'/game/tjc')]")  # 天津時時彩
        game_xjc = (By.XPATH, "//*[contains(@href,'/game/xjc')]")  # 新疆時時彩
        game_lottery1 = (By.XPATH, "(//*[contains(@href,'/game/lottery1')])[1]")  # 一分彩
        game_lottery2 = (By.XPATH, "//*[contains(@href,'/game/lottery2')]")  # 二分彩
        game_lottery5 = (By.XPATH, "//*[contains(@href,'/game/lottery5')]")  # 五分彩
        game_txffc = (By.XPATH, "//*[contains(@href,'/game/txffc')]")  # 騰訊分分彩
        game_btcffc = (By.XPATH, "//*[contains(@href,'/game/btcffc')]")  # 比特幣分分彩
        game_wxffc = (By.XPATH, "//*[contains(@href,'/game/wxffc')]")  # 微信分分彩
        game_jnd30s = (By.XPATH, "//*[contains(@href,'/game/jnd30s')]")  # 加拿大30秒
        game_tg60 = (By.XPATH, "//*[contains(@href,'/game/tg60')]")  # 泰國60秒
        game_cajc = (By.XPATH, "//*[contains(@href,'/game/cajc')]")  # 加拿大時時彩
        game_skjc = (By.XPATH, "//*[contains(@href,'/game/skjc')]")  # 斯洛伐克時時彩

        """11選5"""  # 11x5 (因應命名規則需要)
        game_sd11x5 = (By.XPATH, "//*[contains(@href,'/game/sd11x5')]")  # 山東11選5
        game_jx11x5 = (By.XPATH, "//*[contains(@href,'/game/jx11x5')]")  # 江西11選5
        game_gd11x5 = (By.XPATH, "//*[contains(@href,'/game/gd11x5')]")  # 廣東11選5
        game_js11x5 = (By.XPATH, "//*[contains(@href,'/game/js11x5')]")  # 江蘇11選5
        game_tw11x5 = (By.XPATH, "//*[contains(@href,'/game/tw11x5')]")  # 台灣11選5
        game_ca11x5 = (By.XPATH, "//*[contains(@href,'/game/ca11x5')]")  # 加拿大11選5
        game_sk11x5 = (By.XPATH, "//*[contains(@href,'/game/sk11x5')]")  # 斯洛伐克11選5

        """快3"""  # Quick3 (因應命名規則需要)
        game_jsk3 = (By.XPATH, "//*[contains(@href,'/game/jsk3')]")  # 江蘇快3
        game_hubk3 = (By.XPATH, "//*[contains(@href,'/game/hubk3')]")  # 湖北快3
        game_hquick3 = (By.XPATH, "//*[contains(@href,'/game/hquick3')]")  # 歡樂快3
        game_quick3 = (By.XPATH, "//*[contains(@href,'/game/quick3')]")  # 一分快3
        game_cak3 = (By.XPATH, "//*[contains(@href,'/game/cak3')]")  # 加拿大快3
        game_skk3 = (By.XPATH, "//*[contains(@href,'/game/skk3')]")  # 斯洛伐克快3

        """PK10"""  # PK10遊戲名與系列標題名重複, 需獨立判別
        game_f1racing = (By.XPATH, "//*[contains(@href,'/game/f1racing')]")  # F1賽車
        game_f2racing = (By.XPATH, "//*[contains(@href,'/game/f2racing')]")  # F2賽車
        game_f3racing = (By.XPATH, "//*[contains(@href,'/game/f3racing')]")  # F3賽車
        game_xyft = (By.XPATH, "//*[contains(@href,'/game/xyft')]")  # 幸運飛艇
        game_caracing = (By.XPATH, "//*[contains(@href,'/game/caracing')]")  # 加拿大賽車
        game_skracing = (By.XPATH, "//*[contains(@href,'/game/skracing')]")  # 加拿大賽車

        """六合彩"""  # MarkSix (因應命名規則需要)
        game_mark6 = (By.XPATH, "//*[contains(@href,'/game/mark6')]")  # 香港六合彩
        game_fmark6 = (By.XPATH, "//*[contains(@href,'/game/fmark6')]")  # 極速六合彩
        game_mamark6 = (By.XPATH, "//*[contains(@href,'/game/mamark6')]")  # 澳门六合彩

    # Actions
    def switch_game(self, lottery, codeName):
        # 判斷game name
        if Project in ['vt']:
            localization = 'VN'
        else:
            localization = 'CN'
        game_name = JsonLoader('GameNameList').get_loc(localization, lottery, codeName)
        # 切換lottery game
        game = None
        if Project in ['sta']:
            if Platform == 'Android' and Target == 'app':
                start_location = self.find_element(*self.first_title).location
                end_location = self.find_element(*self.game_option_home).location
                self.swipe(start_location, end_location, y2scale=1.2, duration=2500)
                # 時時彩
                if codeName in ['xjc', 'lottery1', 'lottery2', 'lottery5', 'txffc', 'btcffc',
                                'wxffc', 'jnd30s', 'tg60', 'twjc', 'cajc']:
                    sortOrder = {'xjc': 0, 'lottery1': 1, 'lottery2': 2, 'lottery5': 3, 'txffc': 4, 'btcffc': 5,
                                 'wxffc': 6, 'jnd30s': 7, 'tg60': 8, 'twjc': 9, 'cajc': 11}
                    sort = sortOrder[codeName]
                    gameNameList = self.find_elements(*self.gameNameList_All)
                    game = gameNameList[sort]
                else:
                    start_location = self.find_element(*self.next_title).location
                    end_location = self.find_element(*self.game_option_home).location
                    self.swipe(start_location, end_location, y2scale=1.2, duration=2500)
                    # 11選5
                    if codeName in ['sd11x5', 'jx11x5', 'gd11x5', 'js11x5', 'tw11x5', 'ca11x5']:
                        sortOrder = {'sd11x5': 0, 'jx11x5': 1, 'gd11x5': 2, 'js11x5': 3, 'tw11x5': 4, 'ca11x5': 6}
                        sort = sortOrder[codeName]
                        gameNameList = self.find_elements(*self.gameNameList_All)
                        game = gameNameList[sort]
                    else:
                        start_location = self.find_element(*self.next_title).location
                        end_location = self.find_element(*self.game_option_home).location
                        self.swipe(start_location, end_location, y2scale=1.2, duration=2500)
                        # 快3/PK10/六合彩
                        if codeName in ['jsk3', 'hubk3', 'hquick3', 'quick3', 'twk3', 'cak3',
                                        'f1racing', 'f2racing', 'f3racing', 'xyft', 'twracing',
                                        'caracing', 'mark6', 'fmark6']:
                            sortOrder = {'jsk3': 0, 'hubk3': 1, 'hquick3': 2, 'quick3': 3, 'twk3': 4, 'cak3': 6,
                                         'f1racing': 7, 'f2racing': 8, 'f3racing': 9, 'xyft': 10, 'twracing': 11,
                                         'caracing': 13, 'mark6': 14, 'fmark6': 15}
                            sort = sortOrder[codeName]
                            gameNameList = self.find_elements(*self.gameNameList_All)
                            game = gameNameList[sort]

            elif Platform == 'iOS' and Target == 'app':
                start_location = self.find_element(*self.first_title).location
                end_location = self.find_element(*self.game_option_home).location
                self.swipe(start_location, end_location, y2scale=1.2, duration=2500)
                # 時時彩
                if codeName in ['xjc', 'lottery1', 'lottery2', 'lottery5', 'txffc', 'btcffc',
                                'wxffc', 'jnd30s', 'tg60', 'twjc', 'cajc']:
                    sortOrder = {'xjc': 0, 'lottery1': 1, 'lottery2': 2, 'lottery5': 3, 'txffc': 4, 'btcffc': 5,
                                 'wxffc': 6, 'jnd30s': 7, 'tg60': 8, 'twjc': 9, 'cajc': 11}
                    sort = sortOrder[codeName]
                    gameNameList_SSC11x5 = self.find_elements(*self.gameNameList_SSC11x5)
                    game = gameNameList_SSC11x5[sort]
                else:
                    start_location = self.find_element(*self.next_title).location
                    end_location = self.find_element(*self.game_option_home).location
                    self.swipe(start_location, end_location, y2scale=1.2, duration=2500)
                    # 11選5
                    if codeName in ['sd11x5', 'jx11x5', 'gd11x5', 'js11x5', 'tw11x5', 'ca11x5']:
                        sortOrder = {'sd11x5': 0, 'jx11x5': 1, 'gd11x5': 2, 'js11x5': 3, 'tw11x5': 4, 'ca11x5': 6}
                        sort = sortOrder[codeName]
                        gameNameList_SSC11x5 = self.find_elements(*self.gameNameList_SSC11x5)
                        game = gameNameList_SSC11x5[sort]
                    else:
                        start_location = self.find_element(*self.next_title).location
                        end_location = self.find_element(*self.game_option_home).location
                        self.swipe(start_location, end_location, y2scale=1.2, duration=2500)
                        # 快3
                        if codeName in ['jsk3', 'hubk3', 'hquick3', 'quick3', 'twk3', 'cak3']:
                            sortOrder = {'jsk3': 0, 'hubk3': 1, 'hquick3': 2, 'quick3': 3, 'twk3': 4, 'cak3': 6}
                            sort = sortOrder[codeName]
                            gameNameList_Quick3 = self.find_elements(*self.gameNameList_Quick3)
                            game = gameNameList_Quick3[sort]
                        # PK10
                        elif codeName in ['f1racing', 'f2racing', 'f3racing', 'xyft', 'twracing', 'caracing']:
                            sortOrder = {'f1racing': 0, 'f2racing': 1, 'f3racing': 2, 'xyft': 3, 'twracing': 4, 'caracing': 6}
                            sort = sortOrder[codeName]
                            gameNameList_PK10 = self.find_elements(*self.gameNameList_PK10)
                            game = gameNameList_PK10[sort]
                        # 六合彩
                        elif codeName in ['mark6', 'fmark6']:
                            sortOrder = {'mark6': 0, 'fmark6': 1}
                            sort = sortOrder[codeName]
                            gameNameList_MarkSix = self.find_elements(*self.gameNameList_MarkSix)
                            game = gameNameList_MarkSix[sort]

            elif Target == 'h5':
                if lottery in ['Sport', 'LiveDealer', 'Poker', 'Slot', 'Fishing']:
                    sortOrder = {'Sport': 0, 'LiveDealer': 1, 'Poker': 2, 'Slot': 3, 'Fishing': 4}
                    sort = sortOrder[lottery]
                    banner_carousell = self.find_element(*self.banner_carousell)
                    nav_game_type = self.find_elements(*self.thirdParty_Nav)
                    # 先點一次nav bar第一個選項讓頁面上移才能看到所有nav bar
                    start_location = nav_game_type[0].location
                    end_location = banner_carousell.location
                    self.swipe(start_location, end_location, y1scale=1, y2scale=1)
                    time.sleep(3)
                    game_type = nav_game_type[sort]
                    game_type.click()
                    time.sleep(3)

                # 體育
                if codeName in ['cmd']:
                    game = self.find_element(*self.thirdParty_cmd)
                elif codeName in ['saba', 'imSport', 'imEsport', 'leihuo', 'obSport']:
                    sortOrder = {'saba': 0, 'imSport': 1, 'imEsport': 2, 'leihuo': 3, 'obSport': 4}
                    sort = sortOrder[codeName]
                    gameNameList_Sport = self.find_elements(*self.thirdParty_Sport)
                    game = gameNameList_Sport[sort]

                # 真人
                if codeName in ['agCasino']:
                    game = self.find_element(*self.thirdParty_agCasino)
                elif codeName in ['bgCasino', 'dgCasino', 'obCasino']:
                    sortOrder = {'bgCasino': 0, 'dgCasino': 1, 'obCasino': 2}
                    sort = sortOrder[codeName]
                    gameNameList_LiveDealer = self.find_elements(*self.thirdParty_LiveDealer)
                    game = gameNameList_LiveDealer[sort]

                # 棋牌
                if codeName in ['kyPoker']:
                    game = self.find_element(*self.thirdParty_kyPoker)
                elif codeName in ['blPoker', 'imPoker', 'leg']:
                    sortOrder = {'blPoker': 0, 'imPoker': 1, 'leg': 2}
                    sort = sortOrder[codeName]
                    gameNameList_Poker = self.find_elements(*self.thirdParty_Poker)
                    game = gameNameList_Poker[sort]

                # 電子
                if codeName in ['mgSlot']:
                    game = self.find_element(*self.thirdParty_mgSlot)
                elif codeName in ['agSlot', 'bgSlot']:
                    sortOrder = {'agSlot': 0, 'bgSlot': 1}
                    sort = sortOrder[codeName]
                    gameNameList_Slot = self.find_elements(*self.thirdParty_Slot)
                    game = gameNameList_Slot[sort]
                # 捕魚
                if codeName in ['bgFishingMaster']:
                    game = self.find_element(*self.thirdParty_bgFishingMaster)
                elif codeName in ['bgFishing', 'agFishing']:
                    sortOrder = {'bgFishing': 0, 'agFishing': 1}
                    sort = sortOrder[codeName]
                    gameNameList_Fishing = self.find_elements(*self.thirdParty_Fishing)
                    game = gameNameList_Fishing[sort]

            elif Target == 'web':
                # 時時彩
                if codeName == 'tjc':
                    game = self.find_element(*self.game_tjc)
                elif codeName == 'xjc':
                    game = self.find_element(*self.game_xjc)
                elif codeName == 'lottery1':
                    game = self.find_element(*self.game_lottery1)
                elif codeName == 'lottery2':
                    game = self.find_element(*self.game_lottery2)
                elif codeName == 'lottery5':
                    game = self.find_element(*self.game_lottery5)
                elif codeName == 'txffc':
                    game = self.find_element(*self.game_txffc)
                elif codeName == 'btcffc':
                    game = self.find_element(*self.game_btcffc)
                elif codeName == 'wxffc':
                    game = self.find_element(*self.game_wxffc)
                elif codeName == 'jnd30s':
                    game = self.find_element(*self.game_jnd30s)
                elif codeName == 'tg60':
                    game = self.find_element(*self.game_tg60)
                elif codeName == 'cajc':
                    game = self.find_element(*self.game_cajc)
                elif codeName == 'skjc':
                    game = self.find_element(*self.game_skjc)

                # 11選5
                elif codeName == 'sd11x5':
                    game = self.find_element(*self.game_sd11x5)
                elif codeName == 'jx11x5':
                    game = self.find_element(*self.game_jx11x5)
                elif codeName == 'gd11x5':
                    game = self.find_element(*self.game_gd11x5)
                elif codeName == 'js11x5':
                    game = self.find_element(*self.game_js11x5)
                elif codeName == 'tw11x5':
                    game = self.find_element(*self.game_tw11x5)
                elif codeName == 'ca11x5':
                    game = self.find_element(*self.game_ca11x5)
                elif codeName == 'sk11x5':
                    game = self.find_element(*self.game_sk11x5)

                # 快3
                elif codeName == 'jsk3':
                    game = self.find_element(*self.game_jsk3)
                elif codeName == 'hubk3':
                    game = self.find_element(*self.game_hubk3)
                elif codeName == 'hquick3':
                    game = self.find_element(*self.game_hquick3)
                elif codeName == 'quick3':
                    game = self.find_element(*self.game_quick3)
                elif codeName == 'cak3':
                    game = self.find_element(*self.game_cak3)
                elif codeName == 'skk3':
                    game = self.find_element(*self.game_skk3)

                # PK10
                elif codeName == 'f1racing':
                    game = self.find_element(*self.game_f1racing)
                elif codeName == 'f2racing':
                    game = self.find_element(*self.game_f2racing)
                elif codeName == 'f3racing':
                    game = self.find_element(*self.game_f3racing)
                elif codeName == 'xyft':
                    game = self.find_element(*self.game_xyft)
                elif codeName == 'caracing':
                    game = self.find_element(*self.game_caracing)
                elif codeName == 'skracing':
                    game = self.find_element(*self.game_skracing)

                # 六合彩
                elif codeName == 'mark6':
                    game = self.find_element(*self.game_mark6)
                elif codeName == 'fmark6':
                    game = self.find_element(*self.game_fmark6)
                elif codeName == 'mamark6':
                    game = self.find_element(*self.game_mamark6)

        elif Project in ['vt']:
            if Target == 'web':
                switch_to_gamepage = self.find_element(*self.switch_to_gamepage)
                switch_to_gamepage.click()
            else:
                pass
            if Target == 'app':
                if lottery in ['LiveDealer', 'Sport', 'Lottery', 'CockFight', 'Poker', 'Slot', 'Fishing']:
                    sortOrder = {'LiveDealer': 0, 'Sport': 1, 'Lottery': 2, 'CockFight': 3, 'Poker': 4, 'Slot': 5, 'Fishing': 6}
                    sort = sortOrder[lottery]
                    nav_game_type = self.find_elements(*self.thirdParty_Nav_vt)
                    if sort > 5:
                        start_location = nav_game_type[5].location
                        end_location = nav_game_type[0].location
                        self.swipe(start_location, end_location, y1scale=1, y2scale=1)
                        time.sleep(3)
                        nav_game_type = self.find_elements(*self.thirdParty_Nav_vt)
                    game_type = nav_game_type[sort]
                    game_type.click()
                    time.sleep(3)

                    # 體育
                if codeName in ['cmd', 'sboSport', 'saba', 'imSport', 'imEsport', 'leihuo']:
                    sortOrder = {'cmd': 0, 'sboSport': 1, 'saba': 2, 'imSport': 3, 'imEsport': 4, 'leihuo': 5}
                    sort = sortOrder[codeName]
                    gameNameList_Sport = self.find_elements(*self.thirdParty_Entrance_vt)
                    if sort > 3:
                        start_location = gameNameList_Sport[2].location
                        end_location = gameNameList_Sport[0].location
                        self.swipe(start_location, end_location, y1scale=1, y2scale=1)
                        time.sleep(3)
                        gameNameList_Sport = self.find_elements(*self.thirdParty_Entrance_vt)
                    game = gameNameList_Sport[sort]

                    # 彩票
                if codeName in ['vt', 'ok368', 'vr', 'TCG']:
                    sortOrder = {'vt': 0, 'ok368': 1, 'vr': 2, 'TCG': 3}
                    sort = sortOrder[codeName]
                    gameNameList_Lottery = self.find_elements(*self.thirdParty_Entrance_vt)
                    game = gameNameList_Lottery[sort]

                    # 真人
                if codeName in ['wmCasino', 'sexyCasino', 'sboCasino', 'agCasino', 'bgCasino', 'dgCasino', 'bbinCasino']:
                    sortOrder = {'wmCasino': 0, 'sexyCasino': 1, 'sboCasino': 2, 'agCasino': 3, 'bgCasino': 4, 'dgCasino': 5, 'bbinCasino': 6}
                    sort = sortOrder[codeName]
                    gameNameList_LiveDealer = self.find_elements(*self.thirdParty_Entrance_vt)
                    if sort > 3:
                        start_location = gameNameList_LiveDealer[3].location
                        end_location = gameNameList_LiveDealer[0].location
                        self.swipe(start_location, end_location, y1scale=1, y2scale=1)
                        time.sleep(3)
                        gameNameList_LiveDealer = self.find_elements(*self.thirdParty_Entrance_vt)
                    game = gameNameList_LiveDealer[sort]

                    # 鬥雞
                if codeName in ['sv388']:
                    game = self.find_element(*self.thirdParty_Entrance_vt)

                    # 棋牌
                if codeName in ['v8']:
                    game = self.find_element(*self.thirdParty_Entrance_vt)

                    # 電子
                if codeName in ['agSlot', 'cgSlot', 'jlSlot', 'jdbSlot', 'mgSlot', 'sboSlot', 'cq9Slot', 'pgSlot', 'fcSlot']:
                    sortOrder = {'agSlot': 0, 'cgSlot': 1, 'jlSlot': 2, 'jdbSlot': 3, 'mgSlot': 4, 'sboSlot': 5, 'cq9Slot': 6, 'pgSlot': 7, 'fcSlot': 8}
                    sort = sortOrder[codeName]
                    gameNameList_Slot = self.find_elements(*self.thirdParty_Entrance_vt)
                    if sort > 3:
                        start_location = gameNameList_Slot[3].location
                        end_location = gameNameList_Slot[0].location
                        self.swipe(start_location, end_location)
                        time.sleep(3)
                        gameNameList_Slot = self.find_elements(*self.thirdParty_Entrance_vt)
                        if sort > 6:
                            start_location = gameNameList_Slot[5].location
                            end_location = gameNameList_Slot[4].location
                            self.swipe(start_location, end_location)
                            time.sleep(3)
                            gameNameList_Slot = self.find_elements(*self.thirdParty_Entrance_vt)
                    game = gameNameList_Slot[sort]

                    # 捕魚
                if codeName in ['bgFishingMaster']:
                    game = self.find_element(*self.thirdParty_bgFishingMaster)
                elif codeName in ['bgFishingMaster', 'bgFishing', 'cq9Fishing']:
                    sortOrder = {'bgFishingMaster': 0, 'bgFishing': 1, 'cq9Fishing': 2}
                    sort = sortOrder[codeName]
                    gameNameList_Fishing = self.find_elements(*self.thirdParty_Entrance_vt)
                    game = gameNameList_Fishing[sort]

            elif Target == 'h5':
                if lottery in ['Sport', 'Lottery', 'LiveDealer', 'CockFight', 'Poker', 'Slot', 'Fishing']:
                    sortOrder = {'Sport': 0, 'Lottery': 1, 'LiveDealer': 2, 'CockFight': 3, 'Poker': 4, 'Slot': 5, 'Fishing': 6}
                    sort = sortOrder[lottery]
                    banner_carousell = self.find_element(*self.banner_carousell)
                    nav_game_type = self.find_elements(*self.thirdParty_Nav)
                    # 先點一次nav bar第一個選項讓頁面上移才能看到所有nav bar
                    start_location = nav_game_type[0].location
                    end_location = banner_carousell.location
                    self.swipe(start_location, end_location, y1scale=1, y2scale=1)
                    time.sleep(3)
                    game_type = nav_game_type[sort]
                    game_type.click()
                    time.sleep(3)

                    # 體育
                if codeName in ['cmd']:
                    game = self.find_element(*self.thirdParty_cmd)
                elif codeName in ['sboSport', 'saba', 'imSport', 'imEsport', 'leihuo']:
                    sortOrder = {'sboSport': 0, 'saba': 1, 'imSport': 2, 'imEsport': 3, 'leihuo': 4}
                    sort = sortOrder[codeName]
                    gameNameList_Sport = self.find_elements(*self.thirdParty_Sport)
                    game = gameNameList_Sport[sort]

                    # 彩票
                if codeName in ['ok368']:
                    game = self.find_element(*self.thirdParty_ok368)
                elif codeName in ['vr']:
                    sortOrder = {'vr': 0}
                    sort = sortOrder[codeName]
                    gameNameList_Sport = self.find_elements(*self.thirdParty_Sport)
                    game = gameNameList_Sport[sort]

                    # 真人
                if codeName in ['wmCasino']:
                    game = self.find_element(*self.thirdParty_wmCasino)
                elif codeName in ['sexyCasino', 'sboCasino', 'agCasino', 'bgCasino', 'dgCasino', 'bbinCasino']:
                    sortOrder = {'sexyCasino': 0, 'sboCasino': 1, 'agCasino': 2, 'bgCasino': 3, 'dgCasino': 4, 'bbinCasino': 5}
                    sort = sortOrder[codeName]
                    gameNameList_LiveDealer = self.find_elements(*self.thirdParty_LiveDealer)
                    game = gameNameList_LiveDealer[sort]

                    # 鬥雞
                if codeName in ['sv388']:
                    game = self.find_element(*self.thirdParty_CockFight)

                    # 棋牌
                if codeName in ['v8']:
                    game = self.find_element(*self.thirdParty_v8Poker)

                    # 電子
                if codeName in ['cq9Slot']:
                    game = self.find_element(*self.thirdParty_cq9Slot)
                elif codeName in ['cgSlot', 'sboSlot', 'agSlot', 'mgSlot', 'jdbSlot', 'pgSlot']:
                    sortOrder = {'cgSlot': 0, 'sboSlot': 1, 'agSlot': 2, 'mgSlot': 3, 'jdbSlot': 4, 'pgSlot': 5}
                    sort = sortOrder[codeName]
                    gameNameList_Slot = self.find_elements(*self.thirdParty_Slot)
                    game = gameNameList_Slot[sort]

                    # 捕魚
                if codeName in ['bgFishingMaster']:
                    game = self.find_element(*self.thirdParty_bgFishingMaster)
                elif codeName in ['bgFishing', 'cq9Fishing']:
                    sortOrder = {'bgFishing': 0, 'cq9Fishing': 1}
                    sort = sortOrder[codeName]
                    gameNameList_Fishing = self.find_elements(*self.thirdParty_Fishing)
                    game = gameNameList_Fishing[sort]

            elif Target == 'web':
                # 時時彩
                if codeName == 'tjc':
                    game = self.find_element(*self.game_tjc)
                elif codeName == 'xjc':
                    game = self.find_element(*self.game_xjc)
                elif codeName == 'lottery1':
                    game = self.find_element(*self.game_lottery1)
                elif codeName == 'lottery2':
                    game = self.find_element(*self.game_lottery2)
                elif codeName == 'lottery5':
                    game = self.find_element(*self.game_lottery5)
                elif codeName == 'txffc':
                    game = self.find_element(*self.game_txffc)
                elif codeName == 'btcffc':
                    game = self.find_element(*self.game_btcffc)
                elif codeName == 'wxffc':
                    game = self.find_element(*self.game_wxffc)
                elif codeName == 'jnd30s':
                    game = self.find_element(*self.game_jnd30s)
                elif codeName == 'tg60':
                    game = self.find_element(*self.game_tg60)
                elif codeName == 'cajc':
                    game = self.find_element(*self.game_cajc)
                elif codeName == 'skjc':
                    game = self.find_element(*self.game_skjc)

                # 11選5
                elif codeName == 'sd11x5':
                    game = self.find_element(*self.game_sd11x5)
                elif codeName == 'jx11x5':
                    game = self.find_element(*self.game_jx11x5)
                elif codeName == 'gd11x5':
                    game = self.find_element(*self.game_gd11x5)
                elif codeName == 'js11x5':
                    game = self.find_element(*self.game_js11x5)
                elif codeName == 'tw11x5':
                    game = self.find_element(*self.game_tw11x5)
                elif codeName == 'ca11x5':
                    game = self.find_element(*self.game_ca11x5)
                elif codeName == 'sk11x5':
                    game = self.find_element(*self.game_sk11x5)

                # 快3
                elif codeName == 'jsk3':
                    game = self.find_element(*self.game_jsk3)
                elif codeName == 'hubk3':
                    game = self.find_element(*self.game_hubk3)
                elif codeName == 'hquick3':
                    game = self.find_element(*self.game_hquick3)
                elif codeName == 'quick3':
                    game = self.find_element(*self.game_quick3)
                elif codeName == 'cak3':
                    game = self.find_element(*self.game_cak3)
                elif codeName == 'skk3':
                    game = self.find_element(*self.game_skk3)

                # PK10
                elif codeName == 'f1racing':
                    game = self.find_element(*self.game_f1racing)
                elif codeName == 'f2racing':
                    game = self.find_element(*self.game_f2racing)
                elif codeName == 'f3racing':
                    game = self.find_element(*self.game_f3racing)
                elif codeName == 'xyft':
                    game = self.find_element(*self.game_xyft)
                elif codeName == 'caracing':
                    game = self.find_element(*self.game_caracing)
                elif codeName == 'skracing':
                    game = self.find_element(*self.game_skracing)

        time.sleep(3)
        game.click()
        return game_name

    def switch_lottery(self, lottery, codeName):
        # 判斷game name
        if Project in ['vt']:
            localization = 'VN'
        else:
            localization = 'CN'
        game_name = JsonLoader('GameNameList').get_loc(localization, lottery, codeName)
        # 切換lottery game
        game = None
        if Project in ['sta']:
            if Platform == 'Android' and Target == 'app':
                start_location = self.find_element(*self.first_title).location
                end_location = self.find_element(*self.game_option_home).location
                self.swipe(start_location, end_location, y2scale=1.2, duration=2500)
                # 時時彩
                if codeName in ['xjc', 'lottery1', 'lottery2', 'lottery5', 'txffc', 'btcffc',
                                'wxffc', 'jnd30s', 'tg60', 'twjc', 'cajc']:
                    sortOrder = {'xjc': 0, 'lottery1': 1, 'lottery2': 2, 'lottery5': 3, 'txffc': 4, 'btcffc': 5,
                                 'wxffc': 6, 'jnd30s': 7, 'tg60': 8, 'twjc': 9, 'cajc': 11}
                    sort = sortOrder[codeName]
                    gameNameList = self.find_elements(*self.gameNameList_All)
                    game = gameNameList[sort]
                else:
                    start_location = self.find_element(*self.next_title).location
                    end_location = self.find_element(*self.game_option_home).location
                    self.swipe(start_location, end_location, y2scale=1.2, duration=2500)
                    # 11選5
                    if codeName in ['sd11x5', 'jx11x5', 'gd11x5', 'js11x5', 'tw11x5', 'ca11x5']:
                        sortOrder = {'sd11x5': 0, 'jx11x5': 1, 'gd11x5': 2, 'js11x5': 3, 'tw11x5': 4, 'ca11x5': 6}
                        sort = sortOrder[codeName]
                        gameNameList = self.find_elements(*self.gameNameList_All)
                        game = gameNameList[sort]
                    else:
                        start_location = self.find_element(*self.next_title).location
                        end_location = self.find_element(*self.game_option_home).location
                        self.swipe(start_location, end_location, y2scale=1.2, duration=2500)
                        # 快3/PK10/六合彩
                        if codeName in ['jsk3', 'hubk3', 'hquick3', 'quick3', 'twk3', 'cak3',
                                        'f1racing', 'f2racing', 'f3racing', 'xyft', 'twracing',
                                        'caracing', 'mark6', 'fmark6']:
                            sortOrder = {'jsk3': 0, 'hubk3': 1, 'hquick3': 2, 'quick3': 3, 'twk3': 4, 'cak3': 6,
                                         'f1racing': 7, 'f2racing': 8, 'f3racing': 9, 'xyft': 10, 'twracing': 11,
                                         'caracing': 13, 'mark6': 14, 'fmark6': 15}
                            sort = sortOrder[codeName]
                            gameNameList = self.find_elements(*self.gameNameList_All)
                            game = gameNameList[sort]

            elif Platform == 'iOS' and Target == 'app':
                start_location = self.find_element(*self.first_title).location
                end_location = self.find_element(*self.game_option_home).location
                self.swipe(start_location, end_location, y2scale=1.2, duration=2500)
                # 時時彩
                if codeName in ['xjc', 'lottery1', 'lottery2', 'lottery5', 'txffc', 'btcffc',
                                'wxffc', 'jnd30s', 'tg60', 'twjc', 'cajc']:
                    sortOrder = {'xjc': 0, 'lottery1': 1, 'lottery2': 2, 'lottery5': 3, 'txffc': 4, 'btcffc': 5,
                                 'wxffc': 6, 'jnd30s': 7, 'tg60': 8, 'twjc': 9, 'cajc': 11}
                    sort = sortOrder[codeName]
                    gameNameList_SSC11x5 = self.find_elements(*self.gameNameList_SSC11x5)
                    game = gameNameList_SSC11x5[sort]
                else:
                    start_location = self.find_element(*self.next_title).location
                    end_location = self.find_element(*self.game_option_home).location
                    self.swipe(start_location, end_location, y2scale=1.2, duration=2500)
                    # 11選5
                    if codeName in ['sd11x5', 'jx11x5', 'gd11x5', 'js11x5', 'tw11x5', 'ca11x5']:
                        sortOrder = {'sd11x5': 0, 'jx11x5': 1, 'gd11x5': 2, 'js11x5': 3, 'tw11x5': 4, 'ca11x5': 6}
                        sort = sortOrder[codeName]
                        gameNameList_SSC11x5 = self.find_elements(*self.gameNameList_SSC11x5)
                        game = gameNameList_SSC11x5[sort]
                    else:
                        start_location = self.find_element(*self.next_title).location
                        end_location = self.find_element(*self.game_option_home).location
                        self.swipe(start_location, end_location, y2scale=1.2, duration=2500)
                        # 快3
                        if codeName in ['jsk3', 'hubk3', 'hquick3', 'quick3', 'twk3', 'cak3']:
                            sortOrder = {'jsk3': 0, 'hubk3': 1, 'hquick3': 2, 'quick3': 3, 'twk3': 4, 'cak3': 6}
                            sort = sortOrder[codeName]
                            gameNameList_Quick3 = self.find_elements(*self.gameNameList_Quick3)
                            game = gameNameList_Quick3[sort]
                        # PK10
                        elif codeName in ['f1racing', 'f2racing', 'f3racing', 'xyft', 'twracing', 'caracing']:
                            sortOrder = {'f1racing': 0, 'f2racing': 1, 'f3racing': 2, 'xyft': 3, 'twracing': 4, 'caracing': 6}
                            sort = sortOrder[codeName]
                            gameNameList_PK10 = self.find_elements(*self.gameNameList_PK10)
                            game = gameNameList_PK10[sort]
                        # 六合彩
                        elif codeName in ['mark6', 'fmark6']:
                            sortOrder = {'mark6': 0, 'fmark6': 1}
                            sort = sortOrder[codeName]
                            gameNameList_MarkSix = self.find_elements(*self.gameNameList_MarkSix)
                            game = gameNameList_MarkSix[sort]

            # elif Target == 'h5':
            #     start_location = self.find_element(*self.title_SSC).location
            #     end_location = self.find_element(*self.game_option_home).location
            #     self.swipe(start_location, end_location, y1scale=0.9, y2scale=0.9, duration=2000)
            #     # 時時彩
            #     if codeName in ['xjc', 'lottery1', 'lottery2', 'lottery5', 'txffc', 'btcffc', 'skjc',
            #                     'wxffc', 'jnd30s', 'tg60', 'twjc', 'skjc']:
            #         sortOrder = {'xjc': 0, 'lottery1': 1, 'lottery2': 2, 'lottery5': 3, 'txffc': 4, 'btcffc': 5,
            #                      'wxffc': 6, 'jnd30s': 7, 'tg60': 8, 'twjc': 9, 'skjc': 12}
            #         sort = sortOrder[codeName]
            #         gameNameList_SSC = self.find_elements(*self.gameNameList_SSC)
            #         game = gameNameList_SSC[sort]
            #     else:
            #         start_location = self.find_element(*self.title_11x5).location
            #         end_location = self.find_element(*self.game_option_home).location
            #         self.swipe(start_location, end_location, y1scale=0.9, y2scale=0.9, duration=2500)
            #         # 11選5
            #         if codeName in ['sd11x5', 'jx11x5', 'gd11x5', 'js11x5', 'tw11x5', 'sk11x5']:
            #             sortOrder = {'sd11x5': 0, 'jx11x5': 1, 'gd11x5': 2, 'js11x5': 3, 'tw11x5': 4, 'sk11x5': 7}
            #             sort = sortOrder[codeName]
            #             gameNameList_11x5 = self.find_elements(*self.gameNameList_11x5)
            #             game = gameNameList_11x5[sort]
            #         else:
            #             start_location = self.find_element(*self.title_Quick3).location
            #             end_location = self.find_element(*self.game_option_home).location
            #             self.swipe(start_location, end_location, y1scale=0.9, y2scale=0.9, duration=2500)
            #             # 快3
            #             if codeName in ['jsk3', 'hubk3', 'hquick3', 'quick3', 'twk3', 'skk3']:
            #                 sortOrder = {'jsk3': 0, 'hubk3': 1, 'hquick3': 2, 'quick3': 3, 'twk3': 4, 'skk3': 7}
            #                 sort = sortOrder[codeName]
            #                 gameNameList_Quick3 = self.find_elements(*self.gameNameList_Quick3)
            #                 game = gameNameList_Quick3[sort]
            #             # PK10
            #             elif codeName in ['f1racing', 'f2racing', 'f3racing', 'xyft', 'twracing', 'skracing']:
            #                 sortOrder = {'f1racing': 0, 'f2racing': 1, 'f3racing': 2, 'xyft': 3, 'twracing': 4, 'skracing': 7}
            #                 sort = sortOrder[codeName]
            #                 gameNameList_PK10 = self.find_elements(*self.gameNameList_PK10)
            #                 game = gameNameList_PK10[sort]
            #             # 六合彩
            #             elif codeName in ['mark6', 'fmark6', 'mamark6']:
            #                 sortOrder = {'mark6': 0, 'fmark6': 1, 'mamark6': 2}
            #                 sort = sortOrder[codeName]
            #                 gameNameList_MarkSix = self.find_elements(*self.gameNameList_MarkSix)
            #                 game = gameNameList_MarkSix[sort]

            elif Target == 'web':
                # 時時彩
                if codeName == 'tjc':
                    game = self.find_element(*self.game_tjc)
                elif codeName == 'xjc':
                    game = self.find_element(*self.game_xjc)
                elif codeName == 'lottery1':
                    game = self.find_element(*self.game_lottery1)
                elif codeName == 'lottery2':
                    game = self.find_element(*self.game_lottery2)
                elif codeName == 'lottery5':
                    game = self.find_element(*self.game_lottery5)
                elif codeName == 'txffc':
                    game = self.find_element(*self.game_txffc)
                elif codeName == 'btcffc':
                    game = self.find_element(*self.game_btcffc)
                elif codeName == 'wxffc':
                    game = self.find_element(*self.game_wxffc)
                elif codeName == 'jnd30s':
                    game = self.find_element(*self.game_jnd30s)
                elif codeName == 'tg60':
                    game = self.find_element(*self.game_tg60)
                elif codeName == 'cajc':
                    game = self.find_element(*self.game_cajc)
                elif codeName == 'skjc':
                    game = self.find_element(*self.game_skjc)

                # 11選5
                elif codeName == 'sd11x5':
                    game = self.find_element(*self.game_sd11x5)
                elif codeName == 'jx11x5':
                    game = self.find_element(*self.game_jx11x5)
                elif codeName == 'gd11x5':
                    game = self.find_element(*self.game_gd11x5)
                elif codeName == 'js11x5':
                    game = self.find_element(*self.game_js11x5)
                elif codeName == 'tw11x5':
                    game = self.find_element(*self.game_tw11x5)
                elif codeName == 'ca11x5':
                    game = self.find_element(*self.game_ca11x5)
                elif codeName == 'sk11x5':
                    game = self.find_element(*self.game_sk11x5)

                # 快3
                elif codeName == 'jsk3':
                    game = self.find_element(*self.game_jsk3)
                elif codeName == 'hubk3':
                    game = self.find_element(*self.game_hubk3)
                elif codeName == 'hquick3':
                    game = self.find_element(*self.game_hquick3)
                elif codeName == 'quick3':
                    game = self.find_element(*self.game_quick3)
                elif codeName == 'cak3':
                    game = self.find_element(*self.game_cak3)
                elif codeName == 'skk3':
                    game = self.find_element(*self.game_skk3)

                # PK10
                elif codeName == 'f1racing':
                    game = self.find_element(*self.game_f1racing)
                elif codeName == 'f2racing':
                    game = self.find_element(*self.game_f2racing)
                elif codeName == 'f3racing':
                    game = self.find_element(*self.game_f3racing)
                elif codeName == 'xyft':
                    game = self.find_element(*self.game_xyft)
                elif codeName == 'caracing':
                    game = self.find_element(*self.game_caracing)
                elif codeName == 'skracing':
                    game = self.find_element(*self.game_skracing)

                # 六合彩
                elif codeName == 'mark6':
                    game = self.find_element(*self.game_mark6)
                elif codeName == 'fmark6':
                    game = self.find_element(*self.game_fmark6)
                elif codeName == 'mamark6':
                    game = self.find_element(*self.game_mamark6)

        elif Project in ['vt']:
            if Target == 'web':
                if Target == 'web':
                    switch_to_gamepage = self.find_element(*self.switch_to_gamepage)
                    switch_to_gamepage.click()
                elif Target == 'h5':
                    pass
                else:
                    switch_to_gamepage = self.find_element(*self.switch_to_gamepage)
                    switch_to_gamepage.click()
                    # 需先收合熱門banner
                    lottery_banner_Hot = self.find_element(*self.lottery_banner_Hot)
                    lottery_banner_Hot.click()
            if Target == 'app':
                # 時時彩
                if lottery == 'SSC':
                    lottery_banner_SSC = self.find_element(*self.lottery_banner_SSC)
                    lottery_banner_SSC.click()
                    if codeName in ['xjc', 'lottery1', 'lottery2', 'lottery5', 'txffc', 'btcffc',
                                    'wxffc', 'jnd30s', 'tg60', 'twjc', 'cajc']:
                        sortOrder = {'xjc': 0, 'lottery1': 1, 'lottery2': 2, 'lottery5': 3, 'txffc': 4, 'btcffc': 5,
                                     'wxffc': 6, 'jnd30s': 7, 'tg60': 8, 'twjc': 9, 'cajc': 11}
                        sort = sortOrder[codeName]
                        gameNameBanner = self.find_elements(*self.gameNameBanner_All)
                        game = gameNameBanner[sort]
                # 11選5
                elif lottery == '11x5':
                    lottery_banner_11x5 = self.find_element(*self.lottery_banner_11x5)
                    lottery_banner_11x5.click()
                    if codeName in ['sd11x5', 'jx11x5', 'gd11x5', 'js11x5', 'tw11x5', 'ca11x5']:
                        sortOrder = {'sd11x5': 0, 'jx11x5': 1, 'gd11x5': 2, 'js11x5': 3, 'tw11x5': 4, 'ca11x5': 4}
                        sort = sortOrder[codeName]
                        gameNameBanner = self.find_elements(*self.gameNameBanner_All)
                        game = gameNameBanner[sort]
                # PK10
                elif lottery == 'PK10':
                    lottery_banner_PK10 = self.find_element(*self.lottery_banner_PK10)
                    lottery_banner_PK10.click()
                    if codeName in ['f1racing', 'f2racing', 'f3racing', 'xyft', 'twracing', 'caracing']:
                        sortOrder = {'f1racing': 0, 'f2racing': 1, 'f3racing': 2, 'xyft': 3, 'twracing': 4, 'caracing': 6}
                        sort = sortOrder[codeName]
                        gameNameBanner = self.find_elements(*self.gameNameBanner_All)
                        game = gameNameBanner[sort]
                # 快3
                elif lottery == 'Quick3':
                    lottery_banner_Quick3 = self.find_element(*self.lottery_banner_Quick3)
                    lottery_banner_Quick3.click()
                    if codeName in ['jsk3', 'hubk3', 'hquick3', 'quick3', 'twk3', 'cak3']:
                        sortOrder = {'jsk3': 0, 'hubk3': 1, 'hquick3': 2, 'quick3': 3, 'twk3': 4, 'cak3': 6}
                        sort = sortOrder[codeName]
                        gameNameBanner = self.find_elements(*self.gameNameBanner_All)
                        game = gameNameBanner[sort]

            elif Target == 'h5':
                # 時時彩
                if lottery == 'SSC':
                    lottery_banner_SSC = self.find_element(*self.lottery_banner_SSC)
                    lottery_banner_SSC.click()
                    start_location = lottery_banner_SSC.location
                    end_location = self.find_element(*self.game_type_nav).location
                    self.swipe(start_location, end_location, y2scale=1, duration=2500)
                    if codeName in ['xjc', 'lottery1', 'lottery2', 'lottery5', 'txffc', 'btcffc',
                                    'wxffc', 'jnd30s', 'tg60', 'twjc', 'cajc', 'skjc']:
                        sortOrder = {'xjc': 1, 'lottery1': 2, 'lottery2': 3, 'lottery5': 4, 'txffc': 5, 'btcffc': 6,
                                     'wxffc': 7, 'jnd30s': 8, 'tg60': 9, 'twjc': 10, 'cajc': 12, 'skjc': 13}
                        sort = sortOrder[codeName]
                        game = self.find_element(*(By.XPATH, self.gameNameBanner_SSC + "[" + str(sort) + "]"))
                # 11選5
                elif lottery == '11x5':
                    lottery_banner_11x5 = self.find_element(*self.lottery_banner_11x5)
                    lottery_banner_11x5.click()
                    start_location = lottery_banner_11x5.location
                    end_location = self.find_element(*self.game_type_nav).location
                    self.swipe(start_location, end_location, y2scale=1, duration=2500)
                    if codeName in ['sd11x5', 'jx11x5', 'gd11x5', 'js11x5', 'tw11x5', 'ca11x5', 'sk11x5']:
                        sortOrder = {'sd11x5': 1, 'jx11x5': 2, 'gd11x5': 3, 'js11x5': 4, 'tw11x5': 5, 'ca11x5': 7, 'sk11x5': 8}
                        sort = sortOrder[codeName]
                        game = self.find_element(*(By.XPATH, self.gameNameBanner_11x5 + "[" + str(sort) + "]"))
                # PK10
                elif lottery == 'PK10':
                    start_location = self.find_element(*self.lottery_banner_11x5).location
                    end_location = self.find_element(*self.game_type_nav).location
                    self.swipe(start_location, end_location, y2scale=1, duration=2500)
                    lottery_banner_PK10 = self.find_element(*self.lottery_banner_PK10)
                    lottery_banner_PK10.click()
                    start_location = lottery_banner_PK10.location
                    end_location = self.find_element(*self.game_type_nav).location
                    self.swipe(start_location, end_location, y2scale=1, duration=2500)
                    if codeName in ['f1racing', 'f2racing', 'f3racing', 'xyft', 'twracing', 'caracing', 'skracing']:
                        sortOrder = {'f1racing': 1, 'f2racing': 2, 'f3racing': 3, 'xyft': 4, 'twracing': 5, 'caracing': 7, 'skracing': 8}
                        sort = sortOrder[codeName]
                        game = self.find_element(*(By.XPATH, self.gameNameBanner_PK10 + "[" + str(sort) + "]"))
                # 快3
                elif lottery == 'Quick3':
                    start_location = self.find_element(*self.lottery_banner_11x5).location
                    end_location = self.find_element(*self.game_type_nav).location
                    self.swipe(start_location, end_location, y2scale=1, duration=2500)
                    lottery_banner_Quick3 = self.find_element(*self.lottery_banner_Quick3)
                    lottery_banner_Quick3.click()
                    start_location = lottery_banner_Quick3.location
                    end_location = self.find_element(*self.game_type_nav).location
                    self.swipe(start_location, end_location, y2scale=1, duration=2500)
                    if codeName in ['jsk3', 'hubk3', 'hquick3', 'quick3', 'twk3', 'cak3', 'skk3']:
                        sortOrder = {'jsk3': 1, 'hubk3': 2, 'hquick3': 3, 'quick3': 4, 'twk3': 5, 'cak3': 6, 'skk3': 8}
                        sort = sortOrder[codeName]
                        game = self.find_element(*(By.XPATH, self.gameNameBanner_Quick3 + "[" + str(sort) + "]"))

            elif Target == 'web':
                # 時時彩
                if codeName == 'tjc':
                    game = self.find_element(*self.game_tjc)
                elif codeName == 'xjc':
                    game = self.find_element(*self.game_xjc)
                elif codeName == 'lottery1':
                    game = self.find_element(*self.game_lottery1)
                elif codeName == 'lottery2':
                    game = self.find_element(*self.game_lottery2)
                elif codeName == 'lottery5':
                    game = self.find_element(*self.game_lottery5)
                elif codeName == 'txffc':
                    game = self.find_element(*self.game_txffc)
                elif codeName == 'btcffc':
                    game = self.find_element(*self.game_btcffc)
                elif codeName == 'wxffc':
                    game = self.find_element(*self.game_wxffc)
                elif codeName == 'jnd30s':
                    game = self.find_element(*self.game_jnd30s)
                elif codeName == 'tg60':
                    game = self.find_element(*self.game_tg60)
                elif codeName == 'cajc':
                    game = self.find_element(*self.game_cajc)
                elif codeName == 'skjc':
                    game = self.find_element(*self.game_skjc)

                # 11選5
                elif codeName == 'sd11x5':
                    game = self.find_element(*self.game_sd11x5)
                elif codeName == 'jx11x5':
                    game = self.find_element(*self.game_jx11x5)
                elif codeName == 'gd11x5':
                    game = self.find_element(*self.game_gd11x5)
                elif codeName == 'js11x5':
                    game = self.find_element(*self.game_js11x5)
                elif codeName == 'tw11x5':
                    game = self.find_element(*self.game_tw11x5)
                elif codeName == 'ca11x5':
                    game = self.find_element(*self.game_ca11x5)
                elif codeName == 'sk11x5':
                    game = self.find_element(*self.game_sk11x5)

                # 快3
                elif codeName == 'jsk3':
                    game = self.find_element(*self.game_jsk3)
                elif codeName == 'hubk3':
                    game = self.find_element(*self.game_hubk3)
                elif codeName == 'hquick3':
                    game = self.find_element(*self.game_hquick3)
                elif codeName == 'quick3':
                    game = self.find_element(*self.game_quick3)
                elif codeName == 'cak3':
                    game = self.find_element(*self.game_cak3)
                elif codeName == 'skk3':
                    game = self.find_element(*self.game_skk3)

                # PK10
                elif codeName == 'f1racing':
                    game = self.find_element(*self.game_f1racing)
                elif codeName == 'f2racing':
                    game = self.find_element(*self.game_f2racing)
                elif codeName == 'f3racing':
                    game = self.find_element(*self.game_f3racing)
                elif codeName == 'xyft':
                    game = self.find_element(*self.game_xyft)
                elif codeName == 'caracing':
                    game = self.find_element(*self.game_caracing)
                elif codeName == 'skracing':
                    game = self.find_element(*self.game_skracing)

        time.sleep(3)
        game.click()
        return game_name


if __name__ == '__main__':
    pass
