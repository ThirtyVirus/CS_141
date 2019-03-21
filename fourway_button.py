import turtle

"""
Made by Brandon Calabrese

Welcome to my turtle four way button project! It uses the below method to easily
go to relative coordines, which helps me keep distances and proportions of the image constant.

The method below that draws equilateral triangles and returns the turtle to its original position.
"""

def walkTo(x,y,draw,relative,preferX):
    turtle.up()
    #Determines Whether to draw or not
    if draw == True:
        turtle.down()
    else:
        turtle.up()
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

def drawTriangle():
    turtle.up()
    turtle.forward(100)
    turtle.right(30)
    turtle.down()
    
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)

    turtle.up()
    turtle.right(30)
    turtle.forward(100)

def main():
    #draws a centered circle to start
    turtle.up()
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.down()
    turtle.circle(50)
    walkTo(-250,-200,False,True,False)

    #draws each side of the square and follows up with a triangle
    walkTo(0,500,True,True,False)
    turtle.left(135)
    drawTriangle()
    turtle.left(45)
    walkTo(500,0,True,True,False)
    turtle.right(135)
    drawTriangle()
    turtle.right(45)
    walkTo(0,-500,True,True,False)
    turtle.left(135)
    drawTriangle()
    turtle.left(45)
    walkTo(-500,0,True,True,False)
    turtle.right(135)
    drawTriangle()
    turtle.right(45)

main()
