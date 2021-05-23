#NOTE : However sometimes it's important to check all the conditions of intrest. In this case you should use a series of simple if statement
#       with no elif and else block. This technique make sense when more than one conditons could be true, and you can do act on each condition
#       that is true, which you want to.
# ------------------------------------------------------------------------
# NOTE When you want to check every conditions and situations :

# requested_toppings = ['mushrooms', 'extra cheese']
# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms")
# if 'pepproni' in requested_toppings:
#     print("Adding pepproni")
# if 'extra cheese' in requested_toppings:
#     print("Adding extra cheese")
# print("Your Pizza is ready !")

# -----------------------------------------------------------------------
# NOTE: This code would not work properly if we used an if-elif-else block, Because code would stop after one test pass. 

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
elif 'pepproni' in requested_toppings:
    print("Adding pepproni")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese")
else:
    print("Your Pizza Is ready !")