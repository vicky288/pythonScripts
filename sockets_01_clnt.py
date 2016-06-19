import socket
import sys
tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsocket.connect((sys.argv[1],9000))
while True:
	userIn = raw_input("Please enter a msg:")
	tcpsocket.send(userIn)
	print tcpsocket.recv(2048)

tcpsocket.close()
