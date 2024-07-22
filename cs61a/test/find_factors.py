def find_factors(n):    
    """ 
    >>> find_factors(12)
    2
    2
    3
    >>> find_factors(48)
    2
    2
    2
    2
    3
    """
    assert n > 0
    print('DEBUG:n is', n)
    k = 2
    while n > 1:
        k = samllest_factor(n, k)
        print(k)
        n = n // k


def samllest_factor(n, k):
    while n % k != 0:
        k += 1
    return k






