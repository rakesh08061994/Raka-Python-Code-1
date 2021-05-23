# Write a program to check if a year is leap year or not.
# Note: If a year is divisible by 4 then it is leap year.
#  Note: If the year is century year like 2000, 1900, 2100 then it must be divisible by 400

Year = int(input("Enter The Year:  "))
if(Year % 4 == 0):
    print("This year is a leap year !")
else:
    print("This is not a leap year ! ")