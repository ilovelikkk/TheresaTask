import os
import allure
from selenium import webdriver


# This is to store some other functions that will be use in base steps

# Open browser with chrome driver
def open_browser():
    basepath = os.path.dirname(os.path.dirname(__file__))
    driver_path = basepath + '/lib/chromedriver.exe'
    # desired_capabilities = DesiredCapabilities.CHROME  # 修改页面加载策略
    # desired_capabilities["pageLoadStrategy"] = "none"  # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(driver_path, options=options)
    driver.maximize_window()
    return driver


# Close browser
def close_browser(driver):
    driver.quit()


# Click by JS
def clickByJquery(driver, css):
    js = '$("' + css + '").click()'
    driver.execute_script(js)


def setXpathByText(title):
    newTitle = '//*[contains(text(),"' + title + '")]'
    return newTitle


# def actionChainsClick(driver,btn):
#     action = ActionChains(driver)
#     action.click(btn)
#     action.perform()

# Verify two data is equal or not
def ifEqual(expect, actual):
    if str(expect) == str(actual):
        with allure.step("Verify pass. Expect result is " + str(expect) + ", Actual result is " + str(actual)):
            assert True
    else:
        with allure.step("Verify failed. Expect result is " + str(expect) + ", Actual result is " + str(actual)):
            assert False
