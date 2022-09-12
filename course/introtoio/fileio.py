
"""
#open a file
File = open("Filename", "r") #"r", "w", "a," "r+"
#close a file
File.close
"""

#List of vacation spots
VacationSpots = ["London", "Paris", "New York", "Utah", "Iceland"]

#Open a file to write in it, if it doesn't exist, create the file
VacationFile = open("VacationPlaces", "w")

#For every element in the list, write it in the file
for Spots in VacationSpots:
    #.write only accepts strings
    #convert with str()
    VacationFile.write(Spots + "\n")

#Close file
VacationFile.close()
#Open it again to read
VacationFile = open("VacationPlaces", "r")

#Print a line after every line in the file
for line in VacationFile:
    print(line)

#Read the whole file and print it
TheWholeFile = VacationFile.read()
print(TheWholeFile)

#Close the file
VacationFile.close()
#Add another vacation spot
FinalSpot = "Thailand"

#Open the file and append this new vacation spot
#Append adds, if you use write here, it'll overwrite instead
VacationFile = open("VacationPlaces", "a")
VacationFile.write(FinalSpot)
#Close the file
VacationFile.close

#Open it again to read the file
VacationFile = open("VacationPlaces", "r")
#Get rid of the extra lines
for line in VacationFile:
    print(line,end="")

VacationFile.close



#A different method to open a file, you dont need to close the file in this instance
"""
with open("VacationPlaces", "r") as VacationFile:
    for line in VacatioNFile:
        print(line)

"""