from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome()
driver.get('https://www.orangehrm.com/orangehrm-30-day-trial/')
ele=driver.find_element(By.ID,'Form_getForm_Country')
# sel=Select(ele)
# sel.select_by_index(3) #It will select based on the index position
# sel.select_by_value('Belarus')  #It will select based on value attribute
# sel.select_by_visible_text('Bouvet Island') #It will select based on external Text
#I am Just Checking It is Taking all index value or not
#After competion of all index handling error using exception handling
# try:
#     i=1
#     while True:
#         sel.select_by_index(i)
#         i+=1
# except:
#     print('Selection Completed')
# time.sleep(10)
# all_val=list(sel.options)
# for i in all_val:
#     print(i.text)

#Another Way To Check Dropdown is working or not
# def dropdown(obj):
#     sel=Select(obj)
#     all_val=list(sel.options)
#     all_val[10]='Hii'  #Inserted Additional Option to Check Whether It is Taking Or Not
#     try:
#         for i in all_val:
#             sel.select_by_visible_text(i.text)
#     except:
#         print('Element Not In DropDown')
# dropdown(ele)


#Function To Take Any DropDown And To create its obj
# def dropdown_fun(obj,val):
#     select=Select(obj)
#     for i in select.options:
#         if i.text==val:
#             select.select_by_visible_text(val)
#             print('Search Matched')
#             break
#     else:
#         print('Given Value Not Found In DropDown : ')
# dropdown_fun(ele,'Hii')
# time.sleep(10)

#Without Using Select Method
all_dropdown_val=driver.find_elements(By.XPATH,"//select[@class='dropdown']/option")
print(len(all_dropdown_val))


def dropdown_fun(obj,val):
    for i in val:
        if i.text==val[10].text:
            i.click()
            print('Search Matched')
            break
    else:
        print('Given Value Not Found In DropDown : ')
dropdown_fun(ele,all_dropdown_val)
time.sleep(10)

driver.close()


