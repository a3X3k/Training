# Network Challenges

## Beginner : 

### HTTP : 

- By the challenge name itself we can understand that there is something to do with `HTTP packets`. 
- So analysing the `HTTP` Packets gives the `flag`.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Network/Assets/1.jpeg?raw=true)

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Network/Assets/2.jpeg?raw=true)

```
Flag --> picoCTF{n0ts3cur3_894a6546}
```

### DNS : 

- By the challenge name itself we can understand that there is something to do with `DNS packets`. 
- So analysing the `DNS` Packets gives the `flag`.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Network/Assets/3.jpeg?raw=true)

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Network/Assets/4.jpeg?raw=true)

```
Flag --> picoCTF{w4lt3r_wh1t3_2d6d3c6c75aa3be7f42debed8ad16e3b}
```

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
