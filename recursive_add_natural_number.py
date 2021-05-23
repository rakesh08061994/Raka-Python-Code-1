def addRecursive(n):
    '''Addition of n natural number using recursion'''
    # First we solve base case
    if n == 1:
        return 1
    # Now we solve Recursive case
    else:
        return n + addRecursive(n-1)



print(addRecursive(100))

