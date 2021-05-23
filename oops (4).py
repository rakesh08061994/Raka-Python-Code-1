class Animal:

    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        return (f"Name = {self.name},age = {self.age}, sex = {self.sex}")



class Pets(Animal):
    def __init__(self, name, age, sex):
        super().__init__(name, age, sex)
    
    def __str__(self):
        return (f"Name = {self.name},age = {self.age}, sex = {self.sex}")



class Dog(Pets):
    def __init__(self, name, age, sex):
        super().__init__(name, age, sex)

    def __str__(self):
        return (f"Name = {self.name},age = {self.age}, sex = {self.sex}")

    def barkDog(self):
        return "Bao, baooo, baoo.. hurrrrrmm"




mini = Dog("Mini", 1, "Female")
print(mini)
result = mini.barkDog()
print(result)


parrot = Pets("Hari", 1, "Male")
print(parrot)