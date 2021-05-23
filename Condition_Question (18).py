# Find Greatest among 4 or six number enterd by the user
Greatest_Number =  '''
num1 = int(input("Enter Number 1 :  "))     # Take Input from the user
num2 = int(input("Enter Number 2 :  "))
num3 = int(input("Enter Number 3 :  "))
num4 = int(input("Enter Number 4 :  "))

if (num1 > num4):           # >>>>Semifinal Between num1 VS num4
    flag1 = num1            # num1 win
else:                          # OR           # only One number will be win and that will be under flag1
    flag1 = num4            # num2 win


if(num2 > num3):            # >>>>Semifinal Between num2 VS num3
    flag2 = num2            # num2 win
else:                          # OR           # only One number will be win and that will be under flag2
    flag2 = num3            # num3 win


if(flag1 > flag2):          # >>>>Final Between flag1 VS flag2 
    print(flag1, "Is greatest !")
else:                                      # Only One will be Winner !
    print(flag2, "Is Greatest !")
    
'''

print(Greatest_Number)