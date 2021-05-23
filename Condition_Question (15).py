# If - Else Condition
# This program check food in stock and print appropriate message !

stock = ["tea","coffee","pizza","sandwich","hot coffee","cold coffee","cold drink","choco lava","pastries","patties","maggie"]
print("Food Stock Available ", stock)
order = input("Enter your order please:   ")
if(order in stock):
    print("Your order will take minimum 5 minutes to be ready : ")
else:
    print("Sorry! This order is not in our menu ")
