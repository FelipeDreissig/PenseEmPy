# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 00:57:21 2020

@author: dreis
"""

dicio = {}


def ackermann(m, n):
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)

    if (m, n) in dicio:
        return dicio[m, n]
    else:
        dicio[m, n] = ackermann(m-1, ackermann(m, n-1))
        return dicio[m, n]


ackermann(4, 4)
