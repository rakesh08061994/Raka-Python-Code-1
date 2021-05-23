# #NOTE (CodeWithHarry)
# # Function and recursion
# def absolute_value(number):
#     """Return the absolute value of
# a number entered by the user"""

#     if(number > 0):
#         return number
#     else:
#         return -number




# print(absolute_value(12))
# print(absolute_value(40))
# print(absolute_value(-32))
# print(absolute_value(-78))
# print(absolute_value(26))
# print(absolute_value(76))
# print(absolute_value(0))
# print(absolute_value(.5))
# print(absolute_value.__doc__)

# # -----------------------------------------------------------------------------------------------------------------------------------------

# # Define a function without return value
# #NOTE It will reurn bydefault NONE


# def greet(name):                            # Define user_defined function greet and assigned parameters
#     '''Greet the people
# enter the name'''
#     print("Hello " + name + " Good Day !")


# print(greet("Rakesh"))

# # ------------------------------------------------------------------------------------------------------------

# # Here is a function with a parameter and return, a function that evaluate if a given number is an even number.
# # it is a function which return the number if even, otherwise function return a string and None.

# def even_numbers(number):
#     if number % 2 == 0:
#         return number
#     else:
#         print(f"Sorry ! {number} is not a even number.")

# # Users Input to use this function
# print(even_numbers(10)) 
# print(even_numbers(13)) 
# print(even_numbers(17)) 
# print(even_numbers(14)) 
# print(even_numbers(998)) 
# print(even_numbers(201)) 


# ----------------------------------------------------------------------------------------------------

# I try to create a function according to my mind(This is totaly my practice)
# number = int(input("Enter Number :"))
# for item in range(1, number):
#     a = ("*" * item)
#     print (a)

    # -------------------------------------------------------------------------------
#     def people_id(name):
#     ''' This function greet the person named as parameter'''
#     print("Hi," + name + ", Welcome and enjoy your stay ! Good Day !")

# print(people_id('Rakesh'))
# print(people_id('Mohan'))
# print(people_id('Ankit'))

# -----------------------------------------------------------------------------------------------
# #NOTE : learn from Python Crash Cource by ERIC MATTHES
# # function  are two types in python : (1) Built-In Function
# #                                     (2) User-Defined- function

# # Function are works two types : (1) Display Information
# #                                (2) Process a data and return a value or set of values

# # Finally you will learn to store functions in seprate files called "Module" to help organize your main program files

# # NOTE Syntax of function:
# ''' 
# def function_name(parameters):
#     """docstring"""
#     statement(s)
# ''' 


# # -----------------------------------------------------------------------------------------------------------------------
# #Example 1 
# #  Simple function named "Greet_User" that prints a greeting without use the parameters

# def Greet_User():
#     """Display a simple greeting !"""
#     print("Hello !")

# Greet_User()         # Display message inside of a function
# print(Greet_User())  # Return None

# # -----------------------------------------------------------------

# def avg(number):
#     average = sum(number)/10
#     return average


# a = 1,2
# print("The sum is ",avg(a))

# for i in range(1,11):
#     print(i)
#     # z = avg(i)
#     # print(z)

# # -----------------------------------------------------------------------------------------------------------------------
# # name = input("Enter Your Name:  ")
# def greet(name):
#     print("Hello " + name + " Good Day !")



# greet("Rakesh")     # Function Call
# greet("Parul")
# greet("Mohan")
# greet("Ankit")



# -------------------------------------------------------------------------------------------------------

# def Math_Table(number):
#     """Math Table of User Given Number !"""
#     for item in range(1,11):
#         table = int(number) * item
#         return table

# print(Math_Table(10))

# -------------------------------------------------------------------------
# def absolute_value(number):
#     """Returns the absolute value \n of a number entered by the user"""
#     if number >= 0:
#         return number
#     else:
#         return -number



# print(absolute_value(-25))


# # ----------------------------------------------------------------------------------------------

# def even_Number(number):
#     if ((number % 2) == 0):
#         return number
        

        # ------------------------------------------------------------------------------------------

        # def tri_recursoin(k):
#     if k > 0:
#         result = k + tri_recursoin(k-1)
#         print(result)
#         print("End if block")
#     else:
#         result = 0
#         return result
#         print("End else block")
#     return result





# tri_recursoin(5)


# # ------------------------------------------------------------

# def print_f(f_name,l_name):
#     z = (f_name + l_name)
#     print(z)
#     return z


# print_f("Rakesh", " Kumar")

# ---------------------------------------------------------------------------

# def display_message():
#     print("Function is a nice concept")

# display_message()

# -----------------------------------------------------------------------
# def fevourite_book(title):
#     title = title.title()
#     a = ("One of my fevourite book is " + title)
#     print(a)
#     return a

# fevourite_book("ramayan")

# --------------------------------------------------------------------------



