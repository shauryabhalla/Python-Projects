import spotipy
import requests
from pprint import pprint
from spotipy.oauth2 import SpotifyClientCredentials
birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
client__id='46d51f379e9a42e696405cb581159459'
client__secret='534d5a02b0644bf1997d87d4df118bba'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client__id,client__secret))



track_name = []
for track in spotify.playlist_tracks('69YzqeRbMEq2YVr4qsGHsj')["items"]:
    #URI
    track_uri = track["track"]["uri"]
    
    #Track name
    track_name.append(track["track"]["name"])
    
    #Main Artist
    artist_uri = track["track"]["artists"][0]["uri"]
    artist_info = spotify.artist(artist_uri)
    
    #Name, popularity, genre
    artist_name = track["track"]["artists"][0]["name"]
    artist_pop = artist_info["popularity"]
    artist_genres = artist_info["genres"]
    
    #Album
    album = track["track"]["album"]["name"]
    
    #Popularity of the track
    track_pop = track["track"]["popularity"]

# we can also use for i in track_name:print(i) for an even cleaner look
# pprint(track_name)


with open('D:\Visual_Studio_Codes\Venv\Main.txt', "w", encoding="utf-8") as file:
    file.truncate()
    for row in track_name:
        file.write('%s\n' % row)

file.close()
