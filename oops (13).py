#  A class method is a method which is bound to the class, not the object of the class.

class Employee:
    salary = 500

    @classmethod
    def changeSalary(cls,sal):
        cls.salary = sal


e = Employee()

print(e.salary)
print(Employee.salary)

# e.salary = 1111         # Create instance attribute, not class attribute

# print(e.salary)         # Only changed instance attribute,
# print(Employee.salary)  #  class attribute remain with previous value

#  But when we call changeSalary() method

e.changeSalary(45250)

print(e.salary)             # go with instance attribute value=1111
print(Employee.salary)      # Origional class attribute value permanently changed with 45250



