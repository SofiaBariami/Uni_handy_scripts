
bash_mkdir1 = "mkdir protein"
mkdir1= subprocess.Popen(bash_mkdir1.split(), stdout= subprocess.PIPE)
output, error = mkdir1.communicate()


bash_mkdir2 = "mkdir protein/SIM"
mkdir2= subprocess.Popen(bash_mkdir2.split(), stdout= subprocess.PIPE)
output, error = mkdir2.communicate()

copyfile(prot, "protein/SIM/protein.pdb") 
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("* Protein file is now at protein/SIM folder.")

bash_mkdir3 = "mkdir poses"
mkdir3= subprocess.Popen(bash_mkdir3.split(), stdout= subprocess.PIPE)
output, error = mkdir3.communicate()

print("* Creating folders for the poses")
for i in range (0, int(num_of_poses)):
	bash_mkdir4 = "mkdir poses/pose%s"%i
	mkdir4= subprocess.Popen(bash_mkdir4.split(), stdout= subprocess.PIPE)
	output, error = mkdir4.communicate()


