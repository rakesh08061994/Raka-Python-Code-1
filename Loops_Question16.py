#NOTE: while loop mostly used in day to day life work progam, and game play.
#  when we want to quit the game/program only then program or game will end, otherwise it will not quit.

message = ""

while message != 'quit':                # You have to write 'quite' to stop game, otherwise it will awake or run continuesly 
    message = input()            # input prompt for the user to take input with message
    print(message)                      # Print message


