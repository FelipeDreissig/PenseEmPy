# -*- coding: utf-8 -*-
"""
Created on Sun May 17 22:30:28 2020

@author: dreis
"""


def is_sorted(lala):
    aux = lala[:]
    aux.sort()
    for i in range(len(lala)):
        if aux[i] != lala[i]:
            return print(False)
        else:
            return print(True)


haha = [4, 2, 3, 4, 5, 6]
hehe = ['b', 'c', 'a']
hoho = ['b', 'c']
is_sorted(hoho)
