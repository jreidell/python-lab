# Arithmetic - order of operations = *, /, +
number = 1 + 2 * 3 / 4.0
print(number)

# Modulo % returns the integer remainder of the division. dividend % divisor = remainder
remainder = 11 % 3
print(remainder)

# Two multiplication symbols makes a power relationship
squared = 7 ** 2
cubed = 7 ** 3
print(squared)
print(cubed)

# Using Operators with Strings
helloworld = "hello" + " " + "world"
print(helloworld)

# Python supports mutliplying strings to repeat a sequence (useful for delimited strings)
lotsofhellos = "hello," * 10
print(lotsofhellos)

# Lists can be joined with the addition operator (+)
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = even_numbers + odd_numbers
print(all_numbers)

# Lists can also use the multiplication operator to create a repeating sequence
print([1,2,3] * 3)

# Excercise
x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")