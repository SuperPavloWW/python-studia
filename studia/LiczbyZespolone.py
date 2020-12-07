# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 01:58:15 2020

@author: super
"""
import math

class Complex(object):
    def __init__(self, real, im=0.0):
        self.real = real
        self.im = im
        
    @classmethod
    def fromstring(cls, string):
        lhs, rhs = string.split(',')
        lhs = float(lhs[1:])
        rhs = float(rhs[:1])
        return cls(lhs, rhs)

    def __add__(self, other):
        return Complex(self.real + other.real,
                       self.im + other.im)

    def __sub__(self, other):
        return Complex(self.real - other.real,
                       self.im - other.im)

    def __mul__(self, other):
        return Complex(self.real*other.real - self.im*other.im,
                       self.im*other.real + self.real*other.im)

    def __truediv__(self, other):
        mianownik = float(other.real**2 + other.im**2)
        return Complex((self.real*other.real+self.im*other.im)/mianownik,
                       (self.im*other.real-self.real*other.im)/mianownik)

    def __abs__(self):
        return math.sqrt(self.real**2 + self.im**2)
    
    def __str__(self):
        return '%g + %gj' % (self.real, self.im)

    def __eq__(self, other):
        return self.real == other.real and self.im == other.im
    
     
a = Complex(5, -4)
b = Complex(2, 7)

addition = a+b
subtraction = a-b
multiplexing = a*b
division = a/b
print(addition)
print(subtraction)
print(multiplexing)
print(division)
