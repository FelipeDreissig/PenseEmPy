# desenhar diagramda de pilha

def b(z):  # z=81
    prod = a(z, z)
    print(z, prod)  # z=81, prod=90
    return prod


def a(x, y):  # x=9, y=9
    x = x + 1  # x=10, y=9
    return x * y  # 90


def c(x, y, z):
    total = x + y + z  # total = 9
    square = b(total) ** 2
    return square


x = 1
y = x + 1
print(c(x, y + 3, x + y))  # x=1, y=5 e z=3

# desenhando diagrama completo

# x = 1 e y = 2; Na chamada de fC, c = 1, y = 5 e z = 3, fC soma toma e eleve ao quadrado e chama a fB; fB passa o valor duas vezes a fA;
# fA soma mais um para o primeiro termo, neste caso, (x). Retorna a multiplicação dos valores com o X sendo diferente em 1 do Y; Retorna a fB que
# printa o valor ela mesma recebeu o novo valor que veio de fA. Retorna apenas o que veio de fA; volta a fC que retorna este valor, sendo (PROD)
