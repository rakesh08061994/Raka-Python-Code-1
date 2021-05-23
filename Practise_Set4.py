# List & Tuple related questions
# Write a program to stove seven fruites name from users and store into a list

# a = input("Enter Frutes Names:-  ")
# b=[a]
# print("Frutes are", b)
# marks = input("Enter Your Marks:  \n")
# a =  [marks]
# print(a.sort())


# ------------------------------------------------------
# String from Input convert into int by TypeCast:- 
S1 = int(input("Enter Marks Of S1 Student  "))
S2 = int(input("Enter Marks Of S2 Student  "))
S3 = int(input("Enter Marks Of S3 Student  "))
S4 = int(input("Enter Marks Of S4 Student  "))
S5 = int(input("Enter Marks Of S5 Student  "))
S6 = int(input("Enter Marks Of S6 Student  "))
S7 = int(input("Enter Marks Of S7 Student  "))
a = [S1,S2,S3,S4,S5,S6,S7]      #a is a list of integer set values
a.sort()                        #Sort The list a 
print(a)                        #Print Sort Result
