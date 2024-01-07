from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/news")
yc_webpage =response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles= soup.find_all( class_="athing")
articles_text =[]
articles_list=[]
for article_tag in articles:
    article_text = article_tag.getText()
    articles_list.append(article_text)
    article_link = article_tag.get("href")
    articles_list.append(article_link)
    # article_upvotes = article_tag.get()
print(article_text)
print(article_link)
# print(article_upvotes)

print(articles_text)
print(articles_list)


