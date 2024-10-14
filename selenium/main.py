""" File to show how does work library Selenium WebDriver for automation Web browser operation"""

from selenium import webdriver
from selenium.webdriver.common.by import By
# keep chrome open

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True )
driver = webdriver.Chrome(options=chrome_options)

# For Amazon website:

# driver.get('https://www.amazon.com/COMFEE-Pressure-Kick-Start-Multi-Functional-Programmable/dp/B091TTDRVP/ref=ex_alt_wg_d?_encoding=UTF8&pd_rd_i=B091TTDRVP&psc=1&pd_rd_w=Dxi2O&pf_rd_p=4e1b46a8-daf9-4433-b97e-d6df97cf3699&pf_rd_r=BD7TE0Q02VKGRFHJS60K&pd_rd_wg=uzGUj&pd_rd_r=2e312947-b56b-49a3-b7bf-d3c1fadddb59&content-id=amzn1.sym.4e1b46a8-daf9-4433-b97e-d6df97cf3699')
#
# price_dollar= driver.find_element(By.CLASS_NAME, "a-price-whole")
# price_cents =driver.find_element(By.CLASS_NAME, "a-price-fraction")
# print(f'price is $ {price_dollar.text}.{price_cents.text}')

# for python.org website
#
driver.get('https://www.python.org/')
# search_bar = driver.find_element(By.NAME, 'q')
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.NAME, "submit")
# print(button.size)
#
# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)


# Search element via Xpath !!! <- Great Tool
# footer = driver.find_element(By.XPATH , '//*[@id="site-map"]/div[2]/div/div/p/small/span[2]/a')
# print(footer.text)


# close single tab
# driver.close()
# close full browser
driver.quit()