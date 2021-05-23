# Python Crash Course (Chepter 8)
# Functions
#### DEfination a simple function :
# NOTE Excercise 1
# def greet_user():                               # Without passing Parameter value (Optional)
#     """Display a simple message !"""            # A good programmer always write a docstring about a functiion (Giood Habbit)
#     print("Hello ")                             # Main code, that actually work inside a function, when user call a functoion
#                                                 # No return value (Optional)


# greet_user()                                    # Function call by the programmer/user without argument, but paranthesis is must important                                                
# -------------------------------------------------------------------------
# NOTE Excercise 2
#### Function call by a argument value  in a simple greeting function.(Passing information to a function)
# def greet_user(user_name):                    # This time passing a parameter value inside paranthesis in a function and then colun:
#     """Desplay a simple greeting"""
#     print(f"Hello {user_name.title()}")       #   Main code inside a function, working with user name. when username given by user 


# greet_user("Rakesh")                          # Function call and pass a argument value inside a function to print "Hello Rakesh"

# -------------------------------------------------------------------------
# NOTE Excercise 3
### Parameter(s)) or parameter value(s) (Defination value inside a function paranthesis and then colun)
#          def function_name(Paramater(s)):

### Argument(s) or argument value(s) inside a function paranthesis during function call(Argument given by the programmer/user without use the colun)
#          function_name(argument(s)) 

# -------------------------------------------------------------------------
# NOTE Excercise 4
### Passing Arguments:
# In a function call time we can call a function with 3 way:
# You can pass an argument(s) to your functions in a number of ways:

# Way(1)-   Positional Argument :-   (Based on the order of the argument provided, Value matches this way are called positional argument) 

# Way(2)-   Keyword Argument :   (A name-value pair that you pass a function. Directly associate the name and value within the argument. 
#                                so when you pass the argument to the function, There is no confusion. You never messed up with wrong positional value and viceversa)

# Way(3)-   Default Value :      (If no argument value is passed in a function, It auto select default value, that is passed to a function during function defination)

#NOTE It does't really matter which calling style you use. As long as your function calls produce the output you want, just use the style you found
#     easiest to understand and applicable. This is your choice.

# -------------------------------------------------------------------------
# NOTE Excercise 5

# Way(1) Positional Argument (Order matter in positional argument)

# def describe_pet(animal_type,pet_name):             # function defination with parameters assign
#     """Display information about a pet"""
#     print(f"My pet name is {pet_name}, and his breeds is {animal_type}.")                 # Use this if we not use return valueṇ
#     # Variable_Assign = (f"My pet name is {pet_name}, and his breeds is {animal_type}.")      # we can assign a variable to the main code of function to use return
#     # print(Variable_Assign)                                                                # Print Variable
#     # return Variable_Assign                                                                # And also can return a value, we want to return (Optional) if not pass it will return None 


# describe_pet("Deshi", "Bhoora")     # We can MultipleFunction Call like following function call with argument pass
# describe_pet("Zerman", "Mini")     # Call the function with pass the argument to the function
# describe_pet("BullDog", "Jacky")     # Call the function with pass the argument to the function
# describe_pet("Huskey", "Aslan")     # Call the function with pass the argument to the function
# describe_pet("Doberman", "Boby")     # Call the function with pass the argument to the function


# print(describe_pet("Deshi", "Bhoora"))      # (if in the function return is not used or not proper return), It return None(To prevent this dont call function with print() or assign return value in function defination properly)



# -------------------------------------------------------------------------
# NOTE Excercise 6
# Way(2) Keyword Argument    (To prevent Passing wrong argument position)
# def describe_pet(animal_type,pet_name):
#     """Description about a pet"""
#     print(f"My Pet name is {pet_name}, and his breeds is {animal_type}.")


# describe_pet("Bhoora","Deshi")   # Argument Position is must in positional argument.  (Wrong position of argument to pass a function. Passing argument should be("Deshi","Bhoora")
#                                  # as define in function defination with position for a correct result.) But dont worry with Keyword argument passing

# describe_pet(pet_name="Bhoora",animal_type="Deshi")     # we assign value directly to Function parameters as a keyword argument.(Dont worry about argument position NOW) 



# -------------------------------------------------------------------------
# NOTE Excercise 7
# Way(3) Default value       (If user/programmer not assign argument value during calling function, we assign values to function paramets previously during function defnation)

# def describe_pet(pet_name,animal_type="Dog"):    # ="Dog" is default value with anmal_type(if user/programmer not assign argumants during function call, it automatically assign to animal_type key)
#     print(f"My pet name is {pet_name}, And his breed is {animal_type}.")


# describe_pet(pet_name="Bhoora")     # Not second value assign. (animal_type="Deshi)" ( You may pass argument according to your choice in the passing arguments 3 way)
# describe_pet(animal_type="Deshi")              # Not first value assign (It will show an error: 1 argument is missing pet_name, Because not any default value are reserved in function defination)
# describe_pet(pet_name="Mini", animal_type="Zerman")       # If we assign personaly value for animal_type, then no default value work
# -------------------------------------------------------------------------
# NOTE Excercise 8
# Avoiding Argument error :    Don't be supprised if you encounter errors about unmatched arguments. unmatched argument occor when you provide fewe
# or more argumants then a function need to do it's work.

# Define function with two parameters
# def describe_pet(animal_type,pet_name):                                 # we using here two parameters in function defination (Means two argument must to use the function properly !)
#     """Description about a pet"""
#     print(f"my Pet name is {pet_name}, And is breed is {animal_type}.")


# Function Calling with only one argument or empty argument (Two needed)
# describe_pet(animal_type= "Deshi")     # In both condition we call function with only one argument(Error: missing one parameter value pet_name)
# describe_pet(pet_name="Mini")           # In both condition we call function with only one argument(Error: missing one parameter value animal_type)

# If we pass both arguments value, That actually needed to run a function properly
# describe_pet(animal_type="Deshi", pet_name="Bhoora")        # No error (Because both argumants value are passed during function calling)
# describe_pet(animal_type="Zerman", pet_name="Mini")         # no error (Because both argumants value are passed during function calling)


# -------------------------------------------------------------------------
# NOTE Excercise 9 
# (Try it YOURSELF)

# write a function called Make_shirt() That accept a size and text of message that should be printed on the shirt.
# A sentence summerizing the size of the shirt and print message on it.(Use function call with Positional and Keyword assignment)
# Function Defination 
# def Make_shirt(Size, Message):                                      # Function Defination with two parameters value Size, Message
#     """Print message and shirt size"""                              # DocString. You can acces by print(Make_shirt._doc_)
#     print(f"Shirt size is {Size}, And Message is {Message}. ")    # Actual code inside the function to print size and message

# Function Calling
# Make_shirt("Medium","Get Out From Your Comfort Zone")                         # Using positional argumant function calling
# Make_shirt(Size="Medium", Message="Get Out From Your Comfort Zone")         # Using Keyword argumant function calling

# We can take input from the user to make function userfriendly
# Size = input("Enter Size of Shirt : ")
# Message = input("Enter Message on shirt to print : ")
# Make_shirt(Size,Message)                            # First will take input from user and then assign value to function argument and then print
# -------------------------------------------------------------------------
# NOTE Excercise 10
# Modify make_shirt() function, so that shirt size is "Large" Default value with a message that read "I love Python"

# def Make_shirt(Message,Size="Large"):                               # Size arguments default value is Large(If no argument pass for Size)
#     """Modifying Print message and shirt size"""
#     print(f"Shirt size is {Size}, And Message is {Message}.")

# Make_shirt(Message="I LOVE PYTHON") # Keyword assignment function calling
# Make_shirt("I LOVE PYTHON")         # Positional argument, Python understand this is for message (Because When one value has default previously)


# -------------------------------------------------------------------------
# NOTE Excercise 11
# Write a function describe_city() that city and its country. The function print a simle sentence like "Reykjavik in Iceland". 
# Give the parameter for the country a default value. Call your function for three different cities, atleast one of which is not in the default country

# def describe_city(City_Name,Country_Name="India"):      # Define a function with one parameter default value Country_Name="India"
#     """Deccribe about city-Country Description"""
#     print(f"{City_Name} in {Country_Name}.")

# describe_city("Washington","America")   # Function call with Passing two argument
# describe_city("Hongkong","China")
# describe_city("Jaipur")                 # Function call with passing one argument(Python will take ot for City name, Because python is so smart & Country_Name defauklt value is already mention as "India")

# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
# NOTE Excercise 12
# RETURN VALUE
#  A function does't always have to display its output directly. Insted it process some data and then return a value or set of values. That returing value called as "Return Value"
# Returning a Simple value:

# def get_formatted_name(First_name,Last_name="Jangid"):           
#     """Return a formatted name, neatly formatted, and take two argument First_Name and Last_Name"""
#     full_name = f"{First_name} {Last_name}"      # Two argumrnt will processed here, when user/programmer pass the argumrnt at the function calling
#     return full_name                            # Return a value(Full_name)


# Function Calling and return a value(we can use print() function)
# Using User Input given by user/progrmmer

# First_name = input("Enter Your First Name:  ")
# Last_name = input("Enter Your Last Name:  ")

# # Using Simple Formated and Camle formatted Title 
# print(get_formatted_name(First_name, Last_name))                      # Input will assign there value here
# # print(get_formatted_name(First_name.title(), Last_name.title()))        # In a Camel Formatted Output

# # Using Positioning Argumant
# print(get_formatted_name("Rakesh","Jangid"))                            # Formated way to function calling

# # Using Keyword Argument
# print(get_formatted_name(First_name="Rakesh", Last_name="Jangid"))      # Keyword Argument function calling

# # Using Default Value
# print(get_formatted_name("Rakesh"))                                     # Using default last_name="Jangid"


# -------------------------------------------------------------------------
# NOTE Excercise 13
# Making an Argumane Optional
# def get_formatted_name(First_Name, Last_Name, Middle_Name=""):  # Middle_Name is an optional parameter value
#     """Return a Full Name in Formatted """
#     full_name = f"{First_Name} {Middle_Name} {Last_Name}"
#     return full_name.title()

# # Function Calling using Optional Argument
# musician = get_formatted_name("rakesh","kumar","jangid")    # Making Assign all function in a third variable
# print(musician)                                             # Print Third variable as function calling argumrnts

# musician = get_formatted_name("Rakesh","Jangid")            # Middle Name is Optional
# print(musician)

# -------------------------------------------------------------------------
# NOTE Excercise 14
# Returning a Dictionary : A function can return any kind of value you need it to, Including more complicated Data Structure like lists and dictionary

# Example: The following function takes in part of a name and return a dictionary representing a person

# def build_person(First_Name,Last_Name):
#     """Returning a dictionary of information about a person !"""
#     person = {'First' : First_Name,'Last' : Last_Name}   #Return a dictionary representing a person
#     return person


# print(build_person("Rakesh","Jangid"))                  # Print function callinmg dictionary values output

# musician = build_person("Manish", "Jangid")
# print(musician)

# -------------------------------------------------------------------------
# NOTE Excercise  15
# Use function with while loop
# Let's use the get_formatted_name() function with while loop
# Function Defination


# def get_formatted_name(First_Name,Last_Name):
#     """Return full name in formatted"""
#     full_name = (f"{First_Name}, {Last_Name}")
#     return full_name

# While Infinity Loop
# Function Calling with infinity while loop


# while True:
#     print("Please Tell me Your Name: ")                     # Simple Message Print
#     f_name = input("First Name ")                           # Input first name from user/programmer
#     l_name = input("Last Name ")                            # Input last name from user/programmer
#     Formatted_Name = (get_formatted_name(f_name,l_name))    # function output saved in variable Formatted_Name
#     print(f"Hello {Formatted_Name} !")                      # Print Variable 


# -------------------------------------------------------------------------
# NOTE Excercise 16
#  There is no way to quit the program, whenEver we want. this is became like a infinity while loop.
#  For this we can assign a if condition inside a while loop, That when That condition become happen, condition will break. 
# #  That is Break Statement

# def get_formatted_name(First_Name,Last_Name):
#     """Return full name in formatted"""
#     full_name = (f"{First_Name}, {Last_Name}")
#     return full_name

# ### While Infinity Loop
# ### Function Calling with infinity while loop


# while True:
#     print("Please Tell me Your Name: ") 
#     print("Press q when you want to quit")                    # Simple Message Print
#     f_name = input("First Name ")                           # Input first name from user/programme
#     l_name = input("Last Name ")                            # Input last name from user/programmer
#     if(f_name == "q") or (l_name == "q"):                   # Make a condition to quit or break the function to get out from infinity while loop
#         break
#     else:                                                   # Else things will working previously
#         Formatted_Name = (get_formatted_name(f_name,l_name))    # function output saved in variable Formatted_Name
#         print(f"Hello {Formatted_Name} !")

# -------------------------------------------------------------------------
# NOTE Excercise 17
# Excercise 8.6 (City Names):
# Defination of a function with two parameters (a = City and b = Country) with Camle Title Formated
# def City_Country(a,b):
#     """Take two input City and Country and Dislplay Out in formatted way""" # Docstring about Function
#     Result = (f'"{a.title()}, {b.title()}"')                                # Main Program behind the function defination
#     return Result                                                           # Return the result

# # Function calling with users input 3 times
# Count = 1                               # Count start from 1
# while Count < 4:                        # While condition not become false
#     a = input("City Name : ")           
#     b = input("Country Name : ")
#     print(City_Country(a,b))
#     Count += 1                          # Count eachtime increase by 1

# -------------------------------------------------------------------------
# # NOTE Excercise 18
# # Excercise 8.7 (Album):
# Function Defination with three parameters album title, artist name, number of songs
# def make_album(a,b,c='None'):     # C value is optional with None
    
#     """Dictionary describing a music album. It takes two Parameter a & b as Artist_Name and as Album_Title and 'c' as Songs Number """

#     Album_Desctiption = {f'Album Title' : str(a.title()), 'Artist Name' : str(b.title()), 'Number of Songs' : str(c.title())}
#     return Album_Desctiption        


# # Function Calling 

# a = input("Album Title : ")
# b = input("Artist Name : ")
# c = input("Number of songs (* Optional) : ")
# print(make_album(a, b, c))


# -------------------------------------------------------------------------
# NOTE Excercise 19
# Excercise 8.8 (User Album)
# Add  While loop and quit option in Previous 8.7 excercise proublem


# Function Defination with three parameters album title, artist name, number of songs
# def make_album(a,b,c='None'):     # C value is optional with None
    
#     """Dictionary describing a music album. It takes two Parameter a & b as Artist_Name and as Album_Title and 'c' as Songs Number """

#     Album_Desctiption = {f'Album Title' : str(a.title()), 'Artist Name' : str(b.title()), 'Number of Songs' : str(c.title())}
#     return Album_Desctiption        


# # Function Calling with while infinity loop and break 
# while True:    
#     print("Press 'q' to quit ")
#     a = input("Album Title : ")
#     b = input("Artist Name : ")
#     c = input("Number of songs (* Optional) : ")
#     if((a == 'q') or (b == 'q') or (c == 'q')):
#         break
#     else:
#         print(make_album(a, b, c))

# -------------------------------------------------------------------------
# NOTE Excercise 20
# Passing a list 
# Say we have a list of users and want to printing greeting to each.
# Send a list of name to a function called greet_user(), which greet each person in list individually

# Function Defination 
# def greet_user(names):      # Function defination with parameter names as a list or tuple or string
#     """Input a list,Tuple,String,Set,Dict of users name, And Greet each person individually"""
#     for name in names:                                                          # Function can use list, tuple as a parameter value during function calling
#         msg = f" Hello, {name.title()} !"
#         print(msg)

#Function calling and assign datatype values
#Username = {"rakesh" : 5, "monu" : 5,"parul" : 5,"ajay" : 5,"ankit" : 5,"ram" : 5}                            # Take a dict as a input
# Username = {"rakesh", "monu","parul","ajay","ankit","ram","sita","hanuman","laxman","bharat","satrughn"}    # Take a set as a input 
# # Username = "ram","sita","laxman"                                                                            # Take Simple string value as a input
# Username = ["rakesh", "monu","parul","ajay","ankit"]                                                        # Take List as a Arguments
# # Username = ("ram","sita","hanuman","laxman","bharat","satrughn")                                            # Take Tuple as a Arguments
# #greet_user(Username.keys())                                         # Only to work with dictionary key(Cant use Username.values() Because int object does't have title() method)                                                    
# greet_user(Username)                                                # Call The function using data                                            
# print(greet_user.__doc__)

# -------------------------------------------------------------------------
# NOTE Excercise 21
# Calculate even, odd number using python function 

# def even_number(number):
#     """Calculate even number in between two numbers"""
#     if(number % 2 == 0):
#         result = (f" {number} is an even number." ) # To pass a return value we can assign output to a variable and then assign that variable as return value
#         return result
#     else:
#         result = (f"{number} is not a even number : ")  
#         return result                                   # pass result variable as a return value

# print(even_number(10))
# print(even_number(11))
# print(even_number(110))
# print(even_number(1023))

#----------------------------------------
# NOTE Excercise 
# Greet the person using tere name as a parameter

# def people_id(name):
#     """Greet the person named as a parameter"""
#     result = f"Hello {name}, Welcome and enjoy your stay !"
#     return result

# print(people_id("Rakesh"))
# print(people_id("Parul"))
# print(people_id(name="Monu"))

# -------------------------------------------------------------------------
# NOTE Excercise 
# Lambda function or Anonymous function

# cube = lambda y : y*y*y             # Single line function and expression without return value
# print(cube(5))                      # Function calling
# -----------------------------------------------------------------------------------------------
# even = lambda x:x%2==0  # True for even false for odd
# print(even(6))
# -----------------------------------------------------------------------------------------------------
# Lambda  function are used with filter(), map() and reduce() function

""" filter() function  =  Using lambda() Function with filter() The filter() function in Python takes
                          in a function and a list as arguments.This offers an elegant way to filter 
                          out all the elements of a sequence “sequence”, for which the function returns True """
# NOTE example of lambda with filter function: 

# l1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20]

# final_list = list(filter(lambda x:x%2==0,l1))   # lambda function in filter function and save output in list
# print(final_list)  # Lambda show only true value results
# ---------------------------------------------------------------------------------------------------------------\

# age = [25,45,65,23,35,62,84,45,51,26,54,43,37]      # Age as a list of input value container
# # we use lambda function with filter() function 
# big = list(filter(lambda x:x>40,age))   # show ages only, who is bigger than 25 age. using filter
# print(big) 
# -------------------------------------------------------------------------------------------------------------------



# ------------------------------------------------------------------------------------------------------------------------------------
#  
"""  map() function with lambda : The map() function in Python takes in a function and a list as an argument. 
                                  The function is called with a lambda function and a list and a new list is 
                                  returned which contains all the lambda modified items returned by that function for each item""" 

# l1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20]
# final_list = list(map(lambda x : x%2 == 0,l1))      # Return true false value for even and odd value
# print(final_list)

# --------------------------------------------------------------------------------------------------------------------------------------
# animals = ['dog', 'cat', 'parrot', 'rabbit']
# # Here we intend to change all animal names to upper case and return the same
# upper = list(map(lambda animal : str.upper(animal),animals))
# print(upper)


# ------------------------------------------------------------------------------------------------------------------------------------
# """ reduce() function : Using lambda() Function with reduce() The reduce() function in Python takes 
#                         in a function and a list as an argument. The function is called with a lambda function 
#                         and an iterable and a new reduced result is returned. This performs a repetitive operation
#                          over the pairs of the iterable. The reduce() function belongs to the  functools module."""

# from functools import reduce
# l1 = [5, 8, 10, 20, 50, 100]
# sum = reduce((lambda x, y: x+y),l1)

# print(sum)

# ------------------------------------------------------------------------------------------------------------------------------------







# -------------------------------------------------------------------------
# NOTE Excercise 
# Using function to call another function (In python a function can call another function):
# Example: 
#  School_Sum calls and Class_sum function
# Function 1 Class_Sum
# def Class_sum(num):
#     return num * 3
# def School_Sum(m):
#     return Class_sum(m)+3

# print(School_Sum(5))
# print(School_Sum(8))
# print(School_Sum(15))
# # --------------------------------------------------------------------------------
# #NOTE
# #Example :Program to compute for Weighted Average:
# Rakesh = {
#     "Name" : "Rakesh Kumar",
#     "Quizzes" : [89.0,95.0,78.0,90.0],
#     "Homework" : [89.0,60.0,98.0],
#     "Recitation" : [89.0,90.0,88.0],
#     "Tests" : [85.0,92.0]
# }  

# Parul = {
#     "Name" : "Parul Yadav",
#     "Quizzes" : [89.0,95.0,78.0,90.0],
#     "Homework" : [79.0,50.0,96.0],
#     "Recitation" : [88.0,96.0,38.0],
#     "Tests" : [65.0,13.0]
# } 
# Manish = {
#     "Name" : "Manish Jangid",
#     "Quizzes" : [69.0,55.0,78.0,90.0],
#     "Homework" : [89.0,68.0,78.0],
#     "Recitation" : [89.0,93.0,38.0],
#     "Tests" : [85.0,93.0]
# }

# Define function 1
# def Average(numbers):
#     """Calculate average of given numbers and return average result """
#     total = sum(numbers)
#     result = total/len(numbers)
#     return result

# # Define function 2
# def get_average(student):
#     """Calculate Students Average using function 
#     """
#     Quizzes = Average(student["Quizzes"])
#     Homework = Average(student["Homework"])
#     Recitation = Average(student["Recitation"])
#     Tests = Average(student["Tests"])
#     print(student["Name"])
#     return .2*Quizzes + .1*Homework + .3*Recitation + .4*Tests

# # Function call

# # print(get_average(Rakesh))
# # print(get_average(Parul))
# print(get_average(Manish))
# --------------------------------------------------------------------------------
#NOTE
#Example : 
# calculate factorial of a number using make a function:
# def factorial(number):
#     """Take number as value and return factorial of given number"""
#     a = 1
#     for item in range(1,number+1):
#         a *= item
#     # return f" Factorial of {number} is {a}"
#     return a

# # Function calling     
# number = int(input("Enter Number : "))
# print(factorial(number))

# --------------------------------------------------------------------------------
#NOTE
#Example : Calculate factorial using recursive
# def factorial(number):
#     if number == 1:
#         return 1
#     else:
#         return number*factorial(number-1)

# print(factorial(5))
# print(factorial(10))
# print(factorial(15))
# print(factorial(1))
# --------------------------------------------------------------------------------
#NOTE
#Example : Write a python recursion to calculate the sum of n natural number:

# Simple function to calculate sum of n natural number is :
# def natural_num(number):
#     """Take one argument as number, and return sum of n natural number :"""
#     a = 0
#     for item in range(1,number+1):
#         a += item
#     return a

# #Function calling    
# print(natural_num.__doc__)
# print(natural_num(5)) 
# print(natural_num(15)) 
# print(natural_num(55)) 


# Now we will calculate sum of n natural number usiung recursion function method


# --------------------------------------------------------------------------------
#NOTE
#Example : 


# --------------------------------------------------------------------------------
#NOTE
#Example :

