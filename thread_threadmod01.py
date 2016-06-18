import thread
import time

def worker_thread(id):
	print "Thread Id now alive->%id"%id
	count = 1
	while True:
		print "Thread Id:%d has counter val %d"%(id,count)
		time.sleep(2)
		count +=1

for i in range(5):
	thread.start_new_thread(worker_thread, (i,))

print "Main thread going for an infinite loop"
while True:
	pass
