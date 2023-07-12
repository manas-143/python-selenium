from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
driver=webdriver.Chrome()
act_chain=ActionChains(driver)
driver.implicitly_wait(5)

driver.get("https://jqueryui.com/droppable/")

drag = driver.find_element(By.ID,"draggable")
drop = driver.find_element(By.ID, "droppable")

drag.click()
time.sleep(2)
driver.close()