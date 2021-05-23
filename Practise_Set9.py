# #Question 1 > read the text from a given file = "poems.txt"
# #             findout whether it contains word  = "twinkle"

# # First open file "poems.txt" in write mode("w") using with() Built-In function (make a file if file is not available)
# #  after write we will switch mode from write to read mode !
# count = 0
# with open("poems.txt","r") as open_file:
#     # write_file = open_file.write("twinkle twinkle little star, \n")
#     # write_file = open_file.write(" how are wonder what you are ?, \n")
#     # write_file = open_file.write("up above the world so high, \n")
#     # write_file = open_file.write("like a diamond in the sky, \n")
#     # write_file = open_file.write("twinkle twinkle little star \n")
#     # print(write_file)

#     for word in iter(open_file):
#         count += 1
#         if "twinkle" in word:
#             print(f"{count} > {word}")



# ----------------------------------------------------------------------------------------------------------------------------
# Create a game function, that return score as integer

# def game():
#     """Return score as integer"""
#     return 10

# num = game()


# with open("Hi-Score.txt") as open_file:
#     read_file = open_file.read()

#     if read_file == "":
#         with open("Hi-Score.txt","w") as open_file:
#             write_file = open_file.write(str(num))

#     elif int(read_file) >= num:
#         print("Low Score yet !")
#     else:
#         with open("Hi-Score.txt","w") as open_file:
#             write_file = open_file.write(str(num))
#             print(f"Your High Score is :- {num}")


# # --------------------------------------------------------------------------------------------------------------------------------------4
# for num in range(1,21):
#     # print("\n This is Table of %d"%(num))
#     file = f"Table_File{num}.txt"

#     for i in range(1,11):
#         table = ("%d X %d = %d \n"%(num,i,num*i))
#         # print(table)
#         # print(table)
#         with open(file,"a") as open_file:
#             write_file = open_file.write(table)

# ------------------------------------------------------------------------------------------------------------------------------------------
# with open("Censored.txt") as open_file:
#     read_file = open_file.read()
#     if "Donkey" in read_file:
#         replace = read_file.replace("Donkey","@#&%##$@#")
#         with open("Censored.txt","w") as open_file:
#             write_file = open_file.write(replace)

# -----------------------------------------------------------------------------------------------------------------------------------------
# Censored_List = ["Life","Family","Love","Donkey","Life","Family","Love","Donkey","Life","Family","Love","Donkey",]
# change_str = str(Censored_List)
# if "Donkey" in change_str:
#     result = change_str.replace("Donkey","@#$#@$#@#$")
#     Censored_List = list[result]
#     print(Censored_List)

# -------------------------------------------------------------------------------------------------------------------------------------------
# counter = 1
# with open("log.txt") as open_file:
    
#     for line in open_file:
#         counter += 1
#         if "Python" in line:
#             print(f"{counter} > {line}")
#         # else:
#         #     print("No Python is there !")
# ------------------------------------------------------------------------------------------------------------

# with open("log.txt") as open_file:
#     read_file = open_file.read()
#     if "Python" in read_file:
#         print("Yes")
#     else:
#         print("No")

#         # --------------------------------------------------------------------------------------------------------
# # Copy File to read
# with open("Text.txt") as open_file:
#     read_file = open_file.read()

# # Paste file to write on another file
# with open("Text_copy.txt","w") as open_file:
#     write_file = open_file.write(read_file)
# # ----------------------------------------------------------------------------------------------------------------------
# with open("Text.txt") as open_file:
#     read_file = open_file.read()

# with open("Text_copy.txt") as open_file:
#     read_file1 = open_file.read()

# if read_file == read_file1:
#     print("Same")
# else:
#     print("Different")
# ---------------------------------------------------------------------------------------------------------------------
# Wipe Out thee file content

# open_file = open("Text.txt","w")
# read_file = open_file.write("")
# print(read_file)

# ----------------------------------

# open_file = open("Text.txt", "w").close()

# ---------------------------------------------
# import os
# with open("BeforeRename.txt") as open_file:
#     read_file = open_file.read()
# with open("AfterRename.txt","w") as open_file:
#     read_file = open_file.write(read_file)
    
# --------------------------------------------------
# with open("BeforeRename.txt") as open_file:
# read_file = os.rename("BeforeRename.txt","ThisisRenamed.txt")


