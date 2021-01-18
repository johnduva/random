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

# list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

# the expression can contain conditions
newlist = [x if x != "banana" else "orange" for x in fruits]

# custom sort function
# (i.e. based on distance from 50)
def myfunc(n):
   return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)

# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
mylist = thislist.copy()

# unpacking a tuple
(green, yellow, red) = fruits

# unpacking using asterisk
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropical, red) = fruits

# shorthand 'if/else' statement
print("A") if a > b else print("B")
# three conditions
print("A") if a > b else print("=") if a == b else print("B")

# If you do not know how many arguments that will be passed into your function, 
# add '*' before the parameter name in the function definition
def my_function(*kids):
  print("The youngest child is " + kids[-1])

# If you do not know how many keyword arguments will be passed into your function, 
# add '**' before the parameter name in the function definition.
  

# class syntax
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()


