

def has_no_e():
    caminho = open(r'C:\Users\dreis\Desktop\Estudos\Projetos\words.txt', 'r')
    for palavra in caminho:
        e = 0
        for letter in palavra:
            if letter == 'e':
                e += 1
            else:
                pass
        if e == 0:
            print(True)
        else:
            pass


def has_no_e_part_2():
    caminho = open(r'C:\Users\dreis\Desktop\Estudos\Projetos\words.txt', 'r')
    j, total = 0, 0
    for palavra in caminho:
        total += 1
        e = 0
        for letter in palavra:
            if letter == 'e':
                e += 1
            else:
                pass
        if e == 0:
            j += 1
            print(palavra)
        else:
            pass
    print(f'A porcentagem de palavras sem E é de {(j/total)*100:.2f}.')
