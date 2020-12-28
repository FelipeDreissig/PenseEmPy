# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 01:03:33 2020

@author: dreis
"""


def rotate_word(string2, n):  # Cifra de César
    rota = list()
    string = string2.lower()
    for i in range(len(string)):
        nova = list(chr(ord(string[i]) + n))
        rota.append(nova)
    rota = str(rota)
    rota = (rota.replace(' ', '').replace('[', '').replace(']', '')
            .replace(',', '').replace("'", ""))
    return rota


def desrotate_word(string, n):
    rota = list()
    string_aux = string.lower()
    for i in range(len(string_aux)):
        nova = list(chr(ord(string_aux[i]) + n*(-1)))
        rota.append(nova)
    rota = str(rota)
    rota = (rota.replace(' ', '').replace('[', '').replace(']', '')
            .replace(',', '').replace("'", ""))
    return rota


cifra = input('Digite a palavra com cifra de césar realizada:').strip().lower()
nome = input('Digite a palavra com cifra de césar não realizada:').strip().lower()
n = int(input('Tamanho da codificação e da decoficação:'))
c = rotate_word(nome, n)
n = desrotate_word(cifra, n)


if str(c) == cifra:
    print('Era uma codificação.')
else:
    print('Não era uma codificcação.')
