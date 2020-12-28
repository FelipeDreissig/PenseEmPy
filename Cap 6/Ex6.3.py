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

# print(middle(''))
# o retorno não será nada. Vazio. Já qe nao existe objetos de onde tentamos obter.

def is_palindrome(string):
    if len(string) == 0:
        return None
    elif len(string) == 1:
        if first(string) == last(string):
            return True
        else:
            return False
    elif len(string) == 2:
        if first(string) == last(string):
            return True
        else:
            return False
    else:
        if first(string) == last(string) and middle(string) == middle_2(string):
            return True
        else:
            return False


print(is_palindrome('cachicac'.strip().lower()))
