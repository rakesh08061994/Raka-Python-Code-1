# > Write a program to create a dictionary of hindi word with value as their english translation. 
# > Provide user to an opton to get result for it.

# Dict = {'Anar':'Pomegranate','Aam':'Mango','Imli':'Tamarind','Ikh':'Reed','Ullu':'Owl','Oon':'Wool'}

# print(Dict)
# Key = input("Enter Your Hindi Word to translate:  ")
# print("The english Translation Of Your Hindi Word Will Be",Dict[Key])

# --------------------------------------------------------------------------------------

#  > Write a program to input eight from user and display all the unique number.

# a = input("Enter value:  ")
# b = input("Enter value:  ")
# c = input("Enter value:  ")
# d = input("Enter value:  ")
# e = input("Enter value:  ")
# f = input("Enter value:  ")
# g = input("Enter value:  ")
# h = input("Enter value:  ")
# set = {a,b,c,d,e,f,g,h,}
# print(set)

#  ----------------------------------------------------------------------------------------

# > Can we have 18 integer and 18 string data type values in a set.

# set = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r'}
# print(set)
# print(type(set))
#  -------------------------------------------------------------------------------------------
# > What will be the length of set b. if
# s = set()
# s.add(20)
# s.add(20.0)
# s.add("20")
# print(s)        # printing set s before all above operations
# print(len(s))   # Print length of set s before oprations 
# print(type(s))  # Check the data type of set s
# Length of s after these operations

# -------------------------------------------------------------------------------------------------
#  > s = {} What is data type of s

# s = {}      # s is empty Dict not empty set. For this you have to put value inside it
# print(s)    # printing s as empty dict not empty set
# print(type(s))  # <class 'set'>

# a = set()       # a is empty set but you cant put mixed datatype multiple values at a single time
# print(a)          # printing a as empty set     
# print(type(a))  # <class 'set'>

# b = ()            # b is empty tuple, not empty set
# print(b)        # printing b as empty tuple not empty set
# print(type(b))    <class 'tuple'>

# ---------------------------------------------------------------------------------------------------

#  > Create a empty dictionary. Allow 4 friends to enter there fevourite language as value and there name as a key. 
#  > Assume the Name are unique

# friend_name1 = input("Enter Your Name :  ")
# friend_value1 = input("Enter Your Favourite Language:  ")
# friend_name2 = input("Enter Your Name :  ")
# friend_value2 = input("Enter Your Favourite Language:  ")
# friend_name3 = input("Enter Your Name :  ")
# friend_value3 = input("Enter Your Favourite Language:  ")
# friend_name4 = input("Enter Your Name :  ")
# friend_value4 = input("Enter Your Favourite Language:  ")


# Dict = {friend_name1:friend_value1, friend_name2:friend_value2, friend_name3:friend_value3, friend_name4:friend_value4}
# print(Dict)

# print(Dict[friend_name1])
# print(Dict[friend_name2])
# print(Dict[friend_name3])
# print(Dict[friend_name4])

# ----------------------------------------------------------------------------------------------------------------------

a = {}                                                          # Creating an empty Dictionary

friend_name1 = input("Enter Your Name :  ")                     #friend1 name as key
friend_value1 = input("Enter Your Favourite Language:  ")       #friend1 fevourite language as value
a[friend_name1] = friend_value1                                 # add key:value inside empty Dictonary
print(a)                                                        # printing updated Dictionary before above operation

friend_name2 = input("Enter Your Name :  ")                     #friend2 name as key
friend_value2 = input("Enter Your Favourite Language:  ")       #friend2 fevourite language as value
a[friend_name2] = friend_value2                                 # add key:value inside  Dictonary
print(a)                                                        #printing updated Dictionary before above operation

friend_name3 = input("Enter Your Name :  ")                     #friend3 name as key
friend_value3 = input("Enter Your Favourite Language:  ")       #friend3 fevourite language as value
a[friend_name3] = friend_value3                                 # add key:value inside  Dictonary
print(a)                                                        # printing updated Dictionary before above operation

friend_name4 = input("Enter Your Name :  ")                     #friend4 name as key
friend_value4 = input("Enter Your Favourite Language:  ")       #friend4 fevourite language as value
a[friend_name4] = friend_value4                                 # add key:value inside Dictonary
print(a)                                                        #printing updated Dictionary before above operation

# ---------------------------------------------------------------------------------------------------------------------------

# Question 7:-  > That will happen if two friends name are same and enter same name (Because friends_name are key for Dictionary)
# Answer :  we know In dictionary Keys should be unique, Othervise key previous value will update with updated key's value
# Try Program 6 with same key and see the output
# -----------------------------------------------------------------------------------------------------------------------------

# Question 8 : >  Now if two languages are same then what will happen in program. How Dictionary react actually
# Answer :  Value doesn't affect on Dictionary, both same value will tteched to there unique key name. 
# key should not be Duplicate or same (Should be unique)
# Value can be Duplicate (Doesn't affect)
#Try Progarm 6 with same value and see the output
