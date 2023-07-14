import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as ec
import time
arg1=input("enter name")
arg2=input("enter lastname")
arg3=input("enter email")
arg4=input("enter password")
arg5=input("enter dob")
arg6=input("enter month")
arg7=input("enter year")
arg8=int(input("enter: "))
#
driver = webdriver.Chrome()
driver.implicitly_wait(10)
#
#
#
#
#
#
#
#
#
#
#
driver.get("https://www.facebook.com/")

#the path for sign in page and all the paths for the placeholder has stord in variables......
driver.find_element(By.XPATH,'//div[@class="_6ltg"]/child::a').click()
name=driver.find_element(By.XPATH,'//input[@name="firstname"]')
sur_name = driver.find_element(By.XPATH,'//input[@name="lastname"]')
mail = driver.find_element(By.XPATH,'//input[@name="reg_email__"]')
pswd = driver.find_element(By.XPATH,'//input[@name="reg_passwd__"]')

#dob are in dropdown format
dob =  driver.find_element(By.XPATH,'//select[@id="day"]')
sel_dob=Select(dob)
db = sel_dob.options

#dom are in dropdown format
mnth = driver.find_element(By.XPATH,'//select[@id="month"]')
sel_mnth=Select(mnth)
mn = sel_mnth.options

#year in dropdownformat
yer = driver.find_element(By.XPATH,'//select[@id="year"]')
sel_yr=Select(yer)
yr = sel_yr.options

#for selecting gender as they are in radio format we stored all the buttons in a List
gen=driver.find_elements(By.XPATH,'//input[@type="radio"]')

#Final submit button
submit=driver.find_element(By.XPATH,'//div[@class="_1lch"]/child::button')

#Function for checking all the data as the respective places are taking or not
def check(arg1, arg2, arg3, arg4,arg5, arg6, arg7):
    name.send_keys(arg1)
    sur_name.send_keys(arg2)
    mail.send_keys(arg3)
    pswd.send_keys(arg4)

    #as we are writing risky codes so always have to take it in exception handling block
    #if there any issue then  we will able to handle it
    try:
        for i in db:
            if i.text == arg5:
                i.click()
                break
    except Exception as e:
        print(e)

    try:
        for j in mn:
            if j.text == arg6:
                j.click()
                break
    except Exception as e:
        print(e)
    try:
        for k in yr:
            if k.text == arg7:
                k.click()
                break
    except Exception as e:
        print(e)

    #for the selection of gender
    if arg8== 1:
        gen[0].click()
    if arg8== 2:
        gen[1].click()
    if arg8== -1:
        gen[2].click()

    #final submit of the form
    submit.click()
    time.sleep(3)
    driver.quit()

#calling of the functions
check(arg1, arg2, arg3, arg4,arg5,arg6,arg7)


#finding all the active links in fb page
Links=driver.find_elements(By.TAG_NAME,"a")
Link_names={i.text:i.get_attribute("href") for i in Links if i.text}
print(Link_names)
