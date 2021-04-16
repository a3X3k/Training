from scapy.all import *
f=rdpcap('1.pcap')
a=""
b=""
c=""
temp=""
for i in f[TCP]:
    if i.dport==81 or i.dport==444:
        temp=str(i[TCP].payload)
        for j in temp:
            b=chr((ord(j)-5)%256)
            if i.dport==81:
              a+=b
            if i.dport==444:
              c+=b
    
with open("1.zip", "w") as g:
    g.write(a)
    g.close()

with open("1.pdf", "w") as g:
    g.write(c)
    g.close()
