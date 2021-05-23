class Restaurant:
    """Make a Restaurant class"""
    area = "Food & Bevrages"
    number_served = 10       # set default value 0

    def __init__(self,restaurant_name,cuisine_type):
        """Define __init__ method with two attributes restaurant_name & cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe restaurant information and speciality"""
        print(f"{self.restaurant_name} is best for your dinner destination hotel !")
        print(f"Its speciality in {self.cuisine_type}, must try !")

    def open_restaurant(self):
        """Tell information about restaurant open or not"""
        return (f"{self.restaurant_name} is now open.")
    
    def increment_Number_Served(self,num):
        print(f"customers were served in, a day of business: {num}")


hotel1 = Restaurant("Radission","Ice-Cream")        
# hotel1.describe_restaurant()

# ------------------------------****************************---------------------------******************************---------------------------

class IceCreamStand(Restaurant):    # Inherite parent class Restaurant() in child class IceCreamStand()
    flavours = ["Bacon","Beer","Oreo-Kitket","Blue moon","Butter-Scotch","Paan","Cherry","Vanila","Choclate","Strawberry"]  # New attribute create of child class
    
    
    def display_Flavours(self):
        count = 0
        """Display Various Icecream flavours"""
        for flavour in self.flavours:
            count += 1
            print(f"Flavour No.{count} = {flavour}")

shop1 = IceCreamStand("Laxmi","IceCream")
print(shop1.display_Flavours())
print(shop1.describe_restaurant())



