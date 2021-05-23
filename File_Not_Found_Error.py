try:
    file = "sample1.txt"
    with open(file, encoding='utf-8') as open_file:
        append_file = open_file.read()
except FileNotFoundError:
    print(f"Sorry '{file}' file does't exist !")
except IOError:
    print(f"'{open_file.mode}' mode is not correct for the file operation")
    print("Check Your open file mode !")
else:
    print(append_file)




# Find Particular Text into file with line number and length of character 
counter = 0
with open(file) as open_file:
    for i in open_file:
        length = len(i)
        counter += 1
        if "love" in i:
            print(f"Yes in {counter} line")
            print(f"this line has {length} character length")

        





