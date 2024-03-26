from scapy.all import *
import time

#ether = Ether(dst="c8:47:19:64:92:4a", src="50:e0:85:c6:bf:e2",  type="IPv4")
ether = Ether(type="IPv4")
ip = IP(dst="192.168.18.1")
udp_cpayload_forward = UDP(dport=7080)/b'\x0e\xe8\x97\xe8\x68\x68\x97\xf1'
#udp_cpayload_backward = UDP(dport=7080)/b'\x0e\xe8\x68\xe8\x68\x68\x68\xf1'
#udp_cpayload_left = UDP(dport=7080)/b'\x0e\x97\xe8\xe8\x68\x68\x97\xf1'
#udp_cpayload_right = UDP(dport=7080)/b'\x0e\x69\xe8\xe8\x68\x68\x69\xf1'

udp_fpayload = UDP(dport=1337)/b'\x65\x61\x73\x74\x65\x72\x68\x65\x67\x67\x32\x34\x20\x68\x79\x70\x65\x21\x21'
#easterhegg24 hype!!

packet_cpayload_forward = ether/ip/udp_cpayload_forward
#packet_cpayload_backward = ether/ip/udp_cpayload_backward
#packet_cpayload_left = ether/ip/udp_cpayload_left
#packet_cpayload_right = ether/ip/udp_cpayload_right

packet_fpayload = ether/ip/udp_fpayload

i=0
while(True):
	i += 1

	sendp(packet_cpayload_forward, iface="wlp0s20f3")
	print("Sending good  Packet *forward* Nr: {}".format(i))
	time.sleep(20)
	#sendp(packet_cpayload_backward, iface="wlp0s20f3")
	#print("Sending good Packet *backward*  Nr: {}".format(i))
	#time.sleep(30)	
	#sendp(packet_cpayload_left, iface="wlp0s20f3")
	#print("Sending good  Packet *left*  Nr: {}".format(i))
	#time.sleep(30)
	#sendp(packet_cpayload_right, iface="wlp0s20f3")
	#print("Sending good  Packet *right*  Nr: {}".format(i))
	#time.sleep(30)

	sendp(packet_fpayload, iface="wlp0s20f3")
	print("Sending false1 Packet Nr: {}".format(i))
	time.sleep(15)

#	sendp(packet_fpayload, iface="wlp0s20f3")
#	print("Sending false2 Packet Nr: {}".format(i))
#	time.sleep(2)
