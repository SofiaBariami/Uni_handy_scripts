#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 20:55:01 2017

@author: Sofia Bariami

This script takes as an input a txt file with the amber parameters as described 
at the work of Cornell et al. and converts them to GROMACS compatible ones. The 
two parameters, R* and ε(kcal/mol), must be seperated with "space". 

To call the script write in a terminal: 
    chmod u+x parameter_conv.py
    ./parameter_conv < input_file_name
If you want to print the new parameters to a new file, then: 
    ./parameter_conv < input_file_name > output_file_name
"""

import numpy as np
import sys

x, y = list(), list() 
    
for line in sys.stdin: #reads file from the terminal
    
    line = line.strip() #takes away all kinds of spaces at the end of the line
    cols = line.split() #"space" is the split between the arguments at each line
    
    if len(cols) == 2:
        x.append(float(cols[0]))
        y.append(float(cols[1]))
    else: 
#If there is an error at the input file, it prints the line with the unrecognised format
        print ("Wrong format in line {}".format(len(x)+1))



def par_conv(R, eps):
    R_nm = R / 10
    R_min = 2 * R_nm
    sigma = R_min * 2 ** (-1 / 6)
    epsilon = eps * 4.184
    
    return sigma, epsilon


#Converts the lists to arrays
R = np.array(x)
eps = np.array(y)

sigma, epsilon = par_conv(R, eps)
print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print ('Hooray! Ready-made parameters!')
print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
for s_i, e_i in zip(sigma, epsilon): #parallel calculations of the array 
    print("σ = {0:.6f}nm \t ε = {1:.6f} kJ/mol".format(s_i, e_i)) #6 decimals 