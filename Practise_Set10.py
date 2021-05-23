# # NOTE :Answer 1
# list1 = ["Michael Abrash – program optimization and x86 assembly language \n "
# "Scott Adams – one of earliest developers of CP/M and DOS games \n "
# "Tarn Adams – created Dwarf Fortress \n "
# "Leonard Adleman – co-created RSA algorithm (being the A in that name), coined the term computer virus \n "
# "Alfred Aho – co-created AWK (being the A in that name), and main author of famous Compilers: Principles, Techniques, and Tools (Dragon book) \n "
# "Andrei Alexandrescu – author, expert C++, D languages \n "
# "Paul Allen – Altair BASIC, Applesoft BASIC, co-founded Microsoft \n "
# "Eric Allman – sendmail, syslog \n "
# "Marc Andreessen – co-created Mosaic, co-founded Netscape \n "
# "Jeremy Ashkenas – created CoffeeScript programming language and Backbone.js \n "
# "Bill Atkinson – QuickDraw, HyperCard] \n "]

# class Programmer:   # Define a class named programmer
#     """Description about some Microsoft programmers with there working project name"""
#     company = "Microsoft"

#     def programmer_Info(self):  # static method, That doesn't use self parameter, (even you print or return simple message only)
#         """return info about microsoft programmer"""
#         for name in list1:
#             return name

# # create instance object of class Programmer()
# # Access class attribute company
# obj1 = Programmer()
# print(obj1.company)             # Microsoft


# # Access class method programmer_Info()
# print(obj1.programmer_Info())

# ---------------------------------------------------------------------
# ANswer 1
# class Programmer:
#     """Description about some Microsoft programmers with there working project name"""
#     company = "Microsoft"       # Class Attribute (To access for all instance(object))

#     def __init__(self,name,project):            # Define parameter to use class attributes and methods on each call by instance
#         self.name = name
#         self.project = project

#     def get_Info(self,signature):
#         """return information of programmer and there project"""
#         return f"Programmer name is '{self.name}' and there project is '{self.project}' and This is from {self.company}, so '{signature}' ! "


# user1 = Programmer("Rakesh","Python")
# user2 = Programmer("Parul","Sql")
# user3 = Programmer("Ankit","CA")
# user4 = Programmer("Piyush","BCA")

# print(user1.get_Info("Thanks"))
# print(user2.get_Info("Thanks"))
# print(user3.get_Info("Thanks"))
# print(user4.get_Info("Thanks"))

# print(user1.company)
# print(user2.company)
# print(user3.company)
# print(user4.company)


# ---------------------------------------------------------------------
# # NOTE :Answer 2

# class Calculator:
#     """Capable of finding square, curve, and square root of a given number"""

# def square(self, num):
#     """return square of a given posotional argument 'num'"""
#     return f"Square of {num} is  '{num*num}'"

# def squareRoot(self, num):
#     """return squareRoot of a given posotional argument 'num'"""
#     return f"Square Root of {num} is '{num**0.5}'"

# def cube(self, num):
#     """return cube of a given posotional argument 'num'"""
#     return f"Cube of {num} is '{num**3}'"

# @staticmethod
# def greet():
#     return f" Hello !"

# a = Calculator()
# print(a.square(120))

# print(a.squareRoot(7))

# print(a.cube(5))

# print(a.greet())

# ---------------------------------------------------------------------
# NOTE :Answer 3

# class Abc:
#     """define a class Abc"""
#     a = "Rakesh"       # Define a class attribute 'a' with value "Rakesh" (By-Default)


# # define instance object of class abc
# obj1 = Abc()
# print(obj1.a)    # Rakesh


# obj1.a = "Parul"     # Change instance attribute from "Rakesh" to "Parul" (only for object instance)
# print(obj1.a)       # Parul

# print(Abc.a)        #Rakesh        # Class attribute will keep remain same class attribute


# # # NOTE : If you want to change class attribute for ever 
# # Abc.a = "Ramayan"                       
# # print(Abc.a)            # Ramayan

# ---------------------------------------------------------------------

# NOTE :Answer 4

class Train:
    """Define a Train class, That has method : bookTicket(), getStatus(), getFare() and an attribute"""
    running_train = "Indian Railway" 
   
    def __init__(self,ticket,seat):
        self.ticket = ticket
        self.seat   = seat

    def bookTicket(self):                       
        return f" Your {self.ticket} ticket is booked now "

    def getStatus(self):
        print(f"{self.running_train} is now ready to go. !")
        print(f" You have booked {self.ticket} tickets")
        print(f"The ticket amount of {self.ticket} is  {self.ticket*100}")
        

    def getFare(self):
        return f" Because Fare is 100 rs. per seat"

rakesh = Train(5,3)
print(rakesh.getStatus())


# ---------------------------------------------------------------------
# NOTE :Answer 5

# class Xyz:
#     country = "India"
#     city = "Jaipur"

#     def __init_(harry,name,age,game):
#         harry.name = name
#         harry.age = age
#         harry.game = game

# # rakesh = Xyz("rakesh",25,"counter_Strike")
# rakesh = Xyz()
# print(rakesh.country)
# print(rakesh.city)
# # print(rakesh.name)

# ---------------------------------------------------------------------
# NOTE :Answer 6

# ---------------------------------------------------------------------
