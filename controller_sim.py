from scapy.all import *
import time

#ether = Ether(dst="c8:47:19:64:92:4a", src="11:22:33:44:55:66",  type="IPv4")
ether = Ether()
ip = IP(dst="192.168.18.1")
udp_cpayload = UDP(dport=7080)/b'\x0e\xe8\x97\xe8\x68\x68\x97\xf1'
udp_fpayload = UDP(dport=1337)/b'\x65\x61\x73\x74\x65\x72\x68\x65\x67\x67\x32\x34\x20\x68\x79\x70\x65\x21\x21'
#easterhegg24 hype!!

packet_cpayload = ether/ip/udp_cpayload
packet_fpayload = ether/ip/udp_fpayload

i=0
while(True):
	i += 1
	sendp(packet_cpayload, iface="wlp0s20f3")
	print("Sending good  Packet Nr: {}".format(i))
	time.sleep(30)


	sendp(packet_fpayload, iface="wlp0s20f3")
	print("Sending false1 Packet Nr: {}".format(i))
	time.sleep(15)

	sendp(packet_fpayload, iface="wlp0s20f3")
	print("Sending false2 Packet Nr: {}".format(i))
	time.sleep(15)
