"""
Tristan Shawn Den Ouden 14/5/2021
Homework #6: Advanced Loops
"""

#Function that creates a playing board
def playingBoard(rowNo,columnNo):

    #Limit = 275
    if rowNo >= 275 or columnNo >= 275:
        print("Exceeded the limit")
        exit()

    #Checks if the number of rows is odd or even
    #This ensures the program works regardless of whether the parameters are odd or even.
    if rowNo%2==0:
        row_odd = 0
    if rowNo%2==1:
        row_odd = 1
    #Two if statements instead of one so the program works even if the parameters have the same number.
    if columnNo%2==1:
        col_even = 1
    if columnNo%2==0:
        col_even = 0

    #For loop, repeated for every row 
    for row in range(rowNo+1): #+1 because it's only up to, not including
        #Start drawing the columns
        if row%2==row_odd:
            #For loop, repeated for every column
            for col in range(1,columnNo+1): #+1 because it's only up to, not including
                if col%2==col_even:
                    #Check if it is the last position
                    if col != columnNo:
                        print(" ", end="")
                    #If last, make a new line
                    else: 
                        print(" ")
                else:
                    print("|", end="")
        else:
            #Prints a dash for every column
            for counter in range(columnNo):
                if counter != columnNo-1: #-1 because the range doesn't include the last number
                    print("-", end="")
                else:
                    print("-")
    return True

#Examples

#Even,odd
print("Example 1: ")
playingBoard(4,5)

#Odd,even
print("Example 2:")
playingBoard(5,6)

#Same number
print("Example 3:")
playingBoard(12,12)

#Greater than the limit (275)
print("Example 4:")
playingBoard(350,300)