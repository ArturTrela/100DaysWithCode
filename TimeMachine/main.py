import requests
from bs4 import BeautifulSoup

START_URL ="https://www.billboard.com/charts/hot-100"

# user_prompt = input("Which year do you want to travel to ? Date format is : YYYY-MM-DD ")
user_prompt = "2020-06-01"
URL = f'{START_URL}/{user_prompt}'
print(URL)

response =requests.get(URL)
web_resp = response.text

soup = BeautifulSoup(web_resp,features="html.parser")
title = soup.find_all(name = "h3", )
print(title)

