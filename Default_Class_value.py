class Car:
    """Define a simple car description class"""

    def __init__(self,make,model,year):
        """Define __init__ method with three parameter"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0   # define default value zero to odometer attribute


    def get_descriptive_name(self):
        """Define get_descriptive_name() method to return descriptive info"""
        return (f"Make Year : {self.make}\nModel Year : {self.model}\nPurchase Year : {self.year}\nOdometer_Value : {self.odometer_reading}")
    
    def read_odometer(self):
        """Print a statement showing the car milage"""
        return (f"This car has {self.odometer_reading} miles on it.")

    
my_new_car = Car("A4","Audi",2019)          # Define a new instance of Car() class with three positional argument

# print(my_new_car.make)          # A4
# print(my_new_car.model)         #Audi
# print(my_new_car.year)          #2019
# print(my_new_car.odometer_reading)  # 0(Default attribute value)

# print(my_new_car.read_odometer())

print(my_new_car.get_descriptive_name())



    
