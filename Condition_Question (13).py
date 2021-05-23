# Write a Python program to find those numbers which are divisible by 7 
# and multiple of 5, between 1500 and 2700 (both included).
list1 = []
for Item in range(1500,2701):
    if (Item % 7 == 0) and (Item % 5 == 0):
        list1.append(str(Item))
print (','.join(list1))


