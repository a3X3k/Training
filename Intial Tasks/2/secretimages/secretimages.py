images = list(map(str,input().split()))
c1=0
c2=0
c3=0
for i in range(len(images)):
    length=len(images[i])
    key=images[i][length-2]
    if (key == 'n'):
        c1 = c1 + 1
    if (key == 'm'):
        c2 = c2 + 1
    if (key == 'e'):
        c3 = c3 + 1

print(c1,end =" ")
print(c2,end =" ")
print(c3)
