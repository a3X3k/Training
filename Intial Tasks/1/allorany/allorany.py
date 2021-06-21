s1=0
s2=0
l = list(map(int,input().split()))
for i in l:
    if(i<0):
        s1=1
    if i>0 and i<10:
        s2=1
        
if s1==1:
    print("False")
if s2==1 and s1!=1:
    print("True")
if s1!=1 and s2!=1:
    for i in l:
        temp = i
        rev=0
        while(i>0):
            mod=i%10
            rev=rev*10+mod
            i=i//10
        if(rev==temp):
            print("True")
            temp=1
            break
if s1!=1 and s2!=1 and temp!=1:
    print("False")
        