# Implicit Typecasting
i = 10
j = 20.5
Sum = i + j
print(Sum)

'''
In the above line of code you saw that we started from int val
and ended up getting a float value, this is were the type got
converted from 1 type to another this is called is Implicit
Type Casting
'''

# Explicit Typecasting
name = "Preeti"
rollNo = 123
print("My name is " + name + " and my RollNo is: " + str(rollNo))
'''
In the above program, there are two variables, one is string ans another
is integer, soo now when we are printing, the names and rollno together
the name works because we are concatenating the name which is string with
string soo it works, but when we did the contatenation of rollNo with the string
it gave us an error!, why this happened?? => because the interpretor
cannot convert the integer to a string automatically, hence implicit 
typecasting cannot be done here, soo now we need to apply Explicit Typecasting!
'''
