#App draws random polygons with sides ranging from 3 to 10

#Importing the necessary modules
import turtle
import random

#Define the function
def draw_polygon(noSides):
    internalAngles = ((noSides - 2) * 180) / noSides
    externalAngles = 180 - internalAngles
    for i in range(noSides):
        my_pen.forward(100)
        my_pen.left(externalAngles),
    my_pen.right(externalAngles)

#Forming the window screen
tut = turtle.Screen()
tut.bgcolor("black")
tut.title("Shapes into shapes")
my_pen = turtle.Turtle()
my_pen.color("white")
tut = turtle.Screen()

#Calibrating the drawing
for i in range(30):
    draw_polygon(random.randint(3,10))
turtle.done()   