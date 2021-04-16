# The Cryptopals Crypto Challenge Set 1
&nbsp;

| Challenge No | Challenge Name |
| ------ | ------ |
| **1** | Convert hex to base64 |
| **2** | Fixed XOR |
| **3** | Single-byte XOR cipher |
| **4** | Detect single-character XOR |
| **5** | Implement repeating-key XOR |
| **6** | Break repeating-key XOR |
| **7** | AES in ECB mode |
| **8** | Detect AES in ECB mode |

### Convert hex to base64

![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/28.jpeg?raw=true)

```sh
--> Convert hex to base64 using Online Tool. 
```

- **Online Tool** --> https://base64.guru/converter/encode/hex

![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/26.jpeg?raw=true)

### Fixed XOR

![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/27.jpeg?raw=true)

- First step is to decode from Hex.
```sh
$ bytes.fromhex(hex_string)

--> It returns a bytearray and it reads hex strings with or without space separator.

$ xor(ByteArray1, ByteArray2)
--> It xors two Byte Array and returns the result.
```

```sh
$ from pwn import xor

$ key1 = bytes.fromhex('1c0111001f010100061a024b53535009181c')
$ key2 = bytes.fromhex('686974207468652062756c6c277320657965')

$ flag = xor(key1, key2).hex()
print(flag)
```

![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/29.jpeg?raw=true)

```sh
$ python3 filename
$ File Name = 7.py
$ python3 7.py
```

### Single-byte XOR cipher
![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/34.jpeg?raw=true)

- First step is to decode from Hex.
```sh
$ bytes.fromhex(hex_string)

--> It returns a bytearray and it reads hex strings with or without space separator.

$ xor(ByteArray1, ByteArray2)
--> It xors two Byte Array and returns the result.
```

![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/31.jpeg?raw=true)

```sh
$ from pwn import xor

$ string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
$ a = bytes.fromhex(string)

$ for i in range(256):
    x = xor(i, a)
    print(x)
```

```sh
$ python3 filename
$ File Name = 8.py
$ python3 8.py
```

![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/33.jpeg?raw=true)
![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/32.jpeg?raw=true)

&nbsp;

### Detect single-character XOR

![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/45.jpeg?raw=true)

- This is same as the **Previous Question**.
-  First step is to decode from Hex.

```sh
$ bytes.fromhex(hex_string)

--> It returns a bytearray and it reads hex strings with or without space separator.

$ xor(ByteArray1, ByteArray2)
--> It xors two Byte Array and returns the result.
```

```sh
from pwn import xor

filename = 'xor.txt'

for line in open(filename, 'r'):
    a = bytes.fromhex(line.strip())
    
    for i in range(256):
        x = xor(i, a)
        print(x)
```
![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/46.jpeg?raw=true)

```sh
$ python3 filename
$ File Name = xor.py
$ python3 xor.py
```
![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/47.jpeg?raw=true)

- Here **Piping ( | )** is used to send the output to another destination.
- We use **grep** which is a command line utility for searching plain-text data for lines which matching a regular expression.

```sh
$ grep -v string

$ grep -v \x 

\x --> Eliminates Hex Outputs
```

- **-v** displays the line only which does'nt match the string specified.
- Thus we eliminate the hex output which are not necessary.
- **Reference -->** https://www.tecmint.com/linux-grep-commands-character-classes-bracket-expressions/#:~:text=grep%20is%20a%20command%20line,the%20screen%20i.e.%20standard%20output.

**Output :** b' Now that the party is jumping\n'

### Implement Repeating Key XOR

![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/38.jpeg?raw=true)

```sh
# Hexlify is used here for converting bytes to hex
from binascii import hexlify

def repeating_key_xor(key, string):
    # i is the position within the key
    i = 0
    arr = []
    for ch in string:
    	# Convert the key char and the plaintext char to
        # integers using `ord`, XOR them and add them to
        # the array.
        arr.append(ord(ch) ^ ord(key[i]))
        
		# Manage the "repeating" part of the repeating key.
        # If the end of the key is reached start back at the
        # beginning.
        i += 1
        if (i == len(key)):
            i = 0

	# Finally convert our array to a byte array (which
    # hexlify likes), then convert to hex and return it.
    return hexlify(bytearray(arr))

string = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
key = 'ICE'

encrypted = repeating_key_xor(key, string)
print(encrypted)
```

```sh
$ python3 filename
$ File Name = 9.py
$ python3 9.py
```

![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/39.jpeg?raw=true)

### AES in ECB mode

![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/36.jpeg?raw=true)

```sh

--> Import base64 and other packages related to Crypto

$ import base64
$ from Crypto.Cipher import AES

$ def decrypt_ecb_cipher(ciphertext, key): 
	cipher = AES.new(key, AES.MODE_ECB) 
	plaintext = cipher.decrypt(ciphertext) 
	return plaintext

$ def main():
	key = b'YELLOW SUBMARINE'
	
--> We call base64.b64decode method to decode the base64_bytes into the ciphertext variable. 

	with open('1.txt') as fh: 
		ciphertext = base64.b64decode(fh.read()) 
	message = decrypt_ecb_cipher(ciphertext, key) 
	print (message)

$ if _name_ == '_main_':
	main()
```

![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/37.jpeg?raw=true)

```sh
$ python3 filename
$ File Name = 10.py
$ python3 10.py
```

![Drag Racing](https://github.com/abhishekabi2002/Bi0s/blob/master/Cryptography/Assets/40.jpeg?raw=true)
