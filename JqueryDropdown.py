from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver=webdriver.Chrome()
driver.get('https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/')
driver.find_element(By.ID,'justAnInputBox').click()
dw_ele=driver.find_elements(By.CSS_SELECTOR,"span.comboTreeItemTitle")
#There is no select tag for jquery drodown so we use xpath to get all the value of span tag with same class Name
#So we can filter dropdown values
print(len(dw_ele))
#Checking All Value of dropdown
for val in dw_ele:
    print(val.text)

Checking Single Checkbox is Working Or Not
for val in dw_ele:
    if val.text=='choice 1':
        val.click()
        print('Working Fine')
        break
else:
    raise Exception('Bug Found In Single Selecting CheckBox')

#Checking For Multiple Checkbox Working Or Not
el=['choice 6 2 1','choice 7']
for val in dw_ele:
    if val.text in el:
        val.click()
        time.sleep(2)
        el.remove(val.text)
    if el==[]:
        print('All Test Cases Passed Successfully : ')
        break
else:
    raise Exception('Bugs Found in Selecting Multiple Checkbox')

#For selecting All checkbox
copy_dw_ele=[val.text for val in dw_ele if val.text!=' ']
try:
    for val in dw_ele:
        if val.text == ' ':
            continue
        if val.text in copy_dw_ele:
            val.click()
            copy_dw_ele.remove(val.text)
            time.sleep(2)
        if copy_dw_ele == []:
            print('Passed successfully :')
            break
    else:
        raise Exception('Bug Found In Selecting All Checkbox')
except Exception as msg:
    print(msg)


#Function To Check All Test Cases Like for Single,Multiple and All
def dropdown_check(element,value):
    if 'all' in value:
        try:
            for val in dw_ele:
                val.click()
                time.sleep(1)
        except Exception as msg:
            print(msg)
    else:
        for val in dw_ele:
            if val.text in value:
                val.click()
                value.remove(val.text)
            if value==[]:
                print('All Test Cases Passed ')
                break
        else:
            print('Bugs Found ')



dropdown_check(dw_ele,['choice 6 1'])
dropdown_check(dw_ele,['choice 6 1',dw_ele[3].text,dw_ele[5].text])
dropdown_check(dw_ele,['all'])



time.sleep(2)