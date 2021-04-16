n,m = [int(x) for x in input().split()]
marks=[]
fail_list=[]
dataset=[]
score_list=[]
for i in range(m):
        name=input()
        marks=list(map(int,input().split()))
        sum=0
        f=0
        for j in marks:
                if(j<40):
                        fail_list.append(name)
                        f=1
                        break
                else:
                        sum+=j

        if(f==0):
                dataset.append(name)
                dataset.append(sum)
                score_list.append(sum)

score_list.sort(reverse = True)
new_list=[]
k=1
for i in score_list:
        for j in range(len(dataset)):
                if(i==dataset[j]):
                        new_list.append(k)
                        new_list.append(dataset[j-1])
                        k=k+1
                        break
dictionary = {new_list[i]: new_list[i + 1] for i in range(0, len(new_list), 2)}
fail_list.sort()
print(dictionary)
print(fail_list)
#print(score_list)