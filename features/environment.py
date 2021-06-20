import os
import re

import allure
from selenium import webdriver

from lib.base_functions import *
from lib.parse_yaml import parseyaml


# def before_all(context):


def before_feature(context, feature):
    if re.findall('UI-Automation', context.feature.name):
        context.page = parseyaml("UI")
        context.driver = open_browser()
    else:
        context.page = parseyaml("API")


def after_feature(context, feature):
    if re.findall('UI-Automation', context.feature.name):
        close_browser(context.driver)


# def before_scenario(context, scenario):
#     context.driver = open_browser()
#
# def after_scenario(context, scenario):
#     close_browser(context.driver)
#
#
def before_step(context, step):
    context.step = step


def after_step(context, step):
    if re.findall('UI-Automation', context.feature.name):
        if (context.failed == False):
            allure.attach(context.driver.get_screenshot_as_png(), name=context.step.name,
                          attachment_type=allure.attachment_type.PNG)
