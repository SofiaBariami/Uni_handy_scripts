#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 23:06:14 2017

@author: Sofia Bariami
"""

import numpy as np
import sys

x, y= [], [] 
for line in sys.stdin: #reads file from the terminal
#Ignore lines that start with "@" <-- typical GROMACS .xvg output format
    if line[0]== "@":
        continue
    cols=line.split()
    
    if len(cols) == 2:
        x.append(float(cols[0]))
        y.append(float(cols[1]))
print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print ("If your experiment needs a statistician, you need a better experiment.")
print ("                                                   ― Ernest Rutherford")
print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print ("* The mean value is: {0:.4f} ± {1:.4f}".format(np.mean(y), np.std(y)))
print ("* The minimum value is: {0}".format(np.min(y)))
print ("* The maximum value is: {0}".format(np.max(y)))
