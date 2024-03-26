from scapy.all import *
import time

#ether = Ether(dst="c8:47:19:64:92:4a", src="11:22:33:44:55:66",  type="IPv4")
ether = Ether()
ip = IP(dst="192.168.18.1")
udp  = UDP(dport=7080)/b'\x0e\xe8\x97\xe8\x68\x68\x97\xf1'
packet  = ether/ip/udp

i=0
while(True):
	i += 1
	sendp(packet, iface="wlan0")
	print("Sending Packet Nr: {}".format(+i))
	time.sleep(20)
