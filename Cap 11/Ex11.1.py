# -*- coding: utf-8 -*-
"""
Created on Thu May 21 01:02:19 2020

@author: dreis
"""


def passando_dicionario(k):
    global d
    d = dict()
    caminho = open(r'C:\Users\dreis\Desktop\Estudos\Projetos\words.txt', 'r')
    for i in caminho:
        d[i[:-2]] = None
    for p in d:
        if p == k:
            return print(True)
    return print(False)


passando_dicionario('adduct')
