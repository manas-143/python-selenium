from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time
driver=webdriver.Chrome()
driver.get('https://www.irctc.co.in/nget/train-search')
driver.maximize_window()
driver.implicitly_wait(5)
pnr=driver.find_element(By.LINK_TEXT,'IRCTC EXCLUSIVE')
action=ActionChains(driver)
action.move_to_element(pnr).perform()
ewallet=driver.find_element(By.LINK_TEXT,' IRCTC eWallet')
action.move_to_element(ewallet).perform()
About=driver.find_element(By.LINK_TEXT,'About IRCTC eWallet')
About.click()
time.sleep(20)