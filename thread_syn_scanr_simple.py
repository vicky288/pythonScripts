import Queue
import threading
from scapy.all import *
import time
class Worker(threading.Thread):
	def __init__(self,tid,queue):
		threading.Thread.__init__(self)
		self.queue = queue
		self.tid = tid
		print "Worker started...%d"%self.tid

	def run(self):
		total_ports = 0
		while True:
			port = 0
			try:
				port = self.queue.get()
			except Queue.Empty:
				print "Exiting %d scanned port%d"%(self.tid,total_ports)
				return
			ip=sys.argv[1]
			response = sr1(IP(dst=ip)/TCP(dport=port, flags="S"), verbose=False, timeout=.2)
			if response:
				if response[TCP].flags == 18:
					print "Thread %d open port %d"%(self.tid,port)
			self.queue.task_done()
			total_ports += 1


#response = sr1(IP(dst=ip)/TCP(dport=port, flags="S"), verbose=False, timeout=.2)
queue = Queue.Queue()

for i in range(10):
	worker = Worker(i,queue)
	worker.setDaemon(True)
	worker.start()

for j in range(1000):
	queue.put(j)

queue.join()

print "Scanning complte"

