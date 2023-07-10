
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
# driver.get("https://www.amazon.com/")
# img=driver.find_elements(By.TAG_NAME,'img')
# #Find Elements stores all values in form of list
# print(len(img))
# for link in img:
#     print(link.get_attribute('src')) #Print all href link
# driver.get("https:flipkart.com/")
# link=driver.find_elements(By.TAG_NAME,'a')
# print(len(link))
# for i in link:
#     print(i.text)
#     print(i.get_attribute('href'))

#Xpath
driver.get("https://www.amazon.com/")
driver.find_element(By.XPATH,"//img[@alt='Jeans under $50']").click()



