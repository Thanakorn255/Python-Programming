from itertools import count


num = int(input())
num_list = []
count = 0
while count < num:
    add_num = int(input())
    num_list.append(add_num)
    count += 1
print(min(num_list))
print(max(num_list))
