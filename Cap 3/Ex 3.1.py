# criando uma função e que a ultima letra da função esteja na coluna 70

def right_justify(x, y):
    tm = y - len(x)
    print(' ' * tm, x)


nome = str(input('O que você quer que apareça ajustado? '))
coluna = int(input('Em qual coluna gostaria que terminasse? '))

right_justify(nome, coluna)
