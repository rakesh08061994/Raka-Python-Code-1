# If - Elif - Else Condition 
# Two stocks takes different time to make a order ready. Use if, elif, else condition 

stock1 = ["tea","coffee","pizza","sandwich","hot coffee","cold coffee","cold drink","choco lava","pastries","patties","maggie"]
stock2 = ["patashi","dahi balle","kulche","soup","rice","idli sambhar","shakes"]

order = input("Enter Your Order Please:  \n")

if(order in stock1):
    print("Order will be ready within 5 minutes !")

elif(order in stock2):
    print("if you have much time")
    print("Order will take 15 minutes to make")

else:
    print("We dont serve ", order , " at this moment !")
