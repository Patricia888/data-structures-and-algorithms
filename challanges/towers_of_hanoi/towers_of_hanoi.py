def towers_of_hanoi(n):
    '''towers of hanoi. moves disks form pole a to the target pole and returns the steps needed to get there.'''
    a = []
    b = []
    c = []
    for i in reversed(range(1, n + 1)):
        # do recursive stuff
        a.append(i)
    count = recur(n, a, c, b)
    return (count, c, b, a)


def recur(n, a, c, b):
    """recursive function that keeps getting called until all disks are at the target destination"""
    count = 0
    if n >= 1:
        first = recur(n - 1, a, b, c)
        c.append(a.pop())
        count += 1
        second = recur(n - 1, b, c, a)
        count += first + second
    return count
