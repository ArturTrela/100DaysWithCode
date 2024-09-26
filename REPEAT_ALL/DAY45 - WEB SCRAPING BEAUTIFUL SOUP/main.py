from bs4 import BeautifulSoup
import requests


# Live data scraping
SITE_ADDR = 'https://appbrewery.github.io/news.ycombinator.com/'

response = requests.get(SITE_ADDR)
yc_web = response.text

soup = BeautifulSoup(yc_web, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
articles_upvote = soup.find_all(name="span" , class_ ="score")
for score in articles_upvote:
    article_votes = score.string

for article in articles :
    article_title = article.string
    article_url = article.get('href')

    print(article_title)
    print(article_url)
print(articles_upvote)




























# with open('website.html',"r") as file:
#     contents=file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
#
# # Uzyskanie zawartosci pomiedzy tagami HTML poprzez dodanie .string
# # print(soup.title.string )
#
# # Wyswietlenie zawartosci z wcieciami dla lepszego czytania kodu
# # print(soup.prettify())
#
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
# #
# # for tag in all_anchor_tags:
# #     print(tag.get("href"))
#
# #Wyszukiwanie bezposrednio po id znacznika i zwrot tylko tekstu
# # name = soup.find(id="name").get_text()
# # print(name)
#
# #Wyszukiwanie i pobieranie po klasie "class_" - na koncu musi byc underscroll
# # heading = soup.find(name="h3",class_="heading")
# # print(heading)
#
# # na podstawie selektora CSS
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# # Wyszukiwanie po klasie
# headings = soup.select(".heading")
# print(headings)