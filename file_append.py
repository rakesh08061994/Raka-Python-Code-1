open_file = open("sample.txt","a")
write_file = open_file.write(" This data will append or add just after previous content of file ")
print(write_file)
open_file.close()

note = "File attributes that can provide a number of important information about that file."
print(f"\n\n{note} \n")
print("File name : ",open_file.name)
print("File mode : ",open_file.mode)
print("File closed or not : ",open_file.closed)