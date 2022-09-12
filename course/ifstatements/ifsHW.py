"""
Tristan Shawn Den Ouden 28/4/2021

Homework #3: "If" Statements
"""

#checks for equality between any 2 parameters
def checkEquality (a,b,c):
    if int(a) == int(b):
        return True
    elif int(a) == int(c):
        return True
    elif int(b) == int(c):
        return True
    else:
        return False

#Call function and prints output
print(checkEquality(3,"2",2))

