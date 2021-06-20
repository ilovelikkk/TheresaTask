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
Choose to run API or UI?<br>
Change setting in start_test.py:
>feature_name = "Task1_UIAutomation.feature"<br>
feature_name="Task2_APIAutomation.feature"

## 3.Structure introduction
>data  <br> 
>>--UI &nbsp;&nbsp;&nbsp;&nbsp; *store UI test cases data/page element* <br> 
>>--API &nbsp;&nbsp;&nbsp;&nbsp; *store API test cases data* <br>

>feature<br> 
>>--Module_UI  &nbsp;&nbsp;&nbsp;&nbsp;  *The module step with UI testing, call the base steps* <br>
>>--Module_API     &nbsp;&nbsp;&nbsp;&nbsp;       *The module step with API testing, call the base steps* <br>
>>--steps &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *Only store the base step definition*








# 中文配置
## 一.环境配置
### 略
## 二.框架介绍
### 1.文档结构介绍
>data  <br> 
>>--UI 存放UI的page element <br> 
>>--API 存放API的data <br>

>features


