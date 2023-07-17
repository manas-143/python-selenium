from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@given('I launch chome browser')
def browser_launch(context):
    context.driver = webdriver.Chrome()


@when('I open OrangeHRM homepage')
def open_homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@when('Enter username "{user}" and password "{pwd}"')
def inp_name(context,user,pwd):
    wait=WebDriverWait(context.driver,10)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//input[@name="username"]'))).send_keys(user)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//input[@name="password"]'))).send_keys(pwd)


@when('Click on login button')
def click_ele(context):
    context.driver.find_element(By.XPATH,'//button[@type="submit"]').click()


@then('User must successfully login to the Dashboard page')
def check_ele(context):
    wait=WebDriverWait(context.driver,10)
    try:
        name=wait.until(expected_conditions.presence_of_element_located((By.XPATH,'//h6[@class="oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module"]'))).text
    except:
        context.driver.close()
        assert False, "Test case Failed"
    if name == "Dashboard":
        context.driver.close()
        assert True, "test case passed"

