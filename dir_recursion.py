import os
print os.listdir("/")
print "#######################"
#ctr = 1
#fd="."
def traverse_dir(fd,ctr):
	for item in os.listdir(fd):
		if os.path.isfile(item):
			for val in range(ctr):
				print "-",
			print item
		elif os.path.isdir(item):
			for val in range(ctr):
				print "-",
			print item
			ctr = ctr+1
			traverse_dir(item,ctr)
	

print os.getcwd()
traverse_dir(".",0)	
