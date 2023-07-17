from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
@given(u'I launch Chrome Browser')
def step_impl(context):
    context.driver=webdriver.Chrome()


@when(u'I Opened OrangeHrm HomePage')
def step_impl(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')


@then(u'Verified Logo is Present or Not')
def step_impl(context):
    try:
        logo = context.driver.find_element(By.XPATH, "//*[@class='orangehrm-login-branding']/child::img").is_displayed()
    except Exception as msg:
        print(msg)
    else:
        print('Logo Is Present On The HomePage')


@then(u'Close The Browser')
def step_impl(context):
    context.driver.close()
