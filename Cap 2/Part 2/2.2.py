#1. O volume de uma esfera com raio r é . Qual é o volume de uma esfera com raio 5?
import math
r = 5
volume = (4/3)*math.pi*(pow(r, 3))
print(f'O volume da espera com raio igual a {r} é de {volume} x cúbico.')

#Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um
#desconto de 40%. O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos
#para cada exemplar adicional. Qual é o custo total de atacado para 60 cópias?
q = 60
custo = (24.95*0.6)*q+(3 + 0.75*(q-1))
print(f'O custo para 60 cópias é de {custo} reais.')

#3. Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo (8min15s por
#quilômetro), então 3 quilômetros a um passo mais rápido (7min12s por quilômetro) e
#1 quilômetro no mesmo passo usado em primeiro lugar, que horas chego em casa
#para o café da manhã?

tempo = ((8*60+15)*2+3*(7*60+12))
temptotal = 6*60*60+52*60
tempoacumulado = tempo + temptotal
hora = tempoacumulado/(3600)
resto = (tempoacumulado/3600-int(hora))
minuto = resto*60
segundo = round((minuto - int(minuto))*60, 2)
print(f'Chegará as {int(hora)} horas e {int(minuto)} minutos e {int(segundo)} segundos.')
