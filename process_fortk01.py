import os

def child_process():
	print "I'm the child process, pid:%d"%os.getpid()
	print "The child Exit"

def parent_process():
	print "I'm the parebt process, pid:%d"%os.getpid()
	childpID = os.fork()
	if childpID == 0:
		child_process()
	else:
		print "This is parent process"
		print "Our child pid is %d"%childpID
	while True:
		pass

parent_process()
