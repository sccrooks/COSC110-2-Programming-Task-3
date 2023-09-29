import math
import turtle


def square(turtle, length):
    for i in range(4):
        turtle.fd(length)
        turtle.lt(90)


def polygon(turtle, length, n):
    for i in range(n):
        turtle.fd(length)
        turtle.lt(360 / n)


def circle(turtle, r):
    c = 2 * math.pi * r
    n = 50
    l = c / n
    polygon(turtle, n, l)


def arc(turtle, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    polygon(turtle, step_length, n)


bob = turtle.Turtle()
arc(bob, 50, 50)

# In the browser, you need zto use the following rather than turtle.mainloop()
turtle.done()
