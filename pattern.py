num = int(input("Enter Number : "))

list1 = []
for i in range(1,num+1):
    list1.append(i)
list1.sort(reverse=True)
for i in list1:
    print(i * "*")

