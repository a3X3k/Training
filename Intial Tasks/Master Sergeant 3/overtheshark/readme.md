[![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Assets/1.png?raw=true "Bi0s")](https://tasks.bi0s.in/home)

# 🦈Over the Shark🦈

### Description : 

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Assets/10.jpeg?raw=true)

### Category : 
- **Forensics**
### Challenge Link :

- [Mirror 1](https://drive.google.com/file/d/1JcHyOri1RmyXhYz8AAw73ld7IMEAxTSN/view?usp=sharing)
- [Mirror 2](https://mega.nz/file/FyhEhAwI#73Dl2NCQ29U71iBxTwp40QPkKpDGXGHzLy8BgY2nPvE)

### Initial Analysis :

- First when I read the hint given I thought that we need to crack the zip password and extract some hidden information from the cracked zip.
- Then i went through wiki.bi0s.in 
- Then I found a way to crack the password using the fcrackzip tool.
- I cracked it and extracted it using the tool **unzip** command.
- Then finally extracted the **pcapng** image.
- Since it comes under **Forensics** I went through the Forensics Page of wiki.bi0s.in and tried to find any relevant things. [Forensics](https://wiki.bi0s.in/forensics/roadmap/)
-Then I found **Wireshark Analyzer** under **Network Forensics**.
- I installed it and tried to analyze the **pcapng** Image.
- Then under **HTTP** I found a **flag** with the flag format as mentioned in the description.

### Steps To Be followed :
- Try this out in **UBUNTU LTS**.
- Download the Zip file that has to be cracked from the Mirror Links.
- Then to crack the Password Install **fcrackzip** Tool from https://wiki.bi0s.in/steganography/fcrackzip/ Page.
```
$ sudo apt install fcrackzip
```
- Then there are two methods to crack the Password.
    -  Brute ForceAttack
    -  Dictionary Attack
- Try Both ways and this worked with Brute Force Attack.
- Detailed Explanation is given in https://wiki.bi0s.in/steganography/fcrackzip/
- The following code is for Brute Force Attack method.
```
$ fcrackzip -v -b -u -p Overtheshark.zip
```

- This is will return you the Password.
- The next step is to unzip it using the Password that's which we found.
- For more Detailed Explanation in Unzipping visit https://wiki.bi0s.in/forensics/image-forensics/#zip
- Use the following command to unzip the file. 

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Assets/14.jpeg?raw=true)
```
$ unzip Overtheshark.zip
```
- After Unzipping the file named **Challenge1.pcapng** will be Extracted.
- The next Step is to Analyse the contents of the file using the **Wireshark** tool.
- To install Wireshark and for further more details visit https://wiki.bi0s.in/forensics/wireshark/
```
$ sudo apt install wireshark-qt
```
- Use this command to install the wireshark tool.
- Next step is to open the file using **Wireshark** to analyze it.
- Then have the detailed look at all **Source Destination Protocol**.
- Click on each packages and try to find the Flag or analyze what's been done.
- Then finally under **HTTP** we shall found the **flag** with a flag format as mentioned in the description.

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Assets/12.jpeg?raw=true)
![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Assets/13.jpeg?raw=true)

### Flag 🏴 : 
> **actf{wireshark_isn't_so_bad_huh-a9d8g99ikdf}**





