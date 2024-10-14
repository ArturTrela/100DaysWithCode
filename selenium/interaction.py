from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=chrome_opt)
driver.get('http://secure-retreat-92358.herokuapp.com/')

fname_field = driver.find_element(By.NAME, 'fName')
lname_field = driver.find_element(By.NAME, 'lName')
email_field = driver.find_element(By.NAME, 'email')
btn = driver.find_element(By.XPATH, '/html/body/form/button')
fname_field.click()
time.sleep(0.5)
fname_field.send_keys("Artur")
lname_field.click()
time.sleep(0.5)
lname_field.send_keys("Automatyk")
email_field.click()
time.sleep(0.5)
email_field.send_keys("test@test.com")
btn.click()
