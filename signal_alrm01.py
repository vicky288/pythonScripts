import signal
import sys
def sigHandler(signum, sigfrm):
	print "signal received"
	#do something like print the status of something u are doing whiout closing the whole process
	sys.exit(0)

signal.signal(signal.SIGALRM, sigHandler)
signal.alarm(10)

while True:
	pass
