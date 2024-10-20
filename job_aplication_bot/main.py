""" Bot for Job aplication from Udemy course - day 49 """
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchFrameException
import time

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)
drive = webdriver.Chrome(opt)

def abort_application():
    # Click Close Button
    close_button = drive.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = drive.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()

def open_site():
    drive.get('https://www.linkedin.com/jobs/search/?currentJobId=4051717426&f_AL=true&f_E=1%2C2&keywords=Python%20Developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true')
    time.sleep(2)

def close_popup():
    close_popup = drive.find_element(By.CSS_SELECTOR,'#base-contextual-sign-in-modal > div > section > button')
    close_popup.click()
def odrzuc_cookies():
    odrzuc = drive.find_element(By.XPATH,'//*[@id="artdeco-global-alert-container"]/div/section/div/div[2]/button[2]')
    odrzuc.click()
    time.sleep(2)

# zaloguj_site = drive.find_element(By.CSS_SELECTOR,'body > nav > div > a.nav__button-secondary.btn-secondary-emphasis.btn-md')

def logowanie():
    zaloguj_site = drive.find_element(By.CSS_SELECTOR,'body > div.base-serp-page > header > nav > div > a.nav__button-secondary.btn-secondary-emphasis.btn-md')
    zaloguj_site.click()
    username = drive.find_element(By.ID,'username')
    username.send_keys('arturtrela.automation@gmail.com')
    time.sleep(1)
    password = drive.find_element(By.ID, "password")
    password.send_keys('Automatyk2024')
    time.sleep(1)
    zaloguj_btn = drive.find_element(By.CSS_SELECTOR,"#organic-div > form > div.login__form_action_container > button")
    zaloguj_btn.click()
    print(f'Czas na reczne rozwiazanie CAPCHATa')
    time.sleep(15)

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


def zapisz_oferte():
    zapisz_btn = drive.find_element(By.CSS_SELECTOR,'jobs-save-button artdeco-button artdeco-button--secondary artdeco-button--3')
    zapisz_btn.click()

def aplikuj_wszystkie():
    try :
        list_oferty = drive.find_elements(By.CLASS_NAME,'job-card-container--clickable')
        print(list_oferty)
        for oferta in list_oferty:
            oferta.click()
            apply_btn = drive.find_element(By.CSS_SELECTOR,".jobs-s-apply button")
            apply_btn.click()
            time.sleep(2)
            phone = drive.find_element(By.CSS_SELECTOR,' input[id*=phoneNumber]')
            if phone.text =='':
                phone.send_keys('519193352')
            next = drive.find_element(By.CSS_SELECTOR,'footer button')
            next.click()
            submit_button = drive.find_element(by=By.CSS_SELECTOR, value="footer button")
            if submit_button.get_attribute("data-control-name") == "continue_unify":
                abort_application()
                print("Complex application, skipped.")
                continue
            else:
                # Click Submit Button
                print("Submitting job application")
                submit_button.click()
            time.sleep(2)
            # Click Close Button
            close_button = drive.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
            close_button.click()
    except NoSuchFrameException :
        abort_application()
        print("No application button, skipped.")


    finally:
        print('Zapisano wszystkie oferty')
open_site()
close_popup()
odrzuc_cookies()
logowanie()
aplikuj_wszystkie()
time.sleep(100)
drive.close()