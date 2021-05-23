# with open('sample.txt','r') as label:             # Open file using 'with' function
#     print("Filename      : ",label.name)                  # Info about file name
#     print("Closed or Not : ",label.closed)           # Info about File are closed or not
#     print("Opening Mode  : ",label.mode)              # Info about file are open in which mode
#     label.close()                                 # Close the file


# ---------------------------------------------------------------------------

# label = open('sample.txt','w')             # Open file using open function
# print("Filename      : ",label.name)                  # Info about file name
# print("Closed or Not : ",label.closed)           # Info about File are closed or not
# print("Opening Mode  : ",label.mode)              # Info about file are open in which mode
# label.close()                                 # Close the file


# ---------------------------------------------------------------------------------------------------------

# NOTE : File access mode
# There are 4 Basic file-related operations in python
# (1)   Opening a file                                                                 =   "open()" or "with open" built-in function 
# (2)   Reading a file                      = Open in 'r' or 'rt' mode                 =   read() or readline() built-in function
# (3)   Writing/appending a file            = Open in 'a' or 'w' mode                  =   write() built-in function
# (4)   Closing a file                                                                 =   close() built-in function

# NOTE ***************************** Open File in Read mode ************************************
# open_file = open('sample.txt','r')            # File already exist so, you can read, otherwise not
# # open_file = open('sample.txt','rt')         # 'rt' is bydefault witj open function 
# # open_file = open('sample.txt')         # Even you can read file, without mentions file read text('rt') or read mode('r') in open function 
# read_file = open_file.read()             # readfile using read() function and store info in read_file variable
# print(read_file)                         # That read_variable we will print using print() function
# open_file.close()                        # .close is must after use the fiile, read(),write 


# # NOTE ***************************Open file in write mode *************************************
# # open_file = open('sample.txt','w')        # file available so only open in write('w') or write text("wt") mode both same thing
# # open_file = open('sample.txt','wt')
# open_file = open('NotExistFile.txt','w')    # Create new one, when file does not exist
# write_file = open_file.write("This is write mode file text, This overwrite previous file data !")
# print(write_file)
# open_file.close()

# NOTE ********************************************Open in append mode *****************************************
# open_file = open('sample.txt','a')  # This is safest mode option to append data with prevent risk to rewite data problem as 'w'write mode.  create a new file if not exist
# append_file = open_file.write(" This is append data using keep append mode and using write() function")
# print(append_file)
# open_file.close()

# # ******************************************Open in r+ (read write mode) at a time ***************************************
# open_file = open('sample.txt','r+') # r+ = read and write data (only updated data entered)
# # read_write_file = open_file.read()
# read_write_file = open_file.write("Text 1")
# print(read_write_file)
# open_file.close()
# ******************************************** Open  in w+ (write read mode) *********************************************
# open_file = open('sample.txt','w+')     # w+ = write read data (wipe out all previous data), create a new file if not exist
# # read_write_file = open_file.read()
# read_write_file = open_file.write("Text 2")
# print(read_write_file)
# open_file.close()

# ********************************************* Open in a+ (append read mode) *****************************************************
# open_file = open('Newfile.txt','a')  #append data at last . Create a new file if not exist
# open_file = open('Newfile.txt','a+')  #append data at last . Create a new file if not exist
# # append_read_file = open_file.read()
# append_read_file = open_file.write("Text 4")
# print(append_read_file)
# open_file.close()


# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# NOTE : Read Small and Big file in python:
# The readline() method is simple and great way to go obver the line of small text file:
#  Large text files are better handled by method that facilitate line by line reading.
#  for this we have two way in python : 
# (1) using while() method
# (2) using iter/for() method

# open_file = open('sample.txt','w')   # Open file in write mode to create some data in sample.txt file

# write_file = open_file.write("This is Text 1 \n")           # Write data using write mode and write() method with new line
# write_file = open_file.write("This is Text 2 \n")
# write_file = open_file.write("This is Text 3 \n")
# write_file = open_file.write("This is Text 4 \n")
# write_file = open_file.write("This is Text 5 \n")
# write_file = open_file.write("This is Text 6 \n")
# write_file = open_file.write("This is Text 7 \n")
# write_file = open_file.write("This is Text 8 \n")
# write_file = open_file.write("This is Text 9 \n")
# write_file = open_file.write("This is Text 10 \n")
# write_file = open_file.write("This is Text 11 \n")
# write_file = open_file.write("This is Text 12 \n")
# write_file = open_file.write("This is Text 13 \n")

# print(write_file)                                           # Print writeable text file
# open_file.close()

# **************************************************************************************************

#NOTE  Now we are ready to use this big file using while() and for() method to read

# Line By Line reading of text files with 'while() loop'
# open_file = open('sample.txt','r')      #Open open_file in readonly mode
# read_file = open_file.readline()        # Display red one line at a time

# while read_file:                        # Using while loop to read line line by line
#     print(read_file)                    # Each line will print of read_file till while read_file
#     read_file = open_file.readline()    # Read_file variable to access readline() in open_file
# open_file.close()                       # Close file
# **************************************************************************************************
# Using iterator or for loop to access large file

# for line in open_file:
#     print(line)
# open_file.close()

# # *************************************************************************************************
# line_num = 0
# with open('sample.txt','r') as open_file:
#     for line in open_file:
#         line_num += 1
#         print(f"{line_num} {line}")                 # Write number continue with print each line
#     open_file.close()
# # ******************************************************************************************************

# Append multiple line in text file using for loop

# open_file = open('sample.txt','a')                                                              # Large file to append using for loop in text file
# write_file = open_file.write(" \nThis is append files using for loop \n")
# write_file = open_file.write(" \nThis is append files using for loop \n")
# write_file = open_file.write(" \nThis is append files using for loop \n")
# write_file = open_file.write(" \nThis is append files using for loop \n")
# write_file = open_file.write(" \nThis is append files using for loop \n")
# write_file = open_file.write(" \nThis is append files using for loop \n")
# write_file = open_file.write(" \nThis is append files using for loop \n")
# write_file = open_file.write(" \nThis is append files using for loop \n")
# write_file = open_file.write(" \nThis is append files using for loop \n")
# write_file = open_file.write(" \nThis is append files using for loop \n")
# write_file = open_file.write(" \nThis is append files using for loop \n")
# write_file = open_file.write(" \nThis is append files using for loop \n")
# write_file = open_file.write(" \nThis is append files using for loop \n")
# write_file = open_file.write(" \nThis is append files using for loop \n")
# write_file = open_file.write(" \nThis is append files using for loop \n")
# write_file = open_file.write(" \nThis is append files using for loop \n")
# write_file = open_file.write(" \nThis is append files using for loop \n")
# write_file = open_file.write(" \nThis is append files using for loop \n")
# write_file = open_file.write(" \nThis is append files using for loop \n")
# write_file = open_file.write(" \nThis is append files using for loop \n")

# open_file.close()                                                                               # Close the file
# # count = 0
# open_file = open('sample.txt')
# for item in open_file:
#     # count += 1                                                                                  # Foe integer number wise data insert/append
#     # print(f" {item} {count}")
#     print(item)
# open_file.close()

# -----------------------------------------------------------------------------------------------------------------------------------------
# NOTE Rename a file

# Python  os modile offers some methods, that can be used to perform various file operations such as deleting & Renimaing file
import os
# # os.rename(src, dst, src_dir_fd=..., dst_dir_fd=...) 
# os.rename('SAMPLE.txt', 'sample.txt')

# ------------------------------------------------------------
# # **************************************************************** Open  Binary file ***************************************************
mypict = open('img.jpg','rb')
info = mypict.read()
# print(info)

print(mypict.name)      # What is File name 

print(mypict.closed)    # Is file closed or not(True/False)

print(mypict.mode)      # What is mode of file open

print(type(mypict))     # Type is <class '_io.Bufferreader'>

print(type(info))       # Type is <class 'bytes'>

print(mypict.tell())    # number of lines, that has been read

print(mypict.seek(0))   
print(mypict.seek(1))
print(mypict.seek(0,2))
mypict.close()
# # -----------------------------------------------------------------------------------------------------------------------------------------
# NOTE




# -----------------------------------------------------------------------------------------------------------------------------------------
# NOTE




# -----------------------------------------------------------------------------------------------------------------------------------------
# NOTE




# -----------------------------------------------------------------------------------------------------------------------------------------
# NOTE




# -----------------------------------------------------------------------------------------------------------------------------------------
# NOTE




# -----------------------------------------------------------------------------------------------------------------------------------------
# NOTE




# -----------------------------------------------------------------------------------------------------------------------------------------
# NOTE




# -----------------------------------------------------------------------------------------------------------------------------------------
# NOTE




# -----------------------------------------------------------------------------------------------------------------------------------------
# NOTE




# -----------------------------------------------------------------------------------------------------------------------------------------
# NOTE




# -----------------------------------------------------------------------------------------------------------------------------------------
# NOTE




# -----------------------------------------------------------------------------------------------------------------------------------------
# NOTE




# -----------------------------------------------------------------------------------------------------------------------------------------
# NOTE




# -----------------------------------------------------------------------------------------------------------------------------------------
