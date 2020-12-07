# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 18:28:22 2020

@author: super
"""
with open('text1.txt', 'r', encoding="utf8") as file:
    data = file.read()#.replace('\n', '')
    
words = data.split()
removable = ["i", "się", "oraz", "nigdy", "dlaczego"]

#for word in words:
#   if word in removables:
        
resultwords  = [word for word in words if word.lower() not in removable]

result = ' '.join(resultwords)

print(result)

# pisanie do nowego pliku
#text_file = open("newfile1.txt", "w+")
#n = text_file.write(result)
#text_file.close()