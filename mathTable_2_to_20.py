for num in range(1,41):

    for i in range(1,11):

        table = f"{num} X {i} = {num * i}\n"
        print(table,end="")

        file_name = f"File{num}.txt"
        with open(file_name,"a") as open_file:
            write_file = open_file.write(table)