
import pandas as pd
import sys

# def find_restrained_atoms(pdbfile):
#pdbfile = prot.pdb
l1 = list(range(2,34))
l2= list(range(36, 307))
l3 =list(range(309, 351))
l4 =list(range(353, 376))
l = l1+l2 +l3+ l4
new_file = open("restrained_atoms.txt", "w")
with open ("prot.pdb") as file:
	for i in range(0, (len(l)+1)):
		lines = file.readlines()
		for line in lines:
			cols = line.split()
			if cols[0] == "ATOM" and cols[2] == "CA":
				if cols[5] == str(l[i]):
					print("ulululu")
					print(cols[5])
					print(cols[2])
					new_file.write("{0}".format(cols[1]))
					new_file.write("\n")
				#d = cols[1]
				#new_file.write("{0}\t{1}\n".format(d, cols[3]))
	new_file.close()
