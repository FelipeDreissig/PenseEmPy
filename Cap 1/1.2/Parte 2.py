#1. Quantos segundos há em 42 minutos e 42 segundos?
seg = 42*60+42
print(f'Há {seg} segundos em 42 min e 42 segundos.') #2562 segundos

#2. Quantas milhas há em 10 quilômetros? Dica: uma milha equivale a 1,61 quilômetro.
milha = 10*1.61
print(f'Há {milha} milhas em 10Km.') #6.2111 milhas

#3. Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual é o seu passo
#médio (tempo por milha em minutos e segundos)? Qual é a sua velocidade média em
#milhas por hora?

Passo_medio_em_segundos = milha/seg
minutos = 42 + 0.42/60
print(f'O passo médio em Milhas por segundo é de {Passo_medio_em_segundos:.3f}')
passo_medio_em_minutos = milha/minutos
print(f'O passo médio em milhas por minuto é de {passo_medio_em_minutos:.3f}')

horas = (42+42/60)/60
milhas_por_hora = milha/horas
print(f'A velocidade média em milhas por hora é de {milhas_por_hora:.3f}.')

