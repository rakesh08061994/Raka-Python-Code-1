# Upgrade in Question8.py
# Modify the above question to allow student to sit if he/she has medical cause.
#  Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.

Total_class = int(input("Enter Total Number of classes held:  "))       # Total Classes Held
Attendence = int(input("Enter Your Total Attendence: "))                # Total Attendence of student
Medical_Cause = input("Any Medical Cause: (Y/N): ")                     # Medical Causes (Y/N)

if((Attendence >= ((Total_class*70)/100)) or (Medical_Cause == "Y") ):      # Two conditions Statement 
    print("You are allowed to sit in exam !")
else:
    print("You are not allowed")
