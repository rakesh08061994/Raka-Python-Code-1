# Take input of age of 3 people by user and determine oldest and youngest among them.
age1 = int(input("Enter Your age:  "))
age2 = int(input("Enter Your age:  "))
age3 = int(input("Enter Your age:  "))

if((age1 > age2) and (age1>age3)):
    print(age1, "is biggest")
elif((age2 > age3) and (age2>age1)):
    print(age2, " is biggest")
elif((age3>age2) and (age3>age1)):
    print(age3, "is greatest")
else:
    print("All age are equal")
    
