# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 22:05:58 2020

@author: dreis
"""


def most_frequent(a):
    a = a.strip().lower()
    t = list()
    aux = list()
    pala = list(a)
    for i in range(len(pala)):
        c = 0
        for j in range(len(pala)):
            if pala[i] == pala[j]:
                c += 1
        aux.append(c)
    p = dict(zip(a, aux))
    for key, value in sorted(p.items()):
        t += (key, value)
    return t


print(most_frequent('Adriano'))
