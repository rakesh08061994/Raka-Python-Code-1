#  Ask people to about there winter vacation plan and append to all these in a file, suppose first time file is an empty file, and program should be not stop or break
file = "Blank_file.txt"
with open(file) as open_file:
    read_file = open_file.read()    # read_file has all content material of file

# infinity time code will run except press 'q' to break the loop
    while True:
        ask = input("Where will you go this winter ? : ")
        if ask.lower() == "q":
                break
#  If file are empty then this code will work
        elif read_file == "":
            with open(file,"a") as open_file:
                write_file = open_file.write("%s \n"%(ask))


#  and then file has minimum 1 str in file, then this code will run 
        elif len(read_file) >= 1:
            with open(file,"a") as open_file:
                write_file = open_file.write("%s \n"%(ask))
