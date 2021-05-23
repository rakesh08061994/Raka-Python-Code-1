# requested_toppings = ['mushrooms','green paper','extra cheese']        # This is requested by the user in the form of list (we can use use here user input())
# for requested_topping in requested_toppings:
#     print(f"adding {requested_topping}")
# print("Pizza is getting ready")

# ---------------------------------------------------------------------------------------------------------------------
#NOTE:  If green paper is not available in cafeteria, use if else condition in for loop to recover this situation.

# requested_toppings = ['mushrooms','green paper','extra cheese']         # This is requested by the user in the form of list (we can use use here user input())
# for requested_topping in requested_toppings:
#     if requested_topping =='green paper':
#         print('Sorry ! we are out of green paper right mow')
#     else:
#         print(f"adding {requested_topping}")
# print("Pizza is getting ready")

# ---------------------------------------------------------------------------------------------------------------------

# requested_toppings = []                                     # This is null requested by the user in the form of list (we can use use here user input())
# for requested_topping in requested_toppings:
#     if requested_topping =='green paper':
#         print('Sorry ! we are out of green paper right mow')
#     else:
#         print(f"adding {requested_topping}")
# print("Are You sure you want a plain pizza !")


# ---------------------------------------------------------------------------------------------------------------------

available_toppings = ['mashrooms','olives','green paper','pepproni','pinapple','extra cheese']  # stock of cafeteria
requested_toppings = ['mashrooms','french fries','extra cheese' ]           # Can input from user directly

for requested_topping in requested_toppings:            # requested_topping is variable here ! who will check each element from requested_toppping
    if requested_topping in available_toppings:         
        print(f"Adding {requested_topping}")
    else:
        print(f"We dont have {requested_topping}, right now.")
print("Finished making your pizza")