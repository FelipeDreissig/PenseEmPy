# -*- coding: utf-8 -*-
"""
Created on Tue May 19 01:44:14 2020

@author: dreis
"""


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return print(d)


def histogram_get(s):
    d = dict()
    for letra in s:
        d[letra] = d.get(letra, 0) + 1
    return print(d)


def fibonacci(n):
    global known
    known = {0: 0, 1: 1}
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res


print(fibonacci(40))
