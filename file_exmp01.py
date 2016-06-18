fdes = open("/var/log/messages")
for line in fdes:
	if "USB" in line:
		print line.strip()
