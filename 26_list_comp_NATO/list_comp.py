# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)

# print(new_list)

# range(1, 5)
# range_list = [n * 2 for n in range(1, 5)]
#
# print(range_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
upper_new_names = [name.upper() for name in names if len(name) > 5]
print(upper_new_names)
