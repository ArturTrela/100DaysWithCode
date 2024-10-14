""" File to show how does work library Selenium WebDriver for automation Web browser operation"""

from selenium import webdriver

# keep chrome open

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True )
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.amazon.com')

# close single tab
# driver.close()
# close full browser
# driver.quit()