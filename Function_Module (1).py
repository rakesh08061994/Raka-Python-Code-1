# NOTE Function Modules
# Any file that contains proper python code and has the .py extention can be called a python module.
# Modules contain statements and defination. They usually contain arbitrary objects such as classes, functions, files, attributes,
#  and commonpython statements These objects can be accesses by the importing them. Modules help breakdown large files into managable files.
#  They also promote code reuseability

# Modules are  kown as main .py file name : Example here multiplier.py python file contain multiply, addition, substract, Division, Mod function
# Now multiplier without .py extention known as module as these multiply, addition, substract, division, called as collection of function 
# inside multiplier main module
#  we can access modue to importing them with  (import module name), and to access there function we use . (dot) and argument after module name.

#import module_name
#module_name.function_name(Arguments)

# ----------------------------------------------------------------------------------------------------------------------------------
# NOw we create a module name ganit and mke some ganit function
# NOTE:

# import multiplier                   # made a python module file name is multiplier.py
# print(multiplier.addition(5, 4))    # Use there functions
# print(multiplier.mod(10))
# ------------------------------------------------------------

# from multiplier import multiplication       # Import only specific function from module 
# print(multiplication(5, 10))


# ------------------------------------------------------------

# from multiplier import *                                                                # Import all functions use in one line statement 
# print(multiplication(5, 10) + addition(5, 5) + mod(5) + substract(10, 3))               # Call all module function at one statement


# ------------------------------------------------------------
# to show content list of an module after importing it
# import multiplier
# # print(dir(multiplier)) # Direct print or can store output in a variable
# a = dir(multiplier)
# print(a) 

# # To show contant of list functions and items
# print(dir(multiplier.addition))
# print(multiplier.addition.__doc__)

# ----------------------------------------------------------------------------------
# import math

# help(math)      # Get help about math module after importing it
# help(math.factorial)    # Get help about math modules specific functions

# ---------------------------------------------------------------------------------------------------------------------------------------

# NOTE # Now we try some modules

import random
# help(random) # Get help about random module
# print(random.randint(1, 10))        # Generate a randowm integer number from specified given range(lowest, highest)
# a = random.choice(["Ram","Sita","Hanuman","Bharat","Laxman","Satrughan"])       # Choose random sequence from a list and can stored in a variable to print
# print(a)    # Print a

# print(random.choice(dir(random)))           # Can give access of list in sequence parameter of random.choice(sequence,list)

my_list = ['p','r','o','g','r','a','m','m','e']
print(random.shuffle(my_list))

# ---------------------------------------------------------------------------------------------------------------------------------------

# NOTE



# ---------------------------------------------------------------------------------------------------------------------------------------

# NOTE



# ---------------------------------------------------------------------------------------------------------------------------------------

# NOTE



# ---------------------------------------------------------------------------------------------------------------------------------------

# NOTE



# ---------------------------------------------------------------------------------------------------------------------------------------

# NOTE



# ---------------------------------------------------------------------------------------------------------------------------------------

# NOTE



# ---------------------------------------------------------------------------------------------------------------------------------------

# NOTE



# ---------------------------------------------------------------------------------------------------------------------------------------