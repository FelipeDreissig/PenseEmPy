# -*- coding: utf-8 -*-
"""
Created on Mon May 18 13:13:32 2020

@author: dreis
"""


def lista_ondenada():
    caminho = open(r'C:\Users\dreis\Desktop\Estudos\Projetos\words.txt', 'r')
    t = list()
    for palavra in caminho:
        t.append(palavra.strip())
    return list(t)


def inverso(p):
    invertidas = list()
    for i in range(0, len(p)):
        auxiliar = ('')
        auxiliar = str(p[i])
        auxiliar = auxiliar[::-1]
        invertidas.append(auxiliar)
    return list(invertidas)


def iguais(lista, inverso):
    auxiliar = list()
    t = 0
    for letra in range(0, len(inverso)):
        for letrinha in range(0, len(inverso)):
            if len(lista[letra]) == len(inverso[letrinha]):
                c = 0
                for i in range(0, len(lista[letra])):
                    if lista[letra][i] == inverso[letra][-i-1]:
                        c += 1
                if c == len(lista[letrinha]):
                    t += 1
                    auxiliar.append(str(lista[letra]))
    return (auxiliar, t)


emordem = lista_ondenada()
viradas = inverso(emordem)
iguais(emordem, viradas)
