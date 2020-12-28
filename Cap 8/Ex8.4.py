

def any_lowercase1(s):  # Esta função retorna um booleano diferente para cada letra
    for c in s:        # Não é eficiente para verificar se a palavra está em minúsculo
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):  # aqui verifica-se apenas a letra 'c' mesmo. Não importa qual letra haja na string. Verificará 'c'.
    for c in s:         # O retorno é uma string, não um booleano. E é verificada cada letra, alterando o retorno.
        if 'c'.islower():  # não é eficiente para verificar se a palara está em minúsculo.
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):  # um booleano está armazenado na 'flag'
    for c in s:
        flag = c.islower()  # o retorno não será a letra minúscula.
    return flag


def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


def any_lowercase5(s):
    for c in s:
        if not c.islower():  # esta inverte a operação com o 'not' e verifica apenas a letra.
            return False
    return True
