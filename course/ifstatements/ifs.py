#General structure of an if statement
"""
if condition:
    Action

"""

#example 1
click = False

Like = 0

click = True
if click == True:
    Like +=1
    click = False

print(Like)


#example 2
Temperature = 20
Thermo = 15
print(Thermo)

if Temperature <= 15:
    Thermo += 5

print(Thermo)

if Temperature >= 20:
    Thermo -= 3

print(Thermo)


#example 3
Time = "Morning"
Sleepy = False
Pajamas = "Unknown"


print(Pajamas)

if Time == "Night":
    Pajamas = "On"
elif Time == "Morning":
    Pajamas = "On"
else:
    Pajamas = "Off"

print(Pajamas)

