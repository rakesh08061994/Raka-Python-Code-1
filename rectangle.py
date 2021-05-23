class Rectangle():
    "class_name(length,bredth,unit_cost=0)"
    

    def __init__(self,length,bredth,unit_cost): # Create __init__ method for object to access class attribute & methods
        self.length = length
        self.bredth = bredth
        self.unit_cost = unit_cost

    def get_area(self):
        return  self.length * self.bredth

    def calculate_cost(self):
        area = self.get_area        # Multiple time function calling in other function of same class
        return area * unit_cost

    

r = Rectangle(160,120,2000)   # These instance object values will assign to class attributes and access via __init__ method 

print(r.get_area())




