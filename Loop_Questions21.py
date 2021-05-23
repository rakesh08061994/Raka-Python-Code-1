# # Using while loop with lists and dictionaries

# unconfirmed_users = ['alice','brian','candace']
# confirmed_users = []

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print(f"Verified User Now, {current_user}")
#     confirmed_users.append(current_user)
#     print("The following users have been confirmed")
#     for confirmed_user in confirmed_users:
#         print(confirmed_user.title())



# # ------------------------------------------------------------------------

# pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']  # Create a pets string lists with repeated value elements
# print(pets)                 # print old list and there elements
# while 'cat' in pets:
#     pets.remove('cat')      # all element with 'cat' names deleted in the list
# print(pets)                 # print updated list

# # -----------------------------------------------------------------------------


responses = {}          # Empty Dictionary
poling_active = True    # ensless loop while True
while poling_active:    
    name = input("What is your name ? : ")                                      # Dictionary Key
    response = input("Which mountain would you like to climb someday : ")       # Dictionary value
    responses[name] = response       #  Dictionary filled by the value dict[Key] = value
    repeat = input("Would you like to let another person response ! (Yes/No)")  # Ask users to make it continue or not
    if repeat == 'No':  
        poling_active = False                       # Flag or trigger to make while loop false
print("\-*-*-*-Polling Result Announced-*-*-*-/")
for name, response in responses.items():                # all pair from responses dictionary in form of items will seen 
    print(f"{name} would like to climb {response}")
    

    ------------------------------------------------------------------------------------------------------------------