from scapy.all import *


sendp(Ether()/IP(dst="google.com")/ICMP()/"lol...lol...lol...lol...lol...",iface="eth0",loop=1, inter=1)
