# Define a class Employee using 'class' keyword

class Employee:
    '''Define a class with attributes and methods/functions'''
    company = "Google"

    def getSalary(self):            # This is a static method (function that does't use self parameter, or simple print )
        '''return salary information'''
        return "Salary is not there !"

rakesh = Employee()
parul = Employee()

# print(rakesh.company)     #Google (Because no instance attribute is exist yet)
# print(parul.company)      #Google (Because no instance attribute is exist yet)



print(rakesh.getSalary())   # Call class function from rakesh instance
print(parul.getSalary())    # Call class function from parul instance

rakesh.company = "YouTube"  # Initiate instance attribute

print(rakesh.company)       #YouTube
print(parul.company)        #Google #(Because instance attribute is exist)