s=input()
length=len(s)
f1=0
f2=0
f3=0
f4=0
if(s[length-4]=='.'):
    f1=1

if(f1==1):
    extension=s[length-3:length]
    #print(extension)
    if extension.isalpha():
        f2=1

pos=0
str=""
if(f1==1 and f2==1):
    for i in range(len(s)):
        if(s[i]=='@'):
            pos=i
    domain=s[pos+1:length-4]
    temp_len=len(domain)
    c1=0
    c = 0
    for i in domain:
        if(i.isalpha() or i.isnumeric()):
            if (i.isalpha()):
                    c=c+1
        else:
            c1+=1
    if(c1>2):
        f3=1
    if(c1<2 and c1!=0):
        if (domain[0]=='-' and domain[temp_len-1]=='-'):
                f3=0
        elif(domain[0]=='-'):
                f3=0
        elif(domain[temp_len-1]=='-'):
                f3=0
        else:
            f3=1
    if(c==0):
        f3=1

if(f1==1 and f2==1 and f3==0):
        local_part=s[0:pos]
        if(len(local_part)>64):
            f4=1
        if(f4==0):
            for i in local_part:
                if(i.isalpha() or i.isnumeric()):
                    f4=0
                elif(i=='!' or i=='#' or i=='$' or i=='%' or i=='^' or i=='&' or i=="*" or i=='{' or i=='}'):
                    f4=0
                elif(i=='|' or i=='~' or i=='_' or i=='+' or i=='-' or i=='=' or i=='/' or i=="'" or i=='.'):
                    f4=0
                else:
                    f4=1
                    break
        if(local_part[0]=='.' or local_part[pos-1]=='.'):
            f4=1

if(f1==1 and f2==1 and f3==0 and f4==0):
    print("True")
else:
    print("False")

