# !/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
# _________________________CONSTATS_______________________
BASE_URI = 'https://www.billboard.com/charts/hot-100/'
test_uri = '2020-01-01'
SPOTIFY_ID = str(os.environ.get("SPOTIFY_CLIENT_ID"))
SPOTIFY_SECRET = str(os.environ.get("SPOTIFY_CLIENT_SECRET"))
SPOTIFY_REDIRECT = str(os.environ.get("SPOTIFY_REDIRECT"))

print('Music Time machine')
# user_prompt = input('Type date which you want to come back : (In format YYYY-MM-DD)')

user_uri = BASE_URI + str(test_uri)

contents = requests.get(user_uri)
response = contents.text

soup = BeautifulSoup(response, parser= 'html.parser',features="lxml")
title_spans = soup.select(selector='li ul li h3')

song_names = [song.getText().strip() for song in title_spans]
print(song_names)



sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="0967e6ad3ed04484ae2a5699687596e7",
                                               client_secret="c75365f54e9f4c6cb3284383f16b207e",
                                               redirect_uri="https://developer.spotify.com/dashboard/0967e6ad3ed04484ae2a5699687596e7",
                                               scope="playlist-modify-private"))
# user-library-read
results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track'].encode("utf-8")
    print(idx, track['artists'][0]['name'], " – ", track['name'])
