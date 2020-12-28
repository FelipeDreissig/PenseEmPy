import turtle
from time import *

pen = turtle.Turtle()


def triangulo(tam, gira):
    c = 0
    while c < 3:
        c = c + 1
        pen.fd(tam)
        pen.lt(gira)


def trianguloc(tam, gira):
    triangulo(tam, gira)
    pen.lt(60)
    triangulo(tam, gira)
    pen.lt(60)


trianguloc(150, 120)
trianguloc(150, 120)
trianguloc(150, 120)
trianguloc(150, 120)
