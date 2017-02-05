from scapy.all import *


pkt = IP(dst="google.com")/ICMP()/"hello...hello...hello...hello...hello...hello...hello...hello...hello...hello..."


send(pkt)
