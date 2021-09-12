import pandas as pd
import random as rd
import names as nam


df = pd.DataFrame()
names = []
age = []
listOfSongs = []
instruments = []
email = []
location =[]
bio = []
songList = []
genre = ""
genreList = []
song = ""
scores = []
score = 0
artist = ""
artistList = []

listOfGenres = []
listOfArtists = []
randInt = 0
mainList = ['Fremont', 'Plano', 'San Jose', 'Irvine', 'Madison', 'Sioux Falls', 'Huntington Beach', 'Scottsdale', 'Santa Rosa', 'Pearl City', 'Bismarck', 'Fargo', 'Lincoln', 'San Francisco', 'Overland Park', 'Santa Clarita', 'Oceanside', 'Glendale', 'Anaheim', 'Cape Coral', 'Pembroke Pines', 'Austin', 'Gilbert', 'San Diego', 'Chula Vista', 'Garden Grove', 'Grand Prairie', 'Charleston', 'Cedar Rapids', 'Minneapolis', 'Raleigh', 'Aurora', 'Chandler', 'Des Moines', 'Irving', 'Columbia', 'Oxnard', 'Peoria', 'Oakland', 'St. Paul', 'Fort Lauderdale', 'Yonkers', 'Garland', 'Tempe', 'Boise', 'Durham', 'Las Cruces', 'Aurora', 'Charlotte', 'Omaha', 'Boston', 'Rancho Cucamonga', 'Santa Ana', 'Denver', 'Seattle', 'Honolulu', 'Port St. Lucie', 'Nashua', 'Rapid City', 'Fort Worth', 'Arlington', 'Long Beach', 'Portland', 'Colorado Springs', 'Washington', 'Grand Rapids', 'Nampa', 'El Paso', 'Mesa', 'Salt Lake City', 'Manchester', 'Virginia Beach', 'Billings', 'Burlington', 'Miami', 'Dallas', 'Reno', 'Fontana', 'Brownsville', 'Los Angeles', 'Chesapeake', 'Ontario', 'Riverside', 'Tallahassee', 'Lewiston', 'New York', 'Moreno Valley', 'Missoula', 'Jersey City', 'Portland', 'Atlanta', 'Orlando', 'Modesto', 'Hialeah', 'Vancouver', 'Pittsburgh', 'Tampa', 'West Valley City', 'Sacramento', 'Huntsville', 'Cheyenne', 'Dover', 'Henderson', 'Glendale', 'Bridgeport', 'Nashville', 'South Burlington', 'Anchorage', 'Salem', 'San Antonio', 'Houston', 'Winston-Salem', 'Chicago', 'Tacoma', 'St. Petersburg', 'Fort Wayne', 'Amarillo', 'Phoenix', 'Bakersfield', 'Laredo', 'Worcester', 'Tucson', 'Columbia', 'Greensboro', 'Warwick', 'Richmond', 'Lubbock', 'Springfield', 'San Bernardino', 'Casper', 'Albuquerque', 'Corpus Christi', 'Chattanooga', 'Jacksonville', 'Newport News', 'Columbus', 'Knoxville', 'Rochester', 'Fresno', 'Spokane', 'Oklahoma City', 'Fort Smith', 'Fayetteville', 'Wichita', 'Norfolk', 'Providence', 'Stockton', 'New Haven', 'North Las Vegas', 'Buffalo', 'Juneau', 'Kansas City', 'Las Vegas', 'Indianapolis', 'Louisville', 'Milwaukee', 'New Orleans', 'Wilmington', 'Montgomery', 'Baltimore', 'Jackson', 'Baton Rouge', 'Philadelphia', 'Shreveport', 'Columbus', 'Cincinnati', 'Newark', 'Tulsa', 'Akron', 'St. Louis', 'Memphis', 'Mobile', 'Little Rock', 'Augusta', 'Birmingham', 'Gulfport', 'Cleveland', 'Huntington', 'Toledo', 'Charleston', 'Detroit']
#replace with main list of cities we are using
baseInstruments = ["Piano", "Flute", 'Guitar', 'Saxophone', 'Keyboard', 'Oboe', 'Bass', 'Trombone', 'Trumpet', 'Violin']
music = pd.read_csv('spotify_music.csv')

for i in range(50):
    names.append(nam.get_full_name())
    age.append(rd.randint(18,40))
    instruments.append(baseInstruments[rd.randint(0,len(baseInstruments)-1)])
    email.append(str(rd.randint(0, 1290319))+"@email.com")
    location.append(mainList[rd.randint(0, len(mainList)-1)])
    bio.append("I like to play the " +instruments[i]+" and I live in "+location[i]+".")
    for i in range (5):
        randInt = rd.randint(0,len(list(music['Song Name']))-1)
        song = list(music['Song Name'])[randInt]
        genre = list(music['Genres'])[randInt]
        artist = list(music['Artist'])[randInt]
        while(song in songList):
            randInt = rd.randint(0,len(list(music['Song Name']))-1)
            song = list(music['Song Name'])[randInt]
            genre = list(music['Genres'])[randInt]
            artist = list(music['Artist'])[randInt]
        songList.append(song)
        genreList.append(genre)
        if(genre=="Rock"):
            score += 50
        elif(genre=="Christian"):
            score += 0
        elif(genre=="Soul"):
            score += 90
        elif(genre=="Jazz"):
            score += 100
        elif(genre=="Folk"):
            score += 10
        elif(genre=="Metal"):
            score += 20
        elif(genre=="Electronic"):
            score += 80
        elif(genre=="Country"):
            score += 30
        elif(genre=="Rap"):
            score += 70
        elif(genre=="Pop"):
            score += 60
        elif(genre=="Alternative"):
            score += 40
        elif(genre=="Blues"):
            score += 110
        artistList.append(artist)
        
    listOfSongs.append(songList)
    listOfGenres.append(genreList)
    listOfArtists.append(artistList)
    scores.append(score/5)
    songList = []
    genreList = []
    artistList = []
    score = 0
    song = ""
    genre = ""
    artist = ""
    
    
    
df["Names"] = names
df["Ages"] = age
df["Instruments"] = instruments
df["Email"] = email
df["Location"] = location
df["Bio"] = bio
df["Songs"] = listOfSongs
df["Genre"] = listOfGenres
df["Artists"] = listOfArtists
df["Score"] = scores
df.to_csv("RandomPeople.csv")