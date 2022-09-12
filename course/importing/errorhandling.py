

keyWord = "Hello"

try:
    #raise ValueError
    print(int(keyWord))
except ValueError:
    print("got a ValueError")
except: #except Exception as x (to store the Exception in x)
    print("You got an error")
finally:
    print("finally")

print("Past exception")