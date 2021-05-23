class Employee:
    salary = 100
    company = "Honda"
    location = "Delhi"


# NOTE: What is @classmethod decorator: This is a special kind of decorator method, that take function as an input and change value of it, when ever we use it
# NOTE: __class__ is called as "dender" method in python oop terminology

# -------------------------------------------------------------------------------------------------------------------------


# using classmethod, we are able to change class attribute forever by instance, each time whenever we call this function
    # def change_Salary(self,sal):
    #     self.__class__.salary = sal



# insted of .__class__. method, we use just "cls" both end on place of "self", and use @classmethod decorator 
    @classmethod
    def change_Salary(cls,sal):
        cls.salary = sal

e = Employee()
# print(e.salary)
# print((e.company))
# print((e.location))


#  To change class attribute forever, whenever we want : we have to create new class attribute or instance attribute

# e.salary = 455
# print((e.salary))               # class attribute change for instance, but not for class himself 

# print((Employee.salary))        # 100 still class attribute not changed

# Employee.salary = 500             # This is one way to change, class attribute or we can make its a class method for this(only by class itself)

print((e.salary))

print(Employee.salary)

e.change_Salary(100000)             # but using classmethod, we are able to change class attribute forever by instance, each time whenever we call this function

print(e.salary)                         #100000
print(Employee.salary)                  #100000

