from scapy.all import *

f=rdpcap('data.pcap')

b=''

for i in f[ICMP]:
    if i[IP].src == "10.136.255.127":
	#0020 offset and 2 in position => 20 + 2 = 22
	#Convert hex 22 to bytes.
	# U will get 34 bytes.

        b+=str(i)[34] 

with open("final.gif", "w") as g:
    g.write(b)
    g.close()
