# A 4 digit number is entered through keyboard. 
# Write a program to print a new number with digits reversed as of orignal one. E.g.-
# INPUT : 1234        OUTPUT : 4321
# INPUT : 5982        OUTPUT : 2895


number = int(input("Please Enter Your 4 digit Number:  "))
a = (number // 1000)*1000                           
b = (number % 1000)                              
c = (b % 100)                              
d = (c % 10)                               

# Reverse Number         
d=(d * 1000)     
c=(c // 10) * 100   
b=(b // 100) * 10
a=(a // 1000) * 1 

print(d+c+b+a)

