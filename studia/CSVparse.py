# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 16:22:35 2020

@author: super
"""

import csv
import sys

while True:
    lines = list()
    with open('names.csv', 'r', newline='') as csvfile:
        fieldnames = ['Zadanie', 'Opis', 'Data']
        
        print("SO FAR: ")
        reader = csv.DictReader(csvfile)
        for row in reader:
            vals= list()
            print(row['Zadanie'], row['Opis'], row['Data'])
            vals.append(row['Zadanie'])
            vals.append(row['Opis'])
            vals.append(row['Data'])
            lines.append(vals)
            
    print ('do you want to delete a record? y/n')
    s = input()
    if s == 'y':
        nn = input()
        for field in lines:
            if nn in field:
                lines.remove(field)
        with open('names.csv', 'w', newline='') as out:
            writer = csv.DictWriter(out, fieldnames=fieldnames)
            writer.writeheader()
            for row in lines:
                if row[0] != nn:
                    writer.writerow({'Zadanie' : row[0], 'Opis' : row[1], 'Data' : row[2]})
        print("Record deleted")
    else:
        print ('do you want to write a new record y/n')
        ss = input()
        if ss == 'y':
            with open('names.csv', 'w', newline='') as out:
                writer = csv.DictWriter(out, fieldnames=fieldnames)        
                a, b, c = input().split() 
                writer.writeheader()
                for row in lines:
                    writer.writerow({'Zadanie' : row[0], 'Opis' : row[1], 'Data' : row[2]})
                writer.writerow({'Zadanie' : a, 'Opis' : b, 'Data' : c})
            print("Record added")
        else:
            #continue
            None
    print ("type >>y<< to continue, type >>n<< to exit")
    key = input()
    if key == 'y':
        None
    else:
        sys.exit()