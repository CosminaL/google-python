import copy

list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

asc_ordered_list = list[::]

print(sorted(asc_ordered_list))
print(list)

desc_ordered_list = list[::]
print(sorted(desc_ordered_list, reverse=True))
print(list)

print(list[0::2])  # even index

print(list[1::2])  # odd index

# Method 1
new_list = []

for tmp in list:
    if (tmp % 3 == 0):
        new_list.append(tmp)

print(new_list)

# Method 2
new_list = [element for element in list if element % 3 == 0]
print(new_list)
