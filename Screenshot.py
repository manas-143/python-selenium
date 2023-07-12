from selenium import webdriver
from selenium.webdriver.common.by import By
import time
options=webdriver.ChromeOptions()
options.headless=True
driver=webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get('https://www.reddit.com/')
# driver.get_screenshot_as_file('reddit_1.png')
'''Full Screenshot'''
S=lambda X:driver.execute_script('return document.body.parentNode.scroll'+X)

driver.find_element(By.TAG_NAME,'body').screenshot('reddit_full_body_scrnst1'
                                                   '.png')
time.sleep(2)
driver.close()