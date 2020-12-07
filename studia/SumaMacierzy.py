# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 00:33:23 2020

@author: super
"""
#from numpy import random
import random


#a=random.randint(1000, size=(128))

tab1 = []
tab2 = []

for i in range (128):
    new1 = []
    new2 = []
    for j in range (128):
        new1.append(random.randint(0, 10))
        new2.append(random.randint(0, 10))
    tab1.append(new1)
    tab2.append(new2)

print (tab1)
print (tab2)

res = []
for i in range (128):
    newres = []
    for j in range(128):
        newres.append(tab1[i][j]+tab2[i][j])
    res.append(newres)
print(res)
