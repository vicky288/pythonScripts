from scapy.all import *
pkts = sniff(iface="eth0", filter="icmp", count=5, prn=lambda x: x.summary())


