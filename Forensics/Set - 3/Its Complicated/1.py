from scapy.all import *

f=rdpcap('1.pcap')

b=''

for i in f[ICMP]:
    if i[IP].src == "192.168.1.200":
        b+=str(i)[0:0]
        b+=str(i)[42:]

with open("final.zip", "w") as g:
    g.write(b)
    g.close()
