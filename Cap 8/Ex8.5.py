
def rotate_word(string2, n):  # Cifra de C�sar
    rota = list()
    string = string2.lower()
    for i in range(len(string)):
        nova = list(chr(ord(string[i]) + n))
        rota.append(nova)
    rota = str(rota)
    rota = (rota.replace(' ', '').replace('[', '').replace(']', '')
            .replace(',', '').replace("'", "").upper())
    return print(rota)


nome = input('Digite o nome a ser decodificado:').strip().lower()
n = int(input(f'Tamanho da codifica��o a ser realizada em {nome}:'))
rotate_word(nome, n)
