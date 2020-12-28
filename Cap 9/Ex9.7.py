# exercício 9.7


def repeat():
    caminho = open(r'C:\Users\dreis\Desktop\Estudos\Projetos\words.txt', 'r')
    for palavras in caminho:
        if len(palavras) > 6:
            for i in range(0, len(palavras) - 6):
                if palavras[i] == palavras[i + 1]:
                    if palavras[i + 2] == palavras[i + 3]:
                        if palavras[i + 4] == palavras[i + 5]:
                            print(palavras)


repeat()
