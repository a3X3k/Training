a=[]
b=[]
s=input()
s1=s.replace(" ","")
l1 = list(s1)
l2=l1
for i in range(len(l1)):
        if (i%2!= 0):
                  b.append(l1[i])

b1=b[::-1]
k=0;
for i in range(len(l2)):
        if ((i)%2)!=0:
                l2[i]=b1[k]
                k=k+1

string = ''.join(map(str, l2))
print(string)


