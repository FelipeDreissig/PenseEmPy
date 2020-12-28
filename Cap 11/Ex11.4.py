# -*- coding: utf-8 -*-
"""
Created on Thu May 21 01:42:37 2020

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


def invert_dict(d):  # original do livro
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


def duplicadas(p):
    for k in p:
        if k == 2:
            return True
    return False


print(duplicadas(invert_dict(histogram('felip'))))
