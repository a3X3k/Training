def find_factor_of_tribonocci(tot_sum):
    temp = 0
    for divisor in range(1,tot_sum+1):
        if(tot_sum % divisor == 0):
            temp+=1
    return temp

tot_factor = int(input())
first_num = 0
second_num = 0
third_sum = 1
tot_sum = 0

while(True):
    total_sum = first_num+second_num+third_sum
    if(find_factor_of_tribonocci(total_sum)>=tot_factor):
        break
    first_num = second_num
    second_num = third_sum
    third_sum = total_sum
print(total_sum)