import os


def start_test():
    # ========Control to run which feature
    feature_name = "Task1_UIAutomation.feature"
    # feature_name="Task2_APIAutomation.feature"
    file_path = "features/" + feature_name

    # generate the command line to run
    behave_str = "behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results {file_path}".format(
        file_path=file_path)
    os.system(behave_str)

    # allure report generation command line
    allureGenerateStr = "allure generate --clean reports/allure-results"
    os.system(allureGenerateStr)
    # Open the allure report locally, after run with cases, the report will open , when stop the case, the report
    # will close
    allureOpen = "allure open allure-report"
    os.system(allureOpen)


if __name__ == '__main__':
    # ============Framework main entry=================
    start_test()
