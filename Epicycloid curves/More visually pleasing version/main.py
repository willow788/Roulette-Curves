import turtle 
import math
import random
import time
from turtle import *
import colorsys

pen = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")

pen.speed(0)
pen.color("cyan")
pen.width(2)

pen.hideturtle()

#parameters
R = 110
r = 37
d = 20
k = (R + r)/ r 
hue = 0
steps = 5000

pen.penup()

for i in range(steps):
    angle = i * 0.03
    x = (R + r) * math.cos(angle) - d* math.cos(k * angle)
    y = (R + r) * math.sin(angle) - d * math.sin(k * angle)
    #these are the parametric equations for an epicycloid

    hue += 0.0005
    r_col, g_col, b_col = colorsys.hsv_to_rgb(hue % 1, 1, 1)
    pen.pencolor(r_col, g_col, b_col)

    if i ==0:
        pen.goto(x, y)
        pen.pendown()

    else:
        pen.goto(x, y)

turtle.done()
