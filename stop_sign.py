# CS175L-50
# Juliana Gomez
# stop_sign.py

import math
import turtle

# Named constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10
s = 100
x = s / math.sqrt(2)
diameter = s + (2 * x)

# Size the window.
t = turtle.Turtle()

turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)

t.penup()
t.goto(-50, 115)
t.pendown()

for x in range(0, NUM_SIDES):
    t.fd(100)
    t.rt(45)


t.penup()    
t.goto(-5,-10)
t.pendown()
t.write('STOP')

t.penup()

# t.goto(diameter, diameter)
