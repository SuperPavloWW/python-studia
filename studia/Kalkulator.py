# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 23:50:48 2020

@author: super
"""

import LiczbyZespolone

s = input()

#input: wyrazenie w postaci (real,imag)operator(real,imag)

lhs = LiczbyZespolone.Complex(0, 0)
rhs = LiczbyZespolone.Complex(0, 0)

if ')+(' in s:
    lhs, rhs = s.split("+")
    lhs = LiczbyZespolone.Complex.fromstring(lhs)
    rhs = LiczbyZespolone.Complex.fromstring(rhs)
    print(lhs+rhs)
elif ')-(' in s:
    lhs, rhs = s.split("-")
    lhs = LiczbyZespolone.Complex.fromstring(lhs)
    rhs = LiczbyZespolone.Complex.fromstring(rhs)
    print(lhs-rhs)
elif ')*(' in s:
    lhs, rhs = s.split("*")
    lhs = LiczbyZespolone.Complex.fromstring(lhs)
    rhs = LiczbyZespolone.Complex.fromstring(rhs)
    print(lhs*rhs)
elif ')/(' in s:
    lhs, rhs = s.split("/")
    lhs = LiczbyZespolone.Complex.fromstring(lhs)
    rhs = LiczbyZespolone.Complex.fromstring(rhs)
    print(lhs/rhs)
else:
    print('unknown expression')