def compare(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return (-1)


# calculando hipotenusa

import math


def hip(x1, y1, x2, y2):
    a = math.pow((x2 - x1), 2)
    b = math.pow((y2 - y1), 2)
    h = math.sqrt(a + b)
    return h

# verificando se está entre os extremos


def is_between(x, y, z):
    if x <= y <= z:
        return True
    else:
        return False


# fazendo o fibonacci


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
