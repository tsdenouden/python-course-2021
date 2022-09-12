#Lists

#TestList = ["element1","element2","element3"]
#Starts counting at 0

Scores = [70,85,67.5,90,80]
print(Scores)
print(Scores[-1])

#Print starting from the 1st index up to the 3rd index (but not Index 3)
print(Scores[0:3])

#Everything starting from the 2nd index
print(Scores[2:])

#Replace everything starting from the 2nd index up to the 3rd index (but not Index 3)
Scores[1:3] = []
print(Scores)

Scores[2] = ["Hello","World"]
print(Scores)
print(Scores[2][0])

#Add an element
Scores.append(82)
print(Scores)

