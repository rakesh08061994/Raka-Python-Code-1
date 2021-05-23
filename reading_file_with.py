open_file = open("information.txt","r+")

sequence = "This is text9\n This is text10"
open_file.seek(0,2)
write_file = open_file.writelines(sequence)
print(write_file)

