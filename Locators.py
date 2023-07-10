#Module Needed for Testing
import re
from selenium import webdriver
#Webdriver is needed to communicate with web browser for different web browser web driver are also differrent
from selenium.webdriver.common.by import By
#By is used to access locators
import time
driver=webdriver.Chrome()
#driver is an object for Chrome Class
driver.get('https://www.orangehrm.com/orangehrm-30-day-trial/')
#Using ID Lccator to fill username
driver.maximize_window() #To maximize window view
favname=driver.find_element(By.ID,'Form_getForm_subdomain')
favname.send_keys('Sudhanshu@3231')
#find_element is use to find the element based on the given locators
#send_keys is used to send some value
FullName=driver.find_element(By.ID,'Form_getForm_Name')
name=input('Enter Your Name : ')
if re.search('[A-Z][a-z]+\s{1}[A-Z][a-z]+',name):
    FullName.send_keys(name)
    driver.implicitly_wait(10)
else:
    raise Exception('Enter Valid Name First : ')
Email=driver.find_element(By.CSS_SELECTOR,"input[name='Email']")
email=input('Enter Your EmailId ')
if re.search('\w+\d*@\w*\d*',email):
    Email.send_keys(email)
    driver.implicitly_wait(10)
else:
    raise Exception('Email Is Not Valid')
PhnNum=driver.find_element(By.ID,'Form_getForm_Contact')
num=input('Enter Your Phone Number: ')
if len(num)==10 and re.search('[789]\d{9}',num):
    PhnNum.send_keys(num)
    driver.implicitly_wait(10)
else:
    raise Exception('Phone Number Is Not Valid')
#In Above Code I Have Use some regular expression Technique to satify the requirement
#Name-If Name First Word Start with capital letter and after one space also It Should Start with One letter
#Email- Email Should Start with anycharacter except Special Character and it must have @ and after that it maybe or may not be any character or digit
#Phone Number -Phone Number Should be of length 10 and start with digit 7,8,9




time.sleep(10)
driver.close()
