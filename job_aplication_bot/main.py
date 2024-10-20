""" Bot for Job aplication from Udemy course - day 49 """
from cffi.cffi_opcode import CLASS_NAME
from django.conf.global_settings import CSRF_COOKIE_NAME
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)
drive = webdriver.Chrome(opt)


drive.get('https://www.linkedin.com/jobs/search/?currentJobId=4051717426&f_AL=true&f_E=1%2C2&keywords=Python%20Developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true')
time.sleep(2)
close_popup = drive.find_element(By.CSS_SELECTOR,'#base-contextual-sign-in-modal > div > section > button')
close_popup.click()
odrzuc = drive.find_element(By.XPATH,'//*[@id="artdeco-global-alert-container"]/div/section/div/div[2]/button[2]')
odrzuc.click()
time.sleep(2)
# zaloguj_site = drive.find_element(By.CSS_SELECTOR,'body > nav > div > a.nav__button-secondary.btn-secondary-emphasis.btn-md')
zaloguj_site = drive.find_element(By.CSS_SELECTOR,'body > div.base-serp-page > header > nav > div > a.nav__button-secondary.btn-secondary-emphasis.btn-md')
zaloguj_site.click()
username = drive.find_element(By.ID,'username')
username.send_keys('arturtrela.automation@gmail.com')
password = drive.find_element(By.ID, "password")
password.send_keys('Automatyk2024')
zaloguj_btn = drive.find_element(By.CSS_SELECTOR,"#organic-div > form > div.login__form_action_container > button")
zaloguj_btn.click()
time.sleep(2)
# drive.get('https://www.linkedin.com/jobs/search/?currentJobId=4051717426&f_AL=true&f_E=1%2C2&keywords=Python%20Developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true')
time.sleep(2)
# latwe_aplikowanie = drive.find_element(By.CSS_SELECTOR,'#ember52')
# latwe_aplikowanie.click()
# time.sleep(1)
# numer_pole = drive.find_element(By.ID,'single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4051717426-1830998263322399057-phoneNumber-nationalNumber')
# numer_pole.send_keys('519193350')
# dalej_btn = drive.find_element(By.ID,'#ember334')
# dalej_btn.click()
# city_pole = drive.find_element(By.ID,'single-typeahead-entity-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4051717426-82086447524323197-city-HOME-CITY')
# city_pole.send_keys("Ruda Slaska")

# Zapisanie oferty
zapisz_btn = drive.find_element(By.CSS_SELECTOR,'jobs-save-button artdeco-button artdeco-button--secondary artdeco-button--3')
zapisz_btn.click()



time.sleep(100)
drive.close()