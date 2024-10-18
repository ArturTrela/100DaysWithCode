import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime , timedelta
opti = webdriver.ChromeOptions()
opti.add_experimental_option("detach", True)
drive = webdriver.Chrome(options=opti)
drive.get('https://orteil.dashnet.org/experiments/cookie/')
next_run = datetime.now() + timedelta(seconds=5)
end_game = datetime.now() + timedelta(minutes=5)
def buy_boost():
    myMoney = drive.find_element(By.ID, 'money').text
    buyCursor = drive.find_element(By.ID, "buyCursor")
    buyGrandma = drive.find_element(By.ID, "buyGrandma")
    buyFactory = drive.find_element(By.ID, 'buyFactory')
    buyMine = drive.find_element(By.ID, 'buyMine')
    buyShipment = drive.find_element(By.ID, 'buyShipment')
    buyAlchemyLab = drive.find_element(By.ID, 'buyAlchemy lab')
    buyPortal = drive.find_element(By.ID, 'buyPortal')
    buyTimeMachine = drive.find_element(By.ID, 'buyTime machine')

    priceCookie = drive.find_element(By.CSS_SELECTOR , '#buyCursor b ').text.split()
    priceGrandma = drive.find_element(By.CSS_SELECTOR , '#buyGrandma b ').text.split()
    priceFactory = drive.find_element(By.CSS_SELECTOR , '#buyFactory b ').text.split()
    priceMine = drive.find_element(By.CSS_SELECTOR , '#buyMine b ').text.split()
    priceShimpment = drive.find_element(By.CSS_SELECTOR , '#buyShipment b ').text.split()
    # priceAlchemy = drive.find_element(By.CSS_SELECTOR , '#buyAlchemy  b').text.split()
    pricePortal = drive.find_element(By.CSS_SELECTOR , '#buyPortal b ').text.split()
    # priceTimeMachine = drive.find_element(By.CSS_SELECTOR , '#buyTime b ').text.split()
    myMoney = int(myMoney.replace(',',''))

    if myMoney > int(pricePortal[2].replace(',','')):
        buyPortal.click()
        return myMoney
    elif myMoney > int(priceShimpment[2].replace(',','')):
        buyShipment.click()
        return myMoney
    elif myMoney > int(priceMine[2].replace(',','')):
        buyMine.click()
        return myMoney
    elif myMoney > int(priceFactory[2].replace(',','')):
        buyFactory.click()
        return myMoney
    elif myMoney > int(priceGrandma[2].replace(',','')):
        buyGrandma.click()
        return myMoney
    elif myMoney > int(priceCookie[2].replace(',','')):
        buyCursor.click()
        return myMoney
    else:
        print('blad')

while  datetime.now() <= end_game:
    cookie = drive.find_element(By.ID, "cookie")
    cookie.click()
    if datetime.now() >= next_run:
        buy_boost()
        next_run = datetime.now() + timedelta(seconds=5)
        wynik = str(buy_boost)
print(f'Your score is :')
drive.close()