
ParticipantNumber = 2
participantData = []

registeredParticipants = 0
outputFile = open("ParticipantData.txt","w")

while(registeredParticipants < ParticipantNumber):
    tempPartData = [] #name,country,age
    name = str(input("Please enter your name: "))
    tempPartData.append(name)
    country = str(input("Please enter your country of origin: "))
    tempPartData.append(country)
    age = int(input("Please enter your age: "))
    tempPartData.append(age)

    participantData.append(tempPartData)
    print(participantData)

    registeredParticipants += 1

for participant in registeredParticipants:
    for data in participant:
        outputFile.write(str(data))
        outputFile.write(" ")
    outputFile.write("\n")

outputFile.close()

inputFile = open("ParticipantData.txt", "r")




inputFile.close()

inputList = []

for line in inputFile:
    #strip = takes away new line
    #split = splits everything into elements
    tempParticipant = line.strip().split()
    print(tempParticipant)
    inputList.append(tempParticipant)
    print(inputList)

Age = {}
print(inputList)
for part in inputList:
    tempAge = int(part[-1]) #int('21') -> 21
    if tempAge in Age:
        Age[tempAge] += 1
    else:
        Age[tempAge] = 1

print(Age)

Countries = {}
print(inputList)
for part in inputList:
    tempCountry = (part[-2]) #int('21') -> 21
    if tempCountry in Countries:
        Countries[tempCountry] += 1
    else:
        Countries[tempCountry] = 1

print("Countries that attended:",Countries)

Oldest = 0
Youngest = 100
mostOccuringAge = 0
counter = 0

for tempAge in Age:
    if tempAge>Oldest:
        Oldest = tempAge
    if tempAge<Youngest:
        Youngest = tempAge
    if Age[tempAge]>=counter:
        counter = Age[tempAge]
        mostOccuringAge = tempAge

print(Oldest)
print(Youngest)
print("Most occuring age is: ",mostOccuringAge," with ",counter, "participants")


inputFile.close()