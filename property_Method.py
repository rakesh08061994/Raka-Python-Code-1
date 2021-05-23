class Employee:
    company = "Bharat Gas"
    salary = 10000
    bounus = 400
    totalsalary = 0             #Bydefault set = 0   # This is static not dynamic (what happen, when bonus will change each month. and employee is thousands)
                                        # So we have to make totalsalary as a dynamic attribute to set according to salary + bonus each month


#  for this we will define a method as totalsalary with @property method, that is actualy a function but it will shown as a class attribute 
# so we donnt worry about changable salary and bonus. @property is known as "getter" method


    @property                   # getter @property
    def totalsalary(self):      # work as a function, but call like a class attribute
        return self.salary + self.bounus

    @totalsalary.setter
    def totalsalary(self,bns):
        self.totalsalary = self.salary - bns

# adjust salary or bonus according to totalbonus, when user set instance value for totalsalary
# e.totalsalary = 123456             # set instance value to class attribute
#  for this we use "setter" method


e = Employee()
# print(e.salary)             # 10000
# e.totalsalary
# print(e.totalsalary)        # call dynamic class attribute

e.totalsalary  = 12345 

print(e.salary)
print(e.totalsalary)



