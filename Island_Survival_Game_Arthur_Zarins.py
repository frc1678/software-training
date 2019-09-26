import random
squares = {}
size = 3
xPos = size // 2
yPos = size // 2
for x in range(size):
    for y in range(size):
        #Add a square
        squares.update({str(x) + "-" + str(y): True})
#print(squares)
def printBoard():
    for y in range(size):
        line = ""
        for x in range(size):
            #Add a square
            boolo = squares[str(x) + "-" + str(y)]
            if boolo == True:
                if y == yPos and x == xPos:
                    line = line + "Pl"
                else:
                    line = line + "[]"
            else:
                line = line + "  "
        print(line)
    # else:
        #Off-board
#End of function
game = True
while game == True:
    printBoard()
    legalMove = False
    while legalMove == False:
        oX = xPos
        oY = yPos
        move = input("Where will you move? wasd controls\n ")
        if move == "w":
            yPos = yPos - 1
            if -1 < xPos < size and -1 < yPos < size:
                legalMove = True
        elif move == "a":
            xPos = xPos - 1
            if -1 < xPos < size and -1 < yPos < size:
                legalMove = True
        elif move == "s":
            yPos = yPos + 1
            if -1 < xPos < size and -1 < yPos < size:
                legalMove = True
        elif move == "d":
            xPos = xPos + 1
            if -1 < xPos < size and -1 < yPos < size:
                legalMove = True
        else:
            print("Invalid move")
        #Return to last pos if unaccepted
        if legalMove == False:
            xPos = oX
            yPos = oY
        #end
    #Remove terrain
    RX = 0
    RY = 0
    while (RX == xPos and RY == yPos) or squares[str(RX) + "-" + str(RY)] == False:
        #We want to remove a new part of the Island, and not kill the player
        RX = random.randint(0, size)
        RY = random.randint(0, size)
        if RX > 9:
            RX = 9
        if RY > 9:
            RY = 9 
    if RX == xPos and RY == yPos:
        print()
    else:
        squares.update({str(RX) + "-" + str(RY): False})
        if squares[str(xPos) + "-" + str(xPos)] == False:
            print ("GAME OVER")
            game = False