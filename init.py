class Employees:
    "Common base for all employee"
    counter = 0

    def __init__(self,name,position,salary):        # __init__ is a Constructor
        self.name = name
        self.position = position
        self.salary = salary

    def office(self):
        return "Be Positive, Dont quit !"


emp1 = Employees("Rakesh","2nd",30000)
print("emp1 salary is: ",emp1.salary)
print("emp1 position is: ",emp1.position)
print("emp1 name is: ",emp1.name)

emp2= Employees("Parul","1st",35000)
print("emp2 salary is: ",emp2.salary)
print("emp2 position is: ",emp2.position)
print("emp2 name is: ",emp2.name)

print(emp1.office())
print(emp2.office())



