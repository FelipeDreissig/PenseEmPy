# exercício 7.3 Calculando o número pelo pela fórmula do Ramanujan.
import math


def eps():
    x = 1.0
    while x + 1 > 1:
        x = x/2
    x = x*2
    return x


def estimate_pi():
    total, k = 0, 0
    factor = ((2 * math.sqrt(2)) / 9801)
    while True:
        num = math.factorial(4 * k) * (1103 + (26390 * k))
        den = math.pow(math.factorial(k), 4) * math.pow(396, (4 * k))
        term = (factor * (num / den))
        total += term
        if abs(term) < 1e-15:
            break
        k += 1
    return 1 / total


print(estimate_pi())
