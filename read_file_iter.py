open_file = open("poems.txt")
read_file = open_file.readline()
print(read_file)

for i in iter(open_file):
    print(i,end="")

