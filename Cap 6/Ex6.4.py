# maior divisor comum

def mdc(a, b):
    resto = None
    while resto != 0:
        resto = (a % b) # função módulo não leva com considreação o ponto do float, isto é, o módulo trava para a sua construção.
        a = b
        b = resto
    return print(a)


mdc(2, 0)