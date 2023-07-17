from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions




@given(u'I launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()

@when(u'I opened OrangeHRM homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@when(u'Enter the username "{user}" and password "{pwd}"')
def step_impl(context,user,pwd):
    wait = WebDriverWait(context.driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//input[@name="username"]'))).send_keys(user)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//input[@name="password"]'))).send_keys(pwd)


@when(u'Click on log-in button')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//button[@type="submit"]').click()


@then(u'User must successfully login to the Dashboard')
def step_impl(context):
    wait=WebDriverWait(context.driver,10)
    try:
        name=wait.until(expected_conditions.presence_of_element_located((By.XPATH,'//h6[@class="oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module"]'))).text
    except:
        context.driver.close()
        assert False, "Test case Failed"
    if name == "Dashboard":
        context.driver.close()
        assert True, "test case passed"

@when(u'navigate to search page')
def step_impl(context):
    wait=WebDriverWait(context.driver,10)
    try:
        name=wait.until(expected_conditions.presence_of_element_located((By.XPATH,'//h6[@class="oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module"]'))).text
    except:
        context.driver.close()
        assert False, "Test case Failed"
    if name == "Dashboard":
        context.driver.close()
        assert True, "test case passed"



@then(u'search page should display')
def step_impl(context):
    assert True



@when(u'navigate to Advanced search page')
def step_impl(context):
    assert True


@then(u'Advanced search page should display')
def step_impl(context):
    assert True
