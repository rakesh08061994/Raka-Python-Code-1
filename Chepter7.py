# Create using While loop Program to print 1 - 50 counting

# i = 1                             # from starting we keep i value 1
# while(i<=50):                     # Only when Condition is true, Then body of loop will work .
#                                   #  Othervise While body will not works
#                                   # Condition will continue works till condition become false 
#     print("Number " + str(i))     # str() type casting 
#     i = i+1                       # i value will be increase by 1 per loop
# print(type(str(i)))               # To check that what is actually data type of 1 during print
# print("Done !")                   # At last may be print successful message, when condition 
                                    # become false and get out from the while loop .

# ----------------------------------------------------------------------------------------

# Wtite a program to print list of a fruites using while loop

# fruites = ['Banana','Grapes','Watermelon','Mango']   # Create a List of fruites
# i = 0                                                # Keep starting value 1 of i for star loop from starting
# while(i < len(fruites)):                             # Body of loop will executed, while i not becomes equal length of list
#     print("Fruites ", fruites[i])                    # printing fruites element using list index slicing
#     i = i+1                                          # variable i is increase by 1 every time of loop
#     print(i)
# print("Done !")                                      # confirmation message before condition become false at last

# ---------------------------------------------------------------------------------------------
# Wtite a program to print list of a fruites using for loop

# fruites = ['Banana','Grapes','Watermelon','Mangoes','Papaya']        # Create Fruites list
# for Item in fruites:                                        # Item is variable, who insert value inside of fruites list
#     print(Item)                                             # Print Item variable values
# print("Done !")

# # ------------------------------------------------------------------------------------------------

# Example1 : For loop with string

# name = 'Ramayan'            # Print whole string with iterable data object
# for I in name:           # Item is a variable name. we can keep another variable name, place of item variable
#     print(I)             
# print("Done !")

# ------------------------------------------------------------------------------------------------------
# Example2 : For loop with List

# Weather = ['sunny','windy','rainy','stormy','snowy']
# for Item in Weather:                        # Using in() function in for loop mostly
#     print("This is a ", Item," Day")        # Printing List Indexing elements 
# print("Done")

# -------------------------------------------------------------------------------------------------------------
# For loop with Tuple

# Day = ("Sunday", 1,  "Monday", 2, "Tuesday", 3, "Wednesday", 4, "Thursday", 5, "Friday", 6, "Saturday", 7)
# print(type(Day))
# for Item in Day:
#     print(Item)
# print("Done")

# ---------------------------------------------------------------------------------------------------------------

# numbers = [10,21,32,52,11,63,65,94]
# for i in numbers:
#     if (i % 2 == 0):
#         print(i," Number is Even")
#     else:
#         print(i, " Number is odd")
# print("Done !") 

# ---------------------------------------------------------------------------------------------------

# x = 15
# total = 0
# for Item in range(1,x+1):
#     total += Item
#     print("Sum of 1 and numbers from 1 to %d:%d"%(x,total))

# ---------------------------------------------------------------------------------------------------------------
#  **************************Range Function ()*****************************************************

# for i in range(10):        # Print Integer range from 0 to n-1(8-1 = 7)
#     print(i)

# ------------------------------------------------------------------------------
# for i in range(10, 20):        # Print Integer range from 10 to n-1(8-1 = 7)
#     print(i)
# -----------------------------------------------------------------------------------------------

# Alphabets = ['a','b','c','d']

# for word in Alphabets:
#     print(word)

# --------------------------------------------------------------------------------------------------------------------
# for i in range(1,20,2):     #Range starting value, end value, Step Size
#     print(i)                # Print Range Variable i
# print("Done")               # You can print message for successfully execution of the program
# # ----------------------------------------------------------------------------------------------------------------------
# Break Statement >>>
# i = 0                                       # Initally i value is 0
# while i <= 50:                              # while condition is true
#     if(i == 30):                             # if condition
#         break                               # break the loop
#     print("This is ",i)                     # print of while condition
#     i = i+1                                 # Increase i value by 1 with each step
# print("Stop the print due to condition break (i == 30)")    #  end message

# # --------------------------------------------------------------------------------------------------------------------------
# Break Statement >>>>>
# i = 0
# while i <= 10:
#     if(i == 6):
#         break
#     print(i)
#     i = i+1
# print("Thank you")

# ----------------------------------------------------------------------------------------------
# Continue Statement >>>>

for i in range(5):
    print("Printing")   # Printing will print for 5 time 
    if (i == 2):    # If i value become True, when equal to 2 
        continue      # Continue skipped the iteration Loop 
    print(i)            # Print i (Incresed Number)
# ----------------------------------------------------------------------------------------------------

