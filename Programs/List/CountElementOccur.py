# Count how many times an element appears in a list.

my_list = [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3]
target_value = 9

# Initialize counter to zero
count = 0

# Iterate through the list
for item in my_list:
    if item == target_value:
        count += 1

print(f"The number {target_value} appears {count} times")
# Output: The number 2 appears 4 times
