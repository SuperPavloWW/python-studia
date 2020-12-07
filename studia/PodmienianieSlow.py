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

import re

with open('text2.txt', 'r', encoding="utf8") as file:
    data = file.read()
    
#words = data.split()
replacable = {"i" : "oraz",
              "oraz" : "i",
              "nigdy" : "prawie nigdy",
              "dlaczego" : "czemu",
              "literackiego" : "indyjskiego",
              "ten" : "Ów"}


words = re.split('(\W+)', data)

newwords = []

for word in words: 
    if word in replacable or word.lower() in replacable:
        #print(replacable[word])
        newwords.append(replacable[word.lower()])
        continue
    newwords.append(word)
    
result = ''.join(newwords)
print(result)
