#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 15:01:39 2018

This script creates a submission file for Gaussian16 in Eddie

"""

import sys
import pandas as pd

input_path = sys.argv[1]
print(input_path)
output_path = sys.argv[2]



new_file = open(output_path, "w")

with open (input_path) as file:
    new_file.write("#!/bin/sh\n")
    new_file.write("# Grid Engine options (lines prefixed with #$)\n")
    new_file.write("#$ -N gaussian\n")
    new_file.write("#$ -cwd\n")
    new_file.write("#$ -l h_rt=24:00:00\n")
    new_file.write("#$ -l h_vmem=3G\n")
    new_file.write("#$ -pe sharedmem 4\n")
    new_file.write("\n")
    new_file.write(("input={0}\n").format(sys.argv[1]))
    new_file.write("\n")
    new_file.write("# Initialise the environment modules\n")
    new_file.write(". /etc/profile.d/modules.sh\n")
    new_file.write("\n")
    new_file.write("# Export environment variables\n")
    new_file.write("export g16root=/exports/applications/apps/community/chem\n")
    new_file.write("export GAUSS_SCRDIR=$TMPDIR\n")
    new_file.write("source $g16root/g16/bsd/g16.profile\n")
    new_file.write("\n")
    new_file.write("# Run the program\n")
    new_file.write("/exports/applications/apps/community/chem/g16/g16 $input\n")
    new_file.write("\n")  

new_file.close()

