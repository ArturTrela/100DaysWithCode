from bs4 import BeautifulSoup
import lxml
with open("website.html") as file:
    contents = file.read()


soup = BeautifulSoup(contents,'html.parser')
all_anchor_tags=soup.find_all(name="a")
# print(all_anchor_tags)
# """Search from tags only text or text with links with using method 'get' """
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(f'{tag.getText()} {tag.get("href")}')
#
# heading =soup.find(name= "h1" , id="name")
# print(heading)

# How to skip "class form html file " --> add underscroll after word "class"
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)