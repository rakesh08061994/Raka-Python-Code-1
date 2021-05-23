def mathAdd(*args):
    total = 0
    for i in args:
        total += i
    return f"Total is {total}"
    

def mathMul(*args):
    total = 1
    for i in args:
        total *= i
    return f" Total Multiplication is {total}"

def mathsub(a, b):
    return f"Result of subsraction is : {a-b}"

def greet(name):
    return f"Hello {name}, How are you ? "

if __name__ == '__main__':

    print(mathAdd(1,2,3,4,5,6656,6,7,8,9))

    print(mathMul(1,2,3,4,5,6,7,8,9,10))

    print(mathsub(84,62))

    print(greet("Rakesh"))


