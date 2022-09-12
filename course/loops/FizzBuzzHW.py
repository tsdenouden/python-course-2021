"""
Tristan Shawn Den Ouden 14/5/2021
Homework #5: FizzBuzz
"""
#FizzBuzz

#Loop from 1-100, doesn't include 101
for number in range(1,101):
    #Multiple of 5 & 3 = FizzBuzz
    if number%3==0 and number%5==0:
        print(number, " - FizzBuzz")

    #Multiple of 3 = Fizz
    elif number%3==0:
        print(number, " - Fizz")

    #Multiple of 5 = Buzz
    elif number%5==0:
        print(number, " - Buzz")

    #Check for primes
    elif number%1==0 and number%2!=0 and number%number==0:
        print(number, " - Prime")

    elif number == 2:
        print(number, " - Prime")
    else:
        continue