def hollow_heart(rows):
    for i in range(rows//2, rows):
        for j in range(0, rows - i):
            print(" ", end=" ")
        for j in range(0, 2 * i + 1):
            if j == 0 or j == 2 * i or (i == rows//2 and j % 2 == 0):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        for j in range(0, (rows - i) * 2):
            print(" ", end=" ")
        for j in range(0, 2 * i + 1):
            if j == 0 or j == 2 * i or (i == rows//2 and j % 2 == 0):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    for i in range(rows):
        for j in range(0, 2 * rows - i):
            print(" ", end=" ")
        for j in range(0, 4 * i + 1):
            if j == 0 or j == 4 * i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# Example usage
hollow_heart(6)
