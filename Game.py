import random               # Import Random Module 
def SWG_Game(user):         # Create a function named "SWG_Game" with one positional argument user as input
    """This is popular game Snake/Water/Gun, Take one user input from s/w/g and return result"""
    computer = random.choice(["s","w","g"]) # choice function To prevent cheating between players, we use random choice from computer
    flag = ""                               # Declare flag as empty string
    if(computer == user):                   # Both value are same
        flag =  None                        # flag will be None
    elif((computer == "s") and (user == "w")):  # all possible Game conditions apply
        flag =  False                           # If computer win and we lose the condition then flag is False
    elif((computer == "s") and (user == "g")):
        flag = True                             # If computer Lose and we win the condition then flag was True

    elif((computer == "w") and (user == "s")):
        flag =  True
    elif((computer == "w") and (user == "g")):
        flag =  False

    elif((computer == "g") and (user == "s")):
        flag =  False
    elif((computer == "g") and (user == "w")):
        flag =  True

    print(f"Computer Turn was {computer}\n Your turn is {user}")    # Show Both turn display during result declare
    if flag == None:                                                # If flag is None
        return ("\t\t********** Match is Tie **********")           # return this message
    elif(flag):                                                     # If flag is True  
        return ("\t\t********** You Win **********")                # return this message
    else:                                                           # If flag is false
        return ("\t\t********** You Lose **********")               # return this message



# Function Calling by user

TakeInput = input ("Enter Your Turn : ")
# print(SWG_Game(TakeInput))                                      # ( Using Positional Argument)
print(SWG_Game(user=TakeInput))                                   # ( Using Keyword Argument, and more is available "Default value at function declaration time")

