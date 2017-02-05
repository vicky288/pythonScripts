from scapy.all import *
pkts = sniff(iface="eth0", count=25)

wrpcap("demo.pcap",pkts)
read_pkts = rdpcap("demo.pcap")
read_pkts[10].show()

