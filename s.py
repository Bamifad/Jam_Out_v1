import spotipy
from spotipy.oauth2 import SpotifyClientCredentials 
import pandas as pd
client_id = "7ca9f224458b4bc49ad53ef642d8a000"
client_secret = "107ef8d9d065482fa9d1fceb8fa02a13"
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) 







sp.trace=False 

playlist = sp.user_playlist("frequencine", "7KMtxb9kh3TtVvJTdLtJ2K") 
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
for i in ((artistID)):
    genreList = sp.artist(i)["genres"]
    appended = False
    for i in genreList:
        if(appended):
            break
        if('metal' in (i)):
            genres.append("Metal")
            appended = True
            break
        elif('reggae' in (i)):
            genres.append("Reggae")
            appended = True
            break
        elif( 'rock' in (i)):
            genres.append("Rock")
            appended = True
            break
    if(appended == False):
        genres.append("idk man")
    appended = False
        


df = pd.DataFrame(features)

# df = pd.DataFrame()
df["Song Name"] = names
df["Artist"] = artist
df["Genres"] = genres
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