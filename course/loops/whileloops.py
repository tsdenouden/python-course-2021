"""General structure of a while loop

while (condition):
    Action
    Action2
    Action3

"""
######################
"""
counter = 1
Sum = 0
while (counter <= 100):
    print(counter)
    Sum += counter
    counter += 1
print(Sum)
"""
######################
"""
Letters = ["a","b","c","d","e"]

Index = 0 

while (Index < len(Letters)):
    print(Index)
    print(Letters[Index])
    Index += 1
"""
######################

height = 5000
velocity = 50
time = 0

while (height>0):
    height -= velocity
    time += 1

print(height)
print(time)