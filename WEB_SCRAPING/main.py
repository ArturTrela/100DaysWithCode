import requests
from bs4 import BeautifulSoup


URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
web_data = response.text

titles =[]
soup = BeautifulSoup(web_data,"html.parser")


title = soup.find(name="h3", class_="title").text.encode("utf-8")
for title in soup:
    tytuł = soup.getText("title")
    titles.append(tytuł)

print(titles)
