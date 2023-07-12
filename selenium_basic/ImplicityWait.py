from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

#implicity wait is a dynamic wait for all the web element

#it caan only be applid when we use web elements
driver.implicitly_wait(10)
driver.get("https://app.hubspot.com/login/")
print(driver.title)

#the main disadvantage of this web element is it only apply o webelements not in title, urls, alerts..mainly non-web elements

