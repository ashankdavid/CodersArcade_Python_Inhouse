def are_disjoint(a, b):
    # a and b are Python sets (or any iterables)
    for x in a:
        for y in b:
            if x == y:
                return False
    return True

# Examples
set1 = {1, 2, 3}
set2 = {4, 5}
set3 = {3, 7}

print(are_disjoint(set1, set2))  # True
print(are_disjoint(set1, set3))  # False
