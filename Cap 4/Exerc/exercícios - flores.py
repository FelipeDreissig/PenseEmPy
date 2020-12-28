import turtle

flecha = turtle.Turtle()


def folhavai(length, lados):
    c = 0
    ang = 360/lados
    while c < 100:
        c = c + 9
        flecha.fd(length)
        flecha.rt(ang)


#folhavai(10, 100)


def umafolha(length, lados):
    folhavai(length, lados)
    flecha.rt(135)
    folhavai(length, lados)


def inverte(length, lados):
    while True:
        umafolha(length, lados)
        flecha.rt(180)

inverte(10, 100)



