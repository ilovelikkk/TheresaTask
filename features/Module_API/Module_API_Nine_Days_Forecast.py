from behave import when, Then


@Then('I can get relative humidity for the day after tomorrow')
def step_impl(context):
    context.execute_steps('''
            when I should know date when it is the day after 2 days from today
            Then I can get relative humidity with the date I know before
        ''')
