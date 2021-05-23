#                                                 NOTE Practice Set 8 Solutions:

#NOTE Question 1

# Write a program using function to find greatest of three numbers:
# Function Defination with Three Parameters (a,b,c) in integer value. 
# def gratest(a,b,c):
#     """Find gratest between three numbers:"""   # Docstring of function
#     if (a>b):                                   # Conditional Comparision between a & b
#         f1 = a                                  # Flag1 as a
#     else:
#         f1 = b                                  #Flag1 as b

#     if(f1>c):                                    # Conditional Comparision between remaining numbers
#         Result = (f"{f1} is Gratest !")          # Result are stored in a variable 
#         return Result                            # Return Result 
#     else:
#         Result = (f" {c} is Gratest !")
#         return Result                            # Result return

# # Function Calling by user/programmer
# print(gratest.__doc__)
# a = int(input("A : "))
# b = int(input("B : "))
# c = int(input("C : "))
# print(gratest(a,b,c))


# -----------------------------------------------------------------------------------------------------------
#NOTE Question 2

# Write a python program using function to convert celsius into farenhight using function:
# Formula (1°C × 9/5) + 32 = 33.8°F

# Function Defination with celesius as parameter value!
# def Formula(celsius):   
#     """Convert Celsius to farhenhight. Take celcius number as paramater value ! """
#     Result = (celsius*(9/5) + 32)       # Formula result stored in Result Variable
#     return f"{celsius}°C = {Result}°F"      # return Result as variable(That has stored Convert formula with f string to show more look realistic)

# # Function Calling
# print(Formula.__doc__)
# print(Formula(1))



# -------------------------------------------------------------------------------------------------------------
#NOTE Question 3

# HOw do you prevent a python print() function to print a new line at the end.

# # Print() before function without prevent new line 
# print("This is line one ! ")
# print("This is line two ! ")
# print("This is line three ! ")
# print("This is line four ! ")
# print("This is line five ! ")
# print("This is line six ! ")

# # Print() after function prvention new line 
# # end="" tell python to stop printing a new line 
# print("This is line one ! ",end="")
# print("This is line two ! ",end="")
# print("This is line three ! ",end="")
# print("This is line four ! ",end="")
# print("This is line five ! ",end="")
# print("This is line six ! ",end="")

# -------------------------------------------------------------------------------------------------------------

#NOTE Question 4
# Write a Recursive function to calculate the sum of first n natural number:
# natural number is 0 to the non-negative integers {0, 1, 2, 3, ...} are also called natural numbers or whole number

# Function Defination
# def natural_num(n):
#     """Take n as number & Calculate the sum of first n natural number"""
#     a = 0
#     for i in range(1,n+1):
#         a += i
#     return a

# print(natural_num(10))

# -------------------------------------------------------------------------------------------------------------

#NOTE Question 5
#  Write a python function to print first n lines of the following pattern

# def pattern(n):
#     """print first n lines of the Star pattern"""
#     for i in range(1,n+1):
#         Result = ("*" * i)
#         print(Result)
#     return Result
    
# print(pattern(10))

# -------------------------------------------------------------------------------------------------------------

#NOTE Question 6
#  Python function to convert inches to centemeters

# Function Defination:
# def Con_In_to_Ce(Inches):
#     """Convert Inches to Centemeters !"""
#     Centemeters = Inches * 2.54                             # Main Formula To convert inches to centemeters
#     Result = f"Inches > {Inches} = Centemeters > {Centemeters}"                         
#     return Result                                      # Return value of conversion as a variable Centemeters


# # Function Calling
# print(Con_In_to_Ce(1))
# print(Con_In_to_Ce(2))
# print(Con_In_to_Ce(3))
# print(Con_In_to_Ce(4))
# -------------------------------------------------------------------------------------------------------------


#NOTE Question 7
# Write a python function to remove a given word from a list and strip it at the same time



# -------------------------------------------------------------------------------------------------------------

#NOTE Question 8
# # Write a python function to print multiplicaton table
# def table(number):
#     """Take a number and print his multiplication table""" 
#     for item in range(1,11):                            # Range with for loop 1 to 11 (n,n-1)
#         multiplication = number * item                  # Multiplication table main formula
#         print(multiplication)
#     # return multiplication

# # Function calling 
# print(table.__doc__)
# number = int(input("Enter Number: "))
# print(table(number))
# # table(5)

# -------------------------------------------------------------------------------------------------------------
num = int(input("Enter Number :"))
for i in range(num):
    print(("*" * (num-i)))




    

# -------------------------------------------------------------------------------------------------------------