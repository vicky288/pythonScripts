from scapy.all import *


(resp,no_response)=sr1(IP(dst="google.com")/ICMP()/"hello...hello...hello...hello...hello...hello...hello...hello...hello...hello...")
resp[0].show()
