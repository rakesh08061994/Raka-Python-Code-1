class person:
    # Class Attributes (adjective)
    country = "India"
    state = "Rajasthan"
    city = "Jaipur"
    religion = "Hindu"

    def spritual(self):
        return "Hari Om !"
    
    def angry(self):
        return "M#@%$#$&%$#$"
    
# Rakesh Objects Instance attributes (object attributes)
rakesh = person()
rakesh.age = 255
rakesh.sex = "Male"
rakesh.salary = 25000

# parul object's instance attributes (Object attributes)
parul = person()
parul.age = 25
parul.sex = "Female"
parul.salary = 30000

piyush = person()

print(piyush.country)
print(piyush.city)
print(piyush.religion)
print(rakesh.angry())
print(piyush.spritual())

print(parul.sex)
print(rakesh.sex)
print(parul.salary)
print(parul.age)
print(rakesh.age)


#  Class Attributes for each object(Each object derived these attributes till, no any instance attributes created of related object)
print(rakesh.religion)
rakesh.religion = "Sikh"  # (religion attributes) Instance Attributes Created for rakesh object
print(parul.religion)
print(piyush.religion)
print(rakesh.religion)






