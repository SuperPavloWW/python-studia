# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 19:36:23 2020

@author: super
"""

import math
import sys

numbers = list(map(float, input('wpisz liczby: ').split()))

a = numbers[0]
b = numbers[1]
c = numbers[2]

print(str(a) + 'x^2 + ' + str(b) + 'x + ' + str(c))

delta = b*b - 4*a*c
if a < 0:
    print("nie jest rownanie kwadratowe")
    sys.exit()

if delta < 0:
    print("none")
elif delta == 0:
    print(str(b*(-1)/(2*a)))
else:
    print("x1 = " + str((b*(-1) - math.sqrt(delta))/(2*a)))
    print("x1 = " + str((b*(-1) + math.sqrt(delta))/(2*a)))

#pierw = math.sqrt(delta)
