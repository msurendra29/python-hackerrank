n = int(input())
array_of_ints = input().split()
array_of_ints = [int(i) for i in array_of_ints]
temp_list = []
for i in array_of_ints:
    if ((i in set(array_of_ints)) and (i not in temp_list)):
        temp_list.append(i)
temp_list.sort()
print(temp_list[len(temp_list) - 2])   
