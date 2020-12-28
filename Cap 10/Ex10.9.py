# -*- coding: utf-8 -*-
"""
Created on Mon May 18 01:59:23 2020

@author: dreis
"""

import datetime
import time


def met_append():
    caminho = open(r'C:\Users\dreis\Desktop\Estudos\Projetos\words.txt', 'r')
    t = list()
    for palavra in caminho:
        t.append(palavra.strip())
    return t


def met_mais():
    caminho = open(r'C:\Users\dreis\Desktop\Estudos\Projetos\words.txt', 'r')
    t = list()
    for palavra in caminho:
        word = palavra.strip()
        t = t + [word]
    return t


startappend = time.time()
print('Método append.')
apen = met_append()
print(len(apen))
print(apen[:10])
finalappend = (time.time() - startappend)
print(f'{finalappend}')
print('===============================')
startsoma = time.time()
print('Método concatena.')
som = met_mais()
print(len(som))
print(som[:10])
finalsoma = (time.time() - startsoma)
tempo = finalsoma - finalappend
minutos = datetime.timedelta(seconds=tempo)
print(f'{finalsoma}')
print('===============================')
print(f'A Diferença é de {minutos}')
