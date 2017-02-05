from scapy.all import *
pkts = sniff(iface="eth0", filter="icmp", count=5)

pkts[0].show()
print "###############################\n"
pkts[1].show()
print "###############################\n"
pkts[2].show()
print "###############################\n"

