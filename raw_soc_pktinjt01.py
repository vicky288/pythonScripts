import struct
import socket

#tcpdump -i eth0 -vv -XX "not port 22"

rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

rawSocket.bind(("eth0",socket.htons(0x0800)))

packet = struct.pack("!6s6s2s",'\xaa\xaa\xaa\xaa\xaa\xaa','\xbb\xbb\xbb\xbb\xbb\xbb','\x08\x00')

rawSocket.send(packet+"Hello There")


