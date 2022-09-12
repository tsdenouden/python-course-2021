
Word = "Hello"

#Variables in the for-in loop
#first variable (w) - iterates through the 2nd variable
#second variable - variable that will be iterated through
"""
Word = "Hello"

Letters = []

for w in Word:
    print(w)
    if w == "e":
        print("The letter E")
    Letters.append(w)

print(Letters)

for l in Letters:
    print(l)

Numbers = [1,2,3,4,5]

for n in Numbers:
    if n%2 == 0:
        print(n)
"""

Numbers = []

#range(start,stopping,steps)
#range is up to but not including
for num in range(1,12,2):
    Numbers.append(num)
    print(num)

print(Numbers)