#!/usr/bim/evn python
# This scripts lets us extract strings from a given pcap file 
from scapy.all import *

pcap =rdpcap("capture.pcap")
flag= []
for p in pcap[UDP]:
	try:
		if (p[IP].src == "10.0.0.80" and p[IP].dst == "10.0.0.1"):
			flag.append(p[Raw].load.decode('utf-8'))
	except IndexError:
		continue
print("".join(flag))