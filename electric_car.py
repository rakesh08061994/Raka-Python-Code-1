#  Define a single inheritance class
# This is Parent class or Base Class (Both are same)
# *************************************************---------------------------------------------*********************************************
class Car:

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # Set value "0" bydefault

    def get_Descriptive_name(self):
        long_name = f"{self.year}, {self.make}, {self.model}"
        return long_name.title()

    def read_Odometer(self):
        return f"This cars has {self.odometer_reading} miles on it."

    def update_odometer(self,milage):
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            return f"Odometer from {self.odometer_reading}  to down, can't roll back"

    def increment_Odometer(self,miles):
        self.odometer_reading += miles

    def fill_Gas_Tank(self):
        """ cars have gas tanks."""
        print("This car need a gas tank!")

# *************************************************---------------------------------------------*********************************************
# Instances as Attributes
class Battery:
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self,battery_size = 75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_Battery(self):
        """Print a statement describing the battery size."""
        return (f" This car has a {self.battery_size}-KWH Battery. ")

    def get_Range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            flag1 = 260
        elif self.battery_size == 100:
            flag1 = 315
        return f"This car can go about {flag1} miles on a full charge"
# *************************************************---------------------------------------------*********************************************
    
# This is child class, derived class (both are same ), That inherits all the attributes and methods from parents class Car()

class ElectricCar(Car):         # Inherits parents class by base child class, closed in paranthesis brackets

    def __init__(self,make,model,year):
        """Initialize attributes from parent class"""
        super().__init__(make,model,year)
        ## self.battery_size = 75              # Add a instance attribute of child class and set its initial value 75 to it

        """ ( self.battery_size = 75 ) This attribute will be associated with all instances created from the
            ElectricCar class but won’t be associated with any instances of Car."""

        self.battery = Battery()  # Use a Battery class instance as an attribute


   # # def describe_Battery(self):
   # #     """Print description about battery size"""
   # #     return (f" This car has a {self.battery_size}-KWH Battery. ")

#NOTE: Overriding Methods from the Parent Class
        """To do this, you define a method
        in the child class with the same name as the method you want to override in
        the parent class. Python will disregard the parent class method and only
        pay attention to the method you define in the child class."""

    def fill_Gas_Tank(self): # Overriding Methods from the Parent Class
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")     

# *************************************************---------------------------------------------*********************************************
# Create an instance of Electricar Class, That has all possible attributes & Methods derrived from parents class 'Car()' as an inheritance

my_tesla = ElectricCar("Tesla", "model s", 2019)

# print(my_tesla.get_Descriptive_name())
# print(my_tesla.describe_Battery())

# print(my_tesla.fill_Gas_Tank())     # Desregard parents class method, and pay attention to clid class method
                                    # NOTE: This car doesn't need a gas tank
print(my_tesla.battery.describe_Battery())
print(my_tesla.battery.get_Range())














# NOTE : 
"""There’s no limit to how much you can specialize the ElectricCar class (Derrived/Child class).You can add as many 
   attributes and methods as you need to model an electric car to whatever degree of accuracy you need. """

    