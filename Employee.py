class Employee:

    def __init__(self,first,last,pay):          # __init__ is a constructor not method  
        self.first = first
        self.last = last
        self.pay = pay
        self.mail = first.lower() + '.' + last.lower() + '@company.com'


    def fullname(self):
        return self.first+ " " +self.last

    
# Instantiation of class object 
emp1 = Employee("Rakesh","Jangid",50000)      # Create a object of a class Employee()
emp2 = Employee("Parul","Yadav",60000)        # Create one more object of a class Employee()


# Access Class Attribute
print(emp1.first)
print(emp1.last)
print(emp1.pay)
print(emp1.mail)

print(emp2.first)
print(emp2.last)
print(emp2.pay)
print(emp2.mail)

# Access Class methods (Don't Forgot to use paranthesis() with method name)
print(emp1.fullname())      #print(Employee.fullname(emp1)) Both mean the-same thing
print(emp2.fullname())      #print(Employee.fullname(emp2))





