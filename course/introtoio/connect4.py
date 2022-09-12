"""
Tristan Shawn Den Ouden 20/7/2021
Project #1 - Connect 4

"""

#Importing modules
from termcolor import colored

#Prints the title of the game
print(colored("Conn", "red"), end="")
print(colored("ect 4", "blue"))

#Set game to false at the start
game = False

#Playing Board
playingBoard = [[" "," "," "," "],[" "," "," "," "],[" "," "," "," "],[" "," "," "," "]]
#[Row][Column]

#Function that draws the playing board
def drawBoard():
    for row in range(4):
        for column in range(4):
            if column != 3:
                print(playingBoard[row][column], " | ",end="")
            if column == 3:
                print(playingBoard[row][column])

#Function that controls the game
def gameStart():
    playerTurn = 1
    
    drawBoard()
    while game == True:
        #Different symbol for both players
        #Change turn value added on to playerTurn variable
        if playerTurn == 1:
            symbol = (colored("O","red"))
            changeTurn = 1
        if playerTurn == 2:
            symbol = (colored("O","blue"))
            changeTurn = -1

        #Turns
        #Prints which player has their turn
        print("It is Player ", playerTurn, "'s turn")
        #Enter column number
        playerMove = int(input("Enter a column from 1-4: "))

        #Doesn't accept values outside of the range
        while playerMove <= 0 or playerMove >= 5:
            print("That number is outside of the range")
            playerMove = int(input("Enter a column from 1-4: "))

        #-1 to change it to 0,1,2,3 instead of 1,2,3,4
        playerMove -= 1

        #For loop that places symbols in empty spaces
        for rowNo in range(3,-1,-1):
            #playerMove = Column
            #rowNo = Row
            if playingBoard[rowNo][playerMove] == " ":
                playingBoard[rowNo][playerMove] = symbol
                break
        drawBoard()
        checkWinCondition(playerTurn)
        #adds changeTurn value to change the player
        playerTurn += changeTurn

#Function that checks for 3 win conditions, - Vertical,horizontal & diagonal
def checkWinCondition(turn):

    global game
    if turn == 1:
        symbol = (colored("O","red"))
    if turn == 2:
        symbol = (colored("O","blue"))

    #Check for vertical win
    for columnNo in range(4):
        for rowNo in range(4):
            if playingBoard[rowNo][columnNo] != symbol:
                break
            elif rowNo == 3:
                print("Player ",turn, " Wins!")
                game = False

    #Check for horizontal win
    for rowNo in range(4):
        for columnNo in range(4):
            if playingBoard[rowNo][columnNo] != symbol:
                break
            elif columnNo == 3:
                print("Player ",turn, " Wins!")
                game = False

    columnNo = 0
    rowNo = 0
    #'Increase' variable changes the increment
    increase = 1
    #Check for diagonal wins
    for counter in range(2):
        for counter in range (4):
            if playingBoard[rowNo][columnNo] != symbol:
                break
            elif rowNo == 3 and columnNo == 3:
                print("Player ",turn, " Wins!")
                game = False
            elif rowNo == 0 and columnNo == 3:
                print("Player ",turn, " Wins!")
                game = False
            else:
                columnNo +=1
                rowNo += increase
        #Check for the other direction
        rowNo = 3
        increase = -1
        
        #If a win condition is met, break the loop
        if game == False:
            break


#Start the game
game = True
gameStart()