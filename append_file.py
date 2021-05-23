with open("poems.txt") as open_file:
    read_file = open_file.read()
    result = read_file.find("above")
    print(read_file[result:])
    # print(result)


