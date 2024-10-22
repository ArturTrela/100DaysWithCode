"""Twitter bot using selenium library """
from pydantic.datetime_parse import time_expr
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchFrameException
import time
X_LOGIN_SITE="https://x.com/i/flow/login"
SPEED_TEST_SITE = "https://www.speedtest.net/"
PROMISED_DOWN=300
PROMISED_UP =150
X_EMAIL = 'arturtrela.automation@gmail.com'


class InternetSpeedTwitterBot():

    def __init__(self):
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('detach',True)
        self.driver = webdriver.Chrome(opt)
        self.promised_down = PROMISED_DOWN
        self.promised_up = PROMISED_UP

    def get_internet_speed(self, ):
        self.driver.get(SPEED_TEST_SITE)
        # Cookies reject
        reject_btn = self.driver.find_element(By.ID,'onetrust-reject-all-handler')
        reject_btn.click()
        time.sleep(3)
        start_btn =self.driver.find_element(By.CSS_SELECTOR,'#container > div.pre-fold > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.start-button > a')
        start_btn.click()
        time.sleep(40)
        # wyniki = self.driver.find_element(By.CLASS_NAME,'close-btn')
        wyniki = self.driver.find_element(By.CSS_SELECTOR,'#container > div.pre-fold.mobile-test-complete > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.main-view > div > div.desktop-app-prompt-modal > div > div > div:nth-child(4) > a')
        wyniki.click()
        result_data = self.driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[1]/div/div/div[2]/div[2]/a')
        upload = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        download = self.driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        time.sleep(5)
        self.driver.quit()
        return (f'Hej! Moje ostatnie wyniki testu predkosci internetu podczas testu ID ; {result_data.text} to : '
                f'Upload : {upload.text} oraz Download {download.text}')

    def tweet_at_provider(self,message):
        self.driver.get(X_LOGIN_SITE)
        time.sleep(5)
        user_input = self.driver.find_element(By.CSS_SELECTOR,'input')
        user_input.send_keys(X_EMAIL)
        user_input.send_keys(Keys.ENTER)
        time.sleep(2)
        pass_input=self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        pass_input.send_keys('Automatyk2024')
        pass_input.send_keys(Keys.ENTER)
bot = InternetSpeedTwitterBot()
wynik_testu = bot.get_internet_speed()
bot.tweet_at_provider(wynik_testu)