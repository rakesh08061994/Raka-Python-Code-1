# Write a program to print absolute vlaue of a number entered by user. E.g.-
# INPUT: 1        OUTPUT: 1
# INPUT: -1        OUTPUT: 1

num = int(input("Enter The number:  "))
if (num < 0):
    print(num*-1)
else:
    print(num)