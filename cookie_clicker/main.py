from selenium import webdriver
from selenium.webdriver.common.by import By
import time
opti = webdriver.ChromeOptions()
opti.add_experimental_option("detach", True)
drive = webdriver.Chrome(options=opti)
drive.get('https://orteil.dashnet.org/experiments/cookie/')

while True:
    cookie = drive.find_element(By.ID, "cookie")
    money = (drive.find_element(By.ID, 'money').text)
    buyGrandma = drive.find_element(By.ID, "buyGrandma")
    cookie.click()
    if money >= "100":
        buyGrandma.click()


drive.close()