temp_product=1
list_to_store = list(map(int, input().split(" ")))
for data in list_to_store:
    temp_product*=data
print(temp_product)