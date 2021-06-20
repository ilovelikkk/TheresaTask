import os

def start_test():
    feature_name = "Task1_UIAutomation.feature"
    # feature_name="Task2_APIAutomation.feature"
    file_path="features/"+feature_name


    behave_str = "behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results {file_path}".format(file_path=file_path)

    a = os.system(behave_str)

    htmlStr = "allure generate --clean reports/allure-results"
    os.system(htmlStr)
    allureStr = "allure open allure-report"
    os.system(allureStr)

if __name__ == '__main__':
    start_test()