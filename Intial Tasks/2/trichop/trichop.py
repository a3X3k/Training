a,b,r=input().split()
m=int(input())
ls=list(map(int,input().split()))
count_of_triangles=0
a=int(a)
b=int(b)
for i in ls:
      if((a+b)>i and (b+i)>a and (a+i)>b):
                count_of_triangles=count_of_triangles+1

if(count_of_triangles>=int(r)):
        print(count_of_triangles)
        print("Natsu")
else:
        print(count_of_triangles)
        print("Grey")