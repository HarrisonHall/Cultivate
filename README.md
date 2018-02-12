# Cultivate
Cultivate is a text-based arcade game reminiscent of something I created in high school.
The objective of this game is to keep your garden going as long as possible in order to maximize score. 

## Getting Started
You can play Cultivate with the help of Python3.

*Prerequisites*
* Install Python3

*Running*
* Clone or download to your desired location
* Launch main.py 
  * Use your Python launcher
  * or in unix: `Python3 main.py`
  
## Game Rules
* The goal is to accumulate the highest possible score, before the number of turns run out
* There are 5 tile states in the nxn garden
   * Tilled dirt - "d" - dirt that can be planted in
   * Untilled dirt - "x" - dirt that cannot be planted in
   * Plant - "t","e", or "c" - a plant that needs time to grow
   * Unwatered plants - "w" - plants that need watering
   * Uncollected plants - "r" - plants ready to be harvested for points and turns
* There are four actions
  * Plant plants (a)
    * This plants the desired plants in all available tilled dirt tiles
  * Water plants (w)
    * This waters all plants on the desired side of the garden
  * Collect plants (s)
    * Harvests all "ready" plants
  * Till tiles (d)
    * Tills all untilled garden tiles
* Every turn, a row or column will be destroyed
* Every 10 turns, a new season will begin
  * New seasons reset, or even shrink, the garden
  * Adjust it to your strategy!
* Different plants have different properties, discover them!

## Gameplay Example
```
C U L T I V A T E

By Harrison Hall


Arcade(a) or Sandbox(s)?: a

"stop" to exit, "r" for rules

TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
|  d  d  d  d  d  d  d  d  d  d  d  d  d  d  d  d  |
|  d  d  d  d  d  d  d  d  d  d  d  d  d  d  d  d  |
|  d  d  d  d  d  d  d  d  d  d  d  d  d  d  d  d  |
|  d  d  d  d  d  d  d  d  d  d  d  d  d  d  d  d  |
|  d  d  d  d  d  d  d  d  d  d  d  d  d  d  d  d  |
|  d  d  d  d  d  d  d  d  d  d  d  d  d  d  d  d  |
|  d  d  d  d  d  d  d  d  d  d  d  d  d  d  d  d  |
|  d  d  d  d  d  d  d  d  d  d  d  d  d  d  d  d  |
|  d  d  d  d  d  d  d  d  d  d  d  d  d  d  d  d  |
|  d  d  d  d  d  d  d  d  d  d  d  d  d  d  d  d  |
|  d  d  d  d  d  d  d  d  d  d  d  d  d  d  d  d  |
|  d  d  d  d  d  d  d  d  d  d  d  d  d  d  d  d  |
|  d  d  d  d  d  d  d  d  d  d  d  d  d  d  d  d  |
|  d  d  d  d  d  d  d  d  d  d  d  d  d  d  d  d  |
|  d  d  d  d  d  d  d  d  d  d  d  d  d  d  d  d  |
|  d  d  d  d  d  d  d  d  d  d  d  d  d  d  d  d  |
TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
Day: 0

plant(a) water(w) collect(s) till(d): a
tomatoes(a) eggplants(s) cotton(d): a

The flash flood warning was too late!

Score:  0
9 turns left

TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
|  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  |
|  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  |
|  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  |
|  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  |
|  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  |
|  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  |
|  x  x  x  x  x  x  x  x  x  x  x  x  x  x  x  x  |
|  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  |
|  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  |
|  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  |
|  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  |
|  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  |
|  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  |
|  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  |
|  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  |
|  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  |
TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
Day: 1

plant(a) water(w) collect(s) till(d): w
top(w) bottom(s) left(a) right(d): w

The moles are at it again!

Score:  0
8 turns left

TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
|  t  t  t  t  t  t  t  t  t  t  t  t  t  t  t  t  |
|  t  t  t  t  t  t  t  t  t  t  t  t  t  t  t  t  |
|  t  t  t  t  t  t  t  t  t  t  t  t  t  t  t  t  |
|  t  t  t  t  t  t  t  t  t  t  t  t  t  t  t  t  |
|  t  t  t  t  t  t  t  t  t  t  t  t  t  t  t  t  |
|  t  t  t  t  t  t  t  t  t  t  t  t  t  t  t  t  |
|  x  x  x  x  x  x  x  x  x  x  x  x  x  x  x  x  |
|  t  t  t  t  t  t  t  t  t  t  t  t  t  t  t  t  |
|  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  |
|  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  |
|  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  |
|  x  x  x  x  x  x  x  x  x  x  x  x  x  x  x  x  |
|  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  |
|  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  |
|  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  |
|  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  w  |
TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
Day: 2

plant(a) water(w) collect(s) till(d): 
```
