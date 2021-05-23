def recursiveTable(n,i=1):
    # Base Case
    if i > 10:
        return
    
    else:
        print(f"{n} X {i} = {n*i}")

    return recursiveTable(n, i+1)

recursiveTable(10) 

