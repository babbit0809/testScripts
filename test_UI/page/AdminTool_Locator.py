from selenium.webdriver.common.by import By
from config.SetUIConfig import Platform, Target
from test_UI.common import BasePage


class Xpath(BasePage.BasePage):
    # Locators
    if Platform == 'windows':

        if Target == 'admintool':
            # common
            language_dropdown = (By.XPATH, "//*[@class='ant-space-item']//*[contains(@class,'dropdown-link')]")
            popup_close_icon = (By.XPATH, "//*[@aria-label='close']//*[@data-icon='close']")
            drawer_mask = (By.XPATH, "//*[@class='ant-drawer-mask']")
            # # 查詢模組
            field_search_start_date = (By.XPATH, "//*[@placeholder='Start date']")
            field_search_end_date = (By.XPATH, "//*[@placeholder='End date']")
            button_confirm_date = (By.XPATH, "//*[@class='ant-picker-ok']//button")
            clear_query_period = (By.XPATH, "(//*[@aria-label='close-circle'])[1]")
            clear_transaction_period = (By.XPATH, "(//*[@aria-label='close-circle'])[1]")
            clear_login_period = (By.XPATH, "(//*[@aria-label='close-circle'])[2]")
            advanced_condition_item = (By.XPATH, "//*[@id='AdvancedSearchConditionItem']"
                                                 "/ancestor::*[contains(@class,'selection-search')]")
            advanced_condition_value = (By.XPATH, "//*[@id='AdvancedSearchConditionValue']")
            button_search = (By.XPATH, "//*[@aria-label='search']/ancestor::button")
            button_export = (By.XPATH, "//*[@aria-label='export']/ancestor::button")
            # open_subtotal = (By.XPATH, "//*[@class='ant-collapse-header' and @aria-expanded='false']") #Adam 小計區預設是關閉故要點擊打開
            open_subtotal = (By.XPATH,
                             "//*[@class='ant-collapse-header' and @aria-expanded='false']//*[@data-icon='right']")  # Adam 小計區預設是關閉故要點擊打開
            close_subtotal = (
                By.XPATH, "(//*[@class='ant-collapse-header' and @aria-expanded='true'])[2]")  # ADam 小計區為打開故要點擊關閉
            # no_result = (By.XPATH, "//*[@class='ant-spin-container ant-spin-blur']")  ################20210224
            no_result = (By.XPATH, "//*[@class='ant-spin-dot ant-spin-dot-spin']")
            field_pagination = (
                By.XPATH, "//ul[1]//*[@class='ant-pagination-options']//*[@class='ant-select-selector']")
            option_pagination_10 = (By.XPATH, "//ul[1]//*[@class='ant-pagination-options']//*[contains(@title,'10 ')]")
            option_pagination_25 = (By.XPATH, "//ul[1]//*[@class='ant-pagination-options']//*[contains(@title,'25')]")
            option_pagination_50 = (By.XPATH, "//ul[1]//*[@class='ant-pagination-options']//*[contains(@title,'50')]")
            option_pagination_100 = (By.XPATH, "//ul[1]//*[@class='ant-pagination-options']//*[contains(@title,'100')]")
            button_next_page = (By.XPATH, "//ul[1]//*[@title='Next Page' and @aria-disabled='false']")
            button_end_page = (By.XPATH, "//ul[1]//*[@title='Next Page' and @aria-disabled='true']")

            # 系統管理
            main_menu_control = (By.XPATH, "//*[@id='app-menu']//*[@aria-label='control']/following-sibling::span")
            control_sub = (By.XPATH, "//*[@aria-label='control']/ancestor::li//*[@role='menuitem']")

            # 全站管理
            main_menu_apartment = (By.XPATH, "//*[@id='app-menu']//*[@aria-label='apartment']/following-sibling::span")
            apartment_sub = (By.XPATH, "//*[@aria-label='apartment']/ancestor::li//*[@role='menuitem']")

            # 帳號管理
            # # Menu
            main_menu_user = (By.XPATH, "//*[@id='app-menu']//*[@aria-label='user']/following-sibling::span")
            user_sub = (By.XPATH, "//*[@aria-label='user']/ancestor::li//*[@role='menuitem']")
            # # # 查詢功能
            member_search_result_account = (By.XPATH, "//tr[1]/td[1]/a")
            member_search_result_nickname = (By.XPATH, "//tr[1]/td[2]")
            member_search_result_point = (By.XPATH, "//tr[1]/td[4]")
            member_search_result_type = (By.XPATH, "//tr[1]/td[5]")
            member_search_result_level = (By.XPATH, "//tr[1]/td[7]")
            member_log_search = (By.XPATH, "//*[@class='ant-drawer-body']//*[@aria-label='search']/ancestor::button")
            member_search_result_account_in_transaction = (By.XPATH, "//tr[2]/td[3]/a")
            member_search_result_account_in_log_transaction = (By.XPATH, "//tr[2]/td[5]/a")
            member_button_freeze = (By.XPATH, "//*[contains(@class,'level-0')]//button[contains(@class,'primary')]")
            member_button_freeze_confirm = (
                By.XPATH, "//*[@class='ant-popover-buttons']//*[contains(@class,'primary')]")
            member_title_freeze = (By.XPATH, "//*[contains(@class,'modal-mask') and not(contains(@class,'hidden'))]"
                                             "/ancestor::*[@class='ant-modal-root']//*[@class='ant-modal-title']")
            member_field_freeze_reason = (By.XPATH, "//*[@id='Remarks']")
            member_button_freeze_submit = (
                By.XPATH, "//*[@class='ant-modal-footer']/button[contains(@class,'primary')]")
            # # # 新增會員及代理商
            button_create_member = (By.XPATH, "//*[@aria-label='user-add']/ancestor::button")
            create_member_field_type = (By.XPATH, "//*[@id='MemberTypeId']/ancestor::span/following-sibling::span")
            create_member_field_name = (By.XPATH, "//input[@id='MemberName']")
            create_member_field_pwd = (By.XPATH, "//input[@id='Password']")
            create_member_field_confirm_pwd = (By.XPATH, "//input[@id='ConfirmPassword']")
            create_member_field_nickname = (By.XPATH, "//input[@id='NickName']")
            create_member_field_level = (By.XPATH, "//*[@id='AffiliateLevelId']/ancestor::span/following-sibling::span")
            create_member_field_point = (By.XPATH, "//input[@id='ReturnPoint']")
            create_member_parent = (By.XPATH, "//input[@id='ParentMemberName']")
            create_member_button_submit = (By.XPATH, "//button[@type='submit']")
            button_back = (By.XPATH, "//*[@aria-label='arrow-left']")
            # # # 編輯會員及代理商
            button_edit_member = (By.XPATH, "(//*[@class='ant-typography'])[1]")
            edit_member_title_basic_data = (
                By.XPATH, "(//*[@class='ant-drawer-body']//*[@class='ant-descriptions-title'])[1]")
            button_save_edit_member = (By.XPATH, "//*[@aria-label='save']/ancestor::button[@type='submit']")
            button_edit_member_submit = (By.XPATH, "//*[@class='ant-modal-footer']/button[contains(@class,'primary')]")
            button_edit_member_search = (By.XPATH, "//*[contains(@class,'drawer-body')]//*[@aria-label='search']"
                                                   "/ancestor::button")
            # # # # 判斷編輯會員資料 Tab isSelected
            edit_member_tab_basic_data_selected = (
                By.XPATH, "//*[@aria-selected='true' and contains(@id,'BasicData')]")  # 基本資料
            tab_bank_data_selected_selected = (
                By.XPATH, "//*[@aria-selected='true' and contains(@id,'BankData')]")  # 銀行資料
            tab_account_setting_selected = (
                By.XPATH, "//*[@aria-selected='true' and contains(@id,'AccountSetting')]")  # 帳號設定
            tab_account_security_selected = (
                By.XPATH, "//*[@aria-selected='true' and contains(@id,'AccountSecurity')]")  # 帳號安全
            tab_summarized_log_selected = (
                By.XPATH, "//*[@aria-selected='true' and contains(@id,'SummarizedLog')]")  # 綜合紀錄
            tab_change_log_selected = (By.XPATH, "//*[@aria-selected='true' and contains(@id,'ChangeLog')]")  # 異動紀錄
            tab_change_default = (By.XPATH, "//*[@aria-selected='false' and contains(@id,'BasicData')]")

            # # # # 基本資料
            # edit_member_tab_basic_data = (By.XPATH, "//*[@role='tab' and contains(@id,'BasicData') and @aria-selected='true']")
            edit_member_tab_basic_data = (By.XPATH, "//*[@aria-selected='true' and contains(@id,'BasicData')]")  # adam
            edit_member_button_status = (By.XPATH, "//button[@id='Status']")
            edit_member_field_member_level = (By.XPATH, "//*[@class='ant-drawer-content']//input[@id='MemberLevelId']"
                                                        "/ancestor::*[@class='ant-select-selector']")
            edit_member_option_member_level = (By.XPATH, "(//*[@id='MemberLevelId_list']/following-sibling::div"
                                                         "//*[contains(@class,'option-content')])[2]")
            edit_member_button_return_increase = (
                By.XPATH, "//label[@for='ReturnPoint']/parent::div/following-sibling::div"
                          "//*[@aria-label='Increase Value']")
            edit_member_button_return_decrease = (
                By.XPATH, "//label[@for='ReturnPoint']/parent::div/following-sibling::div"
                          "//*[@aria-label='Decrease Value']")
            edit_member_field_return = (By.XPATH, "//label[@for='ReturnPoint']/parent::div/following-sibling::div"
                                                  "//*[@id='ReturnPoint']")
            edit_member_button_placebet = (By.XPATH, "//button[@id='IsBetPlaceable']")
            edit_member_button_deposit = (By.XPATH, "//button[@id='IsDepositable']")
            edit_member_button_withdraw = (By.XPATH, "//button[@id='IsWithdrawable']")
            edit_member_button_transfer = (By.XPATH, "//button[@id='IsFundTransferable']")
            # # # # 銀行資料
            tab_bank_data = (By.XPATH, "//*[@aria-selected='false' and contains(@id,'BankData')]")  # adam
            bank_data_button_create = (By.XPATH, "//*[@aria-label='credit-card']/ancestor::button")
            bank_data_field_account_name = (By.XPATH, "//*[@id='AccountName']")
            bank_data_field_bank = (By.XPATH, "//*[@id='MemberBankTypeId']/ancestor::span")
            bank_data_option_bank = (By.XPATH, "(//*[@id='MemberBankTypeId_list']/parent::div"
                                               "//*[contains(@class,'option-content')])[1]")
            bank_data_field_bank_name = (By.XPATH, "//*[@id='MemberBankTypeId']/ancestor::span/following-sibling::span")
            bank_data_field_card_num = (By.XPATH, "//*[@id='CardNumber']")
            # # # # 帳號設定
            tab_account_setting = (By.XPATH, "//*[@aria-selected='false' and contains(@id,'AccountSetting')]")  # adam
            game_transfer_setting = (By.XPATH, "//button[contains(@id,'GameTransfer')]")

            # # # # 帳號安全
            tab_account_security = (By.XPATH, "//*[@aria-selected='false' and contains(@id,'AccountSecurity')]")  # adam
            account_security_button_password = (By.XPATH, "//*[@class='ant-drawer-body']//form[1]//button")
            account_security_field_password = (By.XPATH, "//*[@id='Password']")
            account_security_field_confirm_password = (By.XPATH, "//*[@id='ConfirmPassword']")
            account_security_button_birthday = (By.XPATH, "//*[@class='ant-drawer-body']//form[7]//button")
            account_security_button_birthday_today = (By.XPATH, "//*[@class='ant-drawer-body']//form[7]//button")
            account_security_field_birthday = (By.XPATH, "//input[@id='Birthday']")
            account_security_button_confirm_birthday = (By.XPATH, "//*[@class='ant-popover-buttons']"
                                                                  "//button[contains(@class,'primary')]")
            # # # # 綜合紀錄
            tab_summarized_log = (By.XPATH, "//*[@aria-selected='false' and contains(@id,'SummarizedLog')]")
            summarized_log = "(//*[@class='ant-descriptions']//*[@class='ant-descriptions-item'])[2]"
            summarized_log_column = (By.XPATH, "//*[@class='ant-descriptions']//*[@class='ant-descriptions-item']")
            # # # # 異動記錄
            tab_change_log = (By.XPATH, "//*[@aria-selected='false' and contains(@id,'ChangeLog')]")  # adam
            change_log_item_exist = "//*[@class='ant-drawer-body']//*[@class='ant-table-tbody']//tr[2]/td[3]"
            # change_log_first_item = (By.XPATH, "//*[@class='ant-drawer-body']//*[@class='ant-table-tbody']//tr[1//tr[4]/td[3]]/td[3]")
            change_log_first_item = (
                By.XPATH, "//*[@class='ant-drawer-body']//*[@class='ant-table-tbody']//tr[1]//td[3]")
            change_log_items = (By.XPATH, "//*[@class='ant-drawer-body']//*[@class='ant-table-tbody']//tr/td[3]")

            # 代理商管理
            # # Menu
            main_menu_team = (By.XPATH, "//*[@id='app-menu']//*[@aria-label='team']/following-sibling::span")
            team_sub = (By.XPATH, "//*[@aria-label='team']/ancestor::li//*[@role='menuitem']")
            # # # 查詢結果
            button_create_affiliate = (By.XPATH, "//*[@aria-label='usergroup-add']/ancestor::button")
            affiliate_search_result_account = (By.XPATH, "//tr[1]/td[1]//a")
            affiliate_search_result_nickname = (By.XPATH, "//tr[1]/td[2]")
            affiliate_search_result_point = (By.XPATH, "//tr[1]/td[4]")
            affiliate_search_result_type = (By.XPATH, "//tr[1]/td[5]")
            affiliate_search_result_level = (By.XPATH, "//tr[1]/td[7]")
            # # # 契約工資 / 分紅管理
            field_search_contract_type = (
                By.XPATH, "(//*[contains(@class,'collapse-item')]//*[@class='ant-select-selector'])[1]")
            option_search_contract_daily_wages = (
                By.XPATH, "(//*[contains(@class,'select-dropdown') and not(contains(@class,'hidden'))]"
                          "//*[contains(@class,'option-content')])[2]")
            option_search_contract_daily_dividends = (
                By.XPATH, "(//*[contains(@class,'select-dropdown') and not(contains(@class,'hidden'))]"
                          "//*[contains(@class,'option-content')])[3]")
            option_search_contract_monthly_dividends = (
                By.XPATH, "(//*[contains(@class,'select-dropdown') and not(contains(@class,'hidden'))]"
                          "//*[contains(@class,'option-content')])[4]")
            field_search_contract_parent = (By.XPATH, "//*[@id='TopMemberName']")
            field_search_contract_member = (By.XPATH, "//*[@id='MemberName']")
            column_contract_search_result = (By.XPATH, "//tr[contains(@class,'table-row')][1]/td[position()<7]")
            button_reset_contract = (By.XPATH, "//*[contains(@class,'dangerous')]")
            button_confirm_reset_contract = (
                By.XPATH, "//*[@class='ant-popover-buttons']//button[contains(@class,'primary')]")
            button_create_contract = (By.XPATH, "//button[contains(@condition,'object')]")
            title_create_contract = (By.XPATH, "//*[contains(@class,'drawer-open')]//*[@class='ant-drawer-title']")
            field_create_contract_type = (
                By.XPATH, "(//*[contains(@class,'drawer-open')]//*[@class='ant-select-selector'])[1]")
            option_contract_daily_wages = (
                By.XPATH, "(//*[contains(@class,'select-dropdown') and not(contains(@class,'hidden'))]"
                          "//*[contains(@class,'option-content')])[1]")
            option_contract_daily_dividends = (
                By.XPATH, "(//*[contains(@class,'select-dropdown') and not(contains(@class,'hidden'))]"
                          "//*[contains(@class,'option-content')])[2]")
            option_contract_monthly_dividends = (
                By.XPATH, "(//*[contains(@class,'select-dropdown') and not(contains(@class,'hidden'))]"
                          "//*[contains(@class,'option-content')])[3]")
            field_create_contract_parent = (By.XPATH, "//*[@id='TopMemberId']")
            field_create_contract_member = (By.XPATH, "//*[@id='MemberId']")
            field_create_contract_headcount = (By.XPATH, "//*[@id='ValuableMemberCount']")
            field_create_contract_profit = (By.XPATH, "//*[@id='ContractRatio']")
            submit_create_contract = (By.XPATH, "//*[contains(@class,'drawer-footer')]//*[contains(@class,'primary')]")

            # 出入款管理
            # # Menu
            main_menu_transaction = (
                By.XPATH, "//*[@id='app-menu']//*[@aria-label='transaction']/following-sibling::span")
            transaction_sub = (By.XPATH, "//*[@aria-label='transaction']/ancestor::li//*[@role='menuitem']")
            # # # 充值清單
            subtotal_deposit_order = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[1]")
            subtotal_deposit_account = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[2]")
            subtotal_deposit_order_amount = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[3]")
            subtotal_deposit_incomeAmount = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[4]")
            subtotal_deposit_fee_platform = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[5]")
            subtotal_deposit_fee_member = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[6]")
            subtotal_deposit_amount = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[7]")
            subtotal_deposit_preferentialAmount = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[8]")
            button_deposit = (By.XPATH, "//*[@aria-label='money-collect']/ancestor::button")
            title_deposit = (By.XPATH, "//*[contains(@class,'modal-mask') and not(contains(@class,'hidden'))]"
                                       "/ancestor::*[contains(@class,'root')]//*[@class='ant-modal-title']")
            field_deposit_account = (By.XPATH, "//*[contains(@class,'modal-mask') and not(contains(@class,'hidden'))]"
                                               "/ancestor::*[contains(@class,'root')]//*[@id='MemberName']")
            field_deposit_amount = (By.XPATH, "//*[contains(@class,'modal-mask') and not(contains(@class,'hidden'))]"
                                              "/ancestor::*[contains(@class,'root')]//*[@id='DepositAmount']")
            button_deposit_submit = (By.XPATH, "//*[contains(@class,'modal-mask') and not(contains(@class,'hidden'))]"
                                               "/ancestor::*[contains(@class,'root')]//button[@type='submit']")
            # # # 流水審核
            turnover_field_account = (By.XPATH, "//*[@id='MemberName']")
            turnover_subtotal_valid_bet_amount = (
                By.XPATH, "//*[@class='ant-descriptions-view']//tr[2]//*[@class='ant-typography']")
            turnover_subtotal_current = (
                By.XPATH, "//*[contains(@class,'content-box')]//*[contains(@class,'level-0')]/td")
            turnover_button_calculator = (By.XPATH, "//*[@aria-label='calculator']/ancestor::button")
            turnover_title_calculator = (By.XPATH, "//*[@id='rcDialogTitle3']")
            turnover_field_calculator_amount = (By.XPATH, "//*[@id='Amount']")
            turnover_button_calculator_submit = (By.XPATH, "//*[@class='ant-modal-content']//button[@type='submit']")
            turnover_field_calculator_shortage_amount = (By.XPATH, "//*[@class='ant-typography'][1]/ol")
            turnover_button_calculator_close = (By.XPATH, "//button[@aria-label='Close']")
            turnover_column_amount = (By.XPATH, "//tr[contains(@class,'level-0')]/td[6]")
            turnover_column_required = (By.XPATH, "//tr[contains(@class,'level-0')]/td[8]")
            turnover_button_edit = (By.XPATH, "//tr[contains(@class,'level-0')]//button")
            turnover_field_modify_required = (By.XPATH, "//*[@id='DiscountValidBetAmount']")
            turnover_submit_modify_required = (
                By.XPATH, "//*[@class='ant-modal-footer']/button[contains(@class,'primary')]")
            title_modify_required_turnover = (By.XPATH, "//*[@class='ant-modal-header']")
            # # # 提現處理
            withdrawal_field_search_status = (
                By.XPATH, "//*[contains(@class,'col-sm')][3]//*[@class='ant-select-selector']")
            withdrawal_option_search_status_all = (By.XPATH, "(//*[@class='ant-select-item-option-content'])[1]")
            withdrawal_option_search_status_unprocessed = (
                By.XPATH, "(//*[@class='ant-select-item-option-content'])[2]")
            withdrawal_option_search_status_processing = (By.XPATH, "(//*[@class='ant-select-item-option-content'])[3]")
            withdrawal_option_search_status_finished = (By.XPATH, "(//*[@class='ant-select-item-option-content'])[4]")
            withdrawal_option_search_status_rejected = (By.XPATH, "(//*[@class='ant-select-item-option-content'])[5]")
            withdrawal_option_search_status_failed = (By.XPATH, "(//*[@class='ant-select-item-option-content'])[6]")
            withdrawal_field_search_order_id = (By.XPATH, "//*[@id='WithdrawalNo']")
            withdrawal_button_audit = (By.XPATH, "(//button[@class='ant-btn ant-btn-link'])[2]")
            withdrawal_result_field_order_id = (By.XPATH, "//td[contains(@class,'fix-left')]//a")
            withdrawal_detail_title = (By.XPATH, "//*[contains(@class,'modal-mask') and not(contains(@class,'hidden'))]"
                                                 "/ancestor::*[@class='ant-modal-root']//*[@class='ant-modal-title']")
            withdrawal_detail_tab_info = (
                By.XPATH, "//*[contains(@class,'modal-mask') and not(contains(@class,'hidden'))]"
                          "/ancestor::*[@class='ant-modal-root']//*[contains(@id,'tab-1')]")
            withdrawal_detail_tab_turnover = (
                By.XPATH, "//*[contains(@class,'modal-mask') and not(contains(@class,'hidden'))]"
                          "/ancestor::*[@class='ant-modal-root']//*[contains(@id,'tab-TurnoverLog')]")
            withdrawal_detail_tab_summarized = (
                By.XPATH, "//*[contains(@class,'modal-mask') and not(contains(@class,'hidden'))]"
                          "/ancestor::*[@class='ant-modal-root']//*[contains(@id,'tab-2')]")
            withdrawal_detail_tab_log = (
                By.XPATH, "//*[contains(@class,'modal-mask') and not(contains(@class,'hidden'))]"
                          "/ancestor::*[@class='ant-modal-root']//*[contains(@id,'tab-3')]")
            withdrawal_detail_tab_change = (
                By.XPATH, "//*[contains(@class,'modal-mask') and not(contains(@class,'hidden'))]"
                          "/ancestor::*[@class='ant-modal-root']//*[contains(@id,'tab-4')]")
            withdrawal_detail_field_audit = (
                By.XPATH, "//*[contains(@aria-labelledby,'tab-1')]//*[@class='ant-select-selector']")
            withdrawal_detail_option_audit_pass = (
                By.XPATH, "(//*[contains(@class,'dropdown') and not(contains(@class,'hidden'))]"
                          "//*[@class='ant-select-item-option-content'])[1]")
            withdrawal_detail_option_audit_fail = (
                By.XPATH, "(//*[contains(@class,'dropdown') and not(contains(@class,'hidden'))]"
                          "//*[@class='ant-select-item-option-content'])[2]")
            withdrawal_detail_button_audit_submit = (
                By.XPATH, "//*[contains(@aria-labelledby,'tab-1')]//*[@type='submit']")
            withdrawal_detail_change_column_after = (
                By.XPATH, "//*[contains(@class,'modal-mask') and not(contains(@class,'hidden'))]"
                          "/ancestor::*[@class='ant-modal-root']//*[contains(@aria-labelledby,'tab-4')]"
                          "//tbody//*[contains(@class,'table-cell')][5]")
            withdrawal_detail_button_close = (
                By.XPATH, "//*[contains(@class,'modal-mask') and not(contains(@class,'hidden'))]"
                          "/ancestor::*[@class='ant-modal-root']//*[@aria-label='Close']")
            # # # 快速充值
            subtotal_fast_deposit_order = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[1]")
            subtotal_fast_deposit_account = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[2]")
            subtotal_fast_deposit_amount = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[3]")
            subtotal_fast_deposit_giveawayAmount = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[4]")
            subtotal_fast_deposit_preferentialAmount = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[5]")
            button_fast_deposit = (By.XPATH, "//*[@aria-label='money-collect']/ancestor::button")
            title_fast_deposit = (By.XPATH, "//*[@class='ant-modal-header']")
            tab_single_deposit = (By.XPATH, "(//*[@class='ant-tabs-tab-btn'])[1]")
            tab_batch_deposit = (By.XPATH, "(//*[@class='ant-tabs-tab-btn'])[2]")
            tab_manual_deposit = (By.XPATH, "(//*[@class='ant-tabs-tab-btn'])[3]")
            field_single_fast_deposit_account = (By.XPATH, "(//*[@id='MemberNames'])[1]")
            field_single_fast_deposit_type = (
                By.XPATH, "//*[@role='tabpanel' and @aria-hidden='false']//input[@id='SettingTypeId']"
                          "/ancestor::*[@class='ant-select-selector']")
            option_single_fast_deposit_promote = (By.XPATH,
                                                  "//*[contains(@class,'select-dropdown') and not(contains(@class,'hidden'))]//*[@id='SettingTypeId_list']"
                                                  "/following-sibling::*[@class='rc-virtual-list']//*[contains(@class,'item-option')][3]")
            field_single_fast_deposit_amount = (By.XPATH, "(//*[@id='Amount'])[1]")
            button_single_fast_deposit_submit = (By.XPATH, "(//*[@class='ant-space-item']/button[@type='submit'])[1]")
            field_batch_fast_deposit_account = (By.XPATH, "(//*[@id='MemberNames'])[2]")
            field_batch_fast_deposit_amount = (By.XPATH, "(//*[@id='Amount'])[2]")
            button_batch_fast_deposit_submit = (By.XPATH, "(//*[@class='ant-space-item']/button[@type='submit'])[2]")
            field_manual_fast_deposit_account = (By.XPATH, "(//*[@id='MemberNames'])[3]")
            field_manual_fast_deposit_amount = (By.XPATH, "(//*[@id='Amount'])[3]")
            button_manual_fast_deposit_submit = (By.XPATH, "(//*[@class='ant-space-item']/button[@type='submit'])[3]")
            # # # 執行新增快速充值作業設定
            button_create_fast_deposit_setting = (By.XPATH, "//*[@id='dt-header']//button")
            field_fast_deposit_name = (By.XPATH, "//*[@id='control-hooks_ItemName']")
            field_fast_deposit_type = (
                By.XPATH, "//*[@id='control-hooks_TypeId']/ancestor::*[@class='ant-select-selector']")
            value_fast_deposit_type = (
                By.XPATH, "//*[@id='control-hooks_TypeId']/ancestor::span/following-sibling::span")
            field_fast_deposit_subtype = (
                By.XPATH, "//*[@id='control-hooks_SubTypeId']/ancestor::span/following-sibling::span")
            field_fast_deposit_lottery = (By.XPATH, "//*[@id='control-hooks_LotteryCodes']"
                                                    "/ancestor::*[@class='ant-select-selector']")
            field_fast_deposit_turnover = (By.XPATH, "//*[@id='control-hooks_TurnoverMultiple']")
            field_fast_deposit_count_per_day = (By.XPATH, "//*[@id='control-hooks_CountPerDay']")
            field_fast_deposit_calculated = (By.XPATH, "//*[@id='control-hooks_CalculatedPercent']")
            field_fast_deposit_limit_amount = (By.XPATH, "//*[@id='control-hooks_LimitAmount']")
            option_fast_deposit_type = (By.XPATH, "(//*[@id='control-hooks_TypeId_list']"
                                                  "/ancestor::div//*[contains(@class,'item-option-content')])[1]")
            option_fast_deposit_subtype = (By.XPATH, "(//*[@id='control-hooks_SubTypeId_list']"
                                                     "/ancestor::div//*[contains(@class,'item-option-content')])[1]")
            # button_fast_deposit_audit = (By.XPATH, "//*[@id='control-hooks_Audit']/*[@class='ant-switch-inner']")
            button_fast_deposit_audit = (By.XPATH, "(//*[@id='control-hooks_IsAudit']/*[@class='ant-switch-inner'])[1]")
            button_fast_deposit_increase_turnover = (By.XPATH, "//*[@id='control-hooks_TurnoverMultiple']/ancestor::div"
                                                               "/preceding-sibling::div/*[@aria-label='Increase Value']")
            button_fast_deposit_increase_count_per_day = (By.XPATH, "//*[@id='control-hooks_CountPerDay']/ancestor::div"
                                                                    "/preceding-sibling::div/*[@aria-label='Increase Value']")
            button_fast_deposit_increase_calculated = (
                By.XPATH, "//*[@id='control-hooks_CalculatedPercent']/ancestor::div"
                          "/preceding-sibling::div/*[@aria-label='Increase Value']")
            # button_fast_deposit_isEnable = (By.XPATH, "//*[@id='control-hooks_IsEnable']/*[@class='ant-switch-inner']")
            button_fast_deposit_isEnable = (
                By.XPATH, "//*[contains(@class, 'drawer-open')]//*[@id='control-hooks_Status']")
            button_fast_deposit_setting_search = (By.XPATH, "//*[@aria-label='search']/ancestor::button")
            submit_fast_deposit_setting = (By.XPATH, "//*[@class='ant-drawer-footer']//button[2]")
            fast_deposit_setting_result_type = (By.XPATH, "//tr[1]/td[2]")
            fast_deposit_setting_result_subtype = (By.XPATH, "//tr[1]/td[3]")
            fast_deposit_setting_result_name = (By.XPATH, "//tr[1]/td[4]")
            fast_deposit_setting_result_audit = (By.XPATH, "//tr[1]/td[5]")
            fast_deposit_setting_result_turnover = (By.XPATH, "//tr[1]/td[6]")
            fast_deposit_setting_result_calculated = (By.XPATH, "//tr[1]/td[8]")
            fast_deposit_setting_result_limit_amount = (By.XPATH, "//tr[1]/td[9]")
            fast_deposit_setting_result_count_per_day = (By.XPATH, "//tr[1]/td[10]")
            fast_deposit_setting_result_isEnable = (By.XPATH, "//tr[1]/td[11]")
            # # # 帳變紀錄
            field_transaction_search = (By.XPATH, "//*[@id='Type']/ancestor::div[@class='ant-select-selector']")
            option_transaction_search = (By.XPATH, "//*[@id='Type_list']//following-sibling::div"
                                                   "//*[contains(@class,'item-option-content')]")
            # # # # 小計
            subtotal_total_count = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[1]")
            subtotal_incoming_amount = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[2]")
            subtotal_outgoing_amount = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[3]")
            subtotal_balance_amount = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[4]")
            # # # # 查詢結果
            column_transaction_type = (By.XPATH, "//td[@class='ant-table-cell'][1]")
            column_transaction_account = (By.XPATH, "//td[@class='ant-table-cell'][4]")
            column_transaction_amount = (By.XPATH, "//td[@class='ant-table-cell'][5]")
            transaction_search_result_account = (By.XPATH, "//tr[2]/td[5]/a")
            # # # 虛擬幣提現設定
            button_edit_crypto = (By.XPATH, "//tr[3]//*[@type='button'][1]")
            button_crypto_change_record = (By.XPATH, "//tr[3]//*[@type='button'][2]")
            title_edit_crypto = (By.XPATH, "//*[contains(@class,'drawer-open')]//*[@class='ant-drawer-title']")
            field_edit_crypto_protocol = (
                By.XPATH, "(//*[@class='ant-drawer-body']//*[contains(@class,'select-selector')])[2]")
            option_crypto_protocol_ERC20 = (By.XPATH, "//*[@label='ERC20']")
            option_crypto_protocol_TRC20 = (By.XPATH, "//*[@label='TRC20']")
            option_crypto_protocol_Omni = (By.XPATH, "//*[@label='Omni']")
            field_edit_crypto_rate = (By.XPATH, "//*[@id='ExchangeRate']")
            button_edit_crypto_status = (By.XPATH, "//button[@role='switch']")
            button_edit_crypto_submit = (
                By.XPATH, "//*[@class='ant-drawer-footer']//button[contains(@class,'primary')]")
            button_edit_crypto_submit_confirm = (
                By.XPATH, "//*[@class='ant-popover-content']//button[contains(@class,'primary')]")
            button_crypto_change_record_query = (By.XPATH, "//*[@type='submit']")
            column_crypto_search_result_rate = (By.XPATH, "//tr[3]/td[3]")
            column_crypto_change_record_before = (By.XPATH, "//*[@class='ant-drawer-body']//tr[1]/td[4]")
            column_crypto_change_record_after = (By.XPATH, "//*[@class='ant-drawer-body']//tr[1]/td[5]")
            button_crypto_change_record_close = (
                By.XPATH, "//*[contains(@class,'drawer-open')]//*[@class='ant-drawer-close']")

            # 遊戲記錄
            main_menu_filesearch = (
                By.XPATH, "//*[@id='app-menu']//*[@aria-label='file-search']/following-sibling::span")
            filesearch_sub = (By.XPATH, "//*[@aria-label='file-search']/ancestor::li//*[@role='menuitem']")
            field_status_type_search = (
                By.XPATH, "//*[@for='Status']/following::*[@class='ant-form-item-control-input'][1]")

            option_status_search = (By.XPATH, "//*[@class='ant-select-item-option-content']")
            # # 第三方投注記錄
            column_bet_order_cnt = (By.XPATH, "//ul[1]//*[contains(@class,'pagination-total-text')]")
            field_bet_source_search = (By.XPATH, "//*[@id='Source']/ancestor::div[@class='ant-select-selector']")
            option_bet_source_search = (By.XPATH, "//*[@id='Source_list']//following-sibling::div"
                                                  "//*[contains(@class,'item-option-content')]")
            field_bet_status_search = (By.XPATH, "//*[@id='Status']/ancestor::div[@class='ant-select-selector']")
            option_bet_status_search = (By.XPATH, "//*[@id='Status_list']//following-sibling::div"
                                                  "//*[contains(@class,'item-option-content')]")
            field_bet_winLoss_search = (By.XPATH, "//*[@id='WinLoss']/ancestor::div[@class='ant-select-selector']")
            option_bet_winLoss_search = (By.XPATH, "//*[@id='WinLoss_list']//following-sibling::div"
                                                   "//*[contains(@class,'item-option-content')]")
            # # # 小計
            subtotal_bet_order_count = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[1]")
            subtotal_bet_account = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[2]")
            subtotal_bet_amount = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[3]")
            subtotal_bet_available_amount = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[4]")
            subtotal_bet_user_win_amount = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[5]")
            subtotal_bet_platform_win_loss = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[6]")
            # # # 查詢結果
            column_bet_source = (By.XPATH, "//td[@class='ant-table-cell'][3]")
            column_bet_account = (By.XPATH, "//td[@class='ant-table-cell'][8]")
            column_bet_amount = (By.XPATH, "//td[@class='ant-table-cell'][9]")
            column_bet_winLoss = (By.XPATH, "//td[@class='ant-table-cell'][10]")
            column_bet_valid_amount = (By.XPATH, "//td[@class='ant-table-cell'][12]")
            column_bet_bonus_amount = (By.XPATH, "//td[@class='ant-table-cell'][13]")
            column_bet_status = (By.XPATH, "//td[@class='ant-table-cell'][14]")
            bet_search_result_account = (By.XPATH, "//tr[2]/td[9]/a")

            # 遊戲管理
            main_menu_desktop = (By.XPATH, "//*[@id='app-menu']//*[@aria-label='desktop']/following-sibling::span")
            desktop_sub = (By.XPATH, "//*[@aria-label='desktop']/ancestor::li//*[@role='menuitem']")

            # 營運管理
            main_menu_shop = (By.XPATH, "//*[@id='app-menu']//*[@aria-label='shop']/following-sibling::span")
            shop_sub = (By.XPATH, "//*[@aria-label='shop']/ancestor::li//*[@role='menuitem']")
            # # 輪播圖管理
            tab_banner_web = (By.XPATH, "//*[contains(@id,'tab-web')]")
            tab_banner_h5 = (By.XPATH, "//*[contains(@id,'tab-h5')]")
            tab_banner_ios = (By.XPATH, "//*[contains(@id,'tab-ios')]")
            tab_banner_android = (By.XPATH, "//*[contains(@id,'tab-android')]")
            button_add_banner_carousel = (By.XPATH, "//*[contains(@class,'ant-card-small')][1]//*[@aria-label='plus']")
            button_add_banner_game = (By.XPATH, "//*[contains(@class,'ant-card-small')][2]//*[@aria-label='plus']")
            button_edit_banner_carousel = (By.XPATH, "//*[contains(@class,'ant-card-small')][1]//*[@aria-label='edit']")
            button_edit_banner_game = (By.XPATH, "//*[contains(@class,'ant-card-small')][2]//*[@aria-label='edit']")
            button_delete_banner_carousel = (
                By.XPATH, "//*[contains(@class,'ant-card-small')][1]//*[@aria-label='delete']")
            button_delete_banner_game = (By.XPATH, "//*[contains(@class,'ant-card-small')][2]//*[@aria-label='delete']")
            button_delete_banner_confirm = (
                By.XPATH, "//*[@class='ant-popover-buttons']//button[contains(@class,'primary')]")
            field_add_banner_link = (By.XPATH, "//*[@id='control-hooks_TargetUrl']")
            field_add_banner_start = (By.XPATH, "//*[@id='control-hooks_StartTime']")
            button_add_banner_now = (By.XPATH, "//*[@class='ant-picker-now-btn']")
            button_add_banner_forever = (By.XPATH, "//*[@id='control-hooks_IsForever']")
            upload_add_banner = (By.XPATH, "//*[@class='ant-upload']//input")
            button_add_banner_submit = (By.XPATH, "//*[@class='ant-drawer-footer']//button[contains(@class,'primary')]")

            # 活動管理
            main_menu_activity = (By.XPATH, "//*[@id='app-menu']//*[@aria-label='gift']/following-sibling::span")
            activity_sub = (By.XPATH, "//*[@aria-label='gift']/ancestor::li//*[@role='menuitem']")
            # # 活動類別管理
            button_activity_type_edit = (
                By.XPATH, "(//*[contains(@class,'tbody')]//*[contains(@class,'fix-right')])[1]//a")
            column_activity_type_name = (By.XPATH, "//tr[contains(@class,'level-0')]/td[2]")
            column_activity_type_status = (
                By.XPATH, "//tr[contains(@class,'level-0')]/td[3]//*[contains(@class,'text')]")
            field_activity_type_edit_name = (By.XPATH, "//*[@id='control-hooks_Name']")
            button_activity_type_edit_status = (By.XPATH, "//*[@id='control-hooks_IsEnabled']")
            button_activity_type_edit_submit = (
                By.XPATH, "//*[contains(@class,'footer')]//button[contains(@class,'primary')]")
            # # 活動管理
            field_search_activity_status = (By.XPATH, "//*[@id='Status']")
            option_search_activity_caret_down = (
                By.XPATH, "//*[@class='ant-select-tree-list']//*[@aria-label='caret-down']")
            option_search_activity_status_all = (By.XPATH, "(//*[@class='ant-select-tree-title'])[1]")
            option_search_activity_status_standby = (By.XPATH, "(//*[@class='ant-select-tree-title'])[2]")
            option_search_activity_status_ongoing = (By.XPATH, "(//*[@class='ant-select-tree-title'])[3]")
            option_search_activity_status_finished = (By.XPATH, "(//*[@class='ant-select-tree-title'])[4]")
            field_search_activity_name = (By.XPATH, "//input[@id='Name']")
            button_create_activity = (By.XPATH, "//*[@aria-label='plus']/ancestor::button")
            button_edit_activity = (By.XPATH, "(//td[9]/a)[1]")
            field_create_activity_name = (By.XPATH, "//*[@id='control-hooks_Subject']")
            field_create_activity_type = (By.XPATH, "//*[contains(@class,'select-show-arrow')]")
            option_create_activity_type_first = (By.XPATH, "(//*[contains(@class,'option-content')])[1]")
            pinned_create_activity = (By.XPATH, "//*[@id='control-hooks_IsShowOnTop']")
            upload_create_activity_web = (By.XPATH, "(//*[@class='ant-upload']//input)[1]")
            upload_create_activity_app = (By.XPATH, "(//*[@class='ant-upload']//input)[2]")
            button_create_activity_submit = (By.XPATH, "//button[@type='submit']")
            button_create_activity_confirm = (
                By.XPATH, "//*[contains(@class,'confirm-body')]//button[contains(@class,'btn-primary')]")
            button_create_activity_cancel = (
                By.XPATH, "//*[contains(@class,'confirm-body')]//button[not(contains(@class,'btn-primary'))]")
            button_back_to_activity_list = (By.XPATH, "//*[@aria-label='arrow-left']")
            button_leave_activity_edit_confirm = (
                By.XPATH, "//*[contains(@class,'confirm-body')]//button[contains(@class,'btn-primary')]")
            tab_activity_basic_setting = (By.XPATH, "//*[contains(@id, 'tab-Basic')]")
            tab_activity_rule_setting = (By.XPATH, "//*[contains(@id, 'tab-Advanced')]")
            column_activity_name = (By.XPATH, "//tr[contains(@class,'level-0')]/td[1]//a")
            column_activity_type = (By.XPATH, "//tr[contains(@class,'level-0')]/td[3]")
            column_activity_pinned = (By.XPATH, "//tr[contains(@class,'level-0')]/td[6]")
            field_activity_rule_bonus_amount = (
                By.XPATH, "//*[contains(@id,'ActivityBonus_Rules') and contains(@class,'number-input')]")
            field_activity_rule_turnover_amount = (
                By.XPATH, "//*[contains(@id,'ValidBetAmount') and contains(@class,'number-input')]")
            field_activity_rule_receive_times = (
                By.XPATH, "//*[contains(@id,'ReceiveTimes') and contains(@class,'number-input')]")
            field_activity_rule_bonus_upper = (
                By.XPATH, "//*[contains(@id,'BonusUpper') and contains(@class,'number-input')]")
            field_activity_rule_ValidBetMultiple = (
                By.XPATH, "//*[contains(@id,'ValidBetMultiple') and contains(@class,'number-input')]")
            tab_activity_detail_basic = (
                By.XPATH, "(//*[@class='ant-tabs-nav-list']/*[contains(@class,'tabs-tab')])[1]")
            tab_activity_detail_rule = (By.XPATH, "(//*[@class='ant-tabs-nav-list']/*[contains(@class,'tabs-tab')])[2]")
            tab_activity_detail_change = (
                By.XPATH, "(//*[@class='ant-tabs-nav-list']/*[contains(@class,'tabs-tab')])[3]")
            column_activity_detail_name = (By.XPATH,
                                           "//*[@class='ant-drawer-body']//*[@class='ant-row ant-form-item'][1]//*[@class='ant-form-item-control-input-content']")
            column_activity_detail_type = (
                By.XPATH, "//*[@class='ant-row ant-form-item'][5]//*[@class='ant-form-item-control-input-content']")
            column_activity_detail_bonus_amount = (By.XPATH,
                                                   "//*[@class='ant-row ant-form-item'][5]//*[@class='ant-space-item']//*[@class='ant-space-item'][2]")
            column_activity_detail_turnover = (
                By.XPATH, "//*[@class='ant-row ant-form-item'][6]//*[@class='ant-space-item'][3]")
            column_activity_detail_receive_times = (
                By.XPATH, "//*[@class='ant-row ant-form-item'][10]//*[@class='ant-space-item'][2]")
            column_activity_detail_bonus_upper = (
                By.XPATH, "//*[@class='ant-row ant-form-item'][11]//*[@class='ant-space-item'][2]")
            column_activity_detail_ValidBetMultiple = (
                By.XPATH, "//*[@class='ant-row ant-form-item'][12]//*[contains(@class,'input-content')]")

            # 營運報表
            main_menu_barchart = (By.XPATH, "//*[@id='app-menu']//*[@aria-label='bar-chart']/following-sibling::span")
            barchart_sub = (By.XPATH, "//*[@aria-label='bar-chart']/ancestor::li//*[@role='menuitem']")
            # # 代理報表
            field_operation_report_affiliate_search = (
                By.XPATH, "//*[@id='AdvanceSearchOption']/ancestor::*[@class='ant-select-selector']")
            option_affiliate_search = (By.XPATH, "//*[@id='AdvanceSearchOption_list']//following-sibling::div"
                                                 "//*[contains(@class,'ant-select-item-option-content')]")
            operation_report_advanced_condition_item = (By.XPATH, "//*[@id='AdvanceSearchOption']"
                                                                  "/ancestor::*[contains(@class,'selection-search')]")
            operation_report_advanced_condition_value = (By.XPATH, "//*[@class='ant-input']")
            column_member_accounts = (By.XPATH, "//td//*[contains(@class,'ant-dropdown-trigger')]")
            column_affiliate_report_affiliate_cnt = (By.XPATH, "//ul[1]//*[contains(@class,'pagination-total-text')]")
            column_affiliate_report_member_tree_cnt = (By.XPATH, "//tr[contains(@class,'level-0')]/td[3]")
            column_affiliate_report_register_cnt = (By.XPATH, "//tr[contains(@class,'level-0')]/td[4]")
            column_affiliate_report_first_timeCnt = (By.XPATH, "//tr[contains(@class,'level-0')]/td[5]")
            column_affiliate_report_deposit_cnt = (By.XPATH, "//tr[contains(@class,'level-0')]/td[6]")
            column_affiliate_report_deposit3_cnt = (By.XPATH, "//tr[contains(@class,'level-0')]/td[7]")
            column_affiliate_report_deposit5_cnt = (By.XPATH, "//tr[contains(@class,'level-0')]/td[8]")
            column_affiliate_report_bet_member_cnt = (By.XPATH, "//tr[contains(@class,'level-0')]/td[9]")
            column_affiliate_report_bet_order_cnt = (By.XPATH, "//tr[contains(@class,'level-0')]/td[10]")
            column_affiliate_report_bet_amount = (By.XPATH, "//tr[contains(@class,'level-0')]/td[11]")
            column_affiliate_report_valid_bet_amount = (By.XPATH, "//tr[contains(@class,'level-0')]/td[12]")
            column_affiliate_report_bonus_amount = (By.XPATH, "//tr[contains(@class,'level-0')]/td[13]")
            column_affiliate_report_win_loss_amount = (By.XPATH, "//tr[contains(@class,'level-0')]/td[14]")
            column_affiliate_report_deposit_amount = (By.XPATH, "//tr[contains(@class,'level-0')]/td[15]")
            column_affiliate_report_withdrawal_amount = (By.XPATH, "//tr[contains(@class,'level-0')]/td[16]")
            column_affiliate_report_dep_with_amount = (By.XPATH, "//tr[contains(@class,'level-0')]/td[17]")
            column_affiliate_report_deduction_amount = (By.XPATH, "//tr[contains(@class,'level-0')]/td[18]")
            column_affiliate_report_rmAddition_amount = (By.XPATH, "//tr[contains(@class,'level-0')]/td[19]")
            column_affiliate_report_pre_payment_amount = (By.XPATH, "//tr[contains(@class,'level-0')]/td[20]")
            column_affiliate_report_commission_amount = (By.XPATH, "//tr[contains(@class,'level-0')]/td[21]")
            column_affiliate_report_return_point_amount = (By.XPATH, "//tr[contains(@class,'level-0')]/td[22]")
            column_affiliate_report_fee = (By.XPATH, "//tr[contains(@class,'level-0')]/td[23]")
            column_affiliate_report_administration_fee = (By.XPATH, "//tr[contains(@class,'level-0')]/td[24]")
            column_affiliate_report_member_balance = (By.XPATH, "//tr[contains(@class,'level-0')]/td[25]")
            column_affiliate_report_total_win_loss_amount = (By.XPATH, "//tr[contains(@class,'level-0')]/td[26]")
            subtotal_affiliate_affilate_cnt = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[1]")  # 代理帐号数
            subtotal_member_tree_cnt = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[2]")  # 下级人数
            subtotal_affiliate_register_cnt = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[3]")  # 注册人数
            subtotal_affiliate_deposit_first_timeCnt = (
                By.XPATH, "(//*[@class='ant-statistic-content-value'])[4]")  # 首充人数
            subtotal_affiliate_deposit_cnt = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[5]")  # 充值人数
            subtotal_affiliate_deposit3_cnt = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[6]")  # 三存人数
            subtotal_affiliate_deposit5_cnt = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[7]")  # 五存人数
            subtotal_affiliate_bet_member_cnt = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[8]")  # 投注人数
            subtotal_affiliate_bet_order_cnt = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[9]")  # 订单量
            subtotal_affiliate_bet_amount = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[10]")  # 投注金额
            subtotal_affiliate_valid_bet_amount = (
                By.XPATH, "(//*[@class='ant-statistic-content-value'])[11]")  # 有效投注金额
            subtotal_affiliate_bonus_amount = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[12]")  # 结算金额
            subtotal_affiliate_win_loss_amount = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[13]")  # 派彩(输赢)
            subtotal_affiliate_deposit_amount = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[14]")  # 充值金额
            subtotal_affiliate_withdrawal_amount = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[15]")  # 提现金额
            subtotal_affiliate_dep_with_amount = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[16]")  # 存提差
            subtotal_affiliate_deduction_amount = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[17]")  # 扣款金额
            subtotal_affiliate_rmAddition_amount = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[18]")  # 风控补分
            subtotal_affiliate_pre_payment_amount = (
                By.XPATH, "(//*[@class='ant-statistic-content-value'])[19]")  # 优惠金额
            subtotal_affiliate_commission_amount = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[20]")  # 返点
            subtotal_affiliate_return_point_amount = (
                By.XPATH, "(//*[@class='ant-statistic-content-value'])[21]")  # 代理分红
            subtotal_affiliate_fee = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[22]")  # 站台手续费
            subtotal_affiliate_administration_fee = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[23]")  # 行政费
            subtotal_affiliate_member_balance = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[24]")  # 会员余额
            subtotal_affiliate_total_win_loss_amount = (
                By.XPATH, "(//*[@class='ant-statistic-content-value'])[25]")  # 平台利润

            # # 會員報表
            field_operation_report_member_search = (
                By.XPATH, "//*[@id='AdvancedSearchConditionItem']/ancestor::*[@class='ant-select-selector']")
            option_member_search = (By.XPATH,
                                    "//*[@id='AdvancedSearchConditionItem_list']//following-sibling::div//*[contains(@class,'ant-select-item-option-content')]")
            column_member_report_member_cnt = (By.XPATH, "//ul[1]//*[contains(@class,'pagination-total-text')]")
            column_member_report_bet_order_cnt = (By.XPATH, "//tr[contains(@class,'level-0')]/td[2]")
            column_member_report_bet_amount = (By.XPATH, "//tr[contains(@class,'level-0')]/td[3]")
            column_member_report_valid_bet_amount = (By.XPATH, "//tr[contains(@class,'level-0')]/td[4]")
            column_member_report_bonus_amount = (By.XPATH, "//tr[contains(@class,'level-0')]/td[5]")
            column_member_report_win_loss_amount = (By.XPATH, "//tr[contains(@class,'level-0')]/td[6]")
            column_member_report_deposit_account = (By.XPATH, "//tr[contains(@class,'level-0')]/td[7]")
            column_member_report_deposit_amount = (By.XPATH, "//tr[contains(@class,'level-0')]/td[7]")
            column_member_report_withdrawal_amount = (By.XPATH, "//tr[contains(@class,'level-0')]/td[8]")
            column_member_report_depwith_amount = (By.XPATH, "//tr[contains(@class,'level-0')]/td[9]")
            column_member_report_deduction_amount = (By.XPATH, "//tr[contains(@class,'level-0')]/td[10]")
            column_member_report_rmaddition_amount = (By.XPATH, "//tr[contains(@class,'level-0')]/td[11]")
            column_member_report_prepayment_amount = (By.XPATH, "//tr[contains(@class,'level-0')]/td[12]")
            column_member_report_returnpoint_amount = (By.XPATH, "//tr[contains(@class,'level-0')]/td[13]")
            column_member_report_fee = (By.XPATH, "//tr[contains(@class,'level-0')]/td[14]")
            column_member_report_administration_fee = (By.XPATH, "//tr[contains(@class,'level-0')]/td[15]")
            column_member_report_member_balance = (By.XPATH, "//tr[contains(@class,'level-0')]/td[16]")
            column_member_report_totalwinloss_amount = (By.XPATH, "//tr[contains(@class,'level-0')]/td[17]")
            subtotal_member_cnt = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[1]")  # 会员帐号数
            subtotal_member_bet_order_cnt = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[2]")  # 订单量
            subtotal_member_bet_amount = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[3]")  # 投注金额
            subtotal_member_valid_bet_amount = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[4]")  # 有效投注金额
            subtotal_member_bonus_amount = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[5]")  # 结算金额
            subtotal_member_win_loss_amount = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[6]")  # 派彩(输赢)
            subtotal_member_account = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[7]")
            subtotal_member_deposit_amount = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[8]")  # 充值金额
            subtotal_member_withdrawal_amount = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[9]")  # 提现金额
            subtotal_member_depwith_amount = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[10]")  # 存提差
            subtotal_member_deduction_amount = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[11]")  # 扣款金额
            subtotal_member_rmaddition_amount = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[12]")  # 风控补分
            subtotal_member_prepayment_amount = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[13]")  # 优惠金额
            subtotal_member_returnpoint_amount = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[14]")  # 返点
            subtotal_member_fee = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[15]")  # 站台手续费
            subtotal_member_administration_fee = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[16]")  # 行政费
            subtotal_member_member_balance = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[17]")  # 会员余额
            subtotal_member_totalwinloss_amount = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[18]")  # 会员盈亏

            # # 平台報表
            column_op_report_agent_bet_amount = (By.XPATH, "//*[contains(@class,'level-0')]//td[@class='ant-table-cell'"
                                                           " and contains(text(),*)][2]")
            column_op_report_agent_validbet_amount = (
                By.XPATH, "//*[contains(@class,'level-0')]//td[@class='ant-table-cell'"
                          " and contains(text(),*)][3]")
            column_op_report_agent_bonus_amount = (
                By.XPATH, "//*[contains(@class,'level-0')]//td[@class='ant-table-cell'"
                          " and contains(text(),*)][4]")
            column_op_report_agent_winloss_amount = (
                By.XPATH, "//*[contains(@class,'level-0')]//td[@class='ant-table-cell'"
                          " and contains(text(),*)][5]")
            subtotal_op_report_agent_deposit_account = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[1]")
            subtotal_op_report_agent_deposit_amount = (
                By.XPATH, "(//*[@class='ant-statistic-content-value'])[2]")  # 充值金额
            subtotal_op_report_agent_fee = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[3]")  # 手续费
            subtotal_op_report_agent_administration_fee = (
                By.XPATH, "(//*[@class='ant-statistic-content-value'])[4]")  # 行政费
            subtotal_op_report_agent_withdrawal_amount = (
                By.XPATH, "(//*[@class='ant-statistic-content-value'])[5]")  # 提现金额
            subtotal_op_report_agent_depwith_amount = (
                By.XPATH, "(//*[@class='ant-statistic-content-value'])[6]")  # 存提差
            subtotal_op_report_agent_rmde_amountnt = (
                By.XPATH, "(//*[@class='ant-statistic-content-value'])[7]")  # 扣款金额
            subtotal_op_report_agent_rmadd_amount = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[8]")  # 风控补分
            subtotal_op_report_agent_balance_amount = (
                By.XPATH, "(//*[@class='ant-statistic-content-value'])[9]")  # 会员余额
            subtotal_op_report_agent_bet_account = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[10]")
            subtotal_op_report_agent_bet_amount = (By.XPATH, "(//*[@class='ant-statistic-content-value'])[11]")  # 投注金额
            subtotal_op_report_agent_validbet_amount = (
                By.XPATH, "(//*[@class='ant-statistic-content-value'])[12]")  # 有效投注金额
            subtotal_op_report_agent_bonus_amount = (
                By.XPATH, "(//*[@class='ant-statistic-content-value'])[13]")  # 结算金额
            subtotal_op_report_agent_winloss_amount = (
                By.XPATH, "(//*[@class='ant-statistic-content-value'])[14]")  # 派彩(输赢)
            subtotal_op_report_agent_preferential_amount = (
                By.XPATH, "(//*[@class='ant-statistic-content-value'])[15]")  # 优惠金额
            subtotal_op_report_agent_returnpoint_amount = (
                By.XPATH, "(//*[@class='ant-statistic-content-value'])[16]")  # 返点
            subtotal_op_report_agent_commission_amount = (
                By.XPATH, "(//*[@class='ant-statistic-content-value'])[17]")  # 代理分红
            subtotal_op_report_agent_totalwinloss_amount = (
                By.XPATH, "(//*[@class='ant-statistic-content-value'])[18]")  # 平台利润


if __name__ == '__main__':
    pass
