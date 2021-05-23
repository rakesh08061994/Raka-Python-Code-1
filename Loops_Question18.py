# Using  Break to Exit a loop

prompt = "\n Please enter the name of the city you have visited."
prompt += ("\n Enter 'quit' to finished")

while  True:
    city = input()
    if city == 'quit':
        break                       # break terminate the program immidately, when conmdition meet or satisfy. (not lower code execute)
    else:
        print(f"I'd Love go to {city.title()} !")
