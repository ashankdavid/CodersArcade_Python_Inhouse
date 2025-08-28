# Here’s another way, modifying the original list (if permitted):

original_list = [1, 2, 3, 4, 5]
reversed_list = []
while original_list:
    reversed_list.append(original_list.pop())
print(reversed_list)  # Output: [5, 4, 3, 2, 1]
