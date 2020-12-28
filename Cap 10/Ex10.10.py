# -*- coding: utf-8 -*-
"""
Created on Mon May 18 10:39:44 2020

@author: dreis
"""


def lista_ondenada():
    caminho = open(r'C:\Users\dreis\Desktop\Estudos\Projetos\words.txt', 'r')
    t = list()
    for palavra in caminho:
        t.append(palavra.strip())
    return list(t)


def quantil(g, p):
    if g < p[56904]:
        if g < p[28452]:
            for i in range(0, 28453):
                if g == p[i]:
                    return i
        else:
            for i in range(28453, 56905):
                if g == p[i]:
                    return i
    else:
        if g < p[85356]:
            for i in range(56904, 85357):
                if g == p[i]:
                    return i
        else:
            for i in range(85356, 113810):
                if g == p[i]:
                    return i


lista_final = lista_ondenada()
print(lista_final)
print(quantil('adduct', lista_final))
