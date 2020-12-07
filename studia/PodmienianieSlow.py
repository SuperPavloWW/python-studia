# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 19:18:50 2020

@author: super
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 18:28:22 2020

@author: super
"""
with open('text2.txt', 'r', encoding="utf8") as file:
    data = file.read()
    
words = data.split()
replacable = {"i" : "oraz",
              "oraz" : "i",
              "nigdy" : "prawie nigdy",
              "dlaczego" : "czemu"}

newwords = []

for word in words: 
    if word in replacable:
        #print(replacable[word])
        newwords.append(replacable[word])
        continue
    newwords.append(word)

result = ' '.join(newwords)
print(result)

#pisanie do nowego pliku
#text_file = open("newfile2.txt", "w+")
#n = text_file.write(result)
#text_file.close()