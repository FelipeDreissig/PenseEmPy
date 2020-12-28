# exercício 7.1
import math


def eps():
    x = 1.0
    while x + 1 > 1:
        x = x/2
    x = x*2
    return x


def my_sqrt(a):
    x = 1
    while True:
        y = (x + (a/x)) / 2
        if abs(x - y) < eps():
            break
        x = y
    return y


print('a      -      My Sqrt      -      Math.Sqrt     -      Diff  ')
print('--------------------------------------------------------------------------------')
for i in range(1, 101):
    print(f'{i:<6} -     {my_sqrt(i):<6.5f}       -      {math.sqrt(i):<6.5f}       -      {abs(my_sqrt(i)-math.sqrt(i)):<50}')
