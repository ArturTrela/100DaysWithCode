from selenium import webdriver
from selenium.webdriver.common.by import By

opti = webdriver.ChromeOptions()
opti.add_experimental_option("detach", True)
drive = webdriver.Chrome(options=opti)
drive.get('https://orteil.dashnet.org/experiments/cookie/')
