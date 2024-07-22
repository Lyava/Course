def search(f):
    "return when f(x) == true"
    x = 0
    while not f(x):
        x += 1
    return x

def is_three(x):
    return x == 3

def inverse(f):
    return lambda y: search(lambda x: f(x) == y)


square = lambda x: x * x
