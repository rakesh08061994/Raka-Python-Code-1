
#  Using a flag in while loop to tell the program a stop signal when program, get so big  difficlt and conditions in program is so many
# for example in a game program, the program should not only stop when we type "quit" manualy. 
# It should have stop only if when one condition in multiple conditions become false and it act as multiple trigger or flag to monitor the program
#   
# When the player runs out of ship, player fall in fire or cold water sea. all cities is distroyed by the enemy which he come to protect.
# the game should end 



active = True       # This is flag or count 
while active:       # endless loop till condition not become false
    message = input("Enter secret text to end the game !:    ")
    if message == 'quit':   #Flag1
        active = False
    if message == "save me": # Flag2
        active = False
    if message == "die": #Flag3
        active = False
    else:
        print("Not secret text. Send back to type ")
else:                    # After program end or quit
    print("Good ! You type authenticate text !")
    print("You are free. i send you In the else block at the end. ")