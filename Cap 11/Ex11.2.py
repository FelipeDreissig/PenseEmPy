# -*- coding: utf-8 -*-
"""
Created on Thu May 21 01:20:20 2020

@author: dreis
"""


def histogram(s):  # original do livro
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


'''def invert_dict(d):  # original do livro
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse'''


def invertendo_dict(d):  # criada
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
    return inverse


print(invertendo_dict(histogram('felipinho')))
