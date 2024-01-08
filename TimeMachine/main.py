import requests
from bs4 import BeautifulSoup

START_URL ="https://www.billboard.com/charts/hot-100"

user_prompt = input("Which year do you want to travel to ? Date format is : YYYY-MM-DD ")
# user_prompt = "2020-06-01"
URL = f'{START_URL}/{user_prompt}'
print(URL)

response =requests.get(URL)
web_resp = response.text

soup = BeautifulSoup(web_resp,features="html.parser")
song_name_spans = soup.select("div ul li ul h3")
artist_name_spans = soup.select("div ul li ul span")
song_names = [song.getText().strip() for song in song_name_spans]
songs_file =[]
for x in range(1,100):
    song_new = f"{x}) {song_names[x]} \n "
    songs_file.append(song_new)
print(song_names)

with open(f"file_song_{user_prompt}.txt", "w") as file:
    file.writelines(songs_file)


