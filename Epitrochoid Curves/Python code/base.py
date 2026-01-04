import turtle
import math
import colorsys

turtle.colormode(255)

pen = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")

pen.hideturtle()
pen.width(2)

screen.tracer(0, 0)
turtle.delay(0)

R = 120      
r = 35      
d = 90    
sum = r+ R
ratio = sum/ r

steps = 8000

pen.penup()

for i in range(steps):
    t = i * 2 * math.pi / steps

    x = (sum) * math.cos(t) - d * math.cos(ratio * t)
    y = (sum) * math.sin(t) - d * math.sin(ratio * t)

    # rainbow coloring
    h = i / steps
    rc, gc, bc = colorsys.hsv_to_rgb(h, 1, 1)
    pen.pencolor(int(rc * 255), int(gc * 255), int(bc * 255))

    if i == 0:
        pen.goto(x, y)
        pen.pendown()
    else:
        pen.goto(x, y)

screen.update()
turtle.done()
