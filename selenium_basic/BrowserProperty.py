from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#browser property is used to navigate through one page to another page and we can also refresh the page
driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://www.amazon.in/")
driver.find_element(By.XPATH,'//div[@id="nav-xshop"]/child::a[2]').click()

#for going back to the page
driver.back()
time.sleep(2)

#for going forword to the page
driver.forward()
time.sleep(2)

#to refresh the page
driver.refresh()
time.sleep(2)
driver.quit()