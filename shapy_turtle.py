import turtle as t
"""
Shapy Turtle - Brandon Calabrese
"""

def getNum(s):
    """
    Returns multiple digit number following command character.
    s is a string
    Returns None if syntax is incorrect
    """
    counter = 0
    if s[0].isdigit() == False:
        return None
    
    for c in s:       
        if c.isdigit():
            counter += 1
        else:
            return int(s[0:counter])
    return int(s[0:counter])

def get2Num(s):
    """
    Returns a set of two multiple digit numbers following a command character that takes 2 arguments
    s is a string
    Returns None if syntax is incorrect
    """
    counter = 0
    num1 = getNum(s)
    num2 = 0

    if num1 == None:
        return None
    
    for c in s:
        if c == ",":
            num2 = getNum(s[counter + 1:])
            break
        counter += 1

    if num2 == None:
        return None
    
    return(num1,num2)

def turnLeft(d):
    """
    Turns the turtle left by d degrees
    d is an integer
    Returns None if incorrect syntax
    """
    if d == None:
        return None
    t.left(d)
    return True

def turnRight(d):
    """
    Turns the turtle right by d degrees
    d is an integer
    Returns None if incorrect syntax
    """
    if d == None:
        return None
    t.right(d)
    return True

def square(d):
    """
    Tells the turtle to draw counder-clockwise square, the sides of which being d length
    d is an integer
    Returns None if incorrect syntax
    """
    if d == None:
        return None
    t.forward(d)
    t.left(90)
    t.forward(d)
    t.left(90)
    t.forward(d)
    t.left(90)
    t.forward(d)
    t.left(90)
    return True
        
def triangle(d):
    """
    Tells the turtle to draw a triangle counter-clockwise, the sides of which being d length
    d is an integer
    Returns None if incorrect syntax
    """
    if d == None:
        return None
    t.forward(d)
    t.left(120)
    t.forward(d)
    t.left(120)
    t.forward(d)
    t.left(120)
    return True
    
def circle(r):
    """
    Tells the turtle to draw a circle of r radius in a counter-clockwise fashion
    r is an integer
    Returns None if incorrect syntax
    """
    if r == None:
        return None
    t.circle(r)
    return True
    
def forward(d):
    """
    Moves the turtle forward by d units
    d is an integer
    Returns None if incorrect syntax
    """
    if d == None:
        return None
    t.forward(d)
    return True

def backwards(d):
    """
    Moves the turtle back by d units
    d is an integer
    Returns None if incorrect syntax
    """
    if d == None:
        return None
    t.back(d)
    return True

def up():
    """
    Uppers the turtle's pen
    """
    t.up()

def down():
    """
    Lowers the turtle's pen
    """
    t.down()

def drawRectangle(d1,d2):
    """
    Tells the turtle to draw a rectangle counter-clockwise, the sides of which being d1 length and d2 width
    d1 and d2 are intended to be integers
    Returns None if incorrect syntax
    """
    if d1 == None or d2 == None:
        return None
    t.forward(d1)
    t.left(90)
    t.forward(d2)
    t.left(90)
    t.forward(d1)
    t.left(90)
    t.forward(d2)
    t.left(90)
    return True

def drawPolygon(num,side):
    """
    Tells the turtle to draw a polygon counter-clockwise with num sides, the sides of which being side length (both varaibles need to be integers)
    Returns None if incorrect syntax
    """
    if num == None or side == None:
        return None
    counter = 0
    while counter < num:
        t.forward(side)
        t.left(180- ((180 * (num - 2)) / num))
        counter += 1
    return True

def goTo(x,y):
    """
    Tells the turtle to travel to the coordinate (x,y), both integers
    Returns None if incorrect syntax
    """
    if x == None or y == None:
        return None
    t.goto(x,y)
    return True
    
def changeColor(num):
    """
    Changes the color of the turtle's pen, accepts numbers 0-4 and defaults to black otherwise
    Returns None if incorrect syntax
    """
    if num == None:
        return None
    if num == 0:
        t.color("red")
    elif num == 1:
        t.color("blue")
    elif num == 2:
        t.color("green")
    elif num == 3:
        t.color("yellow")
    elif num == 4:
        t.color("brown")
    else:
        t.color("black")
    return True

def processString(s):
    """
    Interprets user's command input and executes functions accordingly
    If any function returns None, the entire program stops and the command string is printed and None ius returned
    Any unknown characters result in return None and printing of the command as well
    """
    counter = 0
    for c in s:
        if c == "<":
            if turnLeft(getNum(s[counter + 1:])) == None:
                print(s)
                return None
        elif c == ">":
            if turnRight(getNum(s[counter + 1:])) == None:
                print(s)
                return None
        elif c == "S":
            if square(getNum(s[counter + 1:])) == None:
                print(s)
                return None
        elif c == "T":
            if triangle(getNum(s[counter + 1:])) == None:
                print(s)
                return None
        elif c == "C":
            if circle(getNum(s[counter + 1:])) == None:
                print(s)
                return None
        elif c == "F":
            if forward(getNum(s[counter + 1:])) == None:
                print(s)
                return None
        elif c == "B":
            if backwards(getNum(s[counter + 1:])) == None:
                print(s)
                return None
        elif c == "U":
            up()
        elif c == "D":
            down()
        elif c == "R":
            info = get2Num(s[counter + 1:])
            if info == None:
                print(s)
                return None
            drawRectangle(info[0],info[1])
        elif c == "P":
            info = get2Num(s[counter + 1:])
            if info == None:
                print(s)
                return None
            if info[0] < 3:
                print(s)
                return None                
            drawPolygon(info[0],info[1])
        elif c == "G":
            info = get2Num(s[counter + 1:])
            if info == None:
                print(s)
                return None
            goTo(info[0],info[1])
        elif c == "Z":
            if changeColor(getNum(s[counter + 1:])) == None:
                print(s)
                return None
        elif c == ",":
            pass
        else:
            if c.isdigit() == False:           
                print(s)
                return None
            
        counter += 1
    t.done()
    
def main():
    """
    The first function to run in the program, asks the user to type a string containing ShapyTurtle commands
    """
    processString(input("Please type a string containing ShapyTurtle commands: "))
    
main()
#for testing purposes
#processString("Z2<90F100>40T30Z5C30R30,40R400,3")
