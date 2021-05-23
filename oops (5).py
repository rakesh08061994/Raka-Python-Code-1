class Employee:
    salary = 1000
    increment = 50
    # salaryAfterIncrement = 1050

    @property                           # @property decorator method, Also known as getter function
    def salaryAfterIncrement(self):
        return self.salary + self.increment

    @salaryAfterIncrement.setter        # .setter() method decorator, known as setter
    def salaryAfterIncrement(self,i_value):
        self.increment = i_value - self.salary



rakesh = Employee()
# print(rakesh.salaryAfterIncrement)
    
rakesh.salaryAfterIncrement = 5000

print(rakesh.salary)
print(rakesh.increment)
print(rakesh.salaryAfterIncrement)