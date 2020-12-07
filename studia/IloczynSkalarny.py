# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 00:21:25 2020

@author: super
"""

a = [1, 2, 12, 4]
b = [2, 4, 2, 8]

res = []

for i in range (len(a)):
    res.append(a[i]*b[i])
    
print(res)