# Definition: A tuple is an ordered, immutable collection of items.

# Properties:
# Ordered
# Immutable
# Allows duplicate elements

myTuple = (1, 2.5, "Coders", 'a', 5, "Coders", "Coders")
anotherTuple = tuple(range(10))

# accessing elements in tuples
print(myTuple[0])
print(myTuple[1:3])
print(myTuple[-2])

# Operations on Tuples
# 1) Concatenating of 2 tuples using + operator
tuple1 = (1,2,3)
tuple2 = (4,5,6)
resultTuple = tuple1 + tuple2
print(resultTuple)

# 2) Repetition of tuples
originalTuple = (1,2,3)
repeatedTuple = originalTuple * 3
print(repeatedTuple)

# 3) Membership of element in a tuple
sampleTuple = (1,2,3,4,5)
print(3 in sampleTuple)
print(10 in sampleTuple)
print(3 not in sampleTuple)
print(10 not in sampleTuple)

# Length of a tuple
Length = len((1,2,3,4,5,8,6))
print(Length)

# Indexing (Finding the index of an element in a tuple)
index = myTuple.index("Coders")
print(index)

# Counting (Counting the number of occurance of an element in a tuple)
count = myTuple.count("Coders")
print(count)

# Note - There are only 2 inbuilt tuple functions - index and count
# why? - because tuples are immutable, they cannot be modified
# sooo we have a very limited options in tuples

# Once the Tuple is created u cannot change anything into it
# This is Tuples

# Bonus Concept!!! - IMPORTANT - TUPLE UNPACKING!!!
# Tuple unpacking, assigning the values from a tuple to various different variables in one single line!
nums1 = (1,2,3)
a,b,c = nums1
print("After Unpacking 1!")
print(a)
print(b)
print(c)

nums2 = (4,5,6)
i,_,k = nums2 # Here _ is a dummy variable
print("After Unpacking 2!")
print(i)
print(k)

nums3 = (1,2,3,4,5,6,7,8,9,10)
a,b,c,*rest = nums3
print(a)
print(b)
print(c)
print(rest)

# Swapping two numbers using tuple unpacking!
x = 5
y = 10

print(f"Before swapping x = {x}, y = {y}")
x, y = y, x
print(f"Before swapping x = {x}, y = {y}")

