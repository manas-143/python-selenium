# from behave import *
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions
# @given('launch Chrome Browser')
# def step_impl(context):
#     context.driver=webdriver.Chrome()
# @when(u'I Opened OrangeHRM Login Page')
# def step_impl(context):
#     context.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
#
#
# @when(u'Entered Username "{user}" and Password "{pwd}"')
# def step_impl(context,user,pwd):
#     wait = WebDriverWait(context.driver, 10)
#     wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//input[@name='username']"))).send_keys(user)
#     context.driver.find_element(By.XPATH,"//input[@name='password']").send_keys(pwd)
#
#
# @when(u'Click On Login Button')
# def step_impl(context):
#     context.driver.find_element(By.XPATH,"//button[@type='submit']").click()
#
#
# @then(u'User Must Successfully Login To Dashboard Page')
# def step_impl(context):
#     try:
#         wait=WebDriverWait(context.driver,10)
#         res = wait.until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@class="oxd-topbar-header-breadcrumb"]/child::h6'))).text
#     except:
#         context.driver.close()
#         assert False ,'Failed To Reach DashBoard'
#
#     if res=='Dashboard':
#         context.driver.close()
#         assert True ,'Test Passed'
