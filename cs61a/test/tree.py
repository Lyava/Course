def tree(label, branches = []):
    return [label] +  list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False

    return True


def fib_tree(n):
    if n <= 1:
        return [n]
    left, right =  fib_tree(n - 2), fib_tree(n - 1)
    return tree(label(left) + label(right), [left, right])
