from scapy.all import *

p=rdpcap('dnscap.pcap')

x=""
y=""
temp=""

for i in p:
    if i in p[DNSQR] and i not in p[DNSRR]:
        x=(i[DNSQR].qname)[18:-18]
        x=x.replace('.','')
        x=x.decode('hex')
        if(x==temp):
            continue
        y+=x
        temp=x

f=open('final.png','w')
f.write(y[95:])
f.close()



 
 
