# Traboda Forensics Challenges

### Back to San Andreas

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/31.jpeg?raw=true)

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/32.jpeg?raw=true)

- Here when we try to open the image then we cannot find anything.
- So next step is to analyze the **JPEG** image.
- Jsteg is a package for hiding data inside JPEG files with a technique known as steganography. 
- This is accomplished by copying each bit of the data into the least-significant bits (LSB) of the image. 

#### Installation

```
$ sudo wget -O /usr/bin/jsteg https://github.com/lukechampine/jsteg/releases/download/v0.1.0/jsteg-linux-amd64
$ sudo chmod +x /usr/bin/jsteg
$ sudo wget -O /usr/bin/slink https://github.com/lukechampine/jsteg/releases/download/v0.2.0/slink-linux-amd64
$ chmod +x /usr/bin/slink
```

#### Revealing data

```
$ jsteg reveal <in.jpg> <output file name>
```

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/33.jpeg?raw=true)

- The data will be extracted in the specified file.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/34.jpeg?raw=true)

- If we open the file we can see that there is a link.
- Now if we open the link then we shall see the **flag**.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/35.jpeg?raw=true)

```
Flag --> inctfj{gr0ve_5treet_f0r_l1fe}
```

### 10111001

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/36.jpeg?raw=true)

- This challenge is based on LSB steganography.
- Zsteg is also a tool like Jsteg but it is used to detect LSB steganography only in the case of PNG and BMP images.

#### Installation

```
$ sudo apt install ruby
$ sudo gem install zsteg
```

#### Usage

```
$ zsteg <filename>
```

- If we run this we can find some meaningful data embedded in the LSBs of the PNG image. 
- This meaningful data can help us in solving the challenge.
- Among the LSB's we can see a line this, 

**This is the Flag --> NFXGG5DGNJ5TI3K7ORUDGX2MGNAVG5C7GVUUO3RRMYYWGNDOKRPWEVKUL4YV6YZUJZPXI4RQOVBEYM27LEYHKXZUL5WDAVD5**

- It is encoded in **Base32** format.
- We need to decode it to get the flag.
- **Online Tool -->** https://emn178.github.io/online-tools/base32_decode.html

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/37.jpeg?raw=true)

```
Flag --> inctfj{4m_th3_L3ASt_5iGn1f1c4nT_bUT_1_c4N_tr0uBL3_Y0u_4_l0T}
```

### Detailed View

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/38.jpeg?raw=true)

- Download the image.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/39.jpeg?raw=true)

- Hint is given as **there is more to know about this file** which symbolically means to look indepth detail of the image. 
- Meta data is the indepth information of the file.
- **Online Tool -->** https://exifinfo.org/detail/psTncqjsVTTZGxnzXzhDEQ

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/40.jpeg?raw=true)

- We can see a link in the **comment**
- **Link -->** https://pastebin.com/KudUCfTC
- If we open the link then we will be able to see the **Base64** encrypted flag.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/41.jpeg?raw=true)

- Next step is to decrypt it.
- **Online Tool -->** https://decode.urih.com/data/

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/42.jpeg?raw=true)

```
Flag --> flag{M15sI0N_aCc0MPL15h3D}
```

### Con-The-Cat

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/43.jpeg?raw=true)

- Download the **PNG** image.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/44.jpeg?raw=true)

- Binwalk is a tool used mainly for searching embedded files and executable code within another data file.

#### Installation

```
$ sudo apt install binwalk
```

#### Usage

```
$ binwalk -e <file-name>
```

```
$ binwalk -e 1.png
```

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/45.jpeg?raw=true)

- Here in the above image, we see that there is a 'jpg image' that has a compressed 'images' in it and we see that, it is embedded within the jpg image file. 
- To extract it we can make use of a carving tool dd. 
- It can carve out data from specific offsets that are passed as arguments to the tool along the with the file that needs to be read. 

```
$ dd if=<filename> of=<filename> bs=1 skip=<offset>
```

- if = the file from which data has to be extracted is passed as an argument.
- of = has the name of the file that we give after extraction. 
- skip = is the offset of the file that has to be read.
- bs = i the byte skip argument that specifies the frequency of reading data from the given file.

```
$ dd if=1.png of=2.png bs=1 skip=7821

--> Here 7821 is one of the offsets of the file.
```

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/46.jpeg?raw=true)

```
Flag --> inctfj{y0u_c4nt_s33_m3!!}
```

### Snow Man

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/47.jpeg?raw=true)

- Download the file and we can understand that it comes under **Whitespace Steganography**.
- Stegsnow is a tool for concealing messages in text files by appending tabs and whitespaces at the end of lines.
- The encoding used by snow relies on the fact that whitespaces and new lines won't be displayed in text editors.

#### Installation

```
$ sudo apt install stegsnow
```

#### Decryption

```
$ stegsnow -C -p "<Password>" <Txt File>
```

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/48.jpeg?raw=true)

- After decrypting we will get a flag which is **BASE-64** Encoded.
- Using online tool we shall decrypt it.
- **Online Tool --> https://www.dcode.fr/base-64-encoding**

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/49.jpeg?raw=true)

```
Flag --> inctfj{h4h4_st3gsn0w_i5_c00000001}
```

### The Office Trouble II

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/50.jpeg?raw=true)

- In this challenge we need to crack the pdf password and find the **flag**
- PDF Crack is a tool for recovering the pass for Encrypted PDF files. 
- Encrypted files means the metadata of the file was encrypted with some characters.

**It has some special features like:**

- Checks with the system password and also the user provided password.
- It can crack password by brute-forcing method only for character sets and only when we provide the maximum and minimum length of the password.
- Searches the password from the wordlist.
- Optimized search for owner-password when user-password is known.

#### Installation

```
$ sudo apt-get install pdfcrack
```

#### Usage

**Brute-forcing**

```
$ pdfcrack -f <file_name>
```

**Wordlist Cracking**

```
$ pdfcrack -f <file_name> -w <wordlist_file>
```

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/51.jpeg?raw=true)

- After decryption we get a password and now we will be able to open the pdf.

```
Password --> fear420
```

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/52.jpeg?raw=true)

### Traffic 13

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/53.jpeg?raw=true)

- As given we have to analyze the network packages sent and received.
- Wireshark is the most commonly used network protocol analyser and the de facto standard across many commercial and non-profit enterprises.
- It shows the protocol of each packet captured and also the protocol hierarchy of the network whose pcap was made.
- The hex buffer of each packet can be analysed separately and layer by layer.

#### Installation

```
$ sudo apt install wireshark-qt
```

- Open **WireShark** and analyze the **TCP** packages.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/54.jpeg?raw=true)

- After analyzing various **TCP** packages we shall find the **flag**.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/55.jpeg?raw=true)

- But the flag is encryted.

```
Encrypted Flag --> vapgsw{o3j4er_0s_plO3E_GUe3ng5}
```

- So we have to decrypt it using the online Tool. 
- **Online Tool --> https://www.dcode.fr/caesar-cipher**

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/56.jpeg?raw=true)

```
Flag --> inctfj{b3w4re_0f_cyB3R_THr3at5}
```

### Crack FDP

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/57.jpeg?raw=true)

- Download the **PDF**. 
- In this challenge we need to crack the pdf password and find the **flag**
- PDF Crack is a tool for recovering the pass for Encrypted PDF files. 
- Encrypted files means the metadata of the file was encrypted with some characters.

**It has some special features like:**

- Checks with the system password and also the user provided password.
- It can crack password by brute-forcing method only for character sets and only when we provide the maximum and minimum length of the password.
- Searches the password from the wordlist.
- Optimized search for owner-password when user-password is known.

#### Installation

```
$ sudo apt-get install pdfcrack
```

#### Usage

**Brute-forcing**

```
$ pdfcrack -f <file_name>
```

**Wordlist Cracking**

```
$ pdfcrack -f <file_name> -w <wordlist_file>
```

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/58.jpeg?raw=true)

```
Password --> diosayudameenelesut
```

- After decryption we get a password and now we will be able to open the pdf.
- We can see the **flag** inside the file.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/59.jpeg?raw=true)

```
Flag --> flag{1ae06a29a7abd6c07dba8976698f756b987f734d}
```

### S3cr3t

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/60.jpeg?raw=true)

- Download the **AUDIO** file.
- Using **Online decoder** we shall decode the **Morse Audio**.

**Online Morse Code Decoder --> https://morsecode.world/international/decoder/audio-decoder-adaptive.html**

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/61.jpeg?raw=true)

```
Flag --> inctfj{M0RS3C0D3I5C001}
```

### Signal Messenger

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/62.jpeg?raw=true)

- Download the **AUDIO** file.
- Using **Online decoder** we shall decode the **Morse Audio**.

**Online Morse Code Decoder --> https://morsecode.world/international/decoder/audio-decoder-adaptive.html**

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/63.jpeg?raw=true)

```
Flag --> flag{Y0UG0T7HES3CRE7ENC0DEDS7RING}
```

### Hidden Data

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/64.jpeg?raw=true)

- Download the Zip FIle.
- The zip file is **corrupted**.
- So edit the **Hex** chunks and then try to open the zip file.
- First start with the **Header--Magic Values** and then **Footer**.

**Online Tool --> https://hexed.it/**

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/65.jpeg?raw=true)

- After editing the **Header and Footer** we will be able to open the Zip file.

```
Flag --> inctfj{GR3aT_m155i0n_4Cc0mpL15h3D}
```

### Corrupted File

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/66.jpeg?raw=true)

- Download the Zip FIle.
- The zip file is **corrupted**.
- So edit the **Hex** chunks and then try to open the zip file.
- First start with the **Header--Magic Values** and then **Footer**.

**Online Tool --> https://hexed.it/**

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/67.jpeg?raw=true)

- Here we will be able to see the **Secret Information**.
- The given information in encrypted in **Base 64** format.
- SO we shall decrypt it back to the ASCII.

**Online Tool --> https://www.base64decode.org/**

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/68.jpeg?raw=true)

```
Flag --> flag{9e360084196a092a15c5c44b54934bfc}
```

### Dig Deep

- Download the image given.
- If we try to open we wont be able to find anything.
- So we have to analyze the chunks.
- Binwalk is a tool used mainly for searching embedded files and executable code within another data file.

#### Installation

```
$ sudo apt install binwalk
```

#### Usage

```
$ binwalk -e <file-name>
```

```
$ binwalk -e 1.jpg
```

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/72.jpeg?raw=true)

- Here in the above image, we see that there is a **jpg image** and a **ZIP** in it and we see that, it is embedded within the jpg image file. 
- To extract it we can make use of a carving tool dd. 
- It can carve out data from specific offsets that are passed as arguments to the tool along the with the file that needs to be read. 

```
$ dd if=<filename> of=<filename> bs=1 skip=<offset>
```

- if = the file from which data has to be extracted is passed as an argument.
- of = has the name of the file that we give after extraction. 
- skip = is the offset of the file that has to be read.
- bs = i the byte skip argument that specifies the frequency of reading data from the given file.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/73.jpeg?raw=true)

- If we try to extract all files we will get three files. 

**PART - 1 --> Image 1**

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/70.jpeg?raw=true)

**PART - 2 --> Text from the Zip FIle**

```
Here is the part2 202015ed269630d
```

**PART - 3 --> Image 2**

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/71.jpeg?raw=true)

- If we combine **3 Parts** we can get the **Flag**.

```
Flag --> flag{7b560d81c0202015ed269630d2b8b1993d2e7788}
```

### Mysterious File

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/74.jpeg?raw=true)

- If we change the **Extension** of the file we will get the **Flag**.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/75.jpeg?raw=true)

### Angry Steve

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/77.jpeg?raw=true)

- Lets Analyze te **Chunks**

**Online Tool --> https://hexed.it/**

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/78.jpeg?raw=true)

```
Flag --> inctfj{string5_m4keth_fl4gs}
```

### Noice

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/79.jpeg?raw=true)

- Now we shall analyze the Audio using **Sonic Visualizer**.
- Sonic-Visualiser is also a GUI based tool. 
- It is similar to Audacity but a bit more powerful than it. 
- It is an application software for viewing and analysing the contents of audio files.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/80.jpeg?raw=true)

```
Flag --> inctfj{y0u_b3tt3r_l00k_cl0s3ly}
```

### Deeper..

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/81.jpeg?raw=true)

- Lets download the image.
- If we try to open we wont be able to find anything.
- So we have to analyze the chunks.
- Binwalk is a tool used mainly for searching embedded files and executable code within another data file.

#### Installation

```
$ sudo apt install binwalk
```

#### Usage

```
$ binwalk -e <file-name>
```

```
$ binwalk -e 1.jpg
```

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/76.jpg?raw=true)

- Here in the above image, we see that there is a **ZIP** in it and we see that, it is embedded within the jpg image file. 
- To extract it we can make use of a carving tool dd. 
- It can carve out data from specific offsets that are passed as arguments to the tool along the with the file that needs to be read. 

```
$ dd if=<filename> of=<filename> bs=1 skip=<offset>
```

- if = the file from which data has to be extracted is passed as an argument.
- of = has the name of the file that we give after extraction. 
- skip = is the offset of the file that has to be read.
- bs = i the byte skip argument that specifies the frequency of reading data from the given file.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/82.jpeg?raw=true)

- Now we open the **ZIP** file then we will be able to find the **Audio**.
- Next step is to analyze the Audio.

**Online Tool --> https://databorder.com/transfer/morse-sound-receiver/**

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/83.jpeg?raw=true)

```
Flag --> inctf{H34R_W1TH_Y0UR_3Y35}
```

### Winter Sport

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/84.jpeg?raw=true)

- After downloading the pdf file we wont be able to find anything.
- Hence we have to analyze the embeded data in it.
- Peepdf is a Python based tool to explore PDF files in order to find out if the file can be harmful or not. 
- The aim of this tool is to provide all the necessary components that a security researcher could need in a PDF analysis without using 3 or 4 tools to make all the tasks. 
- With peepdf it's possible to see all the objects in the document showing the suspicious elements, supports all the most used filters and encodings, it can parse different versions of a file, object streams and encrypted files.

#### Usage

```
$ ./peepdf.py -i pdffile.pdf
```

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/85.jpeg?raw=true)

- As we can see there is an embedded file in the pdf.
- So now we need to extract the embedded file using the stream command

```
$ PDF> stream 8 > <Filename>
$ xdg-open <Filename>

--> File Name --> f1

$ PDF> stream 8 > f1
$ xdg-open f1
```

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/86.jpeg?raw=true)

- After opening the zip file we shall get a pdf.
- If we open the **PDF** then we will be able to find that there is something hidden in the **whitespace**.
- We shall understand that its **White Space Steganography**.
- Reference --> **https://wiki.bi0s.in/steganography/stegsnow/** 
- By refering the **wiki.bi0s.in** we can get to know that there is a tool named Stegsnow which conceals messages in text files by appending tabs and whitespaces at the end of lines.
- Download the txt file which has to be decrypted.

#### Installation

```
$ sudo apt install stegsnow
```

#### Decryption

```
$ stegsnow -C <Filename>

--> Filename = omg.pdf

$ stegsnow -C omg.pdf
```

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/87.jpeg?raw=true)

```
Flag --> inctf{w3lcom3_t0_7h3_w0rld_0f_whit3sp4c3}
```

### Hidden Message

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/88.jpeg?raw=true)

- We are provided with the **Python Script** and **JPEG Image**

```
--> Python Script 

import string
import base64

def encode(x):
    return x.encode("hex") 

if _name=="main_":
	print("63486c306147397561584e6d6457343d")
	print("decode this to get the pass")
	encoded_data = encode(base64.b64encode(""))
	print(encoded_data)
```

- We have to debug it to make it excute to get the necessary output.
- First Change the **encode()** function to **decode()**
- Then in order to pass the **Parameter** to the decode function it should be in **ASCII** format.
- But we have **Hex** here.
- So we have to convert the given hex to ASCII format.

**Online Tool --> https://www.rapidtables.com/convert/number/hex-to-ascii.html**

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/89.jpeg?raw=true)

- After several debuging we shall get the final script.

```
import string
import base64

def decode(x):
    return x.decode('utf8') 

if _name=="main_":
	print("63486c306147397561584e6d6457343d")
	print("decode this to get the pass")
	encoded_data = decode(base64.b64decode("cHl0aG9uaXNmdW4="))
	print(encoded_data)
```

- Next Step is to run the script.

```
--> pythonisfun
```

- Steghide is used to embed and extract secret messages in images. 
- It supports all the general formats of images like .png, .jpg etc.

#### Installation

```
$ sudo apt install steghide
```

#### Usage

```
$ steghide extract -sf <Filename>
Enter passphrase : ********
wrote extracted data to "<Filename>.txt".
```

- We have to enter the password which we got from the **Python Script**.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/90.jpeg?raw=true)


### Mariana_Trench_Deep

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/125.jpeg?raw=true)

- `Download` the given files.
- But we could'nt find anything in the Audio and Video Files.
- After a long analysis we shall understand that the `Txt` file which was given was the only useful file.
- `Ook. Ook! Ook?` was the hint given there. 
- `Ook` is a rewriting of the `BrainFuck`, an already `obfuscated esoteric programming language`, designed to be `writable` and `readable` by `orang-utans` (which would communicate by pronouncing the `onomatopoeia` 'ook, ook'). 

```
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook? Ook. Ook? Ook. Ook. Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook? Ook. Ook? Ook. Ook? Ook. Ook? Ook. Ook! Ook! Ook? Ook! Ook. Ook? Ook. Ook? Ook. Ook? Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook. Ook? Ook. Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook. Ook. Ook? Ook. Ook. Ook. Ook. Ook! Ook. Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook? Ook. Ook! Ook. Ook. Ook? Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook. Ook? Ook. Ook! Ook! Ook! Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook. Ook? Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook? Ook. Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook. Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook. Ook? Ook! Ook! Ook! Ook! Ook! Ook. Ook? Ook. Ook! Ook! Ook! Ook. Ook. Ook? Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook? Ook. Ook! Ook. Ook. Ook? Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook? Ook. Ook! Ook. Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook.
```

- We have to `Decode` it now.
- Use `Online Tool` --> https://www.dcode.fr/ook-language

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/126.jpeg?raw=true)

```
Flag --> inctfj{l4ngu4g35_d0nt_m4k3_s3ns3}
```


#### Reference 1 --> https://wiki.bi0s.in/steganography/intro/

#### Reference 2 --> https://wiki.bi0s.in/forensics/roadmap/
