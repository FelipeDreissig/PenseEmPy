
caminho = open(r'C:\Users\dreis\Desktop\Estudos\Projetos\words.txt', 'r')


def line20():
    for line in caminho:
        if len(line.strip()) > 20:
            print(line.strip())
