#!/bin/python


########################################################################################################
# This file should be at the same path with the following scripts: 
# * parameterise.py
# * combine.py
# * solvate.py
# * amberequilibration.py
# * prepareFEP.py
# These scripts are available from https://github.com/michellab/BioSimSpace/tree/devel/nodes/playground
########################################################################################################


import os,sys
import subprocess
from shutil import copy
import parameterise
import combine
import amberequilibration
# import prepareFEP


prot1 = raw_input("Please provide the first protein pdb: ")
prot2 = raw_input("Now the second one: ")
prot3 = raw_input("And the third one: ")
lig1 = raw_input("Please provide the first ligand pdb: ")
lig2 = raw_input("Please provide the second ligand pdb: ")
# try:
# prot = sys.argv[1]
# lig1 = sys.argv[2]
# lig2 = sys.argv[3]
# except IndexError:
#     print "Please provide a protein pdb file"
#     sys.exit(-1)
#pr = input("Please provide a protein PDB file: %s"%sys.argv[1])

bash_mkdir1 = "mkdir protein.pdb"
mkdir1= subprocess.Popen(bash_mkdir1.split(), stdout= subprocess.PIPE)
output, error = mkdir1.communicate()


bash_mkdir2 = "mkdir ligands.pdb"
mkdir2= subprocess.Popen(bash_mkdir2.split(), stdout= subprocess.PIPE)
output, error = mkdir2.communicate()

copy(prot1, "protein.pdb")
copy(prot2, "protein.pdb")
copy(prot3, "protein.pdb")
copy(lig1, "ligands.pdb")
copy(lig2, "ligands.pdb")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Protein and ligands are now at protein.pdb and ligands.pdb folders respectively.")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")




