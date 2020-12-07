# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 01:02:37 2020

@author: super
"""

import random

tab1 = []
tab2 = []

for i in range (8):
    new1 = []
    new2 = []
    for j in range (8):
        new1.append(random.randint(0, 10))
        new2.append(random.randint(0, 10))
    tab1.append(new1)
    tab2.append(new2)

res = []

for i in range (8):
    newx = []
    for j in range (8):
        x = 0
        for k in range (8):
            x += tab1[i][k] * tab2[k][j]
        newx.append(x)
    res.append(newx)

print(res)