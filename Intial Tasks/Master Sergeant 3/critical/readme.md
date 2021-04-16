[![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Assets/1.png?raw=true "Bi0s")](https://tasks.bi0s.in/home)

# 💥Critical:💥
### Description : 

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Assets/29.jpeg?raw=true)

### Category : 
- **Forensics**

### Challenge Link :

- [Mirror](https://drive.google.com/file/d/1wP4hrZU4fYZG2VHEuGPn5uWjbT1j538W/view?usp=sharing)
- [Mirror](https://mega.nz/file/w2oCjAgK#T1cNEXnBsuxFAAfNImSSkJfq1ye-_a3EArONL_JU_5Y)

### Initial Analysis :

- Since it comes under **Forensics** I went through the Forensics Page of wiki.bi0s.in and tried to find any relevant things [Forensics](https://wiki.bi0s.in/forensics/roadmap/)
- First **Crack** the **Zip Password**.
- Crack the password using the fcrackzip tool.
- Then finally extracted the **png** image.
- I cracked it and extracted it using the tool **unzip** command.
- Now **UNZIP** the Zip File using the **PASSWORD**
- Then uncorrupt the corrupted **PNG** image.

### Steps To Be followed :

- First Go through --> https://wiki.bi0s.in/forensics/image-forensics/
- Try this out in **UBUNTU LTS**.
- Download the Zip file that has to be cracked from the Mirror Links.
- Then to crack the Password Install **fcrackzip** Tool from https://wiki.bi0s.in/steganography/fcrackzip/ Page.
```
$ sudo apt install fcrackzip
```
- Then there are two methods to crack the Password.
    -  Brute ForceAttack
    -  Dictionary Attack
- Try Both ways and this worked with Dictionary Attack.
- Detailed Explanation is given in https://wiki.bi0s.in/steganography/fcrackzip/
- The following code is for Dictionary Method.

```
$ fcrackzip -v -u -D -p rockyou.txt Critical.zip
```

- This is will return you the Password.
- The next step is to unzip it using the Password that's which we found.
- For more Detailed Explanation in Unzipping visit https://wiki.bi0s.in/forensics/image-forensics/#zip
- Use the following command to unzip the file. 

```
$ unzip Critical.zip
```
- After Unzipping the file named **critical.png** will be Extracted.
- Now check the **PNG** **Magic Values** and **Chunks** using **PNGCHECK**.

```
$ sudo apt install pngcheck
```

- You can find lot of Hex online editors.
- One of the Best **Hex Editors** [HEX EDITOR](https://hexed.it/)
- Edit the **MAGIC VALUES** First. 

[Refer this to know about Magic Values and Chunks](https://wiki.bi0s.in/forensics/roadmap/)

- Then save it and **RUN** using **pngcheck**.

```
$ pngcheck <Filename>
```

```
$ pngcheck "critical.png"
```

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Assets/24.jpeg?raw=true)
![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Assets/25.jpeg?raw=true)
![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Assets/26.jpeg?raw=true)

- Repeat this until you get the **OK** in PngCheck.

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Assets/27.jpeg?raw=true)

### Flag 🏴 : 

> **inctf{correcting_all_chunks_gives_the_image}**





