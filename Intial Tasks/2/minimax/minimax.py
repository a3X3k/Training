main_list=list(map(int,input().split()))

sum_term=0
for data in main_list:
    sum_term+=data

main_list.sort()
print(sum_term-main_list[len(main_list)-1],end=' ')
print(sum_term-main_list[0])
