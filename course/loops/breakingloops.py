

Participants = ["Jen", "Alex", "Tina", "Joe", "Ben"]

position = 1
"""
for name in Participants:
    if name == "Tina": 
        print("About to break")
        break
    print("About to increment")
    position += 1

print(position)
"""

"""
Index = 0

for currentIndex in range(len(Participants)):
    if Participants[currentIndex] == "Joe":
        print("We got him mr president")
        break
    print("We dont got him")
print(currentIndex+1)
"""

#Continue skips the rest and goes on to the next loop
for number in range(10):
    if(number%3==0):
        print(number)
        print("Divisible by 3")
        continue
    print(number)
    print("Not Divisible by 3")

