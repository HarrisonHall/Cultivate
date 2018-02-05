## main.py by Harrison Hall, part of Cultivate

import engine
import sys

# Define some important in-game functions

def gameOver(score):
    print('\nYou earned a score of',score,', Good job!')
    print('Sadly, it is a game over...')
    answer = input("Would you like to play again? (y/n): ")
    if answer == "n":
        print("Have a nice day!")
        sys.exit()
    else:
        size = input("What size of garden?")
        garden = engine.initGarden(size)
        startGame(garden)

def displayDetails(turns, score, garden):
    engine.disaster(garden)
    turns -= 1
    realTurns = math.ceil(turns)
    if turns < 0:
        gameOver(score)
    print('Score: ', score)
    print(realTurns,'left')
    engine.printGarden(garden)


print("\n\nCULTIVATE\n\nBy Harrison Hall\n")

turns = 10
score = 0

size = int(input("What size of garden?: "))
garden = engine.initGarden(size)
engine.printGarden(garden)

while(True):
    button = input("Plant(a) water(w) collect(s) till(d): ")
    if button == 'a':
        choice = input("tomatoes(a) eggplants(s) cotton(d): ")
        if choice == 'a':
            engine.advanceTime(garden)
            engine.plantPlants(garden,1)
            displayDetails(turns, score, garden)
        elif choice == 's':
            engine.advanceTime(garden)
            engine.plantPlants(garden,11)
            displayDetails(turns, score, garden)
        elif choice == 'd':
            engine.advanceTime(garden)
            engine.plantPlants(garden,21)
            displayDetails(turns, score, garden)
        else:
            print("--unknown command--")
    elif button == 'w':
        choice = input("top(w) bottom(s) left(a) right(d): ")
        if choice == 'w':
            engine.advanceTime(garden)
            engine.water(garden,'top')
            displayDetails(turns, score, garden)
        elif choice == 'a':
            engine.advanceTime(garden)
            engine.water(garden,'left')
            displayDetails(turns, score, garden)
        elif choice == 's':
            engine.advanceTime(garden)
            engine.water(garden,'bot')
            displayDetails(turns, score, garden)
        elif choice == 'd':
            engine.advanceTime(garden)
            engine.water(garden,'right')
            displayDetails(turns, score, garden)
        else:
            print("--unknown command--")
    elif button == 's':
        engine.collect(garden, score, turns)
        engine.advanceTime(garden)
        displayDetails(turns, score, garden)
    elif button == 'd':
        engine.till(garden)
        engine.advanceTime(garden)
        displayDetails(turns, score, garden)
    elif button == 'stop':
        gameOver(score)
    else: # button == 'd'
        engine.rules()
