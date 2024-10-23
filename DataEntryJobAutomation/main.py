"""Data Entry  Job Automation """
from bs4 import BeautifulSoup
import requests

STRONA ="https://appbrewery.github.io/Zillow-Clone/"
FORMULARZ ="https://docs.google.com/forms/d/e/1FAIpQLSeYaxLl7mGPWsefKiAG3yOsDDBbI3quKiPYSS1T_LTu4Ht9eA/viewform?usp=sf_link"

response = requests.get(STRONA)
strona_text = response.text

soup = BeautifulSoup(strona_text,'html.parser')
oferty = soup.find_all(name ='div', class_="StyledCard-c11n-8-84")
