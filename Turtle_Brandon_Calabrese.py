import turtle
import string
letterProgress = 1
line = 0

"""
Made by Brandon Calabrese

Welcome to my turtle text editor! 
Change the below variable 'message' to any string you want!
The program knows the entire alphabet (minus K, V, and X) and numbers 0-9 (minus 5)
Once run, the turtle will draw your string!
Also, if a string is too long than it will continue to the next line.
"""
message = "Turtle bmc1340@rit.edu"

def walkTo(x,y,draw,relative,preferX):
    turtle.up()
    #Determines Whether to draw or not
    if draw == True:
        turtle.down()
        
    #Determines if x and y are relative to current position
    if relative == True:
        x += turtle.position()[0]
        y += turtle.position()[1]
        
    #Executes x axis movement first
    if preferX == True:
        if turtle.position()[0] < x:
            turtle.setheading(0) #Turns east
            turtle.forward(abs(x - turtle.position()[0]))

        if turtle.position()[0] > x:
            turtle.setheading(180) #Turns west
            turtle.forward(abs(x - turtle.position()[0]))

        if turtle.position()[1] < y:
            turtle.setheading(90) #Turns north
            turtle.forward(abs(y - turtle.position()[1]))
            
        if turtle.position()[1] > y:
            turtle.setheading(270) #Turns south     
            turtle.forward(abs(y - turtle.position()[1]))
            
    #Executes y axis movement first
    else:
        if turtle.position()[1] < y:
            turtle.setheading(90) #Turns north
            turtle.forward(abs(y - turtle.position()[1]))
            
        if turtle.position()[1] > y:
            turtle.setheading(270) #Turns south     
            turtle.forward(abs(y - turtle.position()[1]))

        if turtle.position()[0] < x:
            turtle.setheading(0) #Turns east
            turtle.forward(abs(x - turtle.position()[0]))

        if turtle.position()[0] > x:
            turtle.setheading(180) #Turns west
            turtle.forward(abs(x - turtle.position()[0]))

#Moves Turtle to starting point of the next letter
def nextLetter():
    global letterProgress
    walkTo((letterProgress * 160) + (letterProgress * 20),3000 - (line * 160 + line * 40),False,False, False)
    letterProgress += 1

#Methods that draw each character
def A():
    walkTo(160,160,True,True, False)
    walkTo(0,-160,True,True, False)
    walkTo(-160,80,True,True, False)
    nextLetter()
def B():
    walkTo(160,160,True,True, False)
    walkTo(-80,-80,True,True, False)
    walkTo(80,-80,True,True, True)
    walkTo(-160,0,True,True, True)
    nextLetter()
def C():
    walkTo(160,160,True,True, False)
    walkTo(-160,-160,True,True, True)
    walkTo(160,0,True,True, False)
    nextLetter()
def D():
    walkTo(160,160,True,True, True)
    walkTo(-160,0,True,True, True)
    walkTo(40,-160,True,True, True)
    nextLetter()
def E():
    walkTo(160,160,True,True, False)
    walkTo(-160,-80,True,True, True)
    walkTo(80,0,True,True, True)
    walkTo(-80,-80,True,True, True)
    walkTo(160,0,True,True, True)
    nextLetter()
def F():
    walkTo(160,160,True,True, False)
    walkTo(-160,-80,True,True, True)
    walkTo(80,0,True,True, True) 
    nextLetter()
def G():
    walkTo(160,160,True,True, False)
    walkTo(-160,-160,True,True, True)
    walkTo(160,80,True,True, True)
    walkTo(-80,0,True,True, False)
    nextLetter()
def H():
    walkTo(0,160,True,True, True)
    walkTo(160,-80,True,True, False)
    walkTo(0,80,True,True, True)
    walkTo(0,-160,True,True, True)   
    nextLetter()
def I():
    walkTo(160,0,True,True, True)
    walkTo(-80,160,True,True, True)
    walkTo(-80,0,True,True, True)
    walkTo(160,0,True,True, True)
    nextLetter()
def J():
    walkTo(80,160,True,True, True)
    walkTo(-80,0,True,True, True)
    walkTo(160,0,True,True, True)
    nextLetter()
def K():
    nextLetter()
def L():
    walkTo(0,160,True,True, True)
    walkTo(160,-160,True,True, False)
    nextLetter()
def M():
    walkTo(80,160,True,True, False)
    walkTo(0,-160,True,True, False)
    walkTo(80,160,True,True, False)
    walkTo(0,-160,True,True, False)
    nextLetter()
def N():
    walkTo(160,160,True,True, False)
    walkTo(0,-160,True,True, False)
    nextLetter()
def O():
    walkTo(160,160,True,True, False)
    walkTo(-160,-160,True,True, False)
    nextLetter()
def P():
    walkTo(160,160,True,True, False)
    walkTo(-160,-80,True,True, False)
    nextLetter()
def Q():
    walkTo(140,160,True,True, False)
    walkTo(-140,-160,True,True, False)
    walkTo(160,40,False,True, False)
    walkTo(-80,0,True,True, False)
    nextLetter()
def R():
    walkTo(160,160,True,True, False)
    walkTo(-160,-80,True,True, False)
    walkTo(80,-80,True,True, True)
    nextLetter()
def S():
    walkTo(160,80,True,True, True)
    walkTo(-160,80,True,True, True)
    walkTo(160,0,True,True, True)
    nextLetter()
def T():
    walkTo(0,160,False,True, True)
    walkTo(160,0,True,True, True)
    walkTo(-80,-160,True,True, True)
    nextLetter()
def U():
    walkTo(0,160,True,True, True)
    walkTo(160,-160,True,True, False)
    walkTo(0,160,True,True, False)
    nextLetter()
def V():
    nextLetter()
def W():
    walkTo(0,160,True,True, True)
    walkTo(0,-160,True,True, True)
    walkTo(80,0,True,True, True)
    walkTo(0,160,True,True, True)
    walkTo(0,-160,True,True, True)
    walkTo(80,0,True,True, True)
    walkTo(0,160,True,True, True)
    walkTo(0,-160,True,True, True)
    nextLetter()
def X():
    #      x, y,  draw, relative, preferX
    
    nextLetter()
def Y():
    walkTo(80,0,False,True, True)
    walkTo(0,80,True,True, True)
    walkTo(-80,80,True,True, True)
    walkTo(160,-80,True,True, False)
    walkTo(0,80,True,True, True)
    nextLetter()
def Z():
    nextLetter()
def Zero():
    walkTo(160,160,True,True, True)
    walkTo(-160,-160,True,True, True)
    walkTo(80,160,True,True, True)
    nextLetter()
def One():
    walkTo(160,0,True,True, True)
    walkTo(-80,160,True,True, True)
    walkTo(-80,0,True,True, True)
    nextLetter()
def Two():
    walkTo(160,0,False,True, True)
    walkTo(-160,80,True,True, True)
    walkTo(160,80,True,True, True)
    walkTo(-160,0,True,True, True)
    nextLetter()
def Three():
    walkTo(160,0,False,True, True)
    walkTo(0,160,True,True, True)
    walkTo(-160,0,True,True, True)
    walkTo(160,-80,True,True, True)
    walkTo(-160,0,True,True, True)
    walkTo(160,-80,True,True, True)
    walkTo(-160,0,True,True, True)
    nextLetter()
def Four():
    walkTo(160,0,False,True, True)
    walkTo(0,160,True,True, True)
    walkTo(-160,-80,True,True, False)
    walkTo(0,80,True,True, True)
    nextLetter()
def Five():
    nextLetter()
def Six():
    walkTo(160,80,True,True, True)
    walkTo(-160,-80,True,True, True)
    walkTo(0,160,True,True, True)
    nextLetter()
def Seven():
    walkTo(160,0,False,True, True)
    walkTo(-160,160,True,True, False)
    nextLetter()
def Eight():
    walkTo(160,160,True,True, True)
    walkTo(-160,-160,True,True, True)
    walkTo(160,80,True,True, False)
    nextLetter()
def Nine():
    walkTo(160,0,False,True, True)
    walkTo(-160,160,True,True, False)
    walkTo(160,-80,True,True, False)
    nextLetter()
def Period():
    walkTo(80,0,False,True, True)
    turtle.down()
    turtle.circle(5)
    nextLetter()
def At():
    walkTo(0,80,False,True, True)
    turtle.down()
    turtle.right(180)
    turtle.circle(80)
    turtle.circle(60)
    walkTo(120,60,False,True,True)
    walkTo(0,-120,True,True,True)
    nextLetter()

def debug():
    global message
    message = "abcdefghijklmnopqrstuvwxyz0123456789@."

def main():
    #debug()
    turtle.setup(1200,600)
    turtle.setworldcoordinates(0,0,4800,3200)
    #turtle.speed(0) #FOR DEBUGGING ONLY
    global line
    walkTo(0,3000 - (line * 160 + line * 40),False,False,False)
    #      x, y,  draw, relative, preferX
    global message

    #Loops through each character in string
    for ch in message:

        #Goes to next line if needed
        global letterProgress
        if letterProgress == 26:
            letterProgress = 0
            line += 1

        #Calls character draw methods if valid character detected
        if ch == 'A' or ch == "a":
            A()
        elif ch == 'B' or ch == "b":
            B()
        elif ch == 'C' or ch == "c":
            C()
        elif ch == 'D' or ch == "d":
            D()
        elif ch == 'E' or ch == "e":
            E()
        elif ch == 'F' or ch == "f":
            F()
        elif ch == 'G' or ch == "g":
            G()
        elif ch == 'H' or ch == "h":
            H()
        elif ch == 'I' or ch == "i":
            I()
        elif ch == 'J' or ch == "j":
            J()
        elif ch == 'K' or ch == "k":
            K()
        elif ch == 'L' or ch == "l":
            L()
        elif ch == 'M' or ch == "m":
            M()
        elif ch == 'N' or ch == "n":
            N()
        elif ch == 'O' or ch == "o":
            O()
        elif ch == 'P' or ch == "p":
            P()
        elif ch == 'Q' or ch == "q":
            Q()
        elif ch == 'R' or ch == "r":
            R()
        elif ch == 'S' or ch == "s":
            S()
        elif ch == 'T' or ch == "t":
            T()
        elif ch == 'U' or ch == "u":
            U()
        elif ch == 'V' or ch == "v":
            V()
        elif ch == 'W' or ch == "w":
            W()
        elif ch == 'X' or ch == "x":
            X()
        elif ch == 'Y' or ch == "y":
            Y()
        elif ch == 'Z' or ch == "z":
            Z()
        elif ch == '0':
            Zero()
        elif ch == '1':
            One()
        elif ch == '2':
            Two()
        elif ch == '3':
            Three()
        elif ch == '4':
            Four()
        elif ch == '5':
            Five()
        elif ch == '6':
            Six()
        elif ch == '7':
            Seven()
        elif ch == '8':
            Eight()
        elif ch == '9':
            Nine()
        elif ch == ' ':
            nextLetter()
        elif ch == ".":
            Period()
        elif ch == "@":
            At()
        else:
            nextLetter()

    turtle.done()


main()
