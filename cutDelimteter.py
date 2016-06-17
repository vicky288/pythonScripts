iFile = open("dir.txt")
oFile = open("odir.txt","w")
for line in iFile:
 newString = line.split("/")[1]
 #print newString
 oFile.write(newString)
 oFile.write("\n")

