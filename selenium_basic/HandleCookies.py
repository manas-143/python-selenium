from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

driver.get("https://www.reddit.com/")

#cookies are small block of data created by a webserver while a user is browsing through a website.

#add cookies are used to add a user cookies to set of cookies. its a temporary format
driver.add_cookie({"name":"manas", "domain":"reddit.com", "value": "12341234"})

#get cookies are used to get the cookies from the website it stores the cookies in form of dict,
cookie = driver.get_cookies()
for item in cookie:
    print(item)