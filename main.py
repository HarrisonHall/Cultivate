## main.py by Harrison Hall, part of Cultivate

import engine
import sys
import math
import os

# Define some important in-game functions

def gameOver(score):
    print('\nYou earned a score of ',str(score),', Good job!',sep='')
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
        score = 0
        cultivate(garden,turns,score)

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

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")
    
print("\n\nC U L T I V A T E\n\nBy Harrison Hall\n")

turns = 10
score = 0

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
engine.printGarden(garden)
def cultivate(garden, turns, score):
  while(True):
      button = input("\nplant(a) water(w) collect(s) till(d): ")
      if button == 'a':
          choice = input("tomatoes(a) eggplants(s) cotton(d): ")
          if choice == 'a':
              engine.advanceTime(garden)
              engine.plantPlants(garden,1)
              turns, score = displayDetails(turns, score, garden)
          elif choice == 's':
              engine.advanceTime(garden)
              engine.plantPlants(garden,11)
              turns, score = displayDetails(turns, score, garden)
          elif choice == 'd':
              engine.advanceTime(garden)
              engine.plantPlants(garden,21)
              turns, score = displayDetails(turns, score, garden)            
          else:
              print("--unknown command--")
      elif button == 'w':
          choice = input("top(w) bottom(s) left(a) right(d): ")
          if choice == 'w':
              engine.advanceTime(garden)
              engine.water(garden,'top')
              turns, score = displayDetails(turns, score, garden)
          elif choice == 'a':
              engine.advanceTime(garden)
              engine.water(garden,'left')
              turns, score = displayDetails(turns, score, garden)
          elif choice == 's':
              engine.advanceTime(garden)
              engine.water(garden,'bot')
              turns, score = displayDetails(turns, score, garden)
          elif choice == 'd':
              engine.advanceTime(garden)
              engine.water(garden,'right')
              turns, score = displayDetails(turns, score, garden)
          else:
              print("--unknown command--")
      elif button == 's':
          turns, score = engine.collect(garden, score, turns)
          engine.advanceTime(garden)
          turns, score = displayDetails(turns, score, garden)
      elif button == 'd':
          engine.till(garden)
          engine.advanceTime(garden)
          turns, score = displayDetails(turns, score, garden)
      elif button == 'stop':
          gameOver(score)
      else: # button == 'd'
          engine.rules()

cultivate(garden, turns, score)
