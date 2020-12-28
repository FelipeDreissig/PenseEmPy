# -*- coding: utf-8 -*-
"""
Created on Sun May 17 21:10:31 2020

@author: dreis
"""


def chop(p):
    del p[0]
    del p[-1]
    return print(p)


pipi = [1, 2, 3, 4, 5]
k = chop(pipi)
print(k)
