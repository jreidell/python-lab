# https://www.learnpython.org/en/Variables_and_Types

# Number can be either an int or a float
myint = 7
print(myint)

myfloat = 7.0
print(myfloat)

myfloat = float(7)
print(myfloat)

# Strings can be defined with a single or double quote
mystring = 'hello'
print(mystring)

mystring = "hello"
print(mystring)

# Double quotes allow you to use an apostrophe in the string
mystring = "Don't worry Nanook, the Crux of the Biscuit, is the apostrophe..."
print(mystring)

one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

a, b = 3, 4
print(a, b)

# # THIS WILL FAIL!
# one = 1
# two = 2
# hello = "hello"
# print(one + two + hello)

# Excercise
mystring = "hello"
myint = 20
myfloat = float(10)

if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Int: %i" % myint)

