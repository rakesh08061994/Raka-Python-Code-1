def recursiveTable(N, i=1):
    # Base Case

    if i > 10:
        return
    
    else:
        print(f"{N} X {i} = {N * i}")
    
    # Recursive Case
    return recursiveTable(N, i+1)


# Function Call with positional argument 10
recursiveTable(10)