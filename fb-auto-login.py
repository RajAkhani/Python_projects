from selenium import webdriver
from time import sleep

usr='#ur_email_id'
pwd='#ur_passwprd'

driver=webdriver.Chrome('D:\python\chromedriver_ver89\chromedriver')
driver.get('https://www.facebook.com/')
print("Opened fb")
sleep(1)

username_box=driver.find_element_by_id('email')
username_box.send_keys(usr)
print("email id entered")
sleep(1)

password_box=driver.find_element_by_id('pass')
password_box.send_keys(pwd)
print("password entered")

login_box=driver.find_element_by_name('login')
login_box.click()
print("done")
