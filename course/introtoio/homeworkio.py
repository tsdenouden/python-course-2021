"""
Tristan Shawn Den Ouden 17/7/2021
Homework #8 - I/O

"""
#import library
import os

#List commands
def ListCommands():
    print("A)Read the file")
    print("B)Delete the file and start over")
    print("C)Append the file")

#Prompt for filename
file = input("What file do you want to open? ")

#Check if the file exists
if os.path.isfile(file) == True:
    #If the file exists, open it
    openFile = open(file, "r")
    
    #Ask for a command
    ListCommands()
    command = input(">")

    #Print the contents of the file
    if command == "A":
        print(openFile.read())
    #Delete the file and make a new one
    elif command == "B":
        openFile.close()
        os.remove(file)
        file = input("Enter new filename: ")
        openFile = open(file, "x")
        openFile.close()
    #Append text to the file
    elif command == "C":
        openFile.close()
        openFile = open(file, "a")
        text = input("what do you want to add? ")
        openFile.write(text)
    else:
        exit()
    openFile.close()

#If file doesn't exist, ask to create it
else:
    prompt = input("File doesn't exist, create? (Y/N")
    if prompt == "Y":
        openFile = open(file,"w")
        text = input("Enter text to the file: ")
        openFile.write(text)
        openFile.close()



