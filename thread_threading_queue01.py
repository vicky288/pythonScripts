import threading
import Queue
import time

class WorkerThread(threading.Thread):
	def __init__(self,queue):
		threading.Thread.__init__(self)
		self.queue =  queue

	def run(self):
		print "In worker Thread"
		while True:
			counter = self.queue.get()
			print "Ordered to sleep for %d seconds"%counter
			time.sleep(counter)
			print "Finshed sleeping %d seconds"%counter
			self.queue.task_done()

queue = Queue.Queue()

for i in range(10):
	print "Creating worker Thread:%d"%i
	worker = WorkerThread(queue)
	worker.setDaemon(True)
	worker.start()
	print "Worker Thread %d created"%i

for j in range(10):
	queue.put(j)

queue.join()

print "All tasks over!"

