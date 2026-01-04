import turtle
import math
import colorsys
from turtle import *
import colorsys

pen = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Curtate Tropoid Animation")

pen.speed(0)
pen.width(2)
pen.hideturtle()

turtle.colormode(1)
screen.tracer(0, 0)

steps = 1000
r = 80
scale = 1.5


dt = 0.02 #fr smoothness
t_max = (steps - 1) * dt

#precompute points so we can auto-fit the entire curve into the window.
points = []
min_x = float("inf")
max_x = float("-inf")
min_y = float("inf")
max_y = float("-inf")

for i in range(steps):
    t = i * dt 

    x = r * (t - math.sin(t)) * scale
    y = r * (1 -  math.cos(t)) * scale

    points.append((x, y))
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)

margin = max(20, 0.08 * max(max_x - min_x, max_y - min_y))
screen.setworldcoordinates(min_x - margin, min_y - margin, max_x + margin, max_y + margin)


for i, (x, y) in enumerate(points):

    hue = (i/steps) % 1.0

    r_col, g_col, b_col = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    pen.pencolor(r_col, g_col, b_col)
    if i == 0:
        pen.goto(x, y)
        pen.pendown()

    else:
        pen.goto(x, y)

turtle.done()
