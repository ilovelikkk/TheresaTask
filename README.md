# English Setting
## * 1.Environment setup
### Install:
pip install behave<br>
pip install allure-behave<br>
pip install request<br>
Download allure and add it to system path: https://github.com/allure-framework/allure2/releases <br>
UI test use chrome browser to run. The chromedriver is in the project. Location: /lib/chromedriver.exe<br>
chromedriver version: 91<br>
## 2.Run TEST
### python run with start_test.py
Choose to run API or UI:<br>
Change setting in start_test.py:
>feature_name = "Task1_UIAutomation.feature"<br>
>feature_name = "Task2_APIAutomation.feature" <br>




## 3.Structure introduction
> ___data___  <br> 
>>--UI &nbsp;&nbsp;&nbsp;&nbsp; *store UI test cases data/page element* <br> 
>>--API &nbsp;&nbsp;&nbsp;&nbsp; *store API test cases data* <br>

> ___feature___  <br> 
>>--Module_UI  &nbsp;&nbsp;&nbsp;&nbsp;  *The module step with UI testing, call the base steps* <br>
>>--Module_API     &nbsp;&nbsp;&nbsp;&nbsp;       *The module step with API testing, call the base steps* <br>
>>--steps &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *Only store the base step definition* <br>
>>--environment.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *Environment setting* <br>
>>--Task1_UIAutomation.feature &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  *Test cases for UI testing task1* <br>
>>--Task2_APIAutomation.feature &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  *Test cases for API testing task2* <br>

>lib &nbsp;&nbsp;&nbsp;&nbsp;  *Store some setting functions, don't care* <br>
>report &nbsp;&nbsp;&nbsp;&nbsp;  *Store temp allure report json data, don't care* <br>
> ___start_test.py___ &nbsp;&nbsp;&nbsp;&nbsp;  ***Framework main start function*** <br>


## 4.How case run
Design: feature file > Module_UI(Module_API) > steps(base_steps.py) <br>
**Feature file example :**
```gherkin
Feature: UI-Automation for CRO/USDC trade page
  Scenario: Navigate to CRO/USDC trade page
    When Navigate to CRO trade page
    Then Verify the CRO trade page is showing
```

feature call the step from Module_UI: <br>
**Module file example:** <br> 
```python
@when('Navigate to CRO trade page')
def step_impl(context):
    context.execute_steps('''
        when Navigate to homepage
        when I click CROMarket by the xpath
        then I should see the ETHCROLink exist by the xpath
        when I use js click with CroUsdcLink by the css
    ''')
```

Module call the step from base_steps.py <br>
**base_steps file example:** <br>
```python
# Click action
@when('I click {somewhere} by the {attribute}')
def step_impl(context, somewhere, attribute):
    # context.step.name=context.step.name
    with allure.step(context.step.name):
        elementValue = context.page[somewhere][attribute]
        context.driver.find_element(attribute, elementValue).click()
        with allure.step("Click element: its " + attribute + " is " + elementValue):
            assert True
```
### Task Report:
UI: <br>
![](https://github.com/ilovelikkk/HELLO/blob/master/2.png)

API: <br>
![](https://github.com/ilovelikkk/HELLO/blob/master/3.png)

## 5.How to write case
### For UI testing
#### (1)Capture element and write it in below location: data>UI>xxxxx.yaml
yaml data file example
```yaml
LoginBtn_SellCRO:
  xpath: //*[@class="e-tab-pane active"]//*[contains(@class,"trade-block")][2]//button
Tv_chart_Module:
  id: tv_chart_container
```
#### (2)Write your case in feature file
```gherkin
Feature: UI-Automation for CRO/USDC trade page
  Scenario: Navigate to CRO/USDC trade page
    When Navigate to CRO trade page
    Then Verify the CRO trade page is showing
```
#### (3)Write your module in module step file in below location: feature > Module_UI > xxxx.py
Module file use the page data name the you set in the yaml data file.
```python
@when('Navigate to CRO trade page')
def step_impl(context):
    context.execute_steps('''
        when Navigate to homepage
        when I click CROMarket by the xpath
        then I should see the ETHCROLink exist by the xpath
        when I use js click with CroUsdcLink by the css
    ''')
```


#### Use more base step action:
> `Click action` : "I click {somewhere} by the {attribute}" <br> 
`Sendkey action`: "I input {someword} to the {component} by the {attribute}" <br> 
`Verify element action`: "I should see the {component} exist by the {attribute}}" <br> 
`Verify text exist action`: "I can see the {text} exist with the {component} by the {attribute}" <br> 
`Click by js` : "I use js click with {somewhere} by the {attribute}" <br> 
`Switch to iframe`: "I can switch to the iframe of {component} by the {attribute}" <br> 
`Switch back `: "I can switch out of the iframe" <br> 
`Browser back`: "I want the browser back to the last page" <br> 

Continue...

