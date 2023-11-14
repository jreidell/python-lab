# https://www.learnpython.org/en/Conditions

x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True

name = "John"
age = 23

if name == "John" and age == 23:
    print("Your name is John and your age is 23!")

if name == "John" or name =="Dick":
    print("You're either John or Dick!")

if name in ["John", "Dick"]:
    print("Yep, your name is either John or Dick!")


statement = False
another_statement = True
if statement is True:
    # do something
    print("statement is True!")
    pass
elif another_statement is True: # else if
    print("another_statement is True!")
    # do something else
    pass
else:
    # do another thing
    print("Something else!")
    pass


x = 2
if x == 2:
    print("x equals 2!")
else:
    print("x does not equal 2!")

x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False


print(not False) # Prints out True
print((not False) == (False)) # Prints out False

# Excercise
# change this code
number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")