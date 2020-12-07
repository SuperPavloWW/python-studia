# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 03:00:39 2020

@author: super
"""

import glob

root_dir = "C:\\Users\\super\\PycharmProjects\\pythonProject"
for filename in glob.iglob(root_dir + '**/**', recursive=True):
     print(filename)