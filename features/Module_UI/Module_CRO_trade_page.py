from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium import webdriver
from time import sleep


# This is the module for CRO trade page


@when('Navigate to homepage')
def step_impl(context):
    context.driver.implicitly_wait(15)
    context.driver.get('https://crypto.com/exchange')


@when('Navigate to CRO trade page')
def step_impl(context):
    context.execute_steps('''
        when Navigate to homepage
        when I click CROMarket by the xpath
        then I should see the ETHCROLink exist by the xpath
        when I use js click with CroUsdcLink by the css
    ''')


@then('Verify the CRO trade page is showing')
def step_impl(context):
    context.execute_steps('''
        then I should see the CroUsdcChannel exist by the xpath
    ''')


@then('Verify the CRO trade page header is showing')
def step_impl(context):
    context.execute_steps('''
        then I should see the CryptoLogo exist by the xpath
        then I should see the MarketsLink exist by the xpath
        then I should see the SpotLink exist by the xpath
        then I should see the DerivativesLink exist by the xpath
        then I should see the LendingLink exist by the xpath
        then I should see the LoginLink exist by the xpath
        then I should see the SigninLink exist by the xpath
        then I should see the LanguageLink exist by the xpath
        then I should see the ReferAndGetLink exist by the xpath
        
    ''')


@then('Verify login button in Buy CRO module')
def step_impl(context):
    context.execute_steps('''
        then I should see the LoginBtn_BuyCRO exist by the xpath
        when I click LoginBtn_BuyCRO by the xpath
        then I should see the Login_page_title exist by the xpath
        when I want the browser back to the last page
        then I should see the LoginBtn_SellCRO exist by the xpath
        when I click LoginBtn_SellCRO by the xpath
        then I should see the Login_page_title exist by the xpath
    ''')


@then('Verify the TV trade chart module is showing')
def step_impl(context):
    context.execute_steps('''
        then I should see the Tv_chart_Module exist by the id
        then I should see the Tv_chart_iframe exist by the xpath
        when I can switch to the iframe of Tv_chart_iframe by the xpath
        then I should see the Tv_chart_container exist by the xpath
        then I should see the Tv_chart_tool exist by the xpath
        when I can switch out of the iframe
    ''')


@then('Verify the order book module is showing')
def step_impl(context):
    context.execute_steps('''
        then I should see the OrderBook_title exist by the xpath
        then I should see the OrderBook_Price(USDC) exist by the xpath
        then I should see the OrderBook_Amount(CRO) exist by the xpath
        then I should see the OrderBook_Total(CRO) exist by the xpath
        then I should see the OrderBook_current_price exist by the xpath
        then I should see the OrderBook_Filter_all exist by the xpath
        then I should see the OrderBook_Filter_green exist by the xpath
        then I should see the OrderBook_Filter_red exist by the xpath
    ''')


@then('Verify the Trading History module is showing')
def step_impl(context):
    context.execute_steps('''
        then I should see the TradeHistory_title exist by the xpath
        then I should see the TradeHistory_Price(USDC) exist by the xpath
        then I should see the TradeHistory_Amount(CRO) exist by the xpath
        then I should see the TradeHistory_time exist by the xpath
        then I should see the TradeHistory_list exist by the xpath
    ''')


@then('Verify the current trade info is showing')
def step_impl(context):
    context.execute_steps('''
        then I should see the CurrentInfo_last_price exist by the xpath
        then I can see the Change exist with the CurrentInfo_Change by the xpath
        then I can see the High exist with the CurrentInfo_High_price by the xpath
        then I can see the Low exist with the CurrentInfo_Low_price by the xpath
        then I can see the 24H exist with the CurrentInfo_24H_Vol by the xpath
    ''')


@when('Navigate to Open Order in the Order list box module')
def step_impl(context):
    context.execute_steps('''
        then I should see the Order_list_box exist by the xpath
        when I click OpenOrder_btn by the xpath
        then I should see the OpenOrder_table exist by the xpath
    ''')


@then('Verify the Open Order module is showing')
def step_impl(context):
    context.execute_steps('''
        then I can see the Time exist with the OpenOrder_table by the xpath
        then I can see the Direction exist with the OpenOrder_table by the xpath
        then I can see the Pair exist with the OpenOrder_table by the xpath
        then I can see the Price (USDC) exist with the OpenOrder_table by the xpath
        then I can see the Average exist with the OpenOrder_table by the xpath
        then I can see the Price exist with the OpenOrder_table by the xpath
        then I can see the Executed exist with the OpenOrder_table by the xpath
        then I can see the Unexecuted exist with the OpenOrder_table by the xpath
        then I can see the Trigger exist with the OpenOrder_table by the xpath
        then I can see the Condition exist with the OpenOrder_table by the xpath
        then I can see the Action exist with the OpenOrder_table by the xpath
    ''')


@when('Navigate to Order History in the Order list box module')
def step_impl(context):
    context.execute_steps('''
        then I should see the Order_list_box exist by the xpath
        when I click OrderHistory_btn by the xpath
        then I should see the OrderHistory_table exist by the xpath
    ''')


@then('Verify the Order History module is showing')
def step_impl(context):
    context.execute_steps('''
        then I should see the OrderHistory_filter exist by the css
        then I can see the Time exist with the OrderHistory_table by the xpath
        then I can see the Order exist with the OrderHistory_table by the xpath
        then I can see the ID exist with the OrderHistory_table by the xpath
        then I can see the Direction exist with the OrderHistory_table by the xpath
        then I can see the Pair exist with the OrderHistory_table by the xpath
        then I can see the Price (USDC) exist with the OrderHistory_table by the xpath
        then I can see the Volume (CRO) exist with the OrderHistory_table by the xpath
        then I can see the Average exist with the OrderHistory_table by the xpath
        then I can see the Status exist with the OrderHistory_table by the xpath
        then I can see the Trigger exist with the OrderHistory_table by the xpath
        then I can see the Condition exist with the OrderHistory_table by the xpath
        then I can see the Action exist with the OrderHistory_table by the xpath
    ''')
