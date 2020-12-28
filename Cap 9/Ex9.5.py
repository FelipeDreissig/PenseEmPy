
def avoid(palavra, restrito):
    c = 0
    for letra in palavra:
        for caracter in restrito:
            if letra.strip() == caracter:
                c += 1
            else:
                pass
    return c


def uses_oly(pal, res):
    k = avoid(palavra=pal, restrito=res)
    if k == len(pal):
        return True
    else:
        return False


def uses_all(pal, res):
    return uses_all(res, pal)


print(uses_oly('adriano', 'adrino'))
