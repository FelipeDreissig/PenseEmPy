# exercício 5.3


def is_tringle(a, b, c):
    aux_a = b + c
    aux_b = c + a
    aux_c = a + b
    if (aux_a > a) or (aux_b > b) or (aux_c > c):
        print('Isso é um triângulo.')
    elif (aux_a == a) or (aux_b == b) or (aux_c == c):
        print('Isso é um triângulo degenerado.')
    else:
        print('Não é um triângulo.')


n1 = int(input('Digite a primeira reta:'))
n2 = int(input('Digite a segunda reta:'))
n3 = int(input('Digite a terceira reta:'))
is_tringle(a=n1, b=n2, c=n3)
