from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  Select
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.orangehrm.com/en/30-day-free-trial")
Dropdown = driver.find_element(By.ID,"Form_getForm_Country")
# select = Select(Dropdown)
# val=select.options
# val[10]='Bangalore'
# try:
#     for i in val:
#         select.select_by_visible_text(i.text)
# except:
#     print("error occured")
# time.sleep(10)
# driver.quit()

def dropdown(obj,arg):
    select=Select(obj)
    for val in select.options:
        if arg == val.text:
            val.click()
            print("Successfully Passed")
            break
    else:
        print("invalid option")
dropdown(Dropdown,"India")
time.sleep(10)


