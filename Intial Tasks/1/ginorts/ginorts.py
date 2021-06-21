lowercase=[]
uppercase=[]
oddnos=[]
evennos=[]

for i in sorted(input()):
    if i.isalpha():
        if i>='a' and i<='z':
            lowercase.append(i)
        else:
            uppercase.append(i)
    else:
        if int(i)%2==0:
            evennos.append(i)
        else:
            oddnos.append(i)

print("".join(lowercase+uppercase+oddnos+evennos))