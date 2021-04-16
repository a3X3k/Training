from scapy.all import *
f=rdpcap('1.pcap')
a=""
b=""
temp=""
for i in f[TCP]:
	if i.dport==81:
		temp=str(i[TCP].payload)
		for j in temp:
			b=chr((ord(j)-5)%256)
			a+=b

with open("1.zip", "w") as g:
    g.write(a)
    g.close()

a=""
b=""
temp=""
for i in f[TCP]:
	if i.dport==444:
		temp=str(i[TCP].payload)
		for j in temp:
			b=chr((ord(j)-5)%256)
			a+=b

with open("1.pdf", "w") as g:
    g.write(a)
    g.close()
