from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get('https://app.hubspot.com/login')
driver.implicitly_wait(10)
#Implicitly_wait is applicable to web_element only (like find_element, find_elements ,click)
#It is global wait applicable to all web_element
#It is not applicable to title,popup etc.(Non-Web Element)
#It can be Overridden
email=driver.find_element(By.XPATH,"//input[@id='username']")
email.send_keys('Sid@123@gmail.com')
pas=driver.find_element(By.XPATH,"//input[@id='password']")
pas.send_keys('1234567')
lgbtn=driver.find_element(By.XPATH,"//button[@id='loginBtn']")
lgbtn.click()
print(driver.title)
driver.close()

#Drawback of Implicit Wait :
#If username will appear in 5 sec only no need to wait for pas and login
#But If we want to solve we have to use implicit_wait() again after the username
#this is overridden
