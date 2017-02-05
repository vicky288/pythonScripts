from scapy.all import *
#lsc()
#conf
#ls()
pkts = sniff(iface="eth0", count=25)
pkts[10].show()
hexdump(pkts[15])

