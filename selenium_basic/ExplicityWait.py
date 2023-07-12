from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

#for explicity wait we have to use webdriverwait which can be import from above module
driver = webdriver.Chrome()
driver.get("https://app.hubspot.com/login/")
#stored it in a variable..it takes  two arguement one for webdriver another for time
wait=WebDriverWait(driver,10)

#below functions for checking the non-web element , title
wait.until(ec.title_is("HubSpot Login"))
wait.until(ec.title_contains("HubSpot Login"))
#checking for url
wait.until(ec.url_contains("https://app.hubspot.com/login/"))
wait.until(ec.url_to_be("https://app.hubspot.com/login/"))


# for web elements
email = wait.until(ec.visibility_of_element_located((By.XPATH,'//div[@class="private-form__input-wrapper"]/child::input[1]')))
email.send_keys('test@123.com')
passd = wait.until(ec.presence_of_element_located((By.XPATH,"//div[@class='private-form__input-wrapper']/child::input[@id='password']")))
passd.send_keys('test123')




driver.close()
