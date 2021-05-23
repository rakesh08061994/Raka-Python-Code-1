#  Using continue in a loop

# Rather then breaking out of a loop entirely without executing the rest of its code. Continue statement is just opposite to break.
# where break statement break lower entirely code properly and terminate the program imidiatly. In continue It will stop only desired
#  condition execution, Otherwise code will perform normaly without interuption 
# NOTE: we can use break, continue,  and pass statement in everywhere of python proramming loop and conditions.
a = [10,20,30,50,1,3,5,0,4,6,8,6,2,55,0,9]
for i in a:
    if(i % 2 == 0):
        print(f"{i}, is an even number !")
    else:
        print(f"{i}, is an odd number")
print("Done !")   