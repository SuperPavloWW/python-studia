# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 16:07:16 2020

@author: super
"""

import xml.dom.minidom as md

file = md.parse( "image3.xml" )
names = file.getElementsByTagName( "name" )

for name in names:
    if name.firstChild.nodeValue == "person":
        name.firstChild.nodeValue = "ZMIENIONE"
    

with open( "test2.xml", "w" ) as fs:  
    fs.write( file.toxml() ) 
    fs.close()  