string1,string2=input().split()

f1=0
for character in string1:
    f1+=ord(character)

f2=0
for character in string2:
    f2+=ord(character)

if(f1==f2):
    print("True")
else:
    print("False")