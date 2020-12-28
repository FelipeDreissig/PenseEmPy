# -*- coding: utf-8 -*-
"""
Created on Sun May 17 20:35:52 2020

@author: dreis
"""


def nested_sum(k):
    j = 0
    for i in k:
        j += sum(i)
    return j


p = [[1, 2, 3], [2], [3, 4, 5]]
nested_sum(p)
