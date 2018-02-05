## Engine of main.py

import sys
import random
import math
import copy

def initGarden(size): #Initialize garden to 0
    i = 0
    garden = []
    while (i < size):
        garden.append([0])
        j = 0
        while (j < size - 1):
            garden[i].append(0)
            j += 1
        i += 1
    print(garden)
    return garden

def printGarden(garden): #Print garden
    for row in garden:
        print(" T ",end='')
    print("")
    for row in garden:
        print("| ",end='')
        for column in row:
            if garden[row][column] > 9 or garden[row][column] < 0:
                printValue = " "+garden[row][column]+" "
                print(printValue,end='')
            else:
                printValue = " "+garden[row][column]+"  "
                print(printValue,end='')
        print(" |")
    for row in garden:
        print(" T ",end='')

def advanceTime(garden): #Advance garden time
    for row in garden:
        for column in row:
            plant = copy.shallowcopy(garden[row][column])
            if plant == 2 or plant == 12 or plant == 14:
                plant += 1
            elif (plant >= 21 and plant < 27):
                plant += 1

def plantPlants(garden, plant): #Plants plants in garden
    for row in garden:
        for column in row:
            if garden[row][column] == 0:
                garden[row][column] = plant

def waterElement(x):
    if x == 1 or x == 11 or x == 13:
        x += 1
    elif (x >= 21 and x < 27):
        x += 1
                
def water(garden,side): #Waters sides of garden
    height = garden.len()
    width = garden[0].len()
    if side == "top":
        i = 0
        while(i < width/2):
            for plant in garden[i]:
                waterElement(x)
            i += 1
    elif side == "bot":
        i = garden.len()-1
        while(i > width/2):
            for plant in garden[i]:
                waterElement(x)
            i -= 1
    elif side == "left":
        for row in garden:
            i = 0
            while(i < width/2):
                waterElement(garden[row][i])
                i += 1
    elif side == "right":
        for row in garden:
            i = garden[0].len()-1
            while(i > width/2):
                waterElement(garden[row][i])
                i -= 1

def till(garden):
    for row in garden:
        for column in row:
            if garden[row][column] == -1:
                garden[row][column] = 0

def collect(garden, score, turnCount):
    for row in garden:
        for column in row:
            plant = copy.shallowcopy(garden[row][column])
            if plant == 3:
                plant = -1
                score += 1
                turnCount += .09
            elif plant == 15:
                plant = -1
                score += 2
                turnCount += .26
            elif plant == 27:
                plant = -1
                score += 4
                turnCount += .4

def disaster(garden):
    randomNum = random.randrange(0,garden.len()*2-1)
    if randomNum < garden.len():
        i = 0
        z = garden.len() - 1
        while(i <= z):
            garden[randomNum][i] = -1
            i += 1
    else:
        randomNum -= garden.len()
        for row in garden:
            garden[row][randomNum] = -1
    randomSaying = random.randrange(0,10)
    y = randomSaying
    print('')
    if y==0:
        print('Uh oh!')
    elif y==1:
        print('A violent hurrican came through!')
    elif y==2:
        print('The lawn-mower went loose again!')
    elif y==3:
        print('The landlord took the crops from his tenant!')
    elif y==4:
        print('Locusts joined the fray!')
    elif y==5:
        print('The moles are at it again!')
    elif y==6:
        print('Whoopsie!')
    elif y==7:
        print('The flash flood warning was too late!')
    elif y==8:
        print('I am ready for rabbit stew!')
    elif y==9:
        print('Watch where you step!')
    else:
        print('dem elpacas!')

def rules():
    print('The game starts in an 8x8 garden, already tilled (brown), so you can p\
        lant either tomatoes, eggplants, or cotton. ')
    print('Tomatoes grow the fastest, with one turn of watering and one turn of w\
            aiting, and yield the least turns and points.')
    print('Eggplants grow slower, with two turns of watering and two turns of wai\
                ting, and yield a medium number of turns and points.')
    print('Cotton grows the slowest, with 7 turns of waiting, and yield the most \
turns and points. Is it worth it?')
    print('Plants needing water will be blue, while plants needing time will be t\
heir own color. You can only water half the garden in a turn.')
    print('Once you collect all of the ready plants, marked by the color green, th\
e only thing remaining is dirt, which will need to be tilled in order to be plantable.')
    print('After every turn a natural disaster will come and destroy a row or col\
umn of your garden.')
    print('You only have so many turns until you get a GAME OVER, so be sure to C\
ultivate your Garden!')

