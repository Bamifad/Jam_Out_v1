import spotipy
from spotipy.oauth2 import SpotifyClientCredentials 
import pandas as pd
client_id = "7ca9f224458b4bc49ad53ef642d8a000"
client_secret = "107ef8d9d065482fa9d1fceb8fa02a13"
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) 







sp.trace=False 
playlist = sp.user_playlist("MAX", "2LOxEzC4KmoWJ9NhW0kz5M") 
songs = playlist["tracks"]["items"] 
ids = []
names = []
artist = []
artistID = [] 
genres = []
for i in range(len(songs)): 
    ids.append(songs[i]["track"]["id"])
    names.append(songs[i]["track"]["name"]) 
    artist.append(songs[i]["track"]["artists"][0]["name"]) 
    artistID.append(songs[i]["track"]["artists"][0]["id"]) 

features = sp.audio_features(ids) 
gb = []
for i in ((artistID)):
    genreList = sp.artist(i)["genres"]
    gb.append( genreList)
    appended = False
    for i in genreList:
        if(appended):
            break
        if('christian' in (i)):
            genres.append("Christian")
            appended = True
            break
        elif( 'folk' in (i)):
            genres.append("Folk")
            appended = True
            break
        elif( 'soul' in (i)):
            genres.append("Soul")
            appended = True
            break
        elif( 'metal' in (i)):
            genres.append("Metal")
            appended = True
            break
        elif( 'blues' in (i)):
            genres.append("Blues")
            appended = True
            break
        elif('jazz' in (i)):
            genres.append("Jazz")
            appended = True
            break
        elif( 'electronic' in (i)):
            genres.append("Electronic")
            appended = True
            break
        elif( 'country' in (i)):
            genres.append("Country")
            appended = True
            break
        elif( 'alternative' in (i)):
            genres.append("Alternative")
            appended = True
            break
        elif( 'rap' in (i)):
            genres.append("Rap")
            appended = True
            break
        elif( 'rock' in (i)):
            genres.append("Rock")
            appended = True
            break
        elif( 'pop' in (i)):
            genres.append("Pop")
            appended = True
            break
    if(appended == False):
        genres.append("Pop")
    appended = False
        


df = pd.DataFrame(features)

# df = pd.DataFrame()
df["Song Name"] = names
df["Artist"] = artist
df["Genres"] = genres
df["gb"] = gb
df.to_csv("spotify_music.csv")


# #Extract Artist's uri
# artists_uris = result['tracks']['items'][0]['artists'][0]['genre']
# #Pull all of the artist's albums
# artist_albums = sp.artist_albums(artists_uris, album_type='album')
# #Store artist's albums' names' and uris in separate lists
# artist_album_names = []
# artist_album_uris = []
# artist_album_genre = []
# for i in range(len(artist_albums['items'])):
#     artist_album_names.append(artist_albums['items'][i]['name'])
#     artist_album_genre.append(artist_albums['items'][i]['genre'])
    
# print(artist_album_names)
# print(artist_album_genre)
# #Keep names and uris in same order to keep track of duplicate albums

# # final_df.to_csv("spotify_music.csv")
