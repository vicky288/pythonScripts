import signal

def ctrlc_handler(signum,frm):
	print "haha u can't kill me"

print "Installing sinal handler..."
signal.signal(signal.SIGINT, ctrlc_handler)

print "Done!!!!"


while True:
	pass
