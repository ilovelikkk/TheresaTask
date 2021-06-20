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
        with allure.step("Click element: its " + attribute + " is " + elementValue):
            assert True


# Sendkey action
@when('I input {someword} to the {component} by the {attribute}')
def step_impl(context, someword, component, attribute):
    with allure.step(context.step.name):
        elementValue = context.page[component][attribute]
        context.driver.find_element(attribute, elementValue).send_keys(someword)
        with allure.step("Input text :" + someword + ". Send to element: its " + attribute + " is " + elementValue):
            assert True


# Verify element exist action
@then('I should see the {component} exist by the {attribute}')
def step_impl(context, component, attribute):
    with allure.step(context.step.name):
        elementValue = context.page[component][attribute]
        try:
            element = WebDriverWait(context.driver, 15).until(
                EC.presence_of_element_located((attribute, elementValue))
            )
            with allure.step("Element find! its " + attribute + " is :" + elementValue):
                assert True
        except:
            with allure.step("Element not find! its " + attribute + " is :" + elementValue):
                assert False


# Click by jquery
@when('I use js click with {somewhere} by the {attribute}')
def step_impl(context, somewhere, attribute):
    with allure.step(context.step.name):
        elementValue = context.page[somewhere][attribute]
        sleep(1)
        # context.driver.find_element(attribute, elementValue).click()
        clickByJquery(context.driver, elementValue)
        with allure.step("Click element: its " + attribute + " is :" + elementValue):
            assert True


# browser back
@when('I want the browser back to the last page')
def step_impl(context):
    with allure.step(context.step.name):
        context.driver.back()


# Verify the element contains the text we want
@then('I can see the {text} exist with the {component} by the {attribute}')
def step_impl(context, text, component, attribute):
    with allure.step(context.step.name):
        elementValue = context.page[component][attribute]
        locator = (attribute, elementValue)
        result = EC.text_to_be_present_in_element(locator, text)(context.driver)
        if result:
            with allure.step("Element contains the text of " + text + "! its " + attribute + " is " + elementValue):
                assert True
        else:
            with allure.step(
                    "Element do not contains the text of " + text + "! its " + attribute + " is " + elementValue):
                assert False


# Switch to iframe
@when('I can switch to the iframe of {component} by the {attribute}')
def step_impl(context, component, attribute):
    with allure.step(context.step.name):
        elementValue = context.page[component][attribute]
        iframer= context.driver.find_element(attribute, elementValue)
        context.driver.switch_to.frame(iframer)
        with allure.step("Switch to iframe,  its " + attribute + " is " + elementValue):
            assert True


# Switch to iframe
@when('I can switch out of the iframe')
def step_impl(context):
    with allure.step(context.step.name):
        context.driver.switch_to.default_content()
        with allure.step("Switch back to the main page."):
            assert True
