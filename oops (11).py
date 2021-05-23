class Calculator:

    def __init__(self,num):
        self.num = num

    def square(self):
        return self.num ** 2

    def cube(self):
        return self.num ** 3     

    def squareRoot(self):
        return self.num ** 0.5

    @staticmethod           # ----------- > This is a static method
    def greet():
        print("Hello User !")



obj1 = Calculator(5)



print(obj1.square())            #print(Calculator.square(obj1))
print(obj1.cube())
print(obj1.squareRoot())


obj1.greet()    #----------> Call the class Calculator's static method greet() by class instance obj1 

