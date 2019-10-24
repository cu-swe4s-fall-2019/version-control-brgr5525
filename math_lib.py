def div(a, b):
    '''
    Takes two integers as input and returns the division of them
        a : numerator
        b : denominator

    Will print a message and return None if b is 0
    '''
    if b == 0:
        print('Cannot divide by Zero')
        return None
    else:
        return a/b


def add(a, b):
    '''
    Takes two integers as input and return the sum of them
    '''
    return a + b
