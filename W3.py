# W3 School Python Review

# set multiple variables in one line
x, y, z = 1, 2, 3

# set single value to multiple variables in one line
x = y = z = "Orange"

# set variables to list elements 
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

# concatenate string and variable
print("Python is " + x)

# concatenate strings
x = "Python is "
y = "awesome"
z =  x + y

#Note: python has no char datatype: individual letters are just strings of length 1 
 
# loop through a string (as opposed to looping through a list)
for x in "banana”:
  ...

# check if a string is in another string
if "free" in str: 
  ...

# replace() method
a = "Hello, World!"
print(a.replace("H", "J"))

# format() method
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# exponent
x ** y

# floor division
x // y
