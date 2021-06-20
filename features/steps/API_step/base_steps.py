import datetime
import allure
import requests
from behave import when, Then
from lib.base_functions import ifEqual


# Use get method to send request, store the respond and status code
@when('I send a request with Get method')
def step_impl(context):
    context.step.name = context.step.name
    with allure.step(context.step.name):
        url = context.page[context.scenario.name]["url"]
        headers = context.page[context.scenario.name]["headers"]
        encoding = context.page[context.scenario.name]["encoding"]
        r = requests.get(url=url, headers=headers)
        r.encoding = encoding
        context.respond = r.json()
        context.status_code = r.status_code
        with allure.step("Respond body is " + r.text):
            assert True


# Verify the expect status code
@Then('Verify the status code')
def step_impl(context):
    context.step.name = context.step.name
    with allure.step(context.step.name):
        expect_status_code = context.page[context.scenario.name]["expect_status_code"]
        ifEqual(expect_status_code, context.status_code)


# Get the date with parameter, example, the day after tomorrow = after 2 days from today
@when('I should know date when it is the day after {num} days from today')
def step_impl(context, num):
    context.step.name = context.step.name
    with allure.step(context.step.name):
        cur = datetime.datetime.now()
        days = int(num)
        delta = datetime.timedelta(days=days)
        expectDay = cur + delta
        expectDate = expectDay.strftime("%Y%m%d")
        context.expectDate = expectDate
        print(context.expectDate)
        with allure.step("Expect date is " + expectDate):
            assert True


# Get the mix and max relative humidity from the date get before
@Then('I can get relative humidity with the date I know before')
def step_impl(context):
    context.step.name = context.step.name
    with allure.step(context.step.name):
        max_rh = ""
        min_rh = ""
        data = context.respond
        for i in data["forecast_detail"]:
            # print(i)
            if i["forecast_date"] == context.expectDate:
                max_rh = i["max_rh"]
                min_rh = i["min_rh"]
                break
        with allure.step("The relative humidity is from " + str(min_rh) + "% to " + str(max_rh) + "%."):
            assert True
