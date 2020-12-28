# -*- coding: utf-8 -*-
"""
Created on Sun May 17 20:56:43 2020

@author: dreis
"""


def midle(p):
    auxiliar = p[:]
    del auxiliar[1:len(p)-1]
    return print(auxiliar)


p = [1, 2, 3, 4, 5, 6]
midle(p)
