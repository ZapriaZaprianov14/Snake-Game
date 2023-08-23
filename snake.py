from pytimedinput import timedInput
from random import randint
from sys import exit
import os

#Test commit comment added here
def printField(cells):
    for cell in cells:
        #Prints snake
        if cell in snakeBody:
            print("X",end="")
        #Prints borders
        elif cell[0] in (0,boxHeight-1) or cell[1] in (0,boxWidth-1):
            print("#",end="")
        #Prints apple
        elif cell[0]==applePos[0] and cell[1]==applePos[1]:
            print("a",end="")
        else:
            print(" ",end="")
        #Sets a new row
        if cell[1]==boxWidth-1:
            print("")

def changeApple(apple):
    apple=(randint(1,boxHeight-1),randint(1,boxWidth-1))


def updateSnake():
    global applePos
    #Creates a new head 1 position forward in the current direction
    newHead=(snakeBody[0][0]+direction[0],snakeBody[0][1] + direction[1])
    #Check if the new head is out of bounds
    if(newHead[0]<=0):
        newHead=(boxHeight-2,snakeBody[0][1] + direction[1])
    elif(newHead[0]>=boxHeight-1):
        newHead=(1,snakeBody[0][1] + direction[1])
    elif(newHead[1]<=0):
        newHead=(snakeBody[0][0]+direction[0],boxWidth-2)
    elif(newHead[1]>=boxWidth-1):
        newHead=(snakeBody[0][0]+direction[0],1)
    #Checks if the snake bit herself
    if(newHead in snakeBody):
        exit("You died")
    #Checks if the snake ate the apple and does not remove the last bodypart making it larger puk i ne bachka dgdgdgdfg
    if(newHead[0]==applePos[0] and newHead[1]==applePos[1]):
       while True:
        x=randint(1,boxHeight-2)
        y=randint(1,boxWidth-2)
        temp=(x,y)
        if(temp not in snakeBody):
            applePos=(x,y)
            break
    #Removes the last bodypart if the above conditions are not met mentaining the size of the snake
    else:
        snakeBody.pop(-1)
    snakeBody.insert(0,newHead)


boxHeight=16
boxWidth=32
h=1+2
applePos=(randint(1,boxHeight-2),randint(1,boxWidth-2))
snakeBody=[(1,2),(1,1)]
#A dictionary containing values for aech direction
DIRECTIONS= {'w': (-1,0),'s': (1,0),'a': (0,-1),'d': (0,1)}
direction=DIRECTIONS['d']
#Inits the playing field
cells=[(row,col) for row in range(boxHeight) for col in range(boxWidth)]
os.system('cls')

while True:
    #Clears terminal
    print("\033[%d;%dH" % (0, 0), end="")
    printField(cells)
    txt,_= timedInput("",timeout=0.2)
    match txt:
        case 'w':
            if direction!=DIRECTIONS['s']:
                direction=DIRECTIONS['w']
        case 'a':
            if direction!=DIRECTIONS['d']:
                direction=DIRECTIONS['a']
        case 's':
            if direction!=DIRECTIONS['w']:
                direction=DIRECTIONS['s']
        case 'd':
            if direction!=DIRECTIONS['a']:
                direction=DIRECTIONS['d']
    updateSnake()
