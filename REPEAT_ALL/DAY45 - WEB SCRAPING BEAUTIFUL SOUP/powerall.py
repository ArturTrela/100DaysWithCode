from bs4 import BeautifulSoup
import requests

SITE = ('https://powerall.pl')

response = requests.get(SITE)
powerall_web = response.text
soup = BeautifulSoup(powerall_web, "html.parser")
print(soup.encode("utf-8"))