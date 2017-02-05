from scapy.all import *

pkt = IP(dst="google.com")
pkt.show()

print "********************************************"
pkt1 = IP(dst="google.com")/ICMP()/"hello..."
pkt1.show()
