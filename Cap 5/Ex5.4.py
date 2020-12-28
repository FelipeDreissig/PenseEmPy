

def recurse(n, s):
    """
    Funções recursiva exemplo.
    :param n:tamanho da recursividade.
    :param s:mostra o tamanho da recursividade ao final
    :return:valores pro recursividade,
    """
    if n == 0:
        print(n, s)
    else:
        print(n, s)
        recurse(n-1, n+s)


recurse(n=3, s=0)

"""1. O que aconteceria se você chamasse esta função desta forma: recurse(-1, 0)?"""
# seria uma recursividade infinita.

"""2. Escreva uma docstring que explique tudo o que alguém precisaria saber para usar esta
função (e mais nada)."""
