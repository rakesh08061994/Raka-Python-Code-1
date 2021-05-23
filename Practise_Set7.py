# Question 1
# Write a python program to print multiplication table of a number (Table of a number)using for loop.


# num = int(input("Enter The number:   "))  # Input from user
# for i in range(1,11):                       # Range from 1 to n-1
#     print(i * num)                # User Number will multiply with range i each time
# print('Done !')                     # printing done message


#                                  ***********************************************************
# Write a Number of given user number:

# num = int(input("Enter a number:"))
# for Item in range(num):
#     print(" Ram")
    
# -------------------------------------------------------------------------------------------------
# Write a python program to greet all the person names stored in a list list1, which name start with "S"

# list1 = ["Harry","Sohan","Sachin","Rahul"]          # Creating a list of users name
# for name in list1:                                  # For loop till name in list list1
#     if(name[0][0] == "S"):                        # Condition if list1 names first character is "S" only then greet
#         print("Welcome ", name)                     
#     else:                                           # Otherwise not
#         print(name)
# print("Done !")    

# ---------------------------------------------------------------------------------------------------------------------------------
# Using while loop create a math count table of given number by user.

# num = int(input("Enter a number:  "))
# Counter = 1
# while Counter <= 11:
#     print(Counter * num)
#     Counter = Counter + 1
# print("Done !")


# ---------------------------------------------------------------------------------------------------------------------------------
# Write a pyton program to find wether it is a prime number or not .
# Note: In math, prime numbers are whole numbers greater than 1, that have only two factors – 1 and the number itself.
# Prime numbers are divisible only by the number 1 or itself.


# >>>>> Code is not proper Right now. 


# num = int(input(" Enter a number :  "))
# if ((num % 2 == 0) or (num % 3 == 0)):
#     print("This is not Prime number")
# # elif((num == 2) or (num == 3)):
# #     print("This is a Prime Number")
# else:
#     print("This is a prime number !") 




# ***********************************************



# ----------------------------------------------------------------------------------------------------------------------------------------
# >>>>>>>   ReProgrammed

# Write a pyton program to find wether it is a prime number or not .
# Note: In math, prime numbers are whole numbers greater than 1, that have only two factors – 1 and the number itself.
# Prime numbers are divisible only by the number 1 or itself.










# ---------------------------------------------------------------------------------------------------------------------------------
# Write a program to find the sum of first n natural number using while loop
# Note :  Natural numbers are a part of the number system, including all the positive integers from 1 till infinity

# num = int(input("Enter a number : ")) # Take input from user
# count = 1                              # Keep count 1 (while start loop from 1)
# result = 0                             # Result will increase by 0 at minimum value
# while count <= num:                     # upto condition false
#     result += count                     # Result increse with count value each time of loop
#     count += 1                          # Count increse each time with 1
#     print(result)   # If you want to show every steps   
# print(result)       # Total result at a time
    

# ---------------------------------------------------------------------------------------------------------------------------------
# Write a program to calculate the factorial of n number

# result = 1
# num = int(input("Enter a number: "))
# for item in range(1,num+1):
#     result *= item                  # Item multiple by REsult value and added in result also (result value each time multply by Item)
# print(f"The Factorial of {num} is {result}")

# ---------------------------------------------------------------------------------------------------------------------------------
# print pattern *

#       **
#       ***
#       ****
#       *****
#       ******
#       *******
#       ********
#       *********
#       ********** 


# num = int(input("Enter Number: "))
# for i in range(num):
#     print('*' * (i+1))

# ---------------------------------------------------------------------------------------------------------------------------------
print("Print table in ascending order !\n")
num = int(input("Enter Number : "))
for i in range(1, 11):      # start at (n to n-1)
    print((num * i))

#  ---------------------------------------------------------------------------------------------------------------------------------
#NOTE : Make a math counting table in reverse order.
print("Print math table in descending order !\n")
num = int(input("Enter a number : "))
for i in range(-10,0):  # Descending order math table
    Table = num * i     # Counting till i
    Result = abs(Table) # Abs() convert any negative value in positive absolute number.
    print(Result)
    
# ---------------------------------------------------------------------------------------------------------------------------------
