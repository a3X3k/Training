## Fresh From the Oven

- After opening the `PCAP` file start analysing each packets.
- In one of the `TCP` packets you can find the `Message` which is being transmitted.
- So now we got an idea that all the messages are transmitted through `TCP` protocol.
- Now apply the `TCP filter` as `tcp` in `wireshark` and `analyze` the `TCP` packets.

![bi0s](https://github.com/a3X3k/Bi0s/blob/master/Forensics/Scapy/Assets/1.png?raw=true)
![bi0s](https://github.com/a3X3k/Bi0s/blob/master/Forensics/Scapy/Assets/2.png?raw=true)
![bi0s](https://github.com/a3X3k/Bi0s/blob/master/Forensics/Scapy/Assets/3.png?raw=true)
![bi0s](https://github.com/a3X3k/Bi0s/blob/master/Forensics/Scapy/Assets/4.png?raw=true)
![bi0s](https://github.com/a3X3k/Bi0s/blob/master/Forensics/Scapy/Assets/5.png?raw=true)
![bi0s](https://github.com/a3X3k/Bi0s/blob/master/Forensics/Scapy/Assets/6.png?raw=true)
![bi0s](https://github.com/a3X3k/Bi0s/blob/master/Forensics/Scapy/Assets/7.png?raw=true)
![bi0s](https://github.com/a3X3k/Bi0s/blob/master/Forensics/Scapy/Assets/8.png?raw=true)

- The message which is being transmitted in further packets is `encrypted`. 
- We dont know about the `cypher encryption`.
- But we got a `hint` in the `packet 61` that `November 5`.
- Now `5` is our hint and we shall try `shifting 5 positions` which we call as `ROT cypher` and in this case its `ROT 5` substitution.
- After `ROT 5` we shall get the `decrypted` text.

![bi0s](https://github.com/a3X3k/Bi0s/blob/master/Forensics/Scapy/Assets/9.png?raw=true)
![bi0s](https://github.com/a3X3k/Bi0s/blob/master/Forensics/Scapy/Assets/10.png?raw=true)
![bi0s](https://github.com/a3X3k/Bi0s/blob/master/Forensics/Scapy/Assets/11.png?raw=true)
![bi0s](https://github.com/a3X3k/Bi0s/blob/master/Forensics/Scapy/Assets/12.png?raw=true)
![bi0s](https://github.com/a3X3k/Bi0s/blob/master/Forensics/Scapy/Assets/13.png?raw=true)

#### Transmitted Message :
```
Hello, Rohith!

Hii, Shyam!

How much do you know about data security?

I don't know much about it. Can you explain it to me?

It means protecting our private data from unauthorized users.

Oh I see!

It also means encoding the data also. So we shall chat by encoding our messages so that others cannot intercept them! Our secret code: Remember remember the FIFTH of november :slight_smile:

Okay, sure.:)

Ymnx nx f xfruqj ns ymfy jshtiji bfd.

Tm, Ny'x ltti fsi ny yttp f qty tk ynrj yt zsijwxyfsi ktw rj.

Xjsinsl dtz xtrj nsyjwjxynsl knqjx, ywd yt knsi ymj xjhwjy gjmnsi ymjr fsi pjju ny htsknijsynfq

Tpfd, xzwj:)

Transferring files....
```

#### Decrypted Message

```
Ymnx nx f xfruqj ns ymfy jshtiji bfd
This is a sample in that encoded way

Tm, Ny'x ltti fsi ny yttp f qty tk ynrj yt zsijwxyfsi ktw rj.
Oh, It's good and it took a lot of time to understand for me.

Xjsinsl dtz xtrj nsyjwjxynsl knqjx, ywd yt knsi ymj xjhwjy gjmnsi ymjr fsi pjju ny htsknijsynfq
Sending you some interesting files, try to find the secret behind them and keep it confidential

Tpfd, xzwj:)
Okay, sure:)
```

- Further Analysing we shall see that the port 81 and 444 are transmitting some large amount of information.
-  So lets have a eye on them.

![bi0s](https://github.com/a3X3k/Bi0s/blob/master/Forensics/Scapy/Assets/22.png?raw=true)
![bi0s](https://github.com/a3X3k/Bi0s/blob/master/Forensics/Scapy/Assets/23.png?raw=true)

- Lets start with the `port 81` and we can see that it starts with `UP`.

![bi0s](https://github.com/a3X3k/Bi0s/blob/master/Forensics/Scapy/Assets/24.png?raw=true)

- Lets analyze the `port 444` and we can see that it starts with `*UIK263`.

![bi0s](https://github.com/a3X3k/Bi0s/blob/master/Forensics/Scapy/Assets/25.png?raw=true)

- Now lets apply `ROT-5` to the initial `payload`.

![bi0s](https://github.com/a3X3k/Bi0s/blob/master/Forensics/Scapy/Assets/26.png?raw=true)

- Now we shall understand that the payloads which we are trying to extract contains a `ZIP` file and `PDF` file.
- Lets do it in scapy now.

```
from scapy.all import *
f=rdpcap('1.pcap')
a=""
b=""
c=""
temp=""
for i in f[TCP]:
    if i.dport==81 or i.dport==444:
        temp=str(i[TCP].payload) #Extracting Pay Loads
        for j in temp:
            b=chr((ord(j)-5)%256) #Shift by 5
            if i.dport==81:
              a+=b #Extract ZIP file
            if i.dport==444:
              c+=b #Extract PDF file
    
with open("1.zip", "w") as g:
    g.write(a)
    g.close()

with open("1.pdf", "w") as g:
    g.write(c)
    g.close()
```

- Now we get 2 files.
- PDF file contains only some `Lorem ipsum` text.
- Trying `peepdf` does'nt give anything.
- So may be its a `Black Box`.
- `ZIP` file is `password` protected.
- So lets use `fcrackzip` to extract the `password`.

![bi0s](https://github.com/a3X3k/Bi0s/blob/master/Forensics/Scapy/Assets/14.png?raw=true)
![bi0s](https://github.com/a3X3k/Bi0s/blob/master/Forensics/Scapy/Assets/15.png?raw=true)

- Now we got a image from the ZIP file but there is no `flag`.

![bi0s](https://github.com/a3X3k/Bi0s/blob/master/Forensics/Scapy/Assets/flag.png?raw=true)

- Lets use some `steganography` tools to analyse them further. 

![bi0s](https://github.com/a3X3k/Bi0s/blob/master/Forensics/Scapy/Assets/16.png?raw=true)

- In binwalk we could'nt find anything.
- Since its a png we shall try with `zsteg` tool.

```
zsteg -a flag.png  # All Info
```

![bi0s](https://github.com/a3X3k/Bi0s/blob/master/Forensics/Scapy/Assets/17.png?raw=true)

- We shall see some `1MLorem ipsum` text in the `LSB` and other information does'nt seem interesting.
- But in `PDF` also we got the `LoremIpsum`.
- So there should be something with the text in this.
- So lets extract the entire `LSB payload` from the Image.

```
zzsteg -E b1,bgr,lsb,xy flag.png
```

![bi0s](https://github.com/a3X3k/Bi0s/blob/master/Forensics/Scapy/Assets/18.png?raw=true)

- When we try to `print` the contents we shall see some `unprintable characters`.

![bi0s](https://github.com/a3X3k/Bi0s/blob/master/Forensics/Scapy/Assets/19.png?raw=true)

- So lets try with `strings` command with `piping` to see if any readable text exist.

```
zzsteg -E b1,bgr,lsb,xy flag.png | strings
```

![bi0s](https://github.com/a3X3k/Bi0s/blob/master/Forensics/Scapy/Assets/20.png?raw=true)

- We got the printable `LoremIpsum` text.
- Now lets `grep` it to see if there is a flag.

```
zzsteg -E b1,bgr,lsb,xy flag.png | strings | grep -i inctf # Case insensitive
```

![bi0s](https://github.com/a3X3k/Bi0s/blob/master/Forensics/Scapy/Assets/21.png?raw=true)

- Finally we got our flag!!

[PCAP -- ](https://github.com/a3X3k/Bi0s/blob/master/Forensics/Scapy/Assets/1.pcap)
[ZIP -- ](https://github.com/a3X3k/Bi0s/blob/master/Forensics/Scapy/Assets/1.zip)
[PNG -- ](https://github.com/a3X3k/Bi0s/blob/master/Forensics/Scapy/Assets/flag.png)
[PDF -- ](https://github.com/a3X3k/Bi0s/blob/master/Forensics/Scapy/Assets/1.pdf)
[Scapy 1 -- ](https://github.com/a3X3k/Bi0s/blob/master/Forensics/Scapy/Assets/1.py)
[Scapy 2](https://github.com/a3X3k/Bi0s/blob/master/Forensics/Scapy/Assets/2.py)

```
Flag --> inctf{3ach_4nd_3v3ry_s3cre7_inf0rm4t10n_w1ll_b3_kn0wn_by_wir3shark!!!!!_:)}
```
