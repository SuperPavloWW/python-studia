# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 23:56:50 2020

@author: super
"""

#from numpy import random
import random

tab=[]


#tab=random.randint(1000, size=(50))

for i in range (50):
    tab.append(random.randint(0,1000))
n = len(tab)

for a in range(n-1, 0 , -1):
    for b in range(a):
        if tab[b] < tab[b+1]:
            tab[b], tab[b+1] = tab[b+1], tab[b]
    

print(tab)