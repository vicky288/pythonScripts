import struct
import socket
import binascii
#ifconfig eth0 promisc
#/usr/include/linux/if_ether.h
rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
pkt = rawSocket.recvfrom(10096)

for i in range(30):
	ethernetheader = pkt[0][0:14]
	eth_hdr = struct.unpack("!6s6s2s",ethernetheader)
	
	src= binascii.hexlify(eth_hdr[0])
	dst = binascii.hexlify(eth_hdr[1])
	typ = binascii.hexlify(eth_hdr[2])
		
	print "source Mac:%s Dest Mac:%s Type:%s"%(src,dst,typ)
	ipheader = pkt[0][14:34]
	
	ip_hdrpart = struct.unpack("!12s4s4s",ipheader)
	src_ip = socket.inet_ntoa(ip_hdrpart[1])
	dst_ip = socket.inet_ntoa(ip_hdrpart[2])
	print "source IP:%s Dest IP:%s "%(src_ip,dst_ip)
	
	tcp_hdr = pkt[0][34:54]
	tcp_hdrpart = struct.unpack("HH16s",tcp_hdr)
	src_prt = tcp_hdrpart[0]
	dst_prt = tcp_hdrpart[1]
	
	print "source port:%d Dest port:%d "%(src_prt,dst_prt)


