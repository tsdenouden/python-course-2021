"""
Tristan Shawn Den Ouden 8/5/2021

Homework #4: Lists
"""

myUniqueList = []
myLeftovers = []

#Sends rejected elements into a different list
def addLeftovers(leftover):
    myLeftovers.append(leftover)

#Appends elements to list unless it's already there
def addToList(elem):
    if elem in myUniqueList:
        addLeftovers(elem)
        return False
    else:
        myUniqueList.append(elem)
        return True

#Testing the function
print(addToList(2))
print(addToList(2))
print(addToList(4))
print(addToList("Hello World"))

#Print the result
print(myUniqueList)
print(myLeftovers)

