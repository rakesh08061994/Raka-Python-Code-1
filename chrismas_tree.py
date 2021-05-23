
try:
    num = int(input("3,5,7,9,11....  :  "))
    count = num
    if num%2 == 0:
        print("Tree will not make proper \nPlease Enter Odd Number !")
    else:
        for i in range(1,num+1,2):
            print(f"{count * ' '} {i * '*'}")
            print(f"\2[33m{count * ' '} {i * '*'}\2[m")
            count -= 1
except ValueError:
    print("Use only Odd Integer Value !")
