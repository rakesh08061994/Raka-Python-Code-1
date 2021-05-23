#     A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.

# print(" Discount of 10% if the cost of purchased quantity is more than 1000")
# print(" Suppose, one unit will cost 100.")


quantity = int(input("Enter the unit of purchased product "))
if (quantity > 10):
    print("You have get 10 % Discount on your Purchase !")
    print("your purchase quantity is more than 1000 ")
    print("Your total purchase is", 100*quantity)
else:
    print("Your price is", 100*quantity)

