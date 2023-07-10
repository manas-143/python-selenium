from selenium import webdriver
#webdriver is one of the component or module in selenium. To work with webdriver we have to import it from selenium
import time
#for slowing the time process while execution
import re
#we import regular expression to validate the user name and password
from selenium.webdriver.common.by import By
#to use locator we have to import By

driver= webdriver.Chrome()
#declaring the path of chrome driver.

driver.get("https://www.facebook.com/login/")
driver.implicitly_wait(5)
#.get is used to access the webpage
mail = driver.find_element(By.ID, "email")
pawd = driver.find_element(By.ID, "pass")
name = input("enter name: ")
pswd= input("enter pawd")
if re.search("[a-z][0-9]*@gmail.com",name):
    mail.send_keys(name)
else:
    raise Exception('Please Enter Valid EmailId')
if len(pswd)>9:
    pawd.send_keys(pswd)
else:
    raise Exception('Please check password')
driver.find_element(By.ID, 'loginbutton').click()
time.sleep(20)
driver.close()
#print the webpage title on terminal
driver.quit()
