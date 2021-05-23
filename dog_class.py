# To define a class, you will use the keyword class followed by a class identifier and a colon.

class dog:
    """Class is a blueprint of an object  (to make a vaild object)
     A Class have attributes and methods """
    name = "Kutta"  # Class Attributes (That uses for each object equaly)
    sex = "male"
    color = "white"
    voice = "bark"
    age = 10

    def sought(self): # Class functions 1
        return "Aoooo"

    def fight(self):   # Class functions 2
        return "AAA AAA AAAA AAAA Huuuu Huuu Hoooo"

    def love(self):   # Class functions 3
        return "ammmm... ammmmm..."
    
    def beatan(self):   # Class functions 4
        return "Piyaann...."

#  To instantiation of an object or to create a valid object use equal operator and define object with class name and paranthesis()

mini = dog()            # Object instantiation
ana = dog()             # object instantiation

#  To use class attributes by an object use attribute with dot after object instantiation and print it

print(mini.name)
print(ana.name)
print(mini.color)
print(ana.color)
print(mini.voice)
print(ana.voice)
print(mini.sex)
print(ana.sex)


# print(mini.age)    # Object mini use class attribute age = 10
# To Initiate instance attributes for an object (Now these attributes called Object attributes, or objects unique/different entity)
# object.instance_attribute = Value

# mini.age = 45   #(Now that object initiate after previous class attributes. so even after object fetched instance attribute first)
# print(mini.age)  # 45
# print(ana.age)   # 10 (Because object ana doesn't make instance object age )

mini.sex = "female" # Instance attributes for object ana with sex attribute

print(mini.sex)




#  To use class metod/function use function after object instantiation with paranthesis()
# print(mini.sought())
# print(ana.sought())

# print(mini.beatan())
# print(ana.beatan())

# print(mini.fight())
# print(ana.fight())

# print(mini.love())
# print(ana.love())

print(type(ana))

