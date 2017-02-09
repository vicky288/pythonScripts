import threading
import Queue
from ftplib import FTP
ftp_sites = ['ftp.x.org', 'ftp4.FreeBSD.org', 'ftp.ncsa.uiuc.edu', 'ftp.mozilla.org', 'ftp.crans.org']
class Worker_Thread(threading.Thread):
	def __init__(self, tid, queue):
		threading.Thread.__init__(self)
		self.tid = tid
		self.queue = queue
		self.lock = threading.Lock()
		print "Worker started...%d"%self.tid

	def run(self):
		print "In worker Thread %d"%self.tid
		while True:
			site = self.queue.get()
			"""try:
				site = self.queue.get()
			except Queue.Empty:
				print "Worker %d exiting.."%self.tid
				return"""
			try:
				conn = FTP(site)
				conn.login()
				self.lock.acquire()
				print "***********************Host:"+site
				print conn.retrlines('LIST')
				print "End#######################Host:"+site
				self.lock.release()
			except:
				print "Error in listing" + site
				#raise
			self.queue.task_done()

#lock mechanism on stdout	
queue = Queue.Queue()
for i in range(5):
	thread=Worker_Thread(i,queue)
	thread.setDaemon(True)
	thread.start()
	print "Worker Thread %d created"%i

for site in ftp_sites:
	queue.put(site)

queue.join()

print "All tasks completed!!!"
	
