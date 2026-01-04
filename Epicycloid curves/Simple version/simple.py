import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)
pen.color("cyan")
pen.width(2)
pen.hideturtle()


R = 100  
r = 30    
k = (R + r) / r   

# Make motion smooth
steps = 2000

pen.penup()

for i in range(steps):
    angle = i * 2 * pi / steps# small step size for smoothness

    x = (R + r) * math.cos(angles) - r * math.cos(k * angles)
    y = (R + r) * math.sin(angles) - r * math.sin(k * angles)

    if i == 0:
        pen.goto(x, y)
        pen.pendown()
    else:
        pen.goto(x, y)

turtle.done()
