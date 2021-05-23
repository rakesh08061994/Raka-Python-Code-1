num = int(input("Enter Number : "))

count = num
list1 = []
for i in range(1,num+1,2):
    list1.append(i)
list1.sort(reverse=True)

for j in list1:
    print(f"{count * ' '}{j * '*'}")
    count += 1


