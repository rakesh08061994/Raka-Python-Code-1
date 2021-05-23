#********************* Tuple *******************************
# we can create all data type elements in list

a = ["Ram", 786, True, 85.9,]; #Semicolun is not necessary
print(a)

'''we can access list same as string using a[2], Because
list elements/objects. positive indexing start from zero to aboue 
from left to right side and negative indexing start -1 to above from right to left ''' 

# print(a[3])         #Accessing the index element
# print(a[-4:0])       #Accessing index from to above three place 
# print(a[0::2])      #slicing is also working
# print(a[-4:-1])     #Negative value also callable
# print(a[-4:])      #Negative from right to left
# print(a[-4:3])      # only above three place 

# a[2] = True        # Update value in List for index a[2]
# print(a)        # True value replace by new update value 5 on index a[2]
# print(type(a))  #check data type of variable a
# print(type(a[2]))   #Check DataType of values inside List
# del a[2]           #Delete Element inside List using del()
# print(a)
# a.insert(2,100)
# print(a)
# a.insert(2,101)
# print(a)