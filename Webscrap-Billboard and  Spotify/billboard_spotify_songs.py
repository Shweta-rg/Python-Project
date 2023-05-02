import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

baseurl = "https://www.billboard.com/charts/hot-100/"
input_date = input(
    "Which date would you like to choose in format yyyy-mm-dd 2000-08-12 "
)
response = requests.get(baseurl+input_date)
# print(response)
billboard_html = response.text
# print(billboard_html)

soup = BeautifulSoup(billboard_html, 'html.parser')

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)
# or this way also works
# song_name = soup.find_all(name="h3", class_="a-no-trucate")

# song_title = [song.getText() for song in song_name]
# client_id = '4e48f10110d542ddab14f55182444767'
# client_secret = '23660643e07844c2b791e2d8937ebc93'


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="4e48f10110d542ddab14f55182444767",
                                               client_secret="23660643e07844c2b791e2d8937ebc93",
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private"))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
