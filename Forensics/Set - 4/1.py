from pwn import *
import base64

print(message)
c = remote('159.65.156.133', 1337)
while(1):
    a = str(c.recvline())
    b = ""
    print(a)
    if (a.find("Decode") != -1):
        result = a.index(': ')
        print("String : {}".format(a[result+2:-3]))
        b += a[result+2:-3]

        if b[0].isalpha():
            b = b.encode('ascii')
            b = base64.b64decode(b)
            b = b.decode('ascii')
        b += "\n"
            b = bytes(b, 'utf-8')
            print(b)
            c.send(b)

    elif b[1] == 'x':
        a = ""
           for i in b:
                if i != '0' and i != 'x' and i != ' ':
                    a += i
            a = bytes.fromhex(a)
            a = a.decode("ASCII")
            a += "\n"
            a = bytes(a, 'utf-8')
            print(a)
            c.send(a)

        elif b[2] != '0' and b[2] != '1':
            a = ""
            for i in b:
                if i != '0':
                    a += i
                b = ""
        for i in a.split(" "):
            b += chr(int(i, 8))
        b += "\n"
           b = bytes(b, 'utf-8')
            print(b)
            c.send(b)
        else:
            b = b.split()
        a = ""
        for i in b:
            c = int(i, 2)
            c = chr(c)
            a += c
        a += "\n"
           a = bytes(a, 'utf-8')
            print(a)
            c.send(a)

    else:
        continue
