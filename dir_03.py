import os
import glob

for item in glob.glob(os.path.join(".","*.txt")):
	print item
