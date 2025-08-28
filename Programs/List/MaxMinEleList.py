my_list = [12, 7, 19, 3, 25, 8]

# Initialize both max and min to the first element
max_value = my_list[0]
min_value = my_list[0]

for num in my_list:
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num

print("Maximum:", max_value)
print("Minimum:", min_value)
