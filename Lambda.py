# In Python, an anonymous function is a function that is defined without a name.
# While normal functions are defined using the def keyword in Python.
#  anonymous functions are defined using the lambda keyword.

# Syntax: 
# lambda arguments: expression .
# NOTE: Lambda functions can have any number of arguments but only one expression. The expression is evaluated and returned. 

##  Program to show the use of lambda function 
# Double = lambda x : x*2
# print(Double(5))
# ------------------------------

# NOTE Use of Lambda Function in python:
# We use lambda functions when we require a nameless function for a short period of time.
# In Python, we generally use it as an argument to a higher-order function (a function that takes in other functions as arguments).
#  Lambda functions are used along with built-in functions like filter(), map() etc

# NOTE: Example use with filter()
# The filter() function in Python takes in a function and a list as arguments.

# The function is called with all the items in the list and a new list is returned which contains items for which the function evaluates to True.

# Here is an example use of filter() function to filter out only even numbers from a list.
# list_a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]   # List_a as a list of Integer number

# even = list(filter(lambda x : (x % 2 == 0),list_a))

# print(even)

# Result will be : [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# --------------------------------------------------------------
# odd = list(filter(lambda x : (x % 2 != 0),list_a))

# print(odd)

# Result will be :  [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# -----------------------------------------------------------------

# NOTE : Example use with map()
# The map() function in Python takes in a function and a list.

# The function is called with all the items in the list and a new list is returned which contains items returned by that function for each item.

# Here is an example use of map() function to double all the items in a list.

num = [i for i in range(1,11)] # Create a list using range function inside a list
table = list(map(lambda x : x * num, num ))
print(table(5))

