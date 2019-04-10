# Finds the CA atoms that need to be restrained in a list of given residues

l1 = list(range(2,34))
l2 = list(range(36, 307))
l3 = list(range(309, 351))
l4 = list(range(353, 376))
l = l1 + l2 + l3 + l4
new_file = open("restrained_atoms.txt", "w")
with open ("5ter.pdb") as file:
        lines = file.readlines()
        for line in lines:
                cols = line.split()
                for i in range(0, (len(l))):
                        if cols[0] == "ATOM" and cols[2] == "CA" and cols[4] == str(l[i]):
                                new_file.write("{0}".format(cols[1]))
                                new_file.write("\n")
        new_file.close()
	
