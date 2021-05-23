# The Open() function
# The open() function facilitates the opening of a file for reading, writing or both. It creates
# a file object, also called a handle, that you can use to call other methods that can be used with the function. 
# Its syntax is: file object=open(filename [, access_mode][, buffering])

# OPen File and read content using open with read mode

open_file = open("sample.txt","r")
read_file = open_file.read()
print(read_file)
open_file.close()

note = "File attributes that can provide a number of important information about that file."
print(f"\n\n {note} \n")
print("File name : ",open_file.name)
print("File mode : ",open_file.mode)
print("File closed or not : ",open_file.closed)


