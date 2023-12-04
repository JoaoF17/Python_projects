from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

load_dotenv()

date_input = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n"
)

# -------------Get top 100 music-------------#
billboard_endpoint = f"https://www.billboard.com/charts/hot-100/{date_input}/"

response = requests.get(billboard_endpoint)
website = response.text

soup = BeautifulSoup(website, "html.parser")

# get the rank
ranks = []
music_names = []
artist_names = []

parent_div = soup.find_all("div", class_="o-chart-results-list-row-container")

for div in parent_div:
  # ranks
  rank_span = div.find("span", class_="c-label")
  ranks.append(
      rank_span.getText().split()[0]
  )  # added the index so the number wont be inside a list
  # music name
  music_element = div.find("h3", class_="c-title")
  music_names.append(music_element.getText().split()[0])
  # artist name
  li_element = div.find("li", class_="lrv-u-width-100p")
  artist_span = li_element.find("span", class_="c-label")
  artist_names.append(artist_span.getText().split()[0])

# -------------Connection to spotify-------------#
SPOTIFY_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_PASS = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_URI = os.getenv("SPOTIFY_REDIRECT_URI")

scope = "playlist-modify-private"

sp = spotipy.Spotify(
  auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_ID,
    client_secret=SPOTIFY_PASS,
    redirect_uri=SPOTIFY_URI,
    scope=scope,
    show_dialog=True,
    cache_path=".cache",
    username="youruserid"
  )
)
song_uris = []
year = date_input.split("-")[0]
#getting the codes for songs
for music in music_names:
  result = sp.search(q=f"track:{music} year:{year}", type="track")
  # print(result)
  try:
    uri = result["tracks"]["items"][0]["uri"]
    song_uris.append(uri)
  except IndexError:
    print(f"{music} doesn't exist in Spotify. Skipped")
print(song_uris)

#creating a playlist with the {date} in the name
playlist = sp.user_playlist_create(user="youruserid", name=f"{date_input} Billboard 100", public=False)

#add songs to created playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)