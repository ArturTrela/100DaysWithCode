"""Instagram follower bot """
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class Instafollower():

    def __init__(self):
        self.opcje = webdriver.ChromeOptions()
        self.opcje.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(self.opcje)
        self.driver.get('https://www.instagram.com/')

    def cookies_reject(self):
        cookies = self.driver.find_element(By.CSS_SELECTOR,
                                           'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x5yr21d.x19onx9a > div > button._a9--._ap36._a9_1')
        cookies.click()

    def login(self):
        login_field = self.driver.find_element(By.CSS_SELECTOR,
                                               '#loginForm > div > div:nth-child(1) > div > label > input')
        time.sleep(1)
        login_field.send_keys('arturtrela.automation@gmail.com')
        time.sleep(2)
        password_field = self.driver.find_element(By.CSS_SELECTOR,
                                                  '#loginForm > div > div:nth-child(2) > div > label > input')
        password_field.send_keys('@Automatyk2024')
        time.sleep(2)
        zaloguj_btn = self.driver.find_element(By.CSS_SELECTOR, '#loginForm > div > div:nth-child(3) > button > div')
        zaloguj_btn.click()
        time.sleep(7)
        zapis_danych = self.driver.find_element(By.XPATH,'//*[@id="mount_0_0_wV"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/section/div/button')
        zapis_danych.click()

    def find_followers(self):
        szukaj_btn = self.driver.find_element(By.CSS_SELECTOR,'button')
        szukaj_btn.click()
        # szukajka = self.driver.find_element(By.CSS_SELECTOR,
        #                                     '#mount_0_0_R7 > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y.x8vgawa > section > nav > div > header > div > div > div.xq8finb > div > div > div > div > div > input')
        # szukajka.send_keys('Python Polska', Keys.ENTER)

    def follow(self):
        pass


bot = Instafollower()
time.sleep(2)
bot.cookies_reject()
bot.login()
bot.find_followers()
