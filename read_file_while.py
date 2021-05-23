open_file = open("information.txt")


read_file = open_file.readline()                     # Define readline variable as True to enter in while loop
while read_file:
    read_file = open_file.readline()
    print(read_file)
open_file.close()




