class Employee:
    company = "Google"

    def getSalary(self, signature):
        print(f" Salary for this person, working in {self.company} is {self.salary} \n {signature}")

    @staticmethod           #@staticmethod Decorator
    def greet():
        print("Good Morning Sir !")


rakesh = Employee()
harry = Employee()

rakesh.salary = 100 # instance personal attribute (Not class attribute)
harry.salary = 200  # instance personal attribute (Not class attribute)

# print(rakesh.company)   # access class attribute by class instance
# print(harry.company)    # accessing class attribute by class insyance

# rakesh.getSalary()  # --------------- >  Employee.getsalary(rakesh)

# harry.getSalary(" Thanks !")   # --------------- >  Employee.getsalary(harry)
# harry.getSalary(" welcome !")   # --------------- >  Employee.getsalary(rakesh)

rakesh.greet()
harry.greet()


