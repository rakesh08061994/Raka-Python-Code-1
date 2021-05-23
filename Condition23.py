
banned_users = ['andrew','carolina','david']
user = 'marie'
if (user not in banned_users):      # Condition True
    print("In if Block !")
    print(user)
    print(user.title())
    print(user.title(), ", you can post a response if you wish")
    print(f"{user.title()}, you can post a response if you wish")       # F{} used to print variable in print
else:
    print("In Else Block ! ")
    print("User in banned_users")