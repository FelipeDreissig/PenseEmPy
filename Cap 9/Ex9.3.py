# exercício 9.3


def avoid(palavra, restrito):
    c = 0
    for letra in palavra:
        for caracter in restrito:
            if letra.strip() == caracter:
                c += 1
                print(letra)
            else:
                pass
    print(f'O número de letras que estão na restrição é de {c}.')


avoid('felipe', 'aiouf')
