def recursiveFactorial(n):
    '''return recursive factorial using recursion'''
    # First we will solve base case
    if n == 1:
        return 1
    
    # Now Recursive case        n! = n * (n-1)!
    else:
        return n * recursiveFactorial(n-1)



print(recursiveFactorial(5))



