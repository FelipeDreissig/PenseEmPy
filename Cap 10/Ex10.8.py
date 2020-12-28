# -*- coding: utf-8 -*-
"""
Created on Mon May 18 00:00:53 2020

@author: dreis
"""
import random


def aniversarios(n):  # amostra de aniversários
    k = list()
    for i in range(n-1):
        p = random.randint(1, 365)
        k.append(p)
    return k


def iguais(p):  # aniversário iguais
    j = p[:]
    j.sort()
    for i in range(len(j)-1):
        if j[i] == j[i+1]:
            return True
    return False


def contador(num_students, n):  # contador para os aniversersarios iguais
    count = 0
    for i in range(n):
        t = aniversarios(num_students)
        if iguais(t):
            count += 1
    return count


print(f'{((contador(23, 1000)/1000)*100):.2f}%')
