import os

location = os.listdir("C:\Program Files")
counter = 0
for i in location:
    counter += 1
    print(f"{counter}.  {i}")
    # print(f"# {i}")


