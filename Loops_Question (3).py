# for in Loop: 
# For loops are used for sequential traversal. For example: traversing a list or string or array etc.
# The for loop takes a collection of items and execute a block of code once for each time in the collection.  
'''
Syntax:

for iterator_var in sequence:
    statements(s)
'''

n = 4                   # Value given of n = 4 (We can use here list, tuple, string)
for item in range(0,4): # From (indexing 0) to (indexing n-1), # range(4) will work same output. 
    print(item)