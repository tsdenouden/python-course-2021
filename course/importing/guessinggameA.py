

from random import randint

randVal = randint(0,100)

while(True): #While (True==True):
    guess = int(input("Enter a guess: "))
    if guess == randVal:
        print("You guessed the right number!")
        break
    elif guess < randVal:
        print("Your guess was lower than the number!")
    elif guess > randVal:
        print("Your guess was higher than the number!")
    

print("You guessed correctly with: ", guess)

