import turtle
from turtle import *
import math
import colorsys
import time

turtle.colormode(255)

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Prolate Trophoid Pattern")
screen.setup(width=900, height=900)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.width(2)


points = []
min_x = float("inf")
max_x = float("-inf")
min_y = float("inf")
max_y = float("-inf")


screen.tracer(1, 0)
turtle.delay(0)

r = 80
d = 140 
# in prolate trochoid, d > r thats the main difference from curtate trochoid    
scale = 0.02
steps = 1500
update = 20
actual_scale = 1.5

pen.penup()

for i in range(steps):
    t = i * scale

    x = r *t - d * math.sin(t)
    y = r - d * math.cos(t)

    points.append((x, y))
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)

    margin = max(20, 0.08 * max(max_x - min_x, max_y - min_y))
    screen.setworldcoordinates(min_x - margin, min_y - margin, max_x + margin, max_y + margin)

for i, (x, y) in enumerate(points):
    x *= actual_scale
    y *= actual_scale
    

    hue = (i / steps) % 1.0

    r_col, g_col, b_col = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    pen.pencolor(int(r_col * 255), int(g_col * 255), int(b_col * 255))

    if i == 0:
        pen.goto(x, y)
        pen.pendown()
        #will start drawing from the first point

    else:
        pen.goto(x, y)

    if i % update == 0:
        screen.update()
        time.sleep(0.01)

screen.update()
turtle.done()

