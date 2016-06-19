import socket
tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#tcpsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
tcpsocket.bind(("0.0.0.0",8002))
tcpsocket.listen(2)
print "Waiting for Client...."
(client,(ip,port)) = tcpsocket.accept()
print "ip and port of connecting machine:%s %d"%(ip,port)

while True:
	data = client.recv(2048)
	print data
	client.send("Welcome client....u sent:%s"%data)

client.close()
tcpsocket.close()
