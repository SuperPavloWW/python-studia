# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 17:16:27 2020

@author: super
"""
from PIL import Image
import os

#img_path = "C:\\Users\\super\\Desktop\\Engine"
img_path = os.path.dirname(os.path.abspath(__file__))

fileExt = '.png'

for file in os.listdir(img_path):
    filename, ext = os.path.splitext(file)
    if (ext == '.jpg'):
        im = Image.open(os.path.join(img_path, filename + ext))
        im = im.convert("RGB")
        im.save(os.path.join(img_path,filename + fileExt))
        

    

