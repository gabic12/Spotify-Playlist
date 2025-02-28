import requests
import datetime
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
website_link = "https://www.billboard.com/charts/hot-100/"
song_uri = []

#User inputs the date
user_date = input("Enter the date (YYYY-MM-DD): ")
try:
    datetime.date.fromisoformat(user_date)
except ValueError:
    raise ValueError("Incorect date format, it should be YYYY-MM-DD.")
year = user_date.split("-")[0]

#spotipy authentication - it created a token.txt file after acces is allowed
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="YOUR CLIENT ID",
        client_secret="YOUR CLIENT SECRET",
        show_dialog=True,
        cache_path="token.txt",
        username="YOUR SPOTIFY NAME",
    )
)
user_id = sp.current_user()["id"]

#Web scraping the Billboard Hot 100 site
response = requests.get(url=f"{website_link}/{user_date}/", headers=header)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
songs = soup.select("li ul li h3")
song_list = [song.getText().strip() for song in songs]

#Extracting the song URIs
for song in song_list:
    results = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        song_uri.append(results["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f"{song} doesn't exist in Spotify")

#Creates a new playlist on Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{user_date} Billboard 100", public=False)

#Adding the songs to the playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uri)
