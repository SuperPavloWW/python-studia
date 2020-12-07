# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 18:28:22 2020

@author: super
"""
with open('text1.txt', 'r', encoding="utf8") as file:
    data = file.read()#.replace('\n', '')
    
#words = data.split()
removable = ["i", "się", "oraz", "nigdy", "dlaczego"]

specials = ['.', ',', '?', '!']

for word in removable:
    data = data.replace(' ' + word + ' ', ' ')
    for spec in specials:
            data = data.replace(' ' + word + spec, ' ')
            data = data.replace(spec + word + ' ', '')

print(data)
# pisanie do nowego pliku
#text_file = open("newfile1.txt", "w+")
#n = text_file.write(result)
#text_file.close()
