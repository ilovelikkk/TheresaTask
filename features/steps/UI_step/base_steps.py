import allure
from behave import given, when, then
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from lib.base_functions import *


# Click action
@when('I click {somewhere} by the {attribute}')
def step_impl(context, somewhere, attribute):
    # context.step.name=context.step.name
    with allure.step(context.step.name):
        elementValue = context.page[somewhere][attribute]
        context.driver.find_element(attribute, elementValue).click()


# Sendkey action
@when('I input {someword} to the {component} by the {attribute}')
def step_impl(context, someword, component, attribute):
    with allure.step(context.step.name):
        elementValue = context.page[component][attribute]
        context.driver.find_element(attribute, elementValue).send_keys(someword)


# Verify element exist action
@then('I should see the {component} exist by the {attribute}')
def step_impl(context, component, attribute):
    with allure.step(context.step.name):
        elementValue = context.page[component][attribute]
        try:
            element = WebDriverWait(context.driver, 15).until(
                EC.presence_of_element_located((attribute, elementValue))
            )
            assert True
        except:
            assert False


# Click by jquery
@when('I use js click with {somewhere} by the {attribute}')
def step_impl(context, somewhere, attribute):
    with allure.step(context.step.name):
        elementValue = context.page[somewhere][attribute]
        sleep(1)
        # context.driver.find_element(attribute, elementValue).click()
        clickByJquery(context.driver, elementValue)


# browser back
@when('I want the browser back to the last page')
def step_impl(context):
    with allure.step(context.step.name):
        context.driver.back()