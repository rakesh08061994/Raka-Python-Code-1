# Question 1
# Write a program to find 4 Digits Gratest Value Entered by the user.
# Python program to solve if-elif ladder problem

# Num1 = int(input("Enter The 1st Value:  "))              # Taking 4 Input from User and then type cast to int
# Num2 = int(input("Enter The 2nd Value:  "))
# Num3 = int(input("Enter The 3rd Value:  "))   
# Num4 = int(input("Enter The 4th Value:  "))

# Greatest = [Num1, Num2, Num3, Num4]                      # Create a List With Greatest Variable name
# Greatest.reverse()                                          # Greatest.reverse() will arrange number in highest to lower value
# print(Greatest)                                          # print sorted list result                           
# if (Num1 > Num2 and Num1 > Num3 and Num1 > Num4):        # and logical operator to compare four conditions(All conditions should be true to get find "True")
#     print(Num1, "Is Greatest to", Num2, Num3, Num4)      # print the Greatest value among comparision between numbers
# elif(Num2 > Num1 and Num2 > Num3 and Num2 > Num4):
#     print(Num2, "Is Greatest to", Num1, Num3, Num4)
# elif(Num3 > Num1 and Num3 > Num2 and Num3 > Num4):
#     print(Num3, "Is Greatest to", Num1, Num2, Num4)
# elif(Num4 > Num1 and Num4 > Num2 and Num4 > Num3):
#     print(Num4, "Is Greatest to", Num1, Num2, Num3)
# else:
#     print("User Given Value are equal or wrong Value")
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                    # or

# Num1 =  int(input("Enter Number1 : "))
# Num2 =  int(input("Enter Number2 : "))
# Num3 =  int(input("Enter Number3 : "))
# Num4 =  int(input("Enter Number4 : "))

# if(Num1 > Num4):                    #Semifinal Between Num1 vs Num4
#     F1 = Num1
# else:
#     F1 = Num4

# if(Num2 > Num3):                    # SemiFinal Between Num2 vs Num3
#     F2 = Num2
# else:
#     F2 = Num3

# if(F1 > F2):                        # Final Match Between Two Flags F1 and F2 of Semifinal Winning Teams
#     print(str(F1)+" is Gratest !")       #str function 
# else:
#     print(str(F2)+" is Gratest")

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Question 2
# Write a program to find out whether a student is pass or fail, 
# if it required 40% and atleast 33% in each subjects to pass.
# Assume 3 subjects and take marks as input from the user.

# SubNum1 = int(input("Enter Subject 1 Number Out of 100:-   "))   #User Input marks for subject 1
# SubNum2 = int(input("Enter Subject 2 Number Out of 100:-   "))   #User Input marks for subject 2
# SubNum3 = int(input("Enter Subject 3 Number Out of 100:-   "))   #User Input marks for subject 3
# TotalSubMarks = 100                                              # We assume that Total Marks is 100
# a = (SubNum1*100)/100       # SubNum1 percentage in a Variable  
# b = (SubNum2*100)/100       # SubNum2 percentage in a Variable
# c = (SubNum3*100)/100       # SubNum3 percentage in a Variable
# Percentage = ((a+b+c)*100)/300  # Veriable Percentage save the calculation of a+b+c total percentage
# # In following line and operation is between or operation to evaluate percentage atleast 33 or 44 to pass 
# if (((SubNum1*100)/100 >= 33  or (SubNum1*100)/100 >= 40 ) and ((SubNum2*100)/100 >= 33  or (SubNum2*100)/100 >= 40 ) and ((SubNum3*100)/100 >= 33  or (SubNum3*100)/100 >= 40 )):
#     print("You are passed")
#     print("Your overall Percentage is", Percentage)
# else:
#     print("You are failed")
#     print("Your overall Percentage is", Percentage)
    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Question 3

# A spam comment is defined as a text, containing following keywords:-
# "Make a lot of money", "Buy Now","Subscribe This","Click This"
# Write a program to detect these spam

# Comment = input("Comment Please !\n")         #Take a input from user as a comment
# if (("Make a lot of money" in Comment) or ("Buy Now" in Comment) or ("Subscribe This" in Comment) or ("Click This" in Comment)):
#     print("This is a SPAM Message !")
#     print("Don't Click on it")
# else:
#     print("Thanks! For Comment")
# --------------------------------------------------------------------------------------------------------------------------
                    # or
# ---------------------------------------------------------------------------------------------------------------------
# Text = input("Enter the text:\n")
# if ("make a lot of money" in Text):
#     Spam = True
# elif("buy now" in Text):
#     Spam = True
# elif("subscribe this" in Text):
#     Spam = True
# elif("click this" in Text):
#     Spam = True
# else:
#     Spam = False

# if(Spam):                             # if you dont write here elif(spam = True) Actually True value is bydefault 
#     print("This is Spam")
# else:
#     print("This is Not Spam")
# -----------------------------------------------------------------------------------------------------------------------------------

# Question 4
# Write a program to check, whether a username is containing 10 character or not.
# Username = input("Type your Uername:\n  ")
# b = len(Username)         # Get lenth of variable b string
# if (b >= 10):             # If b is equal or Greater Than 10 Then Print the if's print statement
#     print("Username Containing Proper Character ")
# else:
#     print("Username is not proper")

# -----------------------------------------------------------------------------------------------------------------------

# Question 5
# Write a program, which find out, whether a given name is present in a list or not.
# Name = input("Enter Your Friends name to check, whether this is on my database or not:\n")
# Creating a list of string 
# NameList = ["Rakesh", "Parul", "Ankit", "Monu", "Harsh", "Ajay", "Manish","Keshav", "Pradeep","Jeetram","Khali","Bittu","Chhotu"]
# if (Name in NameList): # Using in function to check value are in list or not
#     print("Name is in Data List")
# else:
#     print("Name is not present")

# -------------------------------------------------------------------------------------------------------------------------------------------

# Question 6

# Write a program to calculate grade of a student, from his marks from the following scheme
# 90-100 = EX
# 80-90 = A
# 70-80 = B
# 60-70 = C
# 50-60 = D
# <50 = F


# Marks = int(input("Enter Your Marks, Grade \n "))
# if(Marks >= 90 and Marks <= 100):
#     print("Your Grade is  'EX'")
# elif(Marks >= 80 and Marks <= 90):
#     print("Your Grade is 'A'")
# elif(Marks >= 70 and Marks <= 80):
#     print("Your Grade is 'B'")
# elif(Marks >= 60 and Marks <= 70):
#     print("your Grade is 'C'")
# elif(Marks >= 50 and Marks <= 60):
#     print("Your Grade is 'D'")
# elif(Marks <= 50):
#     print("Your Grade is 'F'")
# else:
#     print("Marks is wrong ! ")

# ---------------------------------------------------------------------------------------------------------------
# Question  7

# Write a program to find out whether a given post is talking about "Harry" or not.

# Post = input("Write a Post: \n")
# if("Harry" in Post):
#     print("Post is Talking About 'Harry'")
# else:
#     print("Post is Not Talking About 'Harry'")
