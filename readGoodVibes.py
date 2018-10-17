#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 10:33:00 2018

@author: s1786388
"""
file = open("Goodvibes_output.dat", "r")
filetext = file.read()
filelines = filetext.split('\n')
with open('data.csv', 'w') as output:
    for line in filelines:
        if len(line) > 0 and line[0] == "o":
            cols = line.split()
            print (*(cols[1:]),sep=',', file=output)      
