#  palíndromo


def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


def middle_2(word):
    return word[-2:0:-1]


# 6.1
#  print(middle())
# o retorno não será nada. Vazio. Já qe nao existe objetos de onde tentamos obter.


def is_palindrome(string):
    if len(string) == 0:
        return 0
    elif len(string) == 1:
        if first(string) == last(string):
            return 0
        else:
            return 0
    elif len(string) == 2:
        if first(string) == last(string):
            return 1
        else:
            return 0
    else:
        if first(string) == last(string) and middle(string) == middle_2(string):
            return 1
        else:
            return 0


def palindro_numbers():
    p = 0
    for i in range(0, 66):  # entre 56 e 65 anos
        string = str(i)
        p = p + is_palindrome(string.zfill(2))
    print(p)


palindro_numbers()
