# A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.


Total_class = int(input("Enter Total Number of classes held:  "))
Attendence = int(input("Enter Your Total Attendence: "))

if(Attendence >= ((Total_class*70)/100)):
    print("You are allowed to sit in exam !")
else:
    print("You are not allowed")

    