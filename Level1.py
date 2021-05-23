''' Code Notes Programmer : Rakesh Jangid
 Source Of Information : Joe Thompson Book Python Companion
 Starting Date: 05-March-2021 07:59 AM '''
# **********************************************************************************************
# import os                             # Importing Linux OS Features in Python(Specially when we use cmd Interface )
# os.chdir("J:\Study Material")       # Change Directory Path
# os.mkdir("Folder1")                 # Make a New Folder on changable directory
# os.chdir("J:\Study Material\Python\Rakesh_Python_Code\Joe_Thompson_Notes")  # Change New Directory Path
# os.mkdir("Folder1")                 # Make a New Directory (Check it on location)
# os.rmdir("Folder1")                # Remove Directory Folder1  on current path  
# os.getcwd()                        # Get Current working Directory from os module
# ---------------------------------------------------------------------------------------------------

# Variables And values that are assign to Assigenment operator using = operator
# Variable          Value assign to the variable(Using = Opeartor)

# String_Variable = "This is an string class assign value"
# Float_Variable  = 79.6
# Integer_Variable = 786
# Boolian_Variable = True 

# print(String_Variable)
# print(Float_Variable)
# print(Integer_Variable)
# print(Boolian_Variable)

# print("\n\nid(Variable_Name) This is Memory Location ID of variable Value in memory\n")
# print(id(String_Variable))    # Id of memory location (That gives by memory to this variable and there value)
# print(id(Float_Variable))    # Id of memory location
# print(id(Integer_Variable))    # Id of memory Location
# print(id(Boolian_Variable))    # Id of memory location
# -------------------------------------------------------------------------------------------------
# We can use multiple variable Assignment follow positioning order
# Str_Value,Float_Value,Int_Value,Bool_value = "Ramayan",73.5,986,True    
# print(Str_Value)
# print(Float_Value)
# print(Int_Value)
# print(Bool_value)

# -----------------------------------------------------------------------------------------------------------
# Assignment of a common value to several variable in a single statement 
# x=y=z = "Ramayan"
# print(x)
# print(y)
# print(z)

# we can do Above same thing with each time assigmen Value to a new variable
# x = "Same_Value"     # First Time asssign value to x
# print(id(x))           # ID or Memory location of x
# y = "Same_Value"     # Second time same value to y
# print(id(y))           # ID or Memeory assifn to new value y
# z = "Same_Value"     # Third time assign value to y and so.on...
# print(id(z))           # ID or Memeory Location of z
# # we see python is so smart. He Gives same id memory location to each and every variable with "Single value" to save space
# zz = "Different_Value"  # Check different value to different varible
# print(id(zz))           # Id memory Location in memory

# Now we assign different values to single Variable and see the Id location in memory
# x = "Ramayan"               # Value assign to x variable
# print(x)                    # Printing x Value
# print(id(x))                # ID or Memory location in memory 

# x = "Mahabharat"
# print(x)
# print(id(x))

# x = "Shrre_Krishna"         # Newest Value assign to same variable x
# print(x)                    # Printing x value last time
# print(id(x))                # ID or Memory Location in memory

# ------------------------------------------------------------------------------------------------
# Counter = 50        # 50 Integer value assign to Counter Variable
# print(Counter)      # Printing Counter Variable
# # print(id(Counter))  # Check ID

# Counter += 50       # Add or Increase value with 50 Inside The Counter Variable
# print(Counter)      # Printing Counter Variable
# # print(id(Counter))  # Check ID
# -------------------------------------------------------------------------------------------------

# Assignment Operator
# equal or = operator assign the value of the right operand to the left operand 
# a = 10
# b = 7
# print(a)
# print(b)

# += & -= operator
# c = 9
# d = 3
# c += 5  # Increase c variable value with 5 (Right to left)
# d += c  # Increase d Value with c variable's Inresed value
# print(c)
# print(d)

# e = 65
# f = 32
# e -= 5  # Minus value of e with 5
# f -= c  # minus value of f with c value
# print(e)
# print(f)

# # ---------------------------------------------------------------------------------------------------------------
# l1 = [1,32,565,12,-563,-56,-6,-25.0,35.2,85,6,451,278,2322,55212,5522,2540,211,515,-54202,21210121,1020,-21510]
# print(max(l1))     # Maximum Value inside l1 list
# print(min(l1))     # Minimum Value inside l1 list 
# print(round(l1))
# # ---------------------------------------------------------------------------------------------------------------------

# lyric = "aaj kal yaad kuch aur rhta nhi, ek bas aapki yaad aane ke baad"
# print(lyric.upper())        # Print the whole string in uppercase
# print(lyric.lower())        # print the whole string in lowercase
# print(lyric[0:17].lower())   # Print the selected string slicing 0:17 in lowercase
# print(lyric[0:17].upper())   # prin  the selected string slicing 0:17 in uppercase

#--------------------------------------------------------------------------------------------------------------------

# Repeating a string (string)*Number

# a = "chal ","chaiyaa "*4,"chal ","chaiyaa "*4
# print(a)    # Repaeting a variable string  
# Design = "<->~~**-----**~~<->"*22
# print(Design)   # Repeatition of Design string 22 time
# ------------------------------------------------------------------------------------------------------------------

# a = "Ramayan"
# b = "I hate you"
# c = "You are so Beautiful"
# d = "You are my Friend, Friend, Friend, Friend"
# print(a.replace('Ramayan','Geeta'))    # Replace old String with new updated string
# print(b.replace('I hate you','I love you')) # Replace old string with new updated string
# print(a.replace(a[0:3],'o-o-o-o'))
# print(c.replace(c[11:20],'Ugly'))           # Replace particular string slice with new string
# print(d.replace('Friend','Best Friend',1))  # Only one time replace the value in first occurance of string 
# #--------------------------------------------------------------------------------------------------------------------

# Letter = "How much time string or character are there in a vaiable"
# print(Letter.count('i')) # How much time 'i' character comes in variable Letter strings >> 4 Time
# print(Letter.find('or'))    # Find the position of 'or' character in Letter Variable
# # If you find Blank space in a string, It will Find First One 'Blank Space' in the string, When ever he found
# print(Letter.find(' '))  

# -------------------------------------------------------------------------------------------------------------------
# x = 'The value of a is {}, b is {}, and c is {}'
# print(x.format('50','33','45'))
# -------------------------------------------------------------------------------------------------------------------
# a = 'Pogramming is a challenging and {} activity'
# print(a.format('rewarding'))
# -------------------------------------------------------------------------------------------------------------------
# a = 50
# b = 60
# c = 70
# print('The Value of a is {}, And b is {}, And c is {}'.format(a,b,c))   # Formate values on another place !
# --------------------------------------------------------------------------------------------------------------------
# List Data sequence Types

# list1 = ["Ramayan",786,76.5,True]   # Creating a list (May use mixed values seprated by comma in [] Square Brackets)
# print(list1)
# print(type(list1))
# print("Now we using list operations.\t")
# print(" Slicing list Indexing in List list1 \n\t")
# print(list1[0])                     # Index to list1 0th position value 
# print(list1[:3])                    # Slicing list Index to list1 0th(By_default) to n-1 position value
# print(list1[1:3])                   # Slicing list Index to list1 1st ti n-1 position value
# print(list1[0][2])                  # Slicing list Index to list1 0th index'es 2nd position value  
# # print(list1[2][:1])                 # Slicing list Error:- Float Object is not subcriptable
# # print(list1[3][0:])                 # Slicing list Error:- Bool Object is not subscriptable

# # Negative Indexing in list
# print(list1[-4])                        # Slicing list Negative indexing start with -1 to above from right to left
# print(list1[-4][-7:6])                  # Slicing list Negative indexing with nested indexing in list1

# ------------------------------------------------------------------------------------------------------------------
# Adding element to a list using list.append()
# list2 = []                                  # Creating a empty list list2
# print(list2)                                # print the list list2
# list2.append("Add Value")                    # Append a string value in a list
# print(list2)
# list2.append(1234)                          # Append a integer value in a list
# print(list2)
# list2.append(True)                          # Append a bool value in a list
# print(list2)
# list2.append(99.99)                         # Append a float value in a list
# print(list2)                                # print the list list2

# -----------------------------------------------------------------------------------------------------------------
# If you want to add multiple values in list, then use list attribute extend()
# list3 = []        # Create empty list
# list3.extend(["Ram","Ram",786,96.5,True])
# list3.extend(["Ram","Ram",786,96.5,True])
# ##list3.extend([["Ram","Ram",786,96.5,True],["Ram","Ram",786,96.5,True]])     # TypeError: list.extend() takes exactly one argument (2 given)
# print(list3)



# list3[0] = "Ghanshyam"
# print(list3)

# list3[0:] = ["Radha","Krishna",12,1.1,False]
# print(list3)

# -----------------------------------------------------------------------------------------------------------------------------

# Concatenating'+' and  Repeatation'*' list
#  We cant multiply two list: TypeError: can't multiply sequence by non-int of type 'list'

# a = [1,2,3,4,5,'a','b','c','d',1.1,1.2,1.3,1.4,1.5,True,False]
# b = [1,2,3,4,5,'a','b','c','d',1.1,1.2,1.3,1.4,1.5,True,False]
# a + b   # concatenating list opeartion
# print(a*2)     # Repetation list opration with list a
# print(b*3)     # Repbtation list opration with list b

# ----------------------------------------------------------------------------------------------------------------------
# insert an item on your desired location with insert() attribute of list data type
# a = ["Ramayan",786,True,96.5]
# a.append(6)         # Insert items at end last place of list
# print(a)            # Print list
# a.insert(2,'xxxx')  #insert an item on your desired location
# print(a)
# -------------------------------------------------------------------------------------------------------------------

# name = ("Avinash","Vaidehi","Parul","Akanksha")         # Creating a tuple
# for wish in (name):                                     # wish is a variable name
#     if (wish == "Parul"):                               # If condition become true
#         print("Parul is my bestest Friend")
#     else:
#         print(wish," is my college friend")    
# print("Program is completly sucessed !")                                      # Print function will work

# ---------------------------------------------------------------------------------------------------------------------

# The Range Function 
# The Range() function is used to create lists that contain airthmentic progression.
# Syntax: range(Start, End, Step)   #All arguments rea plain integer 
# range(10)
# print(range(10))


# for i in range(0,10,2):         # (Start, End, Step)
#     print("Hello", + i)

# ---------------------------------------------------------------------------------------------------------

# a = list(range(10))         # Print or convert Range elements in list format use list(range())
# print(a)

# # ------------------------------------------------------------------------------------------------------------
# a = list(range(0,-10,-1))     # To print negative range use step
# print(a)
# --------------------------------------------------------------------------------------------------------------
# a = (int(input("Enter Your range:   ")))            # Range Input from user
# for item in range(a):                               # Range function in for loop
#     print("This is: ", item)                        # print item range with message

# --------------------------------------------------------------------------------------------------------------
# password check verification program


# Dict = {"Rakesh": "@#Rakesh5@","Mohan":"Love@123","Ankit":"Krishna789"}
# user = input("Please enter your username: ")
# if (user in Dict):
#     print("Welcome! ", user, "\n")
#     pwd = input("Enter Your Password: ")
#     if (pwd in Dict[user]):
#         print("You are authentic person")
#     else:
#         print("You are fake !")
# else:
#     print("You are not authentic user. ")
#     print("Please try again.")

# --------------------------------------------------------------------------------------------------------------
# User input to add elements in a list
# and terminate the program after 10 append element

# a = int(input("Enter The length of list:   "))
# list1 = []
# for i in range(a):
#     if (i <= a):
#         b = input("Enter Number to append in the list:  ")
#         list1.append(b)
#         print("You have submited the value! ")
#         print(list1)
#     else:
#         pass
#         # print("You have successfuly created a list ")
#         # print(list1)
# print("Done")

# --------------------------------------------------------------------------------------------------------------

# takes a order to the customer to sever the food
# order = ['kachori','tea','coffee','pizza','pattise','momos','maggie','cake','sendwich']
# take_order = input("Enter Your Order Please:\n")
# if (take_order in order):
#     print("Thank You, for the order!")
#     print('your order '+ take_order +' will take 5 minutes')
#     print('Please wait !')
# else:
#     print("Sorry we don't serve " + take_order + " at the moment !")



# # --------------------------------------------------------------------------------------------------------------
# stock1 = ['kachori','tea','coffee','pizza','pattise','momos','maggie','cake','sendwich']
# stock2 = ['patashi','bhel','poha','daliya','rice']

# take_order = input("Enter your order: ")
# if (take_order in stock1):
#     print('your order ' + take_order + ' will take 15 minutes to be ready')
# elif(take_order in stock2):
#     print('Your order ' + take_order + ' will take 5 minutes')
# else:
#     print('Sorry we dont server ' + take_order + 'at this time')
# --------------------------------------------------------------------------------------------------------------
# WHILE LOOP Example:

# number = int(input("Enter a number: \n"))

# total = 0
# counter = 1

# while counter <= number:
#     total = total + counter

#     counter += 1

#     print("The total is", total)


# --------------------------------------------------------------------------------------------------------------
# CONTINUE STATEMENT

# animals = ['lion','tiger','monkey','bear','sloth','elephant']
# for name in animals:
#     if name == 'sloth':
#         continue                      # Continue the loop statement except this
#     print("Beautiful",name)
# print("Amazing animals")
# --------------------------------------------------------------------------------------------------------------
# BREAK STATEMENT
 
# animals = ['lion','tiger','monkey','bear','sloth','elephant']
# for name in animals:
#     if name == 'sloth':
#         break                         # Break the loop statement now
#     print("Beautiful",name)
# print("Amazing animals")
#  --------------------------------------------------------------------------------------------------------------
# PASS STATEMENT 

# animals = ['lion','tiger','monkey','bear','sloth','elephant']
# for name in animals:
#     if name == 'sloth':
#         pass                    # DO NOTHING
#     print("Beautiful",name)
# print("Amazing animals")

# --------------------------------------------------------------------------------------------------------------
# INFINITY LOOP TECHNIQUES
# import math

# while True:
#     num = int(input("Enter a number:  "))
#     print("The Square root of ", num , "is ", math.sqrt(num))
# print("Done ! ")
  
# --------------------------------------------------------------------------------------------------------------
# 
# --------------------------------------------------------------------------------------------------------------
# 
# --------------------------------------------------------------------------------------------------------------
# 
# --------------------------------------------------------------------------------------------------------------
# 
# --------------------------------------------------------------------------------------------------------------
# 
# --------------------------------------------------------------------------------------------------------------
# 