#  @Property decorator method change class property dynamically.
# Also known as Getter() methhod

class Employee:
    salary = 1000
    bonus = 50

    @staticmethod
    def greet():
        print("Welcome Python.")

    @property
    def totalSalary(self):
       return self.salary + self.bonus

    @classmethod                        
    def changeBonus(cls,val):
        cls.bonus = val

    @totalSalary.setter                 # because we changed totalSalary value (e.totalSalary value = 37500)
    def totalSalary(self, set_val):
        self.bonus = set_val - self.salary


e = Employee()

print(e.greet())             # Static Method
print(e.totalSalary)         # 150

e.changeBonus(456555555)     # Class Method
print(e.totalSalary)         # Property/Getter(method)

e.totalSalary = 37500       # set instance attribute (method in actually), 37500

print(e.totalSalary)

print(e.bonus)

