### Its My Pal :

- After analysing several packets we can conclude that there is something to be done with `ICMP`.
- So apply the `ICMP filter` and start `analyzing`.
- We can see that packets from the `source = 192.168.1.200` has some `ZIP` Magic Numbers.
- In `scapy` there are lots of ways to extract the data.
- We can see that the hex values of the `ZIP` start from the `hex` position `x002A` in all `ICMP` packets.
- The `Bytes` Equivalent of `Hex = x002A` is `42 Bytes`.
- So `slice` the rest of the `chunks`.
- It can be indentified by seeing the `hex` of the `ZIP`.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Network/Assets/10.jpeg?raw=true)

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Network/Assets/11.jpeg?raw=true)

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Network/Assets/12.jpeg?raw=true)

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Network/Assets/13.jpeg?raw=true)

```
from scapy.all import *

f=rdpcap('1.pcap')
b=''

for i in f[ICMP]:  # Filter ICMP Packets
    if i[IP].src == "192.168.1.200": # Source Filter
        b+=str(i)[0:0] # To Avoid Unwanted hex chunks slice the output
	    b+=str(i)[42:] # To Avoid Unwanted hex chunks slice the output

with open("final.zip", "w") as g: # Write to the File
    g.write(b)
    g.close()
```

- After `compliling` and `running` the `script` we shall get the `ZIP` file.
- But its Password Protected.
- So using Frackzip we shall crack the Password.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Network/Assets/14.jpeg?raw=true)

```
Password --> craccer
```

[PCAP File -- ](https://github.com/a3X3k/Training/blob/main/Forensics/Network/Its%20Complicated/1.pcap)
[Script -- ](https://github.com/a3X3k/Training/blob/main/Forensics/Network/Its%20Complicated/1.py)
[Zip File -- ](https://github.com/a3X3k/Training/blob/main/Forensics/Network/Its%20Complicated/final.zip)
[JPG File](https://github.com/a3X3k/Training/blob/main/Forensics/Network/Its%20Complicated/flag.jpg)

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Network/Its%20Complicated/flag.jpg?raw=true)
