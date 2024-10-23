"""Instagram follower bot """
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class Instafollower():

    def __init__(self):
        self.opcje = webdriver.ChromeOptions()
        self.opcje.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(self.opcje)
        self.driver.get('https://www.instagram.com/')
        self.driver.fullscreen_window()

    def cookies_reject(self):
        cookies = self.driver.find_element(By.CSS_SELECTOR,
                                           'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x5yr21d.x19onx9a > div > button._a9--._ap36._a9_1')
        cookies.click()

    def login(self):
        self.driver.fullscreen_window()
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
        zapis_danych = self.driver.find_element(By.XPATH,'//button[contains(text(),"Zapisz")]')
        zapis_danych.click()

    def find_followers(self):
        self.driver.get('https://www.instagram.com/python.polska/followers/')
        time.sleep(5)
    #     czas na reczne otwarcie listy

    def follow(self):
        # all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')
        all_buttons = self.driver.find_elements(By.XPATH, value='//button[contains(text(), "Obserwuj")]')

        for button in all_buttons:
            try:
                button.click()
                time.sleep(1.1)

            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Anuluj')]")
                cancel_button.click()


bot = Instafollower()
time.sleep(2)
bot.cookies_reject()
bot.login()
time.sleep(2)
bot.find_followers()
bot.follow()
