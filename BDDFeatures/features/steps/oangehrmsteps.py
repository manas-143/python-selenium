from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions





@given('launch chome browser')
def launchbrowser(context):
    context.driver = webdriver.Chrome()



@when('open OrangeHRM homepage')
def openhomepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")



@then('verify that the logo present on page')
def verifylogo(context):
    try:
        wait = WebDriverWait(context.driver, 5)
        result = wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//div[@class="orangehrm-login-logo"]/child::img'))).is_displayed()
    except:
        # context.driver.close()
        assert False,'Test Failed Logo Not Visible'




@then('close browser')
def closebrowser(context):
    context.driver.close()

