# '''
# Reading a Python File
# There are several ways to read a text file in Python. Here are the most common ones:
# with the readlines() method
# with ‘while’statement
# with an iterator
# with the ‘with statement’
# '''

# # readline method :

# open_file = open("information.txt","r")
# read_file = open_file.readline()
# print(read_file)

# note = "File attributes that can provide a number of important information about that file."
# print(f"\n{note} \n")
# print("File name : ",open_file.name)
# print("File mode : ",open_file.mode)
# print("File closed or not : ",open_file.closed)

# # ------------------------------------------------------------------------------------------------------

# # Ask people to about there winter vacation plan and append to all these in a file, suppose first time file is an empty file, and program should be not stop or break
# file = "Blank_file.txt"
# with open(file) as open_file:
#     read_file = open_file.read()

#     while True:
#         ask = input("Where will you go this winter ? : ")
#         if ask.lower() == "q":
#             break

#         elif read_file == "":
#             with open(file,"w") as open_file:
#                 write_file = open_file.write("%s \n"%(ask))

#         elif len(read_file) >= 1:
#             with open(file,"a") as open_file:
#                 write_file = open_file.write("%s \n"%(ask))

