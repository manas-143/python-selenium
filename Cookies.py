from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get('https://www.reddit.com/')
#To get Cookies we use get_cookies() method
#
print(driver.get_cookies())
#Cookies are stored in form of dictionaries
#If we want to add our own cookies to that we can use add_cookies() method
driver.add_cookie({'name':'Sudhanshu Pandey','domain':'reddit.com','value':'python'})
for i in driver.get_cookies():
    print(i)
