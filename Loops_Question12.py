# Range () function in loops.
# The range function in python is used to generate a sequence of numbers.
# we can also specify the start, stop, and step size in range parameters
# NOTE >
range_syntax = ''' 
                              syntax :    range(START, STOP, STEP_SIZE):
                                
'''
Range_Diagram = '''
                 <----------------- Negative Side          Positive side ----------------> 
so on.    -10  -9  -8  -7  -6  -5  -4  -3  -2  -1    0     1  2  3  4  5  6  7  8  9  10         .so on
          <__  __  __  __  __  __  __  __  __  __    __    __ __ __ __ __ __ __ __ __ __>  
'''
# print(range_syntax)
# print(Range_Diagram)
# We can use range with loops to enhance there productivity, reliability, and performance
# **********************************************************************************************

# for Item in range(10):              # Print 0 to 9   (a, b-1)
#     print(Item)

# for Item in range(1,10):              # Print 1 to 9   (a, b-1)
#     print(Item) 


# for Item in  range(1,11):               # print 1 to 10 (a, b-1)
#     print(Item)

# for Item in range(1,100,2):             # print 1 to 99 with 2 step size (a, b-1, StepSize)
#     print(Item) 

# for Item in range(-1,-10,-1):             # print Negative side of range
#     print(Item)

for Item in range(1,11,-2):
    print(Item)