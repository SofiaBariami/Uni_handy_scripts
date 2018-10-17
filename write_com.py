#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 15:01:39 2018

This script gets a .pdb file and writes the corresponding input for gaussian 
calculations. The fist argument is the input and the second is the output. 
*Sofia*
"""

import sys
import pandas as pd

input_path = sys.argv[1]
print(input_path)
output_path = sys.argv[2]



new_file = open(output_path, "w")

with open (input_path) as file:
    new_file.write(("%chk={0}.chk\n").format(sys.argv[1].split('.')[0]))
    new_file.write("%mem=3Gb\n")
    new_file.write("%nprocshared=4\n")
    new_file.write("# opt freq wb97xd/6-31G(d,p)\n")
    new_file.write("\n")
    new_file.write("Geometry optimisation with wb97xd/6-31G(d,p)\n")
    new_file.write("\n")
    new_file.write("0 1\n")
    lines = file.readlines()
    for line in lines:
        cols = line.split()
        if cols[0]== "ATOM":
            d=[cols[2]]
            new_file.write("{0}\t{1}\t{2}\t{3}\n".format( d[0][0], cols[5], cols[6], cols[7]))
    new_file.write("\n")
    new_file.write("\n")  
    new_file.write("--link1--\n")
    new_file.write("%mem=3Gb\n")
    new_file.write(("%chk={0}.chk\n").format(sys.argv[1].split('.')[0]))
    new_file.write("%nprocshared=4\n")
    new_file.write("# geom=check guess=read wb97xd/6-311G(d,p) scrf=(solvent=toluene)\n")
    new_file.write("\n")
    new_file.write("Single point calculation\n")
    new_file.write("\n")
    new_file.write("0 1\n")
    new_file.write("\n")  

new_file.close()

