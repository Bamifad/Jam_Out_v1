import pandas as pd

df = pd.read_csv("RandomPeople.csv", index_col=False)

# print(df.columns)

# GENRES = ["Classical", "Folk", "Metal", "Country", "Alternative", "Rock", "Pop", "Electronic", "Rap", "Soul", "Jazz", "Blues"]

GENRES = ["Classical", "Folk", "Metal", "Country", "Alternative", "Rock", "Pop"]
USERS = df["Names"]
# print(USERS)
columns = ["userID", "genreID", "ratings"]

new_data = pd.DataFrame(columns=columns)

userID_list = []
genreID_list = []
ratings = []
print(df.iloc[0]["Genre"])

def number_genre(genre, string):
    num_genre = 0
    while(genre in string):
        num_genre += 1
        string = string[string.find(genre) + len(genre):]
    return num_genre
    

print(number_genre("rock", "['Rock', 'Rock', 'Pop', 'Rock', 'Pop']".lower()))

for i, user in enumerate(USERS):
    for j, genre in enumerate(GENRES):
        userID_list.append(i)
        genreID_list.append(j)
        preferred_genres = df.iloc[i]["Genre"]
        num_genre = number_genre(genre, preferred_genres)
        ratings.append(float(num_genre))

new_data["userID"] = userID_list
new_data["genreID"] = genreID_list
new_data["ratings"] = ratings

print(new_data.iloc[0:25])


new_data.to_csv("ratings.csv")

USERS = df["Names"]

USERS.to_csv("users.csv", index=True, index_label="userID")

        
    
    
