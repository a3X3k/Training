### Orcish :

- After analysing several packets we can conclude that there is something to be done with `ICMP`.
- So apply the `ICMP filter` and start `analyzing`.
- We can see that packets from the `source = 10.136.255.127` has the `GIF` hex in it.
- They are `singly` scattered in all `ICMP` packets as `G` `I` `F` `8` `9`.
- We can see that the hex values of the `GIF` start from the `hex` position `x0022` in all `ICMP` packets.
- The `Bytes` Equivalent of `Hex = x0022` is `34 Bytes`.
- So `slice` the rest of the `chunks`.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Network/Assets/15.jpeg?raw=true)

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Network/Assets/16.jpeg?raw=true)

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Network/Assets/17.jpeg?raw=true)

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Network/Assets/18.jpeg?raw=true)

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Network/Assets/19.jpeg?raw=true)

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Network/Assets/20.jpeg?raw=true)

```
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
```

- After `compliling` and `running` the `script` we shall get the `GIF` file.

[PCAP File -- ](https://github.com/a3X3k/Training/blob/main/Forensics/Network/Orcish/data.pcap)
[Script -- ](https://github.com/a3X3k/Training/blob/main/Forensics/Network/Orcish/1.py)
[GIF File](https://github.com/a3X3k/Training/blob/main/Forensics/Network/Orcish/final.gif)

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Network/Orcish/final.gif?raw=true)
