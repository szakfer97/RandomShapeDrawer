# App that randomly draws triangles,squares and hexagons

# Importing the necessary modules
import turtle
import random

# Define the functions
def form_tri(side):
    for i in range(3):
        my_pen.fd(side)
        my_pen.left(120)
        side -= 10

def form_sq(side):
    for i in range(4):
        my_pen.fd(side)
        my_pen.left(90)
        side -= 5

def form_pen(side):
    for i in range(5):
        my_pen.fd(side)
        my_pen.left(72)

def form_hex(side):
    for i in range(6):
        my_pen.fd(side)
        my_pen.left(300)

shape_list = [form_tri, form_sq, form_pen, form_hex]

# Forming the window screen
tut = turtle.Screen()
tut.bgcolor("black")
tut.title("Continous random shapes")
my_pen = turtle.Turtle()
my_pen.color("white")
tut = turtle.Screen()

# Calibrating the drawing
side = 120
for i in range(20):
    random.choice(shape_list)(side)
    my_pen.right(300)
turtle.done()
