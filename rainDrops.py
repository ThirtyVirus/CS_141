import turtle as t
import random
import math

"""
Made by: Brandon Calabrese

Welcome to my raindrop program! The program draws anywhere from 1-100 raindrops with ripples.
The program then returns the area of all of the raindrops combined
"""

#CONSTANTS BELOW

def MAX_RAINDROPS():
    """Maximum number of raindrops"""
    return 100
def MAX_RADIUS():
    """Maximum radius of raindrop"""
    return 20
def MIN_RIPPLES():
    """Minimum number of ripples"""
    return 3
def MAX_RIPPLES():
    """Maximum number of ripples"""
    return 8
def BOUNDING_BOX_WIDTH():
    """Height of bounding box"""
    return 580
def BOUNDING_BOX_HEIGHT():
    """Width of bounding box"""
    return 500

def init():
    """Initializes program by drawing bounding box and setting speed"""
    t.speed(0)

    #Draws bounding box
    t.up()
    t.setpos(-1 * BOUNDING_BOX_WIDTH() / 2,-1 * BOUNDING_BOX_HEIGHT() / 2)
    t.down()
    t.setpos(-1 * BOUNDING_BOX_WIDTH() / 2,BOUNDING_BOX_HEIGHT() / 2)
    t.setpos(BOUNDING_BOX_WIDTH() / 2,BOUNDING_BOX_HEIGHT() / 2)
    t.setpos(BOUNDING_BOX_WIDTH() / 2,-1 * BOUNDING_BOX_HEIGHT() / 2)
    t.setpos(-1 * BOUNDING_BOX_WIDTH() / 2,-1 * BOUNDING_BOX_HEIGHT() / 2)
    t.up()
    
def drawRipples(x,y,r,num):
    """Uses iteration to draw the ripples"""
    counter = 2
    while counter < num + 2:
        t.up()
        t.goto(x,y - r * counter + r)

        #Tests if about to go out of bounds
        if x + (r*counter) > (BOUNDING_BOX_WIDTH() / 2) or x - (r*counter) < (-1 * BOUNDING_BOX_WIDTH() / 2) or (y + r) + (r*counter) > (BOUNDING_BOX_HEIGHT() / 2) or (y + r) - (r*counter) < (-1 * BOUNDING_BOX_HEIGHT() / 2):
            break
        t.down()
        t.circle(r * counter)
        counter += 1

def drawCircles(x,y,r,num,total):
    """Uses recursion to draw the raindrops """
    if num < 1:
        pass
    else:     
        t.up()
        t.setpos(x,y)
        t.down()
        
        t.fillcolor(random.random(),random.random(),random.random())
        t.begin_fill()
        t.circle(r)
        t.end_fill()
        
        #Calls the ripple drawing function
        drawRipples(x,y,r,random.randint(MIN_RIPPLES(),MAX_RIPPLES()))
        
        #Adds raindrop area to the toal area
        total += (math.pi * r * r)
        
        drawCircles(random.randint(-1 * BOUNDING_BOX_WIDTH() / 2 + MAX_RADIUS(),BOUNDING_BOX_WIDTH() / 2 - MAX_RADIUS()),random.randint(-1 * BOUNDING_BOX_HEIGHT() / 2 + 20,BOUNDING_BOX_HEIGHT() / 2 - MAX_RADIUS()*2),random.randint(1,MAX_RADIUS()),num - 1,total)
    return total

def main():
    #Gets user input then responds accordingly
    num = int(input("Please input the number of rain drops you want to see (1-100)."))
    if num < 1 or num > 100:
        print("The number of drops must be between 1 and 100!")
    else:
        init()
        print("The total area of the raindrops is " + str(drawCircles(random.randint(-1 * BOUNDING_BOX_WIDTH() / 2 + MAX_RADIUS(),BOUNDING_BOX_WIDTH() / 2 - MAX_RADIUS()),random.randint(-1 * BOUNDING_BOX_HEIGHT() / 2 + 20,BOUNDING_BOX_HEIGHT() / 2 - MAX_RADIUS()*2),random.randint(1,MAX_RADIUS()),num,0)) + " square units.")
        t.hideturtle()
    t.done()
main()
