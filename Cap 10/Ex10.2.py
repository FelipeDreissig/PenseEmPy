# -*- coding: utf-8 -*-
"""
Created on Sun May 17 20:45:43 2020

@author: dreis
"""


def cansum(p):
    t = 0
    k = 0
    aux = 0
    for i in range(len(p)):
        if type(p[i]) != int:
            for j in range(len(p[i])):
                t += int(p[i][j])
        else:
            k += int(p[i])
    aux = k + t
    return print(aux)


lala = [10, 30, 10, [0, 40, 10]]
cansum(lala)
