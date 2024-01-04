from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/")
yc_webpage =response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
article_raw = soup.find( class_="athing")
id = article_raw.get("id")
for id in soup:
    article_title = soup.find(name="span", class_="titleline").text
    article_upvote = soup.find(name="span", class_="score").text
    article_link = soup.find(name="href", class_="titleline")


print(article_title)
print(article_upvote)
print(article_link)

print(article_raw)
print(id)

