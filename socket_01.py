import socket
tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsocket.bind(("0.0.0.0",8002))
tcpsocket.listen(2)
print "Waiting for Client...."
(client,(ip,port)) = tcpsocket.accept()
print "ip and port of connecting machine:%s %d"%(ip,port)
#data = client.recv(2048)
#print data
client.send("Welcome client....")
tcpsocket.close()
