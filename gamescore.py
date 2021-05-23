# Function Defination with none parameter
def gameScore():
    """return score in int"""
    return 11542

# Functon Calling with none argument
score = gameScore()


with open("highscore.txt") as open_file:
    read_file = open_file.read()

    if read_file == '':
        with open("highscore.txt","w") as open_file:
            write_file = open_file.write(str(score))

    elif int(read_file) < score:
        with open("highscore.txt","w") as open_file:
            append_file = open_file.write(str(score))
            print(f"Update score with {score}")
    
    else:
        print("No Hi-Score Available.")


