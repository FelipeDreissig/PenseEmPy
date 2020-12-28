# maior divisor comum levando o zero em consideração


def mdc(a, b):
    resto = None
    while resto != 0:
        if a == 0 and b == 0:
            return print(b)
        elif b == 0:
            return print(a)
        elif a == 0:
            return print(b)
        resto = (a % b)  # função módulo não leva com considreação o ponto do float, isto é, o módulo trava para a sua construção.
        a = b
        b = resto
    return print(a)


mdc(2, 0)
