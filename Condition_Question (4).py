# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.

salary = int(input("Please Enter Your salary:  "))
job_year = int(input("Please Enter Your job service experience (IN YEAR):  "))

if(job_year > 5):
    print("Company decide to give you 5% Bonus on your 5 year valuable service ")
    print("Net Bonus Amount is : ", ((salary*5)/100) + salary )
else:
    print("Your salary is: ", salary)
