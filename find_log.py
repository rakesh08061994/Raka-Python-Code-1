counter = 1
with open("log.txt") as open_file:
    for line in open_file:
        counter += 1
        if "python" in line.lower():
            
            print(f"{counter} > {line}")
            


