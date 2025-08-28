# Reverse a list without using reverse() or slicing. in python

original_list = [1, 2, 3, 4, 5]
reversed_list = []
for item in original_list:
    reversed_list.insert(0, item)
print(reversed_list)  # Output: [5, 4, 3, 2, 1]
