"""Instagram follower bot """
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


opcje = webdriver.ChromeOptions()
opcje.add_experimental_option('detach',True)
driver = webdriver.Chrome(opcje)

#  Uruchomienie strony INSTAGRAM
driver.get('https://www.instagram.com/')
time.sleep(1)
cookies = driver.find_element(By.CSS_SELECTOR,'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x5yr21d.x19onx9a > div > button._a9--._ap36._a9_1')
cookies.click()

def logowanie():
    login_field = driver.find_element(By.CSS_SELECTOR, '#loginForm > div > div:nth-child(1) > div > label > input')
    time.sleep(1)
    login_field.send_keys('arturtrela.automation@gmail.com')
    time.sleep(2)
    password_field = driver.find_element(By.CSS_SELECTOR,'#loginForm > div > div:nth-child(2) > div > label > input')
    password_field.send_keys('@Automatyk2024')
    time.sleep(2)
    zaloguj_btn = driver.find_element(By.CSS_SELECTOR,'#loginForm > div > div:nth-child(3) > button > div')
    zaloguj_btn.click()
    time.sleep(7)
    # odrzuc_zapis_danych  =driver.find_element(By.XPATH,'//*[@id="mount_0_0_hs"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div/div')
    # odrzuc_zapis_danych.click()

def wyszukaj():
    szukaj_btn = driver.find_element(By.CSS_SELECTOR,'#mount_0_0_4R > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.xixxii4.x13vifvy.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1.x1dr59a3.xeq5yr9.x1n327nk > div > div > div > div > div.x1iyjqo2.xh8yej3 > div:nth-child(2) > span > div > a > div')
    szukaj_btn.click()
    szukajka = driver.find_element(By.CSS_SELECTOR,'#mount_0_0_R7 > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y.x8vgawa > section > nav > div > header > div > div > div.xq8finb > div > div > div > div > div > input')
    szukajka.send_keys('Python Polska',Keys.ENTER)

logowanie()
wyszukaj()
time.sleep(100)
driver.quit()
