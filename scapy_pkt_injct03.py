from scapy.all import *


pkt = IP(dst="google.com")/ICMP()/"bye...bye...bye...bye...bye...bye...bye...bye..."


sendp(Ether()/pkt,iface="eth0")
