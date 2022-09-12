"""
Tristan Shawn Den Ouden 23/5/2021
Homework #7: Dictionaries & Sets

"""
#Dictionary 
#key:value
dictionarySong = {
    "Artist":"Nujabes",
    "Producer":"Nujabes",
    "SongTitle":"Aruarian Dance",
    "AlbumTitle":"Samurai Champloo Departure",
    "Genre":"Hip Hop",
    "Subgenre":"Instrumental Hip Hop",
    "DurationInSeconds":251,
    "YearReleased":2004,
    "TrackListing":3,
    "DurationInMinutes":4.18
}

#Loop through dictionary and print all keys&values
for key,val in dictionarySong.items():
    print(key, " -- ", val)

#Check if the key is in the dictionary
def checkKey(key,value):
    if key in dictionarySong:
        #Check if the value is correct
        if value == dictionarySong[key]:
            print("Correct")
            return True
        else:
            print("Wrong")
            return False
    else:
        print("Wrong")
        return False

checkKey("Artist","Nujabes")