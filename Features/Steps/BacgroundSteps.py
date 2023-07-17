import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
@given(u'Open Browser')
def step_impl(context):
    context.driver=webdriver.Chrome()


@when(u'Open Application')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@when(u'Enter Username "{user}" and Password "{pwd}"')
def step_impl(context,user,pwd):
    wait=WebDriverWait(context.driver,10)
    wait.until(e.presence_of_element_located((By.XPATH,"//input[@name='username']"))).send_keys(user)
    wait.until(e.presence_of_element_located((By.XPATH,"//input[@name='password']"))).send_keys(pwd)

@when(u'Click On Login')
def step_impl(context):
    wait=WebDriverWait(context.driver,10)
    wait.until(e.presence_of_element_located((By.XPATH,"//button[@type='submit']"))).click()


@then(u'User Must Login To Dashboard Page')
def step_impl(context):
    wait=WebDriverWait(context.driver,10)
    try:
        res=wait.until(e.presence_of_element_located((By.XPATH,"//*[@class='oxd-topbar-header-breadcrumb']/child::h6"))).text
    except Exception as msg:
        context.driver.close()
        print(msg)
    if res=='Dashboard':
        context.driver.close()
        print('Test Passed')

@when(u'Click to Myinfo')
def step_impl(context):
    wait=WebDriverWait(context.driver,20)
    wait.until(e.presence_of_element_located((By.XPATH,"(//a[@class='oxd-main-menu-item active'])[1]"))).click()
    time.sleep(5)

@then(u'Close Window')
def step_impl(context):
    context.driver.close()