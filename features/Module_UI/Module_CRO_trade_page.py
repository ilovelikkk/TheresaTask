from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium import webdriver
from time import sleep


@when('Navigate to homepage')
def step_impl(context):
    context.driver.implicitly_wait(15)
    context.driver.get('https://crypto.com/exchange')

@when('See whether we already in CRO trade page')
def step_impl(context):
    context.execute_steps('''
        when Navigate to homepage
        when I click CROMarket by the xpath
        then I should see the ETHCROLink exist by the xpath
        when I use js click with CroUsdcLink by the css
    ''')




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
        then I should see the CroUsdeChannel exist by the xpath
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
