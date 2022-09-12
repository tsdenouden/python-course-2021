

#  /   /  0
#-------- 1
#  /   /  2 
#-------- 3 
#  /   /  4


#First loop to print the rows (4 rows)
for row in range(5): #0,1,2,3,4
    if row%2==0:
        #Second loop to print the columns (5 columns)
        for column in range(1,6): #1,2,3,4,5
            #Condition is met when it's an odd column
            if column%2==1:
                if column !=5:
                  print(" ",end="") #When column is odd and not equal to 5, print this
                else:
                    print(" ") #When column is odd and equal to 5, print this
            else:
                print("|",end="")
        #print(" | | ")
    else:
        #Every time row is odd, it'll print this line
        print("-----")