# NOTE: @property method is also known as getter(get Attribute as an property)


class Employee:
    company = "Google"
    salary = 1000
    bonus = 90
    # totalsalary = 1055

    @property                               #property method(seems like an class atribute but actualy is a function)
    def totalsalary(self):
        return self.salary + self.bonus


e = Employee()

print(e.totalsalary)    # 1090 (call as an attribute, but work like an function)
# print(e.totalsalary())


