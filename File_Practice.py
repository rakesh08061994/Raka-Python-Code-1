# NOTE : 
# CodeWithHarry

#NOTE 'rb' will open file for read in binary mode
#NOTE 'rt' will open file for read in text mode



# open_file = open('sample.txt','r')                            # open for read
# open_file = open('sample.txt')                            c   # bydefault open in read mode, if need to open file just for read
# open_file = open('sample.txt','rt')                           #  text 't' is bydefault add with read 'r'
# read_file = open_file.read()                                  # Which file you want to read(if lots of file are open)
# print(read_file)
### In python readline() built in function is one more function to read files but one line with newline space(Because print use ByDefault /n at the end) at a time
###  If you want to read next line, you need to write readline() one more time, and also print variables one more time
# read_file = open_file.readline()                              # readline read first line of files content
# print(read_file,end='')                                                                                 # to remove new line use ,end=''
# read_file = open_file.readline()                              # readline read second line of files content
# print(read_file,end='')
# read_file = open_file.readline()                              # readline read third line of files content
# print(read_file,end='')
# read_file = open_file.readline()                              # readline read fourth line of files content
# print(read_file,end='')


# open_file.close()                                             # Close() is must after use the file

# -------------------------------------------------------------------------------------------------
# NOTE write or append file file = open in write'w' or write text'wt'or 'a' or 'at' mode an after use file.write("Write/append")

# open_file = open('sample.txt','w')                            # Write mode (if file not exist, it make with same name)
# # open_file = open('sample.txt','wt')                         # Write Text mode (Text 't' is bydefalt add) overwrite/rewrite/delete previous data in nature
# # open_file = open('sample.txt','a')                          # Data will append after previous data in file
# # open_file = open('sample.txt','at')                         # 't' Is bydefault with append
# write_file = open_file.write("Type your str here ")           # Which file you want to write
# print(write_file)                                             # Show write content characters number
# open_file.close()                                             # Close is must important after use it

# --------------------------------------------------------------------------------------------------
### NOTE Append file = open in 'a' or 'at' mode not in 'w' or 'wt' mode (rewrite or overwrite in nature) some data is previously required to use append
ui# open_file = open('sample.txt','a')
# # open_file = open('sample.txt','at')
# append_file = open_file.write("This is previous str content file")  # During append data mode should be ('a'append or 'at'append text mode),  not ('w'write mode) 
# print(append_file)
# open_file.close() 
# # ---------------------------------------------------------------------------------------------------

#NOTE append will work only when, when some data are available in file previously(This is append not write)
# And keep mode 'a' during append data, not write'w' mode (write will rewrite/overwrite/delete previous data content of file)

# open_file = open('sample.txt','at')
# append_file = open_file.write("\nappend data in sample.txt file, and this is in 'a' append mode ")
# print(append_file)
# open_file.close()

# --------------------------------------------------------------------------------------------------------------

# NOTE 'with' statement in python i/o files, we dont need to write file.close() . it automatically close the file at same time.
#  But all processes will remain same 

#SYNTAX >      with open('FileName.txt', 'mode') as variable:
#                   New_Variable = variable.read()
#                   print(New_Variable)    

# with open('sample.txt','r') as open_file:
#     read_file = open_file.read()
#     print(read_file)
#     # No need to write:  open_file.close() 


# ----------------------------------------------------------------------------------------------------------------------------------
# Uncompleted 
# NOTE + are used to join two modes at a time in single formula

# open_file = open('sample.txt', 'r+')        # Read + Write (Remember 't'Text mode is bydefault)
# # read_file = open_file.read()                # with open read
# read_file = open_file.write("Write data") # with open write
# print(read_file)

# ------------------------------------------------------------------------------------------------------------------------------------

# with open("sample.txt") as open_file:
#     read_file = open_file.readline()
#     counter = 1
#     while read_file:

#         # python in read_file:
#         read_file = open_file.readline()
#         counter += 1
#         if "Python" in read_file:
#             print(f"Line Number {counter} > {read_file}")   

# -----------------------  #--------------------------------
# counter = 0
# with open("sample.txt") as open_file:
#     # read_file = open_file.readline()
#     for line in open_file:
#         counter += 1
#         if "Python" in line:
#             print(f"{counter} {line}")


# ---------------------------------------------------------------------------------------------------------------------------------------

# counter = 0
# with open("sample.txt") as open_file:
    
#     for line in iter(open_file):
#         counter += 1
#         if "Rakesh" in line:
#             print(f"{counter} >  {line}")

# --------------------------------------------------------------------------------------------------------------------------------------

