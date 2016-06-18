import os
print os.getcwd()
print os.listdir("/")

for item in os.listdir("."):
	if os.path.isfile(item):
		print item + "is a file"
	elif os.path.isdir(item):
		print item + "is a directory"
	else:
		print "unknown!!!"
