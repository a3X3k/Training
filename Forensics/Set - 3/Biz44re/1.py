from scapy.all import *

f=rdpcap('bizz.pcap')

b = ''

for i in f[ICMP]:
	if len(i) == 3528:
		b+=str(i)[329:-1]
	if len(i) == 3526:
		b+=str(i)[411:-1]
	if len(i) == 3524:
		b+=str(i)[451:-1]
	

with open("final.zip", "wb") as g:
	g.write(bytes.fromhex(b))
	g.close()
