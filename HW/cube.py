def get_digit(a):
    '''
    Function that returns the first digit of a 2 digit integer
    '''
    global n
    n = a//10
    return n

def cube(n):
    '''
    Function that returns the cube of a number
    '''
    cube = n**3
    return cube

print(get_digit(28))
print(cube(n))