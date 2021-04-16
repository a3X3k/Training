# Set 2 Forensics Challenges


- Initially the file will be encrypted.
- Use frcrack Zip to crack the Password.

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/91.jpeg?raw=true)
![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/92.jpeg?raw=true)

### B Challenge

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/97.jpeg?raw=true)

#### Installation

```
$ sudo apt install binwalk
```


#### Usage

```
$ binwalk -e <file-name>
$ binwalk -e 1.jpg
```

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/93.jpeg?raw=true)

- Here in the above image, we see that there is a jpeg image and a ZIP in it and we see that, it is embedded within the jpeg image file.
- To extract it we can make use of a carving tool dd.
- It can carve out data from specific offsets that are passed as arguments to the tool along the with the file that needs to be read.

```
$ dd if=<filename> of=<filename> bs=1 skip=<offset>
```

- `if = the file from which data has to be extracted is passed as an argument.`
- `of = has the name of the file that we give after extraction.`
- `skip = is the offset of the file that has to be read.`
- `bs = i the byte skip argument that specifies the frequency of reading data from the given file.`


![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/94.jpeg?raw=true)

- If we try to extract all files we will get a `Zip File`.

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/95.jpeg?raw=true)

- Now we get the `flag` inside the Image.

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/96.jpeg?raw=true)

```
Flag --> inctf{fr33dom_w4s_n0t_w0n_0v3rnit3}
```

### E Challenge

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/98.jpeg?raw=true)

- Here when we analyze using `bin walk` we cant find anything. 
- So Next option is to look into the `Hex Dump`.

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/99.jpeg?raw=true)

- Online Tool --> https://hexed.it/

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/100.jpeg?raw=true)

- Here at last we shall see that there are some `Hex Encrypted Text`.

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/101.jpeg?raw=true)

- We have to decode it to get the `ASCII` Text.

```
696e6374667b337831663730304c5f69735f673030645f215f67756573735f2121217d
```

- Online Tool --> https://www.convertstring.com/EncodeDecode/HexDecode

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/102.jpeg?raw=true)

```
Flag --> inctf{3x1f700L_is_g00d_!_guess!!!}
```

### S Challenge

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/103.jpeg?raw=true)

- When we analyze using `bin walk` we cant find anything. 
- So Next option is to look into the `Hex Dump`.
- Online Tool --> https://hexed.it/

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/104.jpeg?raw=true)

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/100.jpeg?raw=true)

- Here at last we shall see that there are some `Base 64 Encrypted` text.

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/105.jpeg?raw=true)

- We have to decode it to get the `ASCII Text`.

```
aW5jdGZ7c3RyaW5nc19hcmVfdXNlZnVsfQ==
```

- Online Tool --> https://www.base64decode.org/

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/106.jpeg?raw=true)

```
Flag --> inctf{strings_are_useful}
```

### S_H Challenge

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/107.jpeg?raw=true)

- When we analyze using `bin walk` we cant find anything. 
- So Next option is to look into the `Hex Dump`.
- Online Tool --> https://hexed.it/

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/108.jpeg?raw=true)

- Here at last we shall see that there are some Hex Encrypted Text.

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/109.jpeg?raw=true)

- We have to decode it to get the ASCII Text.

```
526d7868636d564a626c526f5a5568766247554b
```

- Online Tool --> https://www.rapidtables.com/convert/number/hex-to-ascii.html

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/110.jpeg?raw=true)

- We shall see that there are some Base 64 Encrypted text.
- We have to decode it to get the ASCII Text.

```
RmxhcmVJblRoZUhvbGUK
```

- Online Tool --> https://www.base64decode.org/

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/111.jpeg?raw=true)

```
FlareInTheHole
```

- We shall understand that this is an Password for the file.
- Now if we try to extract with **StegHide** we shall extract the hidden file.

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/112.jpeg?raw=true)

[Click me to view the File](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/flag.txt)

```
Flag --> inctf{1_l0ve_c0unt3r_str1ke_1.6}
```

### Z Challenge

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/114.jpeg?raw=true)

- We can see that there is an `QR Code`.
- We shall get the `flag` if we decode it.
- Zbarimg is a tool used to scan and decode QR codes from image files

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/113.jpeg?raw=true)

#### Installation

```
$ sudo apt-get install zbar-tools
```

#### Usage

```
$ zbarimg <file-name>
```

```
Flag --> flag{N0w_y0u_a_little_about_zbarimg}
```

### SS Challenge

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/115.jpeg?raw=true)

- In this challenge we shall use the `StegSolve Tool` to decode the `Hidden text`.
- `Stegsolve` is used to `analyze images` in `different planes` by taking off `bits` of the image.

#### Installation

```
$ wget http://www.caesum.com/handbook/Stegsolve.jar -O stegsolve.jar
$ chmod +x stegsolve.jar
$ mkdir bin
$ mv stegsolve.jar bin/
```

#### Usage

- `Stegsolve` can be invoked by placing the image in the `/bin` folder and running stegsolve.

```
$ java -jar stegsolve.jar
```

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/116.jpeg?raw=true)

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/117.jpeg?raw=true)

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/118.jpeg?raw=true)

```
Flag --> pctf{st3gs0lv3_1s_u53ful}
```

### FS Challenge

- The given `PNG` shows error since its `hex dumps` are in wrong format.

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/119.jpeg?raw=true)

- So we have to edit the `Hex Chunks`.
- Online Tool --> https://hexed.it/

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/d0e0757f2c0bfa48732ccf712da95ad9a948a2f0/Forensics/Assets/120.jpeg?raw=true)

 - We have to edit the header and add extra `00` Bytes in that.

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/121.jpeg?raw=true)

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/122.jpeg?raw=true)

- Finally we get the `Flag`.

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/123.jpeg?raw=true)

```
Flag --> inctfj{4Ye@aRr4mbB4_u_g0T_m3!}
```

### Pattern Printing 1

[Pattern Printing 1](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/Pattern_1.sh)

```
#!/bin/bash

for(( i = 5 ; i > 0 ; i--))
do
	for(( j = 0 ; j < $i ; j++))
	do
		echo -n "*"
	done
	echo ""
	
done
```

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/128.jpeg?raw=true)


### Pattern Printing 2

[Pattern Printing 2](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/Pattern_2.sh)

```
#!/bin/bash

space=4
star=1
for(( i = 1 ; i <= 5 ; i++))
do
	for((j=0;j<space;j++))
	do
		echo -n " "
	done
	
	space=$(( space-1 ))
	
	for((j=0;j<$star;j++))
	do
		echo -n "*"
	done
	star=$(( star+2 ))
	echo ""
done
```

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/129.jpeg?raw=true)

### Revers Me

- Using the `Python Script` we can `reverse` the contents of the file.

```
filename = 'revers.me'
f = open("1.txt", "w")

with open(filename, 'rb') as fopen:
    line = fopen.read()
    line1 = line[::-1] 
    f.writelines(line1) 

f.close()
```

- Then we can `print` all `printable characters` from the File using `strings` command and `filter` the output using `grep`.

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/124.jpeg?raw=true)

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/127.jpeg?raw=true)

[Python File](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/1.py)

[Revers File](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/revers.me)

[Text File](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/1.txt)

[Bash Script File](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/1.sh)

```
Flag --> inctf{Y0u_ar3_g00d_4t_rev3rs1ng_1_gu3ss}
```

### Stranger Things

- `Download` the `Challenge` File.
- We shall `Extract` the `text` from the `file` using `strings` command.

```
Obviously, this is not the flag, but I can give you the flag format.
inctf{s0m3_l33t_str1ng}
PS: "inctf" in the flag is also case insensitive. Find three flags in the file.
```

- First try with `case sensitive` command.

```
strings find-flags-in-me | grep 'inctf'
```

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/130.jpeg?raw=true)

 - Now try with `case insensitive` command.

```
strings find-flags-in-me | grep -i 'inctf'
```

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/131.jpeg?raw=true)

- Now we have `Extracted` `Two` `Flags`.
- One more flag is there to be Extracted.
- Now lets try some random `Error and Trial Method` kind of thing.

```
#!/bin/sh
strings find-flags-in-me | grep -i 'i'
```

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/132.jpeg?raw=true)

- Lets `Replace` the `dots` with `Empty Space`.

```
tr "Character to be Replaced" "Replacement Character"

$ tr '.' ' '
```

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/133.jpeg?raw=true)

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/134.jpeg?raw=true)

- We shall see that there are Empty Spaces.
- So next lets try to `Remove` the `White Space`.
- [Reference](https://www.toolbox.com/tech/programming/question/sed-command-to-replace-whitespace-with-comma-032411/#:~:text=Simple%20SED%20commands%20are%3A,space%20with%20a%20single%20comma.)

```
sed 's/ //g'

$ tr '.' ' '
```

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/135.jpeg?raw=true)

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/136.jpeg?raw=true)

- Now lets try to `grep` for `flag` format.
- When we try with different `inctf` combinations we shall get some outputs.

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/138.jpeg?raw=true)

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/137.jpeg?raw=true)

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/139.jpeg?raw=true)

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/140.jpeg?raw=true)

- After trying some `combinations` we shall find that the flag is `scattered` in `different places`. 

```
#!/bin/sh

strings find-flags-in-me | grep -i 'ctf'

# s/ //g means to remove the whitespace
xxd find-flags-in-me | tr '.' ' ' | sed 's/ //g' | grep -i 'inc'

# grep -i is for case insensitive
xxd find-flags-in-me | tr '.' ' ' | sed 's/ //g' | grep -i 't'
```

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/142.jpeg?raw=true)

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/141.jpeg?raw=true)

[Bash Script](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/2.sh)

```
Flags :

inctf{y4yy!!!_found_th3_fir5t_fl4g}
InCtF{G00d_jobb!!This_is_the_2nd_on3}
inctf{th1s_1s_th3_l4st_0ne}
```

### Twins Challenge

- `Download` the `Challenge` Files.

```
I Hope These files are as same as twins. But find it yourself.
```

- Initially tried to `Analyze` through `various Tools` and found out that there are some differences in some `Byte``positions`.

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/159.jpeg?raw=true)

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/161.jpeg?raw=true)

- Then `finally` ended up with the `Bash` Script.

```
#!/bin/sh

f1=Twin1
f2=Twin2

size=$(stat -c%s $f1)
i=0
while [ $i -lt $size ]; do
  if ! r="`cmp -n 1024 -i $i -b $f1 $f2`"; then
    printf "%8x: %s\n" $i "$r"
  fi
  i=$(expr $i + 1024)
done
```

[Reference](https://stackoverflow.com/questions/12118403/how-to-compare-binary-files-to-check-if-they-are-the-same)

- This `output's` the `lines` with the `different` `bytes`. 
- But the `output` contains `offset` and other `informations` too.
- For my convenience I am `formatting` it to get the `proper flag`.
- We shall use the sed to remove the spaces between the `bytes` to properly get our `flag`.
- `sed 's/ //g'` does the `job`.

```
sed 's/ //g'
```

- After `Removing` the `white spaces` lets only `Display` the `Character` at the `Position` where the `Characters` are `Different`.
- `sed -e 's/\(^.*\)\(.$\)/\2/'`  `displays` only the `Last Character` of the `Line`.

```
sed -e 's/\(^.*\)\(.$\)/\2/'
```

- After making `several formats` in the `Bash Output` we get the `Flag` as expected.

```
#!/bin/sh

f1=Twin1
f2=Twin2

size=$(stat -c%s $f1)
i=0

echo -n "The Flag is : "

while [ $i -lt $size ]; do
  if ! r="`cmp -n 1024 -i $i -b $f1 $f2`"; then
    printf "%8x: %s\n" $i "$r" | sed 's/ //g' | sed -e 's/\(^.*\)\(.$\)/\2/' | tr '\n' ' ' | sed 's/ //g'
  fi
  i=$(expr $i + 1024)
done

echo ""
```

[Bash Script](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/4.sh)

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/160.jpeg?raw=true)

- One of the other way of finding the difference by `GUI` is with the `vimdiff` tool.
- [Reference](https://superuser.com/questions/125376/how-do-i-compare-binary-files-in-linux)


```
--> Converting to Hex

$ xxd Twin1 > Twin1.hex
$ xxd Twin2 > Twin2.hex
```

- Then Analyze using Vimdiff

```
$ vimdiff Twin1.hex Twin2.hex
```

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/143.jpeg?raw=true)

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/144.jpeg?raw=true)

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/145.jpeg?raw=true)

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/146.jpeg?raw=true)

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/147.jpeg?raw=true)

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/148.jpeg?raw=true)

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/149.jpeg?raw=true)

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/150.jpeg?raw=true)

- We shall see the `Comparisons` at each `Bytes`.
- Now lets Analyse the differences at `Each Byte` seperately using `xxd` and `grep` commands alike the previous challenge.

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/151.jpeg?raw=true)

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/152.jpeg?raw=true)

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/153.jpeg?raw=true)

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/154.jpeg?raw=true)

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/155.jpeg?raw=true)

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/156.jpeg?raw=true)


```
#!/bin/sh

xxd Twin1 > Twin1.hex
xxd Twin2 > Twin2.hex

xxd Twin1 | grep 0023b990
xxd Twin2 | grep 0023b990

echo ""

xxd Twin1 | grep 0023be20
xxd Twin2 | grep 0023be20

echo ""

xxd Twin1 | grep 0023c200
xxd Twin2 | grep 0023c200

echo ""

xxd Twin1 | grep 0023c640
xxd Twin2 | grep 0023c640

echo ""

xxd Twin1 | grep 0023c960
xxd Twin2 | grep 0023c960

echo ""

xxd Twin1 | grep 0023ce50
xxd Twin2 | grep 0023ce50

echo ""

xxd Twin1 | grep 0023d3c0
xxd Twin2 | grep 0023d3c0

echo ""

xxd Twin1 | grep 0023d830
xxd Twin2 | grep 0023d830

echo ""

xxd Twin1 | grep 0023dca0
xxd Twin2 | grep 0023dca0

echo ""

xxd Twin1 | grep 0023dfd0
xxd Twin2 | grep 0023dfd0

echo ""

xxd Twin1 | grep 0023e620
xxd Twin2 | grep 0023e620

echo ""

xxd Twin1 | grep 0023eab0
xxd Twin2 | grep 0023eab0

echo ""

xxd Twin1 | grep 0023f190
xxd Twin2 | grep 0023f190

echo ""

xxd Twin1 | grep 0023f6d0
xxd Twin2 | grep 0023f6d0

echo ""

xxd Twin1 | grep 0023fb90
xxd Twin2 | grep 0023fb90

echo ""

xxd Twin1 | grep 00240020
xxd Twin2 | grep 00240020
```

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/157.jpeg?raw=true)

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/158.jpeg?raw=true)

- Here we shall see that at `Each Byte position` `One` `letter` `Differs`.
- Now if we try to `Concatenate` all the characters at `Different` `Positions` then we shall get the `Final` `String`.

[Bash Script File](https://github.com/abhishekabi2002/Bi0s/blob/master/Forensics/Assets/3.sh)

```
Flag --> inctf{y0uGotm3}
```
