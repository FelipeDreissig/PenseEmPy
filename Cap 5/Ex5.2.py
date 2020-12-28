# resolução da 5.1 e do 5.2
import math
import random


def check_farmat(a, b, c, n):
    if n > 2:
        if math.pow(a, n) + math.pow(b, n) == math.pow(c, n):
            return print('Holy smokes, Fermat was wrong')
        else:
            return print('No, that doesn’t work')
    else:
        return print('Exporente precisa ser maior que 2.')


check_farmat(a = random.randint(0, 100),
             b = random.randint(0, 100),
             c = random.randint(0, 100),
             n = 3)

A = int(input('Digite um valor para a:'))
B = int(input('Digite um valor para b:'))
C = int(input('Digite um valor para c:'))
N = int(input('Digite um valor para n (sendo maior que 2):'))
check_farmat(a=A, b=B, c=C, n=N)
