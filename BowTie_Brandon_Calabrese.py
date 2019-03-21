import turtle
"""
BowTie Project - By Brandon Calabrese

This program draws bowties in a recursive fashion,
and you can change how many layers deep it goes and the size of the bowties.
"""
def drawBowTie(length, depth):       
   turtle.left(60)
   turtle.forward(length)
   turtle.left(120)
   turtle.forward(length)
   turtle.left(120)
   turtle.forward(length * 2)
   turtle.right(120)
   turtle.forward(length)
   turtle.right(120)
   turtle.forward(length)
   turtle.right(60)

   turtle.up()
   turtle.forward(length / 4)
   turtle.right(90)
   turtle.down()

   #Draws Center Circle
   turtle.fillcolor("green")
   turtle.begin_fill()
   turtle.circle(length / -4)
   turtle.end_fill()

   turtle.up()
   turtle.right(90)
   turtle.forward(length / 4)
   turtle.left(180)

   #Start of Recursion
   if depth == 0:
       pass
   else:
      #Draws Top Two Extension BowTies
      turtle.up()
      turtle.left(60)
      turtle.forward(length*2)
      turtle.right(90)
      
      turtle.down()
      drawBowTie(length / 3,depth - 1)

      turtle.up()      
      turtle.right(90)
      turtle.forward(length*2)
      turtle.left(120)
      #Home
      turtle.right(60)
      turtle.forward(length*2)
      turtle.left(90)

      turtle.down()
      drawBowTie(length / 3,depth - 1)

      turtle.up()      
      turtle.left(90)
      turtle.forward(length*2)
      turtle.right(120)
      #Home
      #Draws Bottom Two Extension BowTies
      turtle.left(180)
      
      turtle.up()
      turtle.left(60)
      turtle.forward(length*2)
      turtle.right(90)
      
      turtle.down()
      drawBowTie(length / 3,depth - 1)

      turtle.up()      
      turtle.right(90)
      turtle.forward(length*2)
      turtle.left(120)
      #Home
      turtle.right(60)
      turtle.forward(length*2)
      turtle.left(90)

      turtle.down()
      drawBowTie(length / 3,depth - 1)

      turtle.up()      
      turtle.left(90)
      turtle.forward(length*2)
      turtle.right(120)
      #Home
      turtle.right(180)

def main():
   turtle.speed(0)
   turtle.left(90)
   drawBowTie(150,4)
   turtle.hideturtle()
   turtle.done()


main()
