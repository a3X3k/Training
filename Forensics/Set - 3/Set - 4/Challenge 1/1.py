from binascii import hexlify

def repeating_key_xor(key, string):
    i = 0
    arr = []
    for ch in string:

        arr.append(ord(ch) ^ ord(key[i]))
        i += 1
        if (i == len(key)):
            i = 0
    return hexlify(bytearray(arr))


with open('xor.jpg','rb') as f:
	buff = f.read()

key = 'https://www.youtube.com/watch?v=_atw-zcQnL8'

encrypted = repeating_key_xor(key, buff)

hex_data = encrypted.decode("hex")

with open("final.jpg", "wb") as g:
    g.write(hex_data)
    g.close()