list1 = []

num1 = int(input("Enter num 1-->  "))
list1.append(num1)
num2 = int(input("Enter num 2-->  "))
list1.append(num2)
num3 = int(input("Enter num 3-->  "))
list1.append(num3)
num4 = int(input("Enter num 4-->  "))
list1.append(num4)

# print(list1)

max_value = max(list1)
print(f"Gratest Number among {num1}, {num2}, {num3},  is {max_value}")

