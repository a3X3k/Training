### Biz44e : 

- After analysing several packets we can conclude that there is something to be done with `ICMP`.
- So apply the `ICMP filter` and start `analyzing`.
- We can see that packets from the `source = 10.30.8.102` and `destination = 192.168.42.83` has some `ZIP` Magic Numbers.
- In `scapy` there are lots of ways to extract the data.
- Here since the `length` is different for each packet we can easily `extract` the content.
- Here to avoid he unwanted chunks apply some filter to slice them.
- It can be indentified by seeing the `hex` of the `ZIP`.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Network/Assets/6.jpeg?raw=true)

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Network/Assets/5.jpeg?raw=true)

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Network/Assets/7.jpeg?raw=true)

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Network/Assets/8.jpeg?raw=true)

```
from scapy.all import *

f=rdpcap('bizz.pcap')
b = ''

for i in f[ICMP]: # Filter ICMP Packets
	if len(i) == 3528: # Filter Packet 1
		b+=str(i)[329:-1] # To Avoid Unwanted hex chunks slice the output
	if len(i) == 3526: # Filter Packet 2
		b+=str(i)[411:-1] # To Avoid Unwanted hex chunks slice the output
	if len(i) == 3524: # Filter Packet 3
		b+=str(i)[451:-1] # To Avoid Unwanted hex chunks slice the output
	
with open("final.zip", "wb") as g: # Write to the File
	g.write(bytes.fromhex(b))
	g.close()
```

- After `compliling` and `running` the `script` we shall get the `ZIP` file.

[PCAP File -- ](https://github.com/a3X3k/Training/blob/main/Forensics/Network/Biz44re/bizz.pcap)
[Script -- ](https://github.com/a3X3k/Training/blob/main/Forensics/Network/Biz44re/1.py)
[Zip File -- ](https://github.com/a3X3k/Training/blob/main/Forensics/Network/Biz44re/final.zip)
[PNG File](https://github.com/a3X3k/Training/blob/main/Forensics/Network/Biz44re/flag.png)

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Network/Assets/9.jpeg?raw=true)

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Network/Biz44re/flag.png?raw=true)
