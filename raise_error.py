while True:
    value = input("Continue Y/N ")
    if value.lower() == "n":
        print("OK")
        break
    try:
        value = int(input("Enter a positive number : "))

        if value <= 0:
            raise ValueError("Thats not a positive number ")
    except ValueError as variable_assign:
        print(variable_assign)
    else:
        print("Bingo !")





