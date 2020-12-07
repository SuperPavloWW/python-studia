# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 14:54:58 2020

@author: super
"""
import random


def wyznacznik(A):
    n = len(A)
    AX = A.copy()

    for row in range(n):
        for i in range(row+1,n):
            if AX[row][row] == 0:
                #AX[row][row] == 1.0e-18
                for p in range (row+1, n):
                    if (AX[p][row]) != 0:
                        AX[row], AX[p] = AX[p], AX[row]#*(-1)
                        for hk in range (n):
                            AX[p][hk] *= (-1)
                        i -=1
                        break
                    else:
                        return 0
                continue     
            w = AX[i][row] / AX[row][row] 
            for j in range(n): 
                AX[i][j] = AX[i][j] - w * AX[row][j]
     
    res = 1.0
    for i in range(n):
        res *= AX[i][i] 
    print("po uproszczeniu metoda Gaussa")
    print(AX)
    return res

tab1 = []

for i in range (4):
    new1 = []
    for j in range (4):
        new1.append(random.randint(0, 5))
    tab1.append(new1)
    
print (tab1)
print ("wyznacznik = " + str(wyznacznik(tab1)))