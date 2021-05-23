try:
    num = int(input("Enter Number : "))
    print("you entered %d." %num)
except ValueError:
    print("I am except")
else:
    print("I am ELse block")
finally:
    print("I am Finally")

    

