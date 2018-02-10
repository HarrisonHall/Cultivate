## arcade.py by Harrison Hall, part of Cultivate

import engine
import sys
import math
import os

# Define some important in-game functions

def gameOver(score):
    print('\nYou earned a score of ',str(score),', Good job!',sep='')
    yourName = input('What is your name?: ')
    writeScores(yourName,score)
    displayScores()
    print('Sadly, it is a game over...')
    answer = input("Would you like to play again? (y/n): ")
    if answer == "n":
        print("Have a nice day!")
        sys.exit()
    else:
        keepGoing = False
        while(keepGoing == False):
            size = int(input("What size of garden?: "))
            print("")
            if (size % 2 == 1):
                size += 1
            if (size < 6 or size > 36):
                print("Invalid size (try even: 6 -36)\n")
            else:
                keepGoing = True
        garden = engine.initGarden(size)
        turns = 10
        totalTurns = 0
        score = 0
        cultivate(garden,turns,score,totalTurns)

def displayDetails(turns, score, garden):
    engine.disaster(garden)
    turns -= 1
    realTurns = math.ceil(turns)
    if turns < 0:
        gameOver(score)
    roundScore = math.floor(score)
    print('\nScore: ', roundScore)
    print(realTurns,'turns left\n')
    engine.printGarden(garden)
    return turns, score

def displayScores():
    scoreFile = open("highscores.txt","r")
    for line in scoreFile:
        print(line,end='')
        
def writeScores(name, score):
    score = int(score.ceil())
    scoreFile = open("highscores.txt","r+")
    scoreFileScores = []
    for line in scoreFile:
        scoreFileScores.append(line)
    scoreFile.close()
    ourLine = str(score) + " - " + name
    i = 10
    while(i >= 1):
        highscore = score
        ##parses for thisScore and thisName
        thisPlace = i
        startValue = 0
        thisPlace = scoreFileScores[i][startValue:scoreFileScores[i].find(" ")]
        if (i < 10):
            theRest = scoreFileScores[i][(scoreFileScores[i].find(thisPlace)+4):]
        else:
            theRest = scoreFileScores[i][(scoreFileScores[i].find(thisPlace)+5):]
        thisScore = theRest[:theRest.find(" ")]
        theRest = theRest[theRest.find(" - ")+3:]
        thisName = theRest
        thisScore = int(thisScore)
        thisNewLine = str(i + 1) + " - " + str(thisScore) + " - " + thisName
        ourNewLine = str(i) + " - " + ourLine + "\n"
        if (score > thisScore):
            scoreFileScores[i] = ourNewLine
            if (i < 10):
                scoreFileScores[i+1] = thisNewLine
        i -= 1
    scoreFile = open("highscores.txt","w")        
    for line in scoreFileScores:
        scoreFile.write(line)

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")
    
print("\n\nC U L T I V A T E\n\nBy Harrison Hall\n")

turns = 10
totalTurns = 0
score = 0
size = 16
garden = engine.initGarden(size)
engine.printGarden(garden)
def cultivate(garden, turns, score, totalTurns):
    while(True):
        print("\nDay:",totalTurns)
        if (totalTurns % 10 == 9):
            print("\nNew season next turn")
        elif (totalTurns == 10):
            print("\nWelcome to the new season!\n")
            garden = engine.initGarden(14)
            engine.printGarden(garden)
        elif (totalTurns == 20):
            print("\nWelcome to the new season!\n")
            garden = engine.initGarden(12)
            engine.printGarden(garden)
        elif (totalTurns == 30):
            print("\nWelcome to the new season!\n")
            garden = engine.initGarden(10)
            engine.printGarden(garden)
        elif (totalTurns != 0 and totalTurns % 10 == 0):
            print("\nWelcome to the new season!\n")
            garden = engine.initGarden(8)
            engine.printGarden(garden)
        button = input("\nplant(a) water(w) collect(s) till(d): ")
        if button == 'a':
            choice = input("tomatoes(a) eggplants(s) cotton(d): ")
            if choice == 'a':
                engine.advanceTime(garden)
                engine.plantPlants(garden,1)
                turns, score = displayDetails(turns, score, garden)
                totalTurns += 1
            elif choice == 's':
                engine.advanceTime(garden)
                engine.plantPlants(garden,11)
                turns, score = displayDetails(turns, score, garden)
                totalTurns += 1
            elif choice == 'd':
                engine.advanceTime(garden)
                engine.plantPlants(garden,21)
                turns, score = displayDetails(turns, score, garden)
                totalTurns += 1
            else:
                print("--unknown command--")
        elif button == 'w':
            choice = input("top(w) bottom(s) left(a) right(d): ")
            if choice == 'w':
                engine.advanceTime(garden)
                engine.water(garden,'top')
                turns, score = displayDetails(turns, score, garden)
                totalTurns += 1
            elif choice == 'a':
                engine.advanceTime(garden)
                engine.water(garden,'left')
                turns, score = displayDetails(turns, score, garden)
                totalTurns += 1
            elif choice == 's':
                engine.advanceTime(garden)
                engine.water(garden,'bot')
                turns, score = displayDetails(turns, score, garden)
                totalTurns += 1
            elif choice == 'd':
                engine.advanceTime(garden)
                engine.water(garden,'right')
                turns, score = displayDetails(turns, score, garden)
                totalTurns += 1
            else:
                print("--unknown command--")
        elif button == 's':
            turns, score = engine.collect(garden, score, turns)
            engine.advanceTime(garden)
            turns, score = displayDetails(turns, score, garden)
            totalTurns += 1
        elif button == 'd':
            engine.till(garden)
            engine.advanceTime(garden)
            turns, score = displayDetails(turns, score, garden)
            totalTurns += 1
        elif button == 'stop':
            gameOver(score)
        else: # button == 'd'
            engine.rules()

cultivate(garden, turns, score, totalTurns)
