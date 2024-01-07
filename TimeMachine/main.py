import requests
from bs4 import BeautifulSoup

START_URL ="https://www.billboard.com/charts/hot-100"

user_prompt = input("Which year do you want to travel to ? Date format is : YYYY-MM-DD ")
URL = f'{START_URL}/{user_prompt}'
print(URL)

response =requests.get(URL)
web_resp = response.text

soup = BeautifulSoup(web_resp,features="html.parser")
title = soup.find(name="h3", class_="title").text
with open ( "titles.txt", "w", encoding="utf-8") as f:
    f.write(title)
