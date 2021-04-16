# Crypto Hack

### INTRODUCTION
&nbsp;
| Challenge No | Challenge Name |
| ------ | ------ |
| **1** | Finding Flags |
| **2** | Great Snakes |
| **3** | Network Attacks |
&nbsp;
### Finding Flags

- As mentioned just paste the flag **crypto{y0ur_first_fl4g}** as an answer.

![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/4.jpeg?raw=true)

##### Flag = crypto{y0ur_first_fl4g}
&nbsp;
### Great Snakes

![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/3.jpeg?raw=true)

- Just we need to run the python program to get the flag and the python version is python3 which is mentioned in the challenge. 

```sh
$ python3 filename
$ File Name = 1.py
$ python3 1.py
```

![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/1.jpeg?raw=true)

##### Flag = crypto{z3n_0f_pyth0n}
&nbsp;

### Network Attacks

- Download the file whihc is mentioned in the challenge or connect using netcat.
```sh 
$ nc socket.cryptohack.org 11112
```
- As mentioned change the JSON object with the key buy and value flag in **line 31**.
&nbsp;
![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/9.jpeg?raw=true)

![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/10.jpeg?raw=true)

- Now run the Program.

```sh
$ python3 filename
$ File Name = 2.py
$ python3 2.py
```

##### Flag = crypto{sh0pp1ng_f0r_fl4g5}
&nbsp;

## GENERAL
#### Encoding
&nbsp;

| Challenge No | Challenge Name |
| ------ | ------ |
| **1** | ASCII |
| **2** | Hex |
| **3** | Base64 |
| **4** | Bytes and Big Integers |
&nbsp;

### ASCII 

![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/7.jpeg?raw=true)
- Just convert the ASCII into Characters either using ASCII table or Online Tool https://www.dcode.fr/ascii-code

##### Flag = crypto{ASCII_pr1nt4bl3}
&nbsp;

### Hex

![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/8.jpeg?raw=true)

- As we know, a byte contains 8 bits. Therefore, we need two hexadecimal digits to create one byte.
- First of all, we'll convert each hexadecimal digit into binary equivalent separately.
- And then, we need to concatenate the two four bit-segments to get the byte equivalent
- We need to check if the length of the hexadecimal String is an even number. 
- This is because a hexadecimal String with odd length will result in incorrect byte representation.
- Now, we'll iterate through the array and convert each hexadecimal pair to a byte.
- Use online tool https://www.scadacore.com/tools/programming-calculators/online-hex-converter/ to decode it.

![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/11.jpeg?raw=true)

##### Flag = crypto{You_will_be_working_with_hex_strings_a_lot}
&nbsp;

### Base64

![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/12.jpeg?raw=true)

- First convert Hexadecimal to Bytes using Online Tool https://www.alterlinks.com/byte-converter/byte-converter.php

```sh
$ Hex - 72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf
$ Bytes - 564501339853374515179229284425
```

- Then convert Bytes to base64

```sh
$ Bytes - 564501339853374515179229284425
$ Base64 - crypto/Base+64+Encoding+is+Web+Safe/
```

- Use https://cryptii.com/pipes/binary-to-base64 Online Tool to directly convert Hex to Base64.

![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/13.jpeg?raw=true)

##### Flag - crypto/Base+64+Encoding+is+Web+Safe/
&nbsp;

### Bytes and Big Integers

![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/16.jpeg?raw=true)

- Simply convert long to byte with the respectively function to get the flag.

```sh
from Crypto.Util.number import bytes_to_long
from Crypto.Util.number import long_to_bytes
data = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
bytes = long_to_bytes(data)
print(bytes)
```

![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/15.jpeg?raw=true)

```sh
$ python3 filename
$ File Name = 3.py
$ python3 3.py
```

![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/14.jpeg?raw=true)

##### Flag - crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}
&nbsp;

### XOR

| Challenge No | Challenge Name |
| ------ | ------ |
| **1** | XOR Starter |
| **2** | XOR Properties |
| **3** | Favourite Byte |
| **4** | You either know, XOR you don't |
| **5** | Lemur XOR |

### XOR Starter

![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/17.jpeg?raw=true)

- Convert Char to Decimal.
- Convert Decimal to Binary.
- Now XOR with decimal 13 whose Binary equivalent is 00001101

&nbsp;
#### XOR Table
&nbsp;
| A | B | A XOR B |
| - | - | - | 
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 | 
| 1 | 1 | 0 |

&nbsp;

```sh

Original String - label
Characters Of String To Decimal - 108 097 098 101 108
Decimal To Binary - 01101100 01100001 01100010 01100101 01101100

## XOR OPERATION

01101100
00001101
--------
01100001
--------

01100001
00001101
--------
01101100
--------

01100010
00001101
--------
01101111
--------

01100101
00001101
--------
01101000
--------

01101100
00001101
--------
01100001
--------

Binary after Xoring with (13) 00001101 --> 01100001 01101100 01101111 01101000 01100001

Binary To Decimal - 097 108 111 104 097

Decimal to ASCIi - aloha
```

- Use https://www.branah.com/ascii-converter to convert using Online Tool.

##### Flag - crypto{aloha}
&nbsp;

### XOR Properties

![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/18.jpeg?raw=true)

- There is a built-in function which converts the Hex Stringg into Byte Array.

```sh
$ bytes.fromhex(hex_string)  # Python ≥ 3
--> b'\xde\xad\xbe\xef'
$ bytearray.fromhex(hex_string)
--> bytearray(b'\xde\xad\xbe\xef')

It returns a bytearray and it reads hex strings with or without space separator.
```

![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/20.jpeg?raw=true)

```sh
$ xor(ByteArray1, ByteArray2)
It xors two Byte Array and returns the result.
```

```sh
$ from pwn import xor

$ key1 = bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
--> Converting Hex to Byte Array

$ xor_of_key2_key3 = bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
--> Converting Hex to Byte Array

$ flag_of_key1_key2_key3= bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')
--> Converting Hex to Byte Array

$ xor_of_key1_key2_key3= xor(key1, xor_of_key2_key3) 
--> This xors the key1 and key2 and key3

$ flag = xor(flag_of_key1_key2_key3, xor_of_key1_key2_key3)
--> This xors the result of XOR (key1,key2,key3) and XOR (XOR (key1,key2,key3,flag),XOR (key1,key2,key3))

$ print(flag)
--> This prints the Flag
```

```sh
$ python3 filename
$ File Name = 4.py
$ python3 4.py
```

![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/21.jpeg?raw=true)

##### Flag - crypto{crypto{x0r_i5_ass0c1at1v3}

&nbsp;

### Favourite Byte

![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/19.jpeg?raw=true)

- First step is to decode from Hex.
```sh
$ bytes.fromhex(hex_string)  # Python ≥ 3
--> b'\xde\xad\xbe\xef'
$ bytearray.fromhex(hex_string)
--> bytearray(b'\xde\xad\xbe\xef')

--> It returns a bytearray and it reads hex strings with or without space separator.

$ xor(ByteArray1, ByteArray2)
--> It xors two Byte Array and returns the result.
```

- The Single-byte XOR cipher algorithm works with an encryption key of size 1 byte - which means the encryption key could be one of the possible 256 values of a byte.
- We iterate through the encrypted message bytewise and XOR each byte with the encryption key - the resultant will be the original message.
```sh
$ from pwn import xor

$ string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
$ a = bytes.fromhex(string)

for i in range(256):
    x = xor(i, a)
    if "crypto" in str(x):
    	print(x)
```
![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/23.jpeg?raw=true)

```sh
$ python3 filename
$ File Name = 5.py
$ python3 5.py
```

![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/22.jpeg?raw=true)

##### Flag - crypto{0x10_15_my_f4v0ur173_by7e}

&nbsp;

### You either know, XOR you don't

![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/25.jpeg?raw=true)

- First step is to decode from Hex.
```sh
$ bytes.fromhex(hex_string)  # Python ≥ 3
--> b'\xde\xad\xbe\xef'
$ bytearray.fromhex(hex_string)
--> bytearray(b'\xde\xad\xbe\xef')

--> It returns a bytearray and it reads hex strings with or without space separator.

$ xor(ByteArray1, ByteArray2)
--> It xors two Byte Array and returns the result.
```

```sh
$ from pwn import xor
$ data = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

$ print(xor(data,"crypto{".encode())) #output - myXORke+y_Q\x0bOMe$~seG8bGURN\x04FWg)a|\x1dM!an\x7f
$ print(xor(data, "myXORkey".encode()))
```

- The string encode() method returns encoded version of the given string. 
- Since Python 3.0, strings are stored as Unicode, i.e. each character in the string is represented by a code point. 
- So, each string is just a sequence of Unicode code points.

```sh
$ python3 filename
$ File Name = 6.py
$ python3 6.py
```

![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/24.jpeg?raw=true)

##### Flag - crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}

&nbsp;

### Lemur XOR

![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/40.jpeg?raw=true)

- Since two images are given we can have a wild guess that we have to XOR both the images.
- For that we have a tool called Stegsolve.

#### Installation
```
wget http://www.caesum.com/handbook/Stegsolve.jar -O stegsolve.jar

chmod +x stegsolve.jar

mkdir bin

mv stegsolve.jar bin/
```

- Move the two images to the **bin** Folder.

 ![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/41.jpeg?raw=true)
![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/42.jpeg?raw=true)

#### Usage

- Stegsolve can be invoked by placing the image in the /bin folder and running stegsolve.

```
`$ java -jar stegsolve.jar`
```

![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/43.jpeg?raw=true)

- The XOR the images by selecting **Analyze** option from **Toolbar**.

![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/44.jpeg?raw=true)

