class NewClass:
    "This is a New Class"
    x = 5      # Define Class Attributes (Every Object can access these class attributes, If object dont inisiate attribute instance with same attribute value ) 


"""You probably notice the parameter ‘self’ in function definition inside classes. Yet, when
the method obj.func was called without an argument, Python went on with the process and
did not raise an error. That is because the object itself is passed as the first argument. In
Python, when an object calls its method, the object automatically becomes the first
argument. By convention, it is called ‘self’. You can use any name but for uniformity, it is
best to stick with the convention. If you need to place more arguments, you have to place
‘self’ as the first argument.
"""

    def Func(self):
        # print("I'M a function object")   # Return None Data Type
        return ("I'M a function object")   # Return message without None


obj  = NewClass()
print(obj.Func())

