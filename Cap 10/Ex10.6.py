# -*- coding: utf-8 -*-
"""
Created on Sun May 17 22:44:15 2020

@author: dreis
"""


def is_anagram(popo, papa):
    popo1 = list(popo.strip())
    popo1.sort()
    papa1 = list(papa.strip())
    papa1.sort()
    if (popo1) == (papa1):
        return print(True)
    else:
        return print(False)


sim_1 = 'roma'
sim_2 = 'amor'
nao_1 = 'nela'
nao_2 = 'pela'


is_anagram(sim_1, sim_2)
