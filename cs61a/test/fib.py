def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

def count(f):
    def counted(n):
        counted.callcount += 1
        return f(n)
    counted.callcount = 0
    return counted

def memo(f):
    mem = {}


