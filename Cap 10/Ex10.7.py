# -*- coding: utf-8 -*-
"""
Created on Sun May 17 23:09:55 2020

@author: dreis
"""


def has_duplicate(k):
    for i in range(len(k)):
        c = 0
        for j in range(len(k)):
            if k[i] == k[j]:
                c += 1
        if c >= 2:
            return print(True)
    return print(False)


nome = list('fldrianor')
has_duplicate(nome)
