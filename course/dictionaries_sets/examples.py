


BlackShoes = {42:2, 41:3,40:4,39:1,38:0}

while(True): #True==True
    print(BlackShoes)
    purchaseSize = int(input("Which shoe size would you like to buy?\n"))

    if purchaseSize < 0:
        break

    if BlackShoes[purchaseSize] <= 0:
        print("Sorry we're out of stock for that size")
    else:
        BlackShoes[purchaseSize] -= 1     # = BlackShoes[purchaseSize] - 1



