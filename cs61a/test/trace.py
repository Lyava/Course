def trace(f):
    def traced(n):
        t = f(n)
        print('f:', n,'->', t)
        return t
    return traced

