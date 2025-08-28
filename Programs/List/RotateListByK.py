# Rotate a list by k steps (e.g. [1,2,3,4,5] → [4,5,1,2,3]).

def rotate_list(lst, k):
    n = len(lst)
    k = k % n  # Handle cases where k > length
    return lst[-k:] + lst[:-k]

# Example
original = [1, 2, 3, 4, 5]
rotated = rotate_list(original, 1)
print(rotated)  # Output: [4, 5, 1, 2, 3]
