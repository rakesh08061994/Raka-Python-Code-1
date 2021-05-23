# Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and
#  then using following rules print their place of service.
# if employee is female, then she will work only in urban areas.
# if employee is a male and age is in between 20 to 40 then he may work in anywhere
# if employee is male and age is in between 41 t0 60 then he will work in urban areas only.
# And any other input of age should print "ERROR".


age = int(input("Enter Your Age:   "))
sex = input("Enter Your Sex (M/F):   ")
# Marital_Status = input("Enter Your Marital Status(Y/N):  ")

if(sex == "F"):
    print("You will work only in urban areas.")
elif((sex == "M") and ((age <= 40) and (age >= 20))):
    print("You may work at anywhere")
elif((sex == "M") and ((age >= 41) and (age < 60))):
    print("You will work in urban areas only !")
else:
    print("Error")