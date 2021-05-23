class Employee:
    company = "Google"

    def getSalary(self):
        print(f" Salary for {self.name}, working in {self.company} is {self.salary}")


rakesh = Employee()
harry = Employee()

 


rakesh.salary = 100 # instance personal attribute (Not class attribute)
harry.salary = 200  # instance personal attribute (Not class attribute)


print(rakesh.company)   # access class attribute by class instance
print(harry.company)    # accessing class attribute by class insyance


# rakesh.getSalary()  # --------------- >  Employee.getsalary(rakesh)
# harry.getSalary()   # --------------- >  Employee.getsalary(harry)

