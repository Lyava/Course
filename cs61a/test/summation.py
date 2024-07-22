from operator import mul

def summation(n, term):
    total, k = 0, 1
    while k < n:
        total, k = total + term(k), k + 1
    
    return total

def iden_term(k):
    '''
    >>> 1
    >>> 1
    '''
    return k

def cube_term(k):
    '''
    >>> 2
    >>> 8
    '''
    return pow(k, 3)

def pi_term(k):
    return 8/mul(4 * k - 3, 4 * k - 1)

