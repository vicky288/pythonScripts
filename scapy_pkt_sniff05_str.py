from scapy.all import *
pkts = sniff(iface="eth0", filter="icmp", count=5)

icmp_str = str(pkts[0])
val = Ether(icmp_str)
print val
