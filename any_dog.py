#  A class may have lots of classes, function and attributes
# In python everythng is an object with his method and data type 


class Dog:                  # Define a class Dog (in Pascal written)
    """A simple attempt to model a dog.""" # __Doc__ str  about a class dog

    def __init__(self,name,age):           # Define a __init__ method with two object attribute.(Each time when object use method or attribute, __init__ will call by the object instance class)
        self.name = name                    # name Attribute 
        self.age = age                      # age Attribute

    def sit(self):                          # define a function in dog class(A verb for a noun)
        """Simulate a dog sitting in response to a command. """
        return (f"{self.name} is now sitting on command.")

    def roll_over(self):                    # define a one more function in dog class
        """Simulate a dog roll_over in response to a command."""
        return (f"{self.name} is now roll_over on command")


#  We can access dog class attributes & class methods/functions to make instance (object)  of a class.
#  we can also make instance attributes for each instance(object) to make each instance unique to other object

#  to access class attributes by a instance object, first make a instance object of a class


my_dog1 = Dog("mini",10)            # Make a instance object of a class and assign argument value as init required
my_dog2 = Dog("ana",25)            # Make one more instance object of same class

# Now we can access class attributes & functions using object

# print(my_dog1.sit())            # to access method/function use with instance object as prefix and then function name and then close with paranthesis
# print(my_dog1.roll_over())

# print(my_dog2.sit())        # Instance Object (as prefix). function Name and paranthesis ()
# print(my_dog2.roll_over())  # Instance Object (as prefix). function Name and paranthesis ()

# print(my_dog1.name)         # to access attributes no need of paranthesis
# print(my_dog1.age)          # to access attributes no need of paranthesis but class instance(as prefix). class attributes

# print(my_dog2.name)
# print(my_dog2.age)


#  To use instance attributes of a class object(for object uniqueness, Each object has there different attributes/adjective)

#  Define a instance attribute:   object_name.new_attribute = value
#  These attributes are called as object's instance attriutes(Different adjective of a object)

my_dog1.color = "Red_Black"    # mini color is "Red_Black"
my_dog2.color = "white"    # ana color is "white"

my_dog1.sex = "male"        # mini is a male dog
my_dog2.sex = "Female"      # ana is a Female dog

print(f"{my_dog1.name} is {my_dog1.color} in color and, It is a {my_dog1.sex} Dog\n If we command {my_dog1.sit()} and {my_dog1.roll_over()}")
print(f"{my_dog2.name} is {my_dog2.color} in color and, It is a {my_dog2.sex} Dog\n If we command {my_dog2.sit()} and {my_dog2.roll_over()}")

