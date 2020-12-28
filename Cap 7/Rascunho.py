# rascunho


def print_n(s, n):  # forma recursiva, ela chama a ela mesma.
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)


def print_n2(s, n):  # forma iterativa, n é modificado para o laço.
    while n > 0:
        print(s)
        n -= 1
    return None


def eps():
    x = 1.0
    while x + 1 > 1:
        x = x/2
    x = x*2
    return x


a = 25
x = 6
while True:
    y = (x + (a/x)) / 2
    if abs(x - y) < eps():
        break
    x = y
