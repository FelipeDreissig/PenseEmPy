import turtle
import math

bob2 = turtle.Turtle()

#Escreva uma função chamada square que receba um parâmetro chamado t, que é um turtle. Ela deve usar o turtle para desenhar um quadrado.

def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

#square(bob2)

#Acrescente outro parâmetro, chamado length, ao square. Altere o corpo para que o
#comprimento dos lados seja length e então altere a chamada da função para fornecer
#um segundo argumento. Execute o programa novamente. Teste o seu programa com
#uma variedade de valores para length.

def square2(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

#square2(bob2, 300)

#3. Faça uma cópia do square e mude o nome para polygon. Acrescente outro parâmetro
#chamado n e altere o corpo para que desenhe um polígono regular de n lados.

def polygon(t, length, n):
    angulo = 360/n
    for i in range(n):
        t.fd(length)
        t.rt(angulo)


#polygon(bob2, 100, 6)

#4. Escreva uma função chamada circle que use o turtle, t e um raio r como parâmetros e
#desenhe um círculo aproximado ao chamar polygon com um comprimento e número
#de lados adequados. Teste a sua função com uma série de valores de r.

def circle(t, r):
    circunferencia = 2*math.pi*r
    n = 50
    length = circunferencia / n
    polygon(t, length, n)


#circle(bob2, 200)

# 5 Faça uma versão mais geral do circle chamada arc, que receba um parâmetro
# adicional de angle, para determinar qual fração do círculo deve ser desenhada. angle
# está em unidades de graus, então quando angle=360, o arc deve desenhar um círculo
# completo.

def arc(ang, comprimento, tamanho):
    t = turtle.Turtle()
    n = ra = 360/ang
    k = 360/ang
    while n <= tamanho:
        n = n + ra
        t.fd(comprimento)
        t.rt(k)


arc(10, 100, 90)