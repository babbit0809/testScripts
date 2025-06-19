from selenium.webdriver.common.by import By
from config.SetUIConfig import Platform, Target
from test_UI.common import BasePage


class Xpath(BasePage.BasePage):
    # Locators
    if Platform == 'Android' and Target == 'app':
        navigationBar_button_back = (By.ID, "toolbar_nav_btn")
        # 個人中心/ 個人資訊區塊(因應H5所需先抓取餘額區塊, 剩餘待後續補足)
        account_balance = (By.ID, "centerWalletAmtTextView")
        # 個人中心/ 財務選項
        finance_option_deposit = (By.ID, "chargeBtn")
        finance_option_withdraw = (By.ID, "refundBtn")
        finance_option_transfer = (By.ID, "transferBtn")
        # 充值頁 (渠道&金額選項皆先採固定UI位置, 後續再視所需調整)
        ch_bank = (By.XPATH, "(//*[@id='channelRecyclerView']//*[@id='filter_item'])[2]")
        ch_bank_vt = (By.XPATH, "(//*[@id='channelRecyclerView']//*[@id='filter_item'])[1]")
        ch_thirdParty = (By.XPATH, "(//*[@id='channelRecyclerView']//*[@id='filter_item'])[3]")
        ch_USDT = (By.XPATH, "(//*[@id='channelRecyclerView']//*[@id='filter_item'])[4]")
        ch_USDT_vt = (By.XPATH, "(//*[@id='channelRecyclerView']//*[@id='filter_item'])[2]")
        amount_input_option = (By.XPATH, "//*[@id='amountRecyclerView']/*[1]/*")
        amount_input_field = (By.ID, "ustd_amount_edit")
        confirm_button_deposit = (By.ID, "button")
        # 充值訂單資訊頁/ 平台銀行
        bank_sn = (By.XPATH, "//*[@id='order_number']/*[@class='android.widget.TextView'][2]")
        bank_name = (By.XPATH, "//*[@id='bank_name']/*[@class='android.widget.TextView'][2]")
        bank_account_name = (By.XPATH, "//*[@id='back_account_name']/*/*[@class='android.widget.TextView'][2]")
        bank_account = (By.XPATH, "//*[@id='bank_account']/*/*[@class='android.widget.TextView'][2]")
        bank_amount = (By.XPATH, "//*[@id='deposit_amount']/*/*[@class='android.widget.TextView'][2]")
        bank_currency = (By.XPATH, "//*[@id='currency']/*[@class='android.widget.TextView'][2]")
        bank_fee = (By.XPATH, "//*[@id='deposit_fee']/*/*[@class='android.widget.TextView'][2]")
        bank_comment = (By.XPATH, "//*[@id='deposit_comment']/*/*[@class='android.widget.TextView'][2]")
        bank_ratio = (By.XPATH, "//*[@id='exchange_ratio']/*[@class='android.widget.TextView'][2]")
        # 充值訂單資訊頁/ 第三方
        thirdParty_sn = (By.XPATH, "//*[@id='order_number_3rd_party']/*[@class='android.widget.TextView'][2]")
        thirdParty_method = (By.XPATH, "//*[@id='deposit_method_3rd_party']/*[@class='android.widget.TextView'][2]")
        thirdParty_amount = (By.XPATH, "//*[@id='apply_amount']/*[@class='android.widget.TextView'][2]")
        thirdParty_fee = (By.XPATH, "//*[@id='deposit_fee_3rd_party']/*[@class='android.widget.TextView'][2]")
        # 充值訂單資訊頁/ USDT
        usdt_sn = (By.XPATH, "//*[@id='order_number']/*[@class='android.widget.TextView'][2]")
        usdt_name = (By.XPATH, "//*[@id='bank_name']/*[@class='android.widget.TextView'][2]")
        usdt_protocol = (By.XPATH, "//*[@id='deposit_protocol']/*/*[@class='android.widget.TextView'][2]")
        usdt_address = (By.XPATH, "//*[@id='bank_account']/*/*[@class='android.widget.TextView'][2]")
        usdt_amount = (By.XPATH, "//*[@id='deposit_amount']/*/*[@class='android.widget.TextView'][2]")
        usdt_currency = (By.XPATH, "//*[@id='currency']/*[@class='android.widget.TextView'][2]")
        usdt_fee = (By.XPATH, "//*[@id='deposit_fee']/*/*[@class='android.widget.TextView'][2]")
        usdt_ratio = (By.XPATH, "//*[@id='exchange_ratio']/*[@class='android.widget.TextView'][2]")
        usdt_actualAmount = (By.XPATH, "//*[@id='target_amount']/*[@class='android.widget.TextView'][2]")
        back_button_deposit = (By.ID, "toolbar_nav_btn")
        done_button_deposit = (By.ID, "button1")
        # 提現頁
        pin_input_field = (By.ID, "pinpassword")
        withdrawOption_bankcard = (By.XPATH, "//*[@class='androidx.appcompat.app.ActionBar$Tab'][1]")
        withdrawOption_USDT = (By.XPATH, "//*[@class='androidx.appcompat.app.ActionBar$Tab'][2]")
        bankcard_bankName = (By.XPATH, "//*[@id='card']/*[1]")
        bankcard_cardNumber = (By.XPATH, "//*[@id='card']/*[2]")
        bankcard_accountName = (By.XPATH, "//*[@id='card']/*[3]")
        usdt_walletName = (By.XPATH, "//*[@id='card']/*[1]")
        usdt_walletAddress = (By.XPATH, "//*[@id='card']/*[2]")
        usdt_walletProtocol = (By.XPATH, "//*[@id='card']/*[3]")
        withdraw_input_field = (By.ID, "inputApplyAmount")
        next_button_withdraw = (By.ID, "btnConfirm")
        confirm_button_feeNotice = (By.ID, "button1")
        # 提現訂單資訊頁
        order_bankcard_BankName = (By.ID, "txtBank")
        order_bankcard_Last4Number = (By.ID, "txtLast4Digits")
        order_apply_amount = (By.ID, "txtApplicationAmount")
        order_admin_fee = (By.ID, "txtAdministrativeFee")
        order_discount_amount = (By.ID, "txtDeductionFee")
        order_handling_fee = (By.ID, "txtHandlingFee")
        order_final_amount = (By.ID, "txtActualWithdrawalAmount")
        confirm_button_withdraw = (By.ID, "button")
        done_button_withdraw = (By.ID, "button1")
        # 轉帳頁
        error_button_transfer = (By.ID, "button1")
        balance_Center = (By.ID, "centerWalletTextView")
        info_thirdParty = "//*[@id='recyclerView']/*"
        transfer_switch_button = (By.ID, "directSwitchBtn")
        button_dropDown = (By.ID, "walletSpinner")
        dropDownList = (By.XPATH, "//*[@id='text1']")
        dropDownList_first = (By.XPATH, "//*[@id='text1'][1]")  # 定位用
        dropDownList_last = (By.XPATH, "//*[@id='text1'][9]")  # 定位用
        transfer_amount_100 = (By.ID, "amt100Btn")
        confirm_button_transfer = (By.ID, "transferBtn")
        auto_transfer_tips = (By.XPATH, "//*[@id='swipe_layout']/*/*/*[2]")  # 定位用
        transfer_amount_title = (By.XPATH, "//*[@id='amtInputor']/*/*[2]")  # 定位用
        # 個人中心/ 充值紀錄
        report_option_deposit = (By.XPATH, "//*[@id='personalRecyclerView']/*[1]")
        info_depositAmount = (By.XPATH, "(//*[@id='layoutItemContent'])[1]//*[@id='layoutItemHead']/*[1]")
        info_depositNo = (By.XPATH, "(//*[@id='layoutItemContent'])[1]//*[@id='layoutItemHead']/*[2]")
        info_depositStatus = (By.XPATH, "(//*[@id='layoutItemContent'])[1]//*[@id='textType']")
        # 個人中心/ 提現紀錄  # TODO: 詳情先不加
        report_option_withdraw = (By.XPATH, "//*[@id='personalRecyclerView']/*[4]")
        report_option_withdraw_vt = (By.XPATH, "//*[@id='personalRecyclerView']/*[5]")
        info_withdrawAmount = (By.XPATH, "(//*[@id='layoutItemContent'])[1]//*[@id='layoutItemHead']/*[1]")
        info_withdrawNo = (By.XPATH, "(//*[@id='layoutItemContent'])[1]//*[@id='layoutItemHead']/*[2]")
        info_withdrawStatus = (By.XPATH, "(//*[@id='layoutItemContent'])[1]//*[@id='textType']")
        # 個人中心/ 轉帳紀錄
        report_option_transfer = (By.XPATH, "//*[@id='personalRecyclerView']/*[5]")
        report_option_transfer_vt = (By.XPATH, "//*[@id='personalRecyclerView']/*[7]")
        info_transferAmount = (By.XPATH, "(//*[@id='layoutItemContent'])[1]//*[@id='layoutItemHead']/*[1]")
        info_transferNo = (By.XPATH, "(//*[@id='layoutItemContent'])[1]//*[@id='layoutItemHead']/*[2]")
        info_transferType = (By.XPATH, "(//*[@id='layoutItemContent'])[1]//*[@id='textType']")
        # 個人中心/ 退出登錄
        button_logout = (By.ID, "logoutBtn")

    elif Platform == 'Android' and Target == 'h5':
        navigationBar_button_back = (By.XPATH, "(//*[@data-testid='shared-component-navigation-bar']"
                                               "//*[contains(@class,'flex items')])[1]")
        # 個人中心/ 個人資訊區塊(因應H5所需先抓取餘額區塊, 剩餘待後續補足)
        account_balance = (By.XPATH, "//*[@class='money']//*[@class='value']")
        icon_refresh = (By.XPATH, "//*[contains(@class, 'refreash')]")
        # 個人中心/ 財務選項
        finance_option_deposit = (By.XPATH, "//*[contains(@class,'quick-link')]//*[@type='button'][1]")
        finance_option_withdraw = (By.XPATH, "//*[contains(@class,'quick-link')]//*[@type='button'][2]")
        finance_option_transfer = (By.XPATH, "//*[contains(@class,'quick-link')]//*[@type='button'][3]")
        finance_option_withdraw_account = (By.XPATH, "//button[contains(@class,'MenuGroup')][6]")
        finance_option_withdraw_account_vt = (By.XPATH, "//button[contains(@class,'MenuGroup')][6]")
        # 充值頁 (渠道&金額選項皆先採固定UI位置, 後續再視所需調整)
        close_button_comm100 = (By.XPATH, "//*[@class='title-buttons window__operation']/*[3]")
        ch_bank = (By.XPATH, "(//*[contains(@class,'px-3 py-4')]//button)[2]")
        ch_bank_vt = (By.XPATH, "(//*[contains(@class,'px-3 py-4')]//button)[4]")
        ch_thirdParty = (By.XPATH, "(//*[contains(@class,'bank-platform')]//button)[3]")
        ch_USDT = (By.XPATH, "(//*[contains(@class,'px-3 py-4')]//button)[4]")
        ch_USDT_vt = (By.XPATH, "(//*[contains(@class,'px-3 py-4')]//button)[2]")
        amount_input_option = (By.XPATH, "(//*[contains(@class,'h-10')]//button)[1]")
        amount_input_field = (By.XPATH, "//input[@type='number']")
        confirm_button_deposit = (By.XPATH, "//*[contains(@class,'flex h-11')]/button")
        # 充值訂單資訊頁/ 平台銀行
        bank_sn = (By.XPATH, "(//*[contains(@class,'body-8')])[1]")
        bank_name = (By.XPATH, "(//*[contains(@class,'between items')]/div[2])[1]")
        bank_account_name = (By.XPATH, "(//*[contains(@class,'between items')]/div[2])[2]")
        bank_account = (By.XPATH, "(//*[contains(@class,'between items')]/div[2])[3]")
        bank_amount = (By.XPATH, "(//*[contains(@class,'between items')]/div[2])[4]")
        bank_currency = (By.XPATH, "(//*[contains(@class,'between items')]/div[2])[6]")
        bank_fee = (By.XPATH, "(//*[contains(@class,'between items')]/div[2])[7]")
        bank_ratio = (By.XPATH, "(//*[contains(@class,'between items')]/div[2])[8]")
        bank_comment = (By.XPATH, "(//*[contains(@class,'between items')]/div[1])[9]")

        # 充值訂單資訊頁/ 第三方
        thirdParty_sn = (By.XPATH, "(//*[contains(@class,'body-8')])[1]")
        thirdParty_method = (By.XPATH, "//*[@nodeName='TBODY']/*[2]/*/*[2]")
        thirdParty_amount = (By.XPATH, "(//*[contains(@class,'between items')]/div[2])[1]")
        thirdParty_fee = (By.XPATH, "(//*[contains(@class,'between items')]/div[2])[2]")
        # 充值訂單資訊頁/ USDT
        usdt_sn = (By.XPATH, "//*[contains(@class,'body-8')]/text()[3]")
        usdt_name = (By.XPATH, "(//*[contains(@class,'between items')]/div[2])[1]")
        usdt_protocol = (By.XPATH, "(//*[contains(@class,'between items')]/div[2])[2]")
        usdt_address = (By.XPATH, "(//*[contains(@class,'between items')]/div[1])[3]")
        usdt_amount = (By.XPATH, "(//*[contains(@class,'between items')]/div[2])[4]")
        usdt_currency = (By.XPATH, "(//*[contains(@class,'between items')]/div[2])[6]")
        usdt_fee = (By.XPATH, "(//*[contains(@class,'between items')]/div[2])[7]")
        usdt_ratio = (By.XPATH, "(//*[contains(@class,'between items')]/div[2])[8]")
        usdt_actualAmount = (By.XPATH, "(//*[contains(@class,'between items')]/div[2])[9]")
        back_button_deposit = (By.XPATH, "//*[contains(@class,'NavigationBar')]//*[contains(@class,'flex items')]")
        done_button_deposit = (By.XPATH, "//*[@class='flex-1'][2]")
        # 提現頁  # TODO: 待重構後再加USDT提現
        pin_input_field = (By.XPATH, "//input[@type='password']")
        confirm_button_pin = (By.XPATH, "//button[@type='submit']")
        withdrawOption_bankcard = (By.XPATH, "//*[contains(@class,'p-2 rounded-full')][1]")
        withdrawOption_USDT = (By.XPATH, "//*[contains(@class,'p-2 rounded-full')][2]")
        bankcard_bank_name = (By.XPATH, "//*[@data-index='0']//*[contains(@class,'text-title-7')]")
        bankcard_card_number = (By.XPATH, "//*[@data-index='0']//*[contains(@class,'text-body-6')]")
        bankcard_account_name = (By.XPATH, "//*[@data-index='0']//*[contains(@class,'text-title-8')]")
        withdraw_input_field = (By.XPATH, "//input[@type='number']")
        next_button_withdraw = (By.XPATH, "//button[@type='submit']")
        confirm_button_feeNotice = (By.XPATH, "//*[@class='swal2-confirm swal2-styled']")
        # 提現訂單資訊頁
        order_bankcard_BankName = (By.XPATH, "//*[contains(@class,'flex-2')]/div[1]")
        order_bankcard_Last4Number = (By.XPATH, "//*[contains(@class,'flex-2')]/div[2]")
        order_apply_amount = (By.XPATH, "(//*[contains(@class,'py-3')]//*[contains(@class,'justify-between')]/div[2])[1]")
        order_admin_fee = (By.XPATH, "(//*[contains(@class,'py-3')]//*[contains(@class,'justify-between')]/div[2])[2]")
        order_discount_amount = (By.XPATH, "(//*[contains(@class,'py-3')]//*[contains(@class,'justify-between')]/div[2])[3]")
        order_handling_fee = (By.XPATH, "(//*[contains(@class,'py-3')]//*[contains(@class,'justify-between')]/div[2])[4]")
        order_final_amount = (By.XPATH, "(//*[contains(@class,'py-3')]//*[contains(@class,'justify-between')]/div[2])[5]")
        confirm_button_withdraw = (By.XPATH, "//*[@class='px-3']//button")
        done_button_withdraw = (By.XPATH, "//*[@class='flex-1']//button")
        # 轉帳頁
        balance_Center = (By.XPATH, "//*[contains(@class,'text-body-6')]/p[2]")
        info_thirdParty = "(//*[contains(@class,'thirdPartyWallet')])"
        transfer_switch_button = (By.XPATH, "//*[contains(@class,'grow-0')]")
        button_dropDown = (By.XPATH, "//*[@class='relative']/select")
        dropDownList = "//*[@class='android.widget.ListView']//*[@id='text1']"  # switch to native app first
        dropDownList_first = (By.XPATH, "//*[@class='android.widget.ListView']//*[@id='text1'][1]")  # 定位用
        dropDownList_last = (By.XPATH, "//*[@class='android.widget.ListView']//*[@id='text1'][8]")  # 定位用
        transfer_amount_100 = (By.XPATH, "//*[contains(@class,'py-3')][1]")
        confirm_button_transfer = (By.XPATH, "//button[contains(@class,'transition')][1]")
        auto_transfer_tips = (By.XPATH, "//*[contains(@class,'px-1')]//p")  # 定位用
        transfer_amount_title = (By.XPATH, "//form//label")  # 定位用
        done_button_transfer = (By.XPATH, "//button[@type='submit']")
        # 個人中心/ 充值紀錄
        report_option_deposit = (By.XPATH, "//button[contains(@class,'MenuGroup')][1]")
        info_depositAmount = (By.XPATH, "(//*[contains(@class,'text-title')])[1]")
        info_depositNo = (By.XPATH, "(//*[contains(@class,'text-title')]/following-sibling::*[contains(@class,'platinum-200')])[1]")
        info_depositStatus = (By.XPATH, "(//*[@colspan='2'])[1]")
        # 個人中心/ 提現紀錄  # TODO: 詳情先不加
        report_option_withdraw = (By.XPATH, "//button[contains(@class,'MenuGroup')][2]")
        report_option_withdraw_vt = (By.XPATH, "//button[contains(@class,'MenuGroup')][2]")
        info_withdrawAmount = (By.XPATH, "(//*[contains(@class,'flex items-baseline')]/div[1])[1]")
        info_withdrawNo = (By.XPATH, "(//*[contains(@class,'flex items-baseline')]/div[2])[1]")
        info_withdrawStatus = (By.XPATH, "(//table/tr[2]/td)[1]")
        # 個人中心/ 轉帳紀錄
        report_option_transfer = (By.XPATH, "//button[contains(@class,'MenuGroup')][4]")
        report_option_transfer_vt = (By.XPATH, "//button[contains(@class,'MenuGroup')][4]")
        info_transferAmount = (By.XPATH, "(//*[contains(@class,'items-baseline')]/span)[1]")
        info_transferNo = (By.XPATH, "(//*[contains(@class,'items-baseline')]/div)[1]")
        info_transferType = (By.XPATH, "(//td[contains(@class,'pt-2')][2])[1]")
        # New H5 我的功能/ 個人中心
        button_user_setting = (By.XPATH, "(//*[contains(@class,'menu-button-icon')])[7]")
        button_user_setting_vt = (By.XPATH, "(//*[contains(@class,'menu-button-icon')])[8]")
        setting_info_nick_name = (By.XPATH, "(//*[contains(@class,'tip')])[1]")
        common_input_field_01 = (By.XPATH, "//input")
        common_input_field_02 = (By.XPATH, "(//input)[2]")
        button_submit = (By.XPATH, "//*[@type='submit']")
        button_confirm = (By.XPATH, "(//*[@data-testid='shared-component-button'])[2]")
        button_back = (By.XPATH, "//*[@clip-rule='evenodd']")
        button_edit_pin_code = (By.XPATH, "(//*[contains(@class,'text-left')])[8]")
        button_edit_pin_code_vt = (By.XPATH, "(//*[contains(@class,'text-left')])[6]")
        button_show_hide_pwd = (By.XPATH, "//*[contains(@class,'mx')]//*[@fill-rule='evenodd']")
        button_next_step = (By.XPATH, "//*[@data-testid='shared-component-button']")
        button_edit_password = (By.XPATH, "(//*[contains(@class,'text-left')])[7]")
        button_edit_password_vt = (By.XPATH, "(//*[contains(@class,'text-left')])[5]")
        button_edit_phone_number = (By.XPATH, "(//*[contains(@class,'text-left')])[2]")
        button_edit_security_email = (By.XPATH, "(//*[contains(@class,'text-left')])[3]")
        # New H5 我的功能
        user_page_nick_name = (By.XPATH, "//*[@class='account']")
        # 我的功能/ 提現帳戶管理
        tab_bank_card = (By.XPATH, "(//button[@type='button'])[1]")
        tab_crypto_wallet = (By.XPATH, "(//button[@type='button'])[2]")
        button_add_bank_card = (By.XPATH, "//*[contains(@class,'AddBank')]")
        button_add_crypto_wallet = (By.XPATH, "//*[contains(@class,'addWallet')]")
        field_input_bank_card_name = (By.XPATH, "//input[@type='text']")
        field_input_bank_card_num = (By.XPATH, "//input[@type='number']")
        button_add_bank_card_next = (By.XPATH, "//button[@type='submit']")
        confirm_bank_card_name = (By.XPATH, "(//*[contains(@class,'flex-col')]/div[contains(@class,'text')][2])[1]")
        confirm_bank_card_num = (By.XPATH, "(//*[contains(@class,'flex-col')]/div[contains(@class,'text')][2])[2]")
        dropdown_bank_list = (By.XPATH, "//*[contains(@class,'SharedInput')]")
        dropdown_bank_first = (By.XPATH, "//*[@id='text1'][2]")
        button_add_bank_card_confirm = (By.XPATH, "//button[@type='submit']")
        button_OTP_request = (By.XPATH, "(//*[@aria-label='core-dialog']//button)[2]")
        field_input_OTP = (By.XPATH, "//input[@type='number']")
        button_OTP_submit = (By.XPATH, "//button[@type='submit']")
        button_OTP_confirm = (By.XPATH, "//*[@aria-label='core-dialog']//button")
        field_bank_card_num = (By.XPATH, "//*[contains(@class,'flex-col')]/div[contains(@class,'text')][2]")
        wallet_protocol_erc = (By.XPATH, "//*[@for='ERC20']")
        wallet_protocol_trc = (By.XPATH, "//*[@for='TRC20']")
        wallet_protocol_omni = (By.XPATH, "//*[@for='Omni']")
        field_input_wallet_address = (By.XPATH, "//*[contains(@class,'flex-col')]//input[@type='text']")
        button_add_wallet_address_next = (By.XPATH, "//button[@type='submit']")
        field_input_wallet_nickname = (By.XPATH, "//*[contains(@class,'flex-col')]//input[@type='text']")
        confirm_wallet_protocol = (By.XPATH, "(//*[contains(@class,'flex-col')]/div[2])[1]")
        confirm_wallet_address = (By.XPATH, "(//*[contains(@class,'flex-col')]/div[2])[2]")
        button_add_wallet_confirm = (By.XPATH, "//button[@type='submit']")

        # VIP
        button_name_member_data_level = (By.XPATH, "(//*[contains(text(),'VIP')])[1]")
        button_vip_details = (By.XPATH, "//*[@class='shared-component-button-text']")
        navigationBar_button_vip = (By.XPATH, "(//*[contains(text(),'VIP')])[2]")
        page_vip_level_name = (By.XPATH, "//*[@class='text-title-4']")
        my_vip_interest = (By.XPATH, "//*[contains(@class,'text-platinum-100')]")
        button_more_vip_interest = (By.XPATH, "//*[@class='shared-component-button-text']")
        button_tab_vip = (By.XPATH, "//*[@class='relative inline-block ']")
        button_member_interest = (By.XPATH, "(//*[contains(@type,'button')])[1]")
        button_member_return = (By.XPATH, "(//*[contains(@type,'button')])[2]")

        # 客服
        button_cs_nav = (By.XPATH, "(//*[contains(@class,'fixed bottom')]//*[@class='flex-1'])[2]")
        button_cs_mine = (By.XPATH, "//*[contains(@class,'UserData')]//*[@class='cs']//button")
        frame_service = (By.XPATH, "//*[@id='__next']/div//iframe[@title='service']")
        frame_chat_widget = (By.XPATH, "//*[@id='chat-widget-container']//*[@id='chat-widget']")
        button_cs_title = "//*[contains(@class,'NavigationBar')]//*[contains(@class,'text-center absolute')]"

        # 我的功能/ 推廣頁 (VT only)
        button_promo = (By.XPATH, "//button[contains(@class,'MenuGroup')][7]")
        button_promo_cs = (By.XPATH, "//*[contains(@class,'flex mb-4')]/div[1]")
        button_promo_download = (By.XPATH, "//*[contains(@class,'flex mb-4')]/div[2]")
        button_promo_qr_code = (By.XPATH, "//*[contains(@class,'flex mb-4')]/div[3]")
        button_copy_promo_code = (By.XPATH, "//button[@data-testid='shared-component-button']/span")
        button_register_with_promo_code = (By.XPATH, "//button/h4")
        button_download_promo_qr_code = (By.XPATH, "//*[@class='my-4']/button")

        # 活動
        button_activity = (By.XPATH, "(//*[@type='button'])[1]")
        activity_total_count = (By.XPATH, "//picture")
        activity_total_count = (By.XPATH, "//picture")
        # 公告
        buttton_notice_board = (By.XPATH, "(//*[@type='button'])[2]")
        notice_board_total_count = (By.XPATH, "//*[@class='relative w-full']")

        # 我的功能 / 下載頁
        button_user_page_download_app = (By.XPATH, "(//*[@data-testid='shared-component-button'])[1]")
        button_login_page_download = (By.XPATH, "//*[@class='text-body-8 font-semibold']")
        button_ios_tab = (By.XPATH, "(//*[@class='flex tab-title']/div)[1]")
        button_android_tab = (By.XPATH, "(//*[@class='flex tab-title']/div)[2]")
        app_version_info = (By.XPATH, "//*[@class='sc-dJjZJu kszVAv text-body-6 text-blue-100 mt-4 text-center']")
        button_user_page_logout = (By.XPATH, "(//*[@data-testid='shared-component-button'])[2]")
        button_confirm_logout = (By.XPATH, "(//button[@type='submit'])[4]")

    elif Platform == 'iOS' and Target == 'app':
        navigationBar_button_back = (By.ID, "id_UIButton_navBtn_back")
        # 個人中心/ 個人資訊區塊(因應H5所需先抓取餘額區塊, 剩餘待後續補足)
        account_balance = (By.XPATH, "//*[@class='UIAScrollView']/*/*/*[@id='id_UILabel_'][3]")
        # 個人中心/ 財務選項
        finance_option_deposit = (By.XPATH, "//*[@knownSuperClass='UIStackView']//*[@class='UIAButton'][1]")
        finance_option_withdraw = (By.XPATH, "//*[@knownSuperClass='UIStackView']//*[@class='UIAButton'][2]")
        finance_option_transfer = (By.XPATH, "//*[@knownSuperClass='UIStackView']//*[@class='UIAButton'][3]")
        finance_option_withdraw_account = (By.XPATH, "//*[@knownSuperClass='UICollectionViewCell'][9]")
        finance_option_withdraw_account_vt = (By.XPATH, "//button[contains(@class,'MenuGroup')][6]")
        # 充值頁 (渠道&金額選項皆先採固定UI位置, 後續再視所需調整)
        ch_bank = (By.XPATH, "//*[@class='UIACollectionView']/*[@XCElementType='XCUIElementTypeCell'][2]")
        ch_bank_vt = (By.XPATH, "(//*[@class='UIACollectionView'])[1]/*[@XCElementType='XCUIElementTypeCell'][1]")
        ch_thirdParty = (By.XPATH, "//*[@class='UIACollectionView']/*[@XCElementType='XCUIElementTypeCell'][3]")
        ch_USDT = (By.XPATH, "//*[@class='UIACollectionView']/*[@XCElementType='XCUIElementTypeCell'][4]")
        ch_USDT_vt = (By.XPATH, "(//*[@class='UIACollectionView'])[1]/*[@XCElementType='XCUIElementTypeCell'][2]")
        amount_input_option = (By.XPATH, "((//*[@class='UIACollectionView'])[2]//*[@name='id_UILabel_'])[1]")
        amount_input_field = (By.ID, "id_UITextField_")
        confirm_button_deposit = (By.XPATH, "//*[@knownSuperClass='UINavigationTransitionView']/*/*/*[@class='UIAButton']")
        # 充值訂單資訊頁/ 平台銀行
        bank_sn = (By.XPATH, "//*[@class='UIATable']/*[2]/*[@id='id_UILabel_'][2]")
        bank_name = (By.XPATH, "//*[@class='UIATable']/*[3]/*[@id='id_UILabel_'][2]")
        bank_account_name = (By.XPATH, "//*[@class='UIATable']/*[4]/*[@id='id_UILabel_'][2]")
        bank_account = (By.XPATH, "//*[@class='UIATable']/*[5]/*[@id='id_UILabel_'][2]")
        bank_amount = (By.XPATH, "//*[@class='UIATable']/*[6]/*[@id='id_MoneyLabel_']")
        bank_currency = (By.XPATH, "//*[@class='UIATable']/*[7]/*[@id='id_UILabel_'][2]")
        bank_fee = (By.XPATH, "//*[@class='UIATable']/*[8]/*[@id='id_MoneyLabel_']")
        bank_comment = (By.XPATH, "//*[@class='UIATable']/*[9]/*[@id='id_UILabel_'][2]")
        bank_ratio = (By.XPATH, "//*[@class='UIATable']/*[10]/*[@id='id_MoneyLabel_']")
        # 充值訂單資訊頁/ 第三方
        thirdParty_sn = (By.XPATH, "//*[@class='UIATable']/*[2]/*[@id='id_UILabel_'][2]")
        thirdParty_method = (By.XPATH, "//*[@class='UIATable']/*[3]/*[@id='id_UILabel_'][2]")
        thirdParty_amount = (By.ID, "id_MoneyLabel_")
        thirdParty_fee = (By.XPATH, "//*[@class='UIATable']/*[5]/*[@id='id_UILabel_'][2]")
        # 充值訂單資訊頁/ USDT
        usdt_sn = (By.XPATH, "//*[@class='UIATable']/*[2]/*[@id='id_UILabel_'][2]")
        usdt_name = (By.XPATH, "//*[@class='UIATable']/*[3]/*[@id='id_UILabel_'][2]")
        usdt_protocol = (By.XPATH, "//*[@class='UIATable']/*[4]/*[@id='id_UILabel_'][2]")
        usdt_address = (By.XPATH, "//*[@class='UIATable']/*[5]/*[@id='id_UILabel_'][2]")
        usdt_amount = (By.XPATH, "//*[@class='UIATable']/*[6]/*[@id='id_MoneyLabel_']")
        usdt_currency = (By.XPATH, "//*[@class='UIATable']/*[7]/*[@id='id_UILabel_'][2]")
        usdt_fee = (By.XPATH, "//*[@class='UIATable']/*[8]/*[@id='id_MoneyLabel_']")
        usdt_ratio = (By.XPATH, "//*[@class='UIATable']/*[9]/*[@id='id_MoneyLabel_']")
        usdt_actualAmount = (By.XPATH, "//*[@class='UIATable']/*[10]/*[@id='id_MoneyLabel_']")
        back_button_deposit = (By.XPATH, "//*[@class='UIAButton'][2]")
        done_button_deposit = (By.XPATH, "//*[@class='UIAScrollView'][2]/*/*/*[3]")
        # 提現頁
        pin_input_field = (By.ID, "id_DeleteBackTextField_")
        withdrawOption_bankcard = (By.XPATH, "(//*[@knownSuperClass='UIControl']//*[@class='UIAStaticText'])[1]")
        withdrawOption_USDT = (By.XPATH, "(//*[@knownSuperClass='UIControl']//*[@class='UIAStaticText'])[2]")
        bankcard_bankName = (By.XPATH, "//*[@knownSuperClass='UICollectionViewCell']//*[@id='id_UILabel_'][1]")
        bankcard_cardNumber = (By.XPATH, "//*[@knownSuperClass='UICollectionViewCell']//*[@id='id_UILabel_'][2]")
        bankcard_accountName = (By.XPATH, "//*[@knownSuperClass='UICollectionViewCell']//*[@id='id_UILabel_'][3]")
        usdt_walletName = (By.XPATH, "//*[@knownSuperClass='UICollectionViewCell']//*[@id='id_UILabel_'][1]")
        usdt_walletAddress = (By.XPATH, "//*[@knownSuperClass='UICollectionViewCell']//*[@id='id_UILabel_'][2]")
        usdt_walletProtocol = (By.XPATH, "//*[@knownSuperClass='UICollectionViewCell']//*[@id='id_UILabel_'][3]")
        withdraw_input_field = (By.XPATH, "//*[@class='UIATextField']")
        next_button_withdraw = (By.XPATH, "(//*[@class='UIAScrollView'])[2]/*/*[@id='id_UIButton_']")
        confirm_button_feeNotice = (By.XPATH, "//*[@knownSuperClass='UIStackView']/*[3]")
        # 提現訂單資訊頁
        order_bankcard_BankName = (By.XPATH, "//*[@knownSuperClass='UINavigationTransitionView']/*/*/*/*/*[1]/*[2]")
        order_bankcard_Last4Number = (By.XPATH, "//*[@knownSuperClass='UINavigationTransitionView']/*/*/*/*/*[1]/*[3]")
        order_apply_amount = (By.XPATH, "//*[@knownSuperClass='UINavigationTransitionView']/*/*/*/*/*[2]/*[2]/*")
        order_admin_fee = (By.XPATH, "//*[@knownSuperClass='UINavigationTransitionView']/*/*/*/*/*[2]/*[3]/*[1]/*[2]/*")
        order_discount_amount = (By.XPATH, "//*[@knownSuperClass='UINavigationTransitionView']/*/*/*/*/*[2]/*[3]/*[2]/*[2]/*")
        order_handling_fee = (By.XPATH, "//*[@knownSuperClass='UINavigationTransitionView']/*/*/*/*/*[2]/*[3]/*[3]/*[2]/*")
        order_final_amount = (By.XPATH, "//*[@knownSuperClass='UINavigationTransitionView']/*/*/*/*/*[2]/*[6]/*")
        confirm_button_withdraw = (By.XPATH, "//*[@knownSuperClass='UINavigationTransitionView']/*/*/*[2]//*[@id='id_UIButton_']")
        done_button_withdraw = (By.XPATH, "(//*[@knownSuperClass='_UIAlertControllerActionView'])[2]")
        # 轉帳頁
        balance_Center = (By.XPATH, "//*[@class='UIAScrollView']/*[2]/*/*/*[@id='id_MoneyLabel_'][1]")
        info_thirdParty = "(//*[@class='UIACollectionView'])[1]/*"
        transfer_switch_button = (By.XPATH, "//*[contains(@label, 'icon transfer switch')]")
        button_dropDown = (By.XPATH, "//*[@class='UIAView']/*/*[@id='id_UIButton_'][2]")
        dropDownList = (By.XPATH, "(//*[@class='UIATable']//*[@id='id_UILabel_'])")
        dropDownList_first = (By.XPATH, "(//*[@class='UIATable']//*[@id='id_UILabel_'])[1]")  # 定位用
        dropDownList_last = (By.XPATH, "(//*[@class='UIATable']//*[@id='id_UILabel_'])[6]")  # 定位用
        dropDownList_first2 = (By.XPATH, "(//*[@class='UIATable']//*[@id='id_UILabel_'])[1]")  # 定位用
        dropDownList_last2 = (By.XPATH, "(//*[@class='UIATable']//*[@id='id_UILabel_'])[12]")  # 定位用
        transfer_amount_100 = (By.XPATH, "//*[@class='UIAView']/*[@text='100']")
        confirm_button_transfer = (By.XPATH, "//*[@class='UIAView']/*[3]/*[@class='UIAButton']")
        auto_transfer_tips = (By.XPATH, "//*[@knownSuperClass='UIScrollView']/*[2]/*[2]")  # 定位用
        transfer_amount_title = (By.XPATH, "//*[@knownSuperClass='UIScrollView']/*[2]/*[3]/*[1]/*[@id='id_UILabel_']")  # 定位用
        # 個人中心/ 充值紀錄
        report_option_deposit = (By.XPATH, "(//*[@class='UIACollectionView'])[1]/*[1]")
        info_depositAmount = (By.XPATH, "(//*[@id='id_MoneyLabel_'])[1]")
        info_depositNo = (By.XPATH, "(//*[@XCElementType='XCUIElementTypeCell'])[1]/*[last()-4]")
        info_depositStatus = (By.XPATH, "(//*[@XCElementType='XCUIElementTypeCell'])[1]/*[last()-3]")
        # 個人中心/ 提現紀錄  # TODO: 詳情先不加
        report_option_withdraw = (By.XPATH, "(//*[@class='UIACollectionView'])[1]/*[4]")
        report_option_withdraw_vt = (By.XPATH, "(//*[@class='UIACollectionView'])[1]/*[5]")
        info_withdrawAmount = (By.XPATH, "(//*[@XCElementType='XCUIElementTypeCell']//*[@id='id_MoneyLabel_'])[1]")
        info_withdrawNo = (By.XPATH, "(//*[@XCElementType='XCUIElementTypeCell']//*[@id='id_UILabel_'])[3]")
        info_withdrawStatus = (By.XPATH, "(//*[@XCElementType='XCUIElementTypeCell']//*[@id='id_UILabel_'])[4]")
        # 個人中心/ 轉帳紀錄
        report_option_transfer = (By.XPATH, "(//*[@class='UIACollectionView'])[1]/*[5]")
        report_option_transfer_vt = (By.XPATH, "(//*[@class='UIACollectionView'])[1]/*[7]")
        info_transferAmount = (By.XPATH, "(//*[@XCElementType='XCUIElementTypeCell']//*[@id='id_MoneyLabel_'])[1]")
        info_transferNo = (By.XPATH, "(//*[@XCElementType='XCUIElementTypeCell']//*[@id='id_UILabel_'])[5]")
        info_transferType = (By.XPATH, "(//*[@XCElementType='XCUIElementTypeCell']//*[@id='id_UILabel_'])[3]")
        # 個人中心/ 退出登錄
        button_logout = (By.XPATH, "//*[@class='UIAScrollView']/*/*[@class='UIAButton']")
        # 我的功能/ 提現帳戶管理
        tab_bank_card = (By.XPATH, "(//*[@knownSuperClass='UIControl']//*[@knownSuperClass='UILabel'])[1]")
        tab_crypto_wallet = (By.XPATH, "(//*[@knownSuperClass='UIControl']//*[@knownSuperClass='UILabel'])[2]")
        button_add_bank_card = (By.XPATH, "//*[@XCElementType='XCUIElementTypeCell'][last()]")
        button_add_crypto_wallet = (By.XPATH, "//*[@XCElementType='XCUIElementTypeCell'][last()]")
        field_input_bank_card_name = (By.XPATH, "//*[@class='UIATable']//*[@class='UIAView'][2]//*[@class='UIATextField']")
        field_input_bank_card_num = (By.XPATH, "//*[@class='UIATable']//*[@class='UIAView'][5]//*[@class='UIATextField']")
        button_add_bank_card_next = (By.XPATH, "//*[@class='UIATable']//*[@name='id_UIButton_']")
        confirm_bank_card_name = (By.XPATH, "//*[@class='UIATable']//*[@class='UIAView'][2]//*[@class='UIAStaticText'][2]")
        confirm_bank_card_num = (By.XPATH, "//*[@class='UIATable']//*[@class='UIAView'][3]//*[@class='UIAStaticText'][2]")
        dropdown_bank_list = (By.XPATH, "//*[@label='icon select bank card']")
        dropdown_bank_first = (By.XPATH, "//*[@knownSuperClass='UISearchBar']/following-sibling::*[@class='UIATable']"
                                         "//*[@XCElementType='XCUIElementTypeCell'][1]")
        button_add_bank_card_confirm = (By.XPATH, "(//*[@knownSuperClass='UIAccessibilityElement' and @class='UIAButton'])[3]")
        button_OTP_request = (By.XPATH, "(//*[@knownSuperClass='_UIAlertControllerActionView'])[2]")
        field_input_OTP = (By.ID, "id_DeleteBackTextField_")
        button_OTP_submit = (By.XPATH, "(//*[@name='id_DeleteBackTextField_']/following::*[@class='UIAButton'])[1]")
        button_OTP_confirm = (By.XPATH, "//*[@class='UIAScrollView']//*[@class='UIAButton']")
        field_bank_card_num = (By.XPATH, "//*[@class='UIATable']//*[@class='UIAView']//*[@class='UIAStaticText'][1]")
        wallet_protocol_erc = (By.ID, "ERC20")
        wallet_protocol_trc = (By.ID, "TRC20")
        wallet_protocol_omni = (By.ID, "Omni")
        field_input_wallet_address = (By.XPATH, "//*[@XCElementType='XCUIElementTypeTextView']")
        button_add_wallet_address_next = (By.XPATH, "//*[@label='icScan']//following::*[@id='id_UIButton_']")
        field_input_wallet_nickname = (By.XPATH, "//*[@class='UIATextField']")
        confirm_wallet_protocol = (By.XPATH, "(//*[@id='id_UILabel_'][2])[1]")
        confirm_wallet_address = (By.XPATH, "(//*[@id='id_UILabel_'][2])[2]")
        button_add_wallet_confirm = (By.XPATH, "//*[@class='UIATable']//*[contains(@name,'id_UIButton')][2]")

        # 客服
        button_cs_nav = (By.XPATH, "(//*[contains(@class,'fixed bottom')]//*[@class='flex-1'])[2]")
        button_cs_mine = (By.XPATH, "//*[contains(@class,'UserData')]//*[@class='cs']//button")
        frame_service = (By.XPATH, "//*[@id='__next']/div//iframe[@title='service']")
        frame_chat_widget = (By.XPATH, "//*[@id='chat-widget-container']//*[@id='chat-widget']")
        button_cs_title = "//*[contains(@class,'NavigationBar')]//*[contains(@class,'text-center absolute')]"

        # 我的功能/ 推廣頁 (VT only)
        button_promo = (By.XPATH, "//button[contains(@class,'MenuGroup')][7]")
        button_promo_cs = (By.XPATH, "//*[contains(@class,'flex mb-4')]/div[1]")
        button_promo_download = (By.XPATH, "//*[contains(@class,'flex mb-4')]/div[2]")
        button_promo_qr_code = (By.XPATH, "//*[contains(@class,'flex mb-4')]/div[3]")
        button_copy_promo_code = (By.XPATH, "//button[@data-testid='shared-component-button']/span")
        button_register_with_promo_code = (By.XPATH, "//button/h4")
        button_download_promo_qr_code = (By.XPATH, "//*[@class='my-4']/button")

    elif Platform == 'iOS' and Target == 'h5':
        pass

    elif Target == 'web':
        # 個人資訊區塊(因應H5所需先抓取餘額區塊, 剩餘待後續補足)
        account_balance = (By.XPATH, "//*[@class='amount']")  # 個人主頁_個人概況_主账户_主账户余额
        # 充值相關 (銀行/第三方皆先採用固定的UI位置, 後續再視所需調整)
        finance_option_deposit = (By.XPATH, "//*[@href='/user/deposit']/*[@class='icon']")  # 側邊_個人主頁_轉帳
        ch_bank = (By.XPATH, "//*[@for='bank_20']")  # 支付宝转银行卡
        ch_bank_vt = (By.XPATH, "//*[@for='bank_30']")
        ch_thirdParty = (By.XPATH, "//*[@for='bank_2']")  # 网关
        ch_USDT = (By.XPATH, "//*[@for='bank_39']")  # 虚拟币支付
        amount_input_option = (By.XPATH, "(//*[@class='list']/li)[1]")  # 第一個金額按鈕
        amount_input_field = (By.XPATH, "//*[@placeholder]")  # 輸入金額
        tips = (By.XPATH, "//*[@class='tabs_titles']/following-sibling::*/*/*[4]/*[@nodeName='SPAN']")
        confirm_button_deposit = (By.XPATH, "//*[@mode='BUTTON_MODE_DANGER']")
        # 充值訂單資訊頁/ 平台銀行
        bank_sn = (By.XPATH, "//tr[1]/td[1]/div[2]")  # 订单编号
        bank_name = (By.XPATH, "//tr[2]/td[1]/div[2]")  # 银行名称
        bank_account_name = (By.XPATH, "//tr[3]/td[1]/div[2]")  # 银行户名
        bank_account = (By.XPATH, "//tr[4]/td[1]/div[2]")  # 银行账户
        bank_amount = (By.XPATH, "//tr[5]/td[1]/div[2]")  # 充值金额
        bank_currency = (By.XPATH, "//*[@class='content']//*[@class='content'][1]//div[2]")  # 币别
        bank_ratio = (By.XPATH, "//*[@class='content']//*[@class='content'][2]//div[2]")  # 汇率
        bank_fee = (By.XPATH, "//tr[6]/td[1]/div[2]")  # 手续费
        bank_comment = (By.XPATH, "//tr[7]/td[1]/div[2]")  # 充值附言
        # 充值訂單資訊頁/ 第三方
        thirdParty_sn = (By.XPATH, "//tr[1]/td[1]/div[2]")  # 第三方订单编号
        thirdParty_method = (By.XPATH, "//tr[3]/td[1]/div[2]")  # 第三方支付方式
        thirdParty_amount = (By.XPATH, "//tr[5]/td[1]/div[2]")  # 第三方充值金额
        thirdParty_fee = (By.XPATH, "//tr[6]/td[1]/div[2]")  # 手续费
        # 充值訂單資訊頁/ USDT
        usdt_sn = (By.XPATH, "//tr[1]/td[1]/div[2]")  # usdt订单编号
        usdt_name = (By.XPATH, "//tr[2]/td[1]/div[2]")  # usdt钱包协议
        usdt_protocol = (By.XPATH, "//tr[3]/td[1]/div[2]")  # usdt支付名称
        usdt_address = (By.XPATH, "//tr[4]/td[1]/div[2]")  # usdt钱包地址
        usdt_method = (By.XPATH, "//tr[3]/td[1]")  # usdt钱包协议
        usdt_amount = (By.XPATH, "//tr[5]/td[1]/div[2]")  # usdt充值金额
        usdt_currency = (By.XPATH, "//*[@class='content']//*[@class='content'][1]//div[2]")  # 币别
        usdt_fee = (By.XPATH, "//*[@class='content']//*[@class='content'][3]//div[2]")
        usdt_ratio = (By.XPATH, "//*[@class='content']//*[@class='content'][2]//div[2]")  # 汇率
        usdt_actualAmount = (By.XPATH, "//tr[6]/td[1]/div[2]")  # usdt实际上分金额
        done_button_deposit = (By.XPATH, "//*[@class='button hollow']")  # 充值訂單_關閉
        # 提現訂單資訊頁
        finance_option_withdraw = (By.XPATH, "//*[@href='/user/withdraw']/*[@class='icon']")  # 側邊_個人主頁_提現
        bankcard_bankName = (By.XPATH, "(//*[@class='bank-card']//div[contains(@class,'bank')]//span)[1]")  # 提現_出款银行名稱
        bankcard_cardNumber = (By.XPATH, "//*[@class='bank-card']//div[contains(@class,'id')]")  # 提現_卡號後四碼
        bankcard_accountName = (By.XPATH, "//*[@class='bank-card']//div[contains(@class,'account')]")  # 提現_卡號帳號
        usdt_walletName = (By.XPATH, "(//*[@class='bank-card']//div[contains(@class,'bank')]//span)[1]")
        usdt_walletAddress = (By.XPATH, "(//*[@class='bank-card']//div[contains(@class,'wordWrapAddress')])[1]")
        usdt_walletProtocol = (By.XPATH, "(//*[@class='bank-card']//div[contains(@class,'protocol')])[1]")
        withdraw_input_field = (By.XPATH, "//*[@placeholder]")  # 提現_輸入提現金額
        next_button_withdraw = (By.XPATH, "//button[@type='submit']")  # 提現_下一步
        order_bankcard_BankName = (By.XPATH, "//*[@class='divTableRow'][1]/*[@class='divTableCell'][2]")  # 提現_出款银行名稱

        order_bankcard_Last4Number = (By.XPATH, "(//*[@class='card_img']//*[@class])[3]")  # 提現_卡號後四碼
        order_apply_amount = (By.XPATH, "//*[@class='divTableRow'][2]/*[@class='divTableCell'][2]")  # 提現_申请金额
        order_admin_fee = (By.XPATH, "//*[@class='divTableRow'][4]/*[@class='divTableCell'][2]")  # 提現_行政费
        order_discount_amount = (By.XPATH, "//*[@class='divTableRow'][5]/*[@class='divTableCell'][2]")  # 提現_优惠金额扣除
        order_handling_fee = (By.XPATH, "//*[@class='divTableRow'][3]/*[@class='divTableCell'][2]")  # 提現_手续费
        # order_final_amount = (By.XPATH, "//*[@class='divTableRow'][6]/*[@class='divTableCell'][2]")    # 提現_实际出款金额
        order_final_amount = (By.XPATH, "(//*[contains(@class,'Cell')])[12]")  # 提現_实际出款金额
        confirm_button_withdraw = (By.XPATH, "//*[@mode='BUTTON_MODE_DANGER']")  # 提現_確認提款訊息_確認提現按鈕
        pin_input_field = (By.XPATH, "//input")
        withdrawOption_bankcard = (
            By.XPATH, "//*[@class='user-content']//*[@class='icon-ic_banknote']/following::li[1]")
        withdrawOption_USDT = (By.XPATH, "//*[@class='user-content']//*[@class='icon-ic_banknote']/following::li[2]")
        confirm_button_pin = (By.XPATH, "//*[@mode='BUTTON_MODE_DANGER']")
        done_button_withdraw = (By.XPATH, "//*[@class='button hollow']")
        balance_reflash = (By.XPATH, "//*[contains(@class,'icon-ic_refreash')]")
        tips_deposit = (By.XPATH, "//*[@class='balance-block']")
        confirm_button_feeNotice = (
            By.XPATH, "//*[@class='divTableRow'][3]/*[@class='divTableCell'][2]")  # 提現_確認提款訊息_手續費
        # 轉帳相關
        finance_option_transfer = (By.XPATH, "//*[@href='/user/transfer/thirdparty']/*[@class='icon']")  # 側邊_個人主頁_轉帳
        button_dropDown = (By.XPATH, "//*[@href='/user/transfer/thirdparty']/li")  # 帳戶互轉
        dropDownList = (By.XPATH, "(//div[@class='table_td thirdparty'])")
        balance_Center = (By.XPATH, "(//h1//span)[2]")  # 主账户余额
        # info_thirdParty = "(//*[@class='transfer_exchange']//p)"
        info_thirdParty = "//*[contains(@src,'ic_"
        account_balance_LEG = (By.XPATH, "//*[contains(@src,'ic_leg')]/following::p[1]")  # 樂遊
        account_balance_IM1 = (By.XPATH, "//*[contains(@src,'ic_im')]/following::p[1]")  # IM體育電競
        account_balance_IM3 = (By.XPATH, "//*[contains(@src,'ic_im3')]/following::p[1]")  # IM棋牌
        account_balance_IBC = (By.XPATH, "//*[contains(@src,'ic_onebook')]/following::p[1]")  # 沙巴
        account_balance_BG = (By.XPATH, "//*[contains(@src,'ic_bg')]/following::p[1]")  # BG
        account_balance_KY = (By.XPATH, "//*[contains(@src,'ic_ky')]/following::p[1]")  # 開元
        account_balance_VA = (By.XPATH, "//*[contains(@src,'ic_va')]/following::p[1]")  # VA
        account_balance_TF = (By.XPATH, "//*[contains(@src,'ic_tf')]/following::p[1]")  # 雷火電競
        account_balance_DG = (By.XPATH, "//*[contains(@src,'ic_dg')]/following::p[1]")  # DG
        transfer_switch_button = (By.XPATH, "//*[@class='exchange']")  # web_轉帳按鈕
        dropDown_menu = (By.XPATH, "//*[@href='/user/transfer/thirdparty']/li")  # 帳戶互轉
        dropDown_list_LEG = (By.XPATH, "//*[@data-for='gameProviderName_LEG']")  # 樂遊
        dropDown_list_IM1 = (By.XPATH, "//*[@data-for='gameProviderName_IM1']")  # IM體育電競
        dropDown_list_IM3 = (By.XPATH, "//*[@data-for='gameProviderName_IM3']")  # IM棋牌
        dropDown_list_IBC = (By.XPATH, "//*[@data-for='gameProviderName_IBC']")  # 沙巴
        dropDown_list_BG = (By.XPATH, "//*[@data-for='gameProviderName_BG']")  # BG
        dropDown_list_KY = (By.XPATH, "//*[@data-for='gameProviderName_KY']")  # 開元
        dropDown_list_VA = (By.XPATH, "//*[@data-for='gameProviderName_VA']")  # VA
        dropDown_list_TF = (By.XPATH, "//*[@data-for='gameProviderName_TF']")  # 雷火電競
        dropDown_list_DG = (By.XPATH, "//*[@data-for='gameProviderName_DG']")  # DG
        transfer_input_field = (By.XPATH, "(//*[@placeholder])[2]")  # WEB_金額輸入
        confirm_button_transfer = (By.XPATH, "//*[@id='btn-confirm_betting']")  # 確認轉賬
        auto_transfer_tips = (By.XPATH, "//*[@class='text']")  # 定位用_免转钱包，自动转入转出
        done_button_transfer = (By.XPATH, "//*[@class='button hollow']")  # 轉帳完成_關閉
        navigationBar_button_back = (By.XPATH, "//*[@class='button hollow']")  # 轉帳完成_關閉
        scrollbars = (By.XPATH, "//*[@class='scrollbars']")
        back_button_transfer = (By.XPATH, "//*[@href='/user/transfer/thirdparty']/*[@class='icon']")  # web側邊_個人主頁_轉帳

        # 個人中心/ 充值紀錄
        report_option_deposit = (By.XPATH, "//*[@href='/user/record']/*[@class='icon']")  # 充值纪录
        info_depositAmount = (By.XPATH, "//tbody/tr[1]//span[2]")  # 申请金额
        info_depositNo = (By.XPATH, "//tbody/tr[1]/td[1]")  # 订单编号
        info_depositStatus = (By.XPATH, "//tbody/tr[1]/td[4]")  # 状态
        # 個人中心/ 提現紀錄  # TODO: 詳情先不加
        report_option_withdraw = (By.XPATH, "//*[@href='/user/record/withdraw']/*[@class='icon']")  # 充值纪录
        report_option_withdraw_vt = (By.XPATH, "//*[@href='/user/record']/*[@class='icon']")
        info_withdrawAmount = (By.XPATH, "//tbody//tr[1]//td[3]//span")  # 申请金额
        info_withdrawNo = (By.XPATH, "//tbody//tr[1]//td[1]//span")  # 订单编号
        info_withdrawStatus = (By.XPATH, "//tbody//tr[1]//td[4]//span")  # 状态
        # 個人中心/ 轉帳紀錄
        report_option_transfer = (By.XPATH, "//*[@href='/user/record/transfer']/*[@class='icon']")  # 轉帳纪录
        report_option_transfer_vt = (By.XPATH, "//*[@href='/user/record/transfer']/*[@class='icon']")
        button_record_open = (By.XPATH, "(//*[@class='header'])[2]")
        button_record_close = (By.XPATH, "(//*[@class='header'])[2]//*[@class='icon-ic_drop_up']")
        info_transferAmount = (By.XPATH, "//tbody//tr[1]//td[3]//span")  # 轉帳金额
        info_transferNo = (By.XPATH, "//tbody//tr[1]//td[1]//span")  # 订单编号
        info_transferType = (By.XPATH, "//tbody//tr[1]//td[4]//span")  # 轉帳類型


if __name__ == '__main__':
    pass
