from random import random

randVal = random()
print(randVal)

upper = 1.0
lower = 0.0
#guess = 0.5 > low > lower bound = 0.5
#guess = 0.9 > high > upper bound = 0.9


while(True):
    guess = float(input("Enter your guess: "))
    if guess == randVal:
        print("You guessed the right number!")
        break
    elif guess < randVal:
        print("You guessed too low!")
        lower = guess
    elif guess > randVal:
        print("You guessed too high!")
        upper = guess