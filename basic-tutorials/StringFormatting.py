# https://www.learnpython.org/en/String_Formatting

# This prints out "Hello John"
name = "John"
print("Hello %s!" % name)

name = "John"
age = 23
print("%s is %d years old!" % (name, age))

mylist = [1,2,3]
print("A list: %s" % mylist)

myint = 123456789
print("myint: %d" % myint)
myint_as_hex_lowercase = "As lowercase hex: %x"
print(myint_as_hex_lowercase % myint)
myint_as_hex_uppercase = "As uppercase hex: %X"
print(myint_as_hex_uppercase % myint)

# Excercise
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s, your balance is $%.2f"

print(format_string % data)
