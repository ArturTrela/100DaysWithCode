from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_experimental_option('detach', True )
driver = webdriver.Chrome(options=chrome_opt)

driver.get('https://www.python.org/')
event_times = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')

events = {}

for n in range(len(event_times)):
    events[n]={
        "time":event_times[n].text,
        "name":event_names[n].text,
    }
# Shortes way ... below
# events = {n: {"time": event_times[n].text, "name": event_names[n].text} for n in range(len(event_times))}
print(events)

driver.close()