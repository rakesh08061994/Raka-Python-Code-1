# The File Object Attributes
# A file object from an opened file can provide a number of important information about that file.

sports_file = open("Player.txt","r")

read_file = sports_file.read()

print(read_file)

sports_file.close()

# Use of file attributes

print("File Name is : ", sports_file.name)
print("File Open Mode : ", sports_file.mode)
print("File Closed or Not : ",sports_file.closed)
