#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 16:08:53 2018
@author: Sofia Bariami

To call the script, first you have to make it executable (chmod u+x).
It should also be OUTSIDE OF THE TOP FOLDER that you are using for the simulation.
"""

import os

working_dir = "top/oplsaa.ff/"
#Create enclosed directory
os.chdir(working_dir)

s=input("Which is the sigma value? ")
e=input("Which is the epsilon value? ")
print ("***************************************")
print ("As you wish! s= " + str(s) +" and e= "+str(e) )
print("Good luck with the parameterisation! :) ")
print ("***************************************")
 
with open("ffnonbonded.itp", "r+") as f:
    
    lines = f.readlines()
    f.close()

with open("ffnonbonded.itp", "w") as f:
    for line in lines:
        first=' '.join(line.split()[:1])
        if first != 'mtl_Pd':
            f.write(line)
    f.close()

with open("ffnonbonded.itp", 'a') as file:
    file.write('\n')
    file.write("mtl_Pd     Pd    46   98.33600     0.000       A    "+ str(s) +"         "+ str(e))
 
