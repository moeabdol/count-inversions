import numpy as np

# method to count inversions in O(n(log(n)))
def merge_count_inversions(x):
    # base condition
    if len(x) == 1:
        inv = 0
        return x, inv
    else:
        length = len(x) / 2
        a, inva = merge_count_inversions(x[:length])
        b, invb = merge_count_inversions(x[length:])

    # merge, sort and count split inversions
    c = np.array([], dtype='int')
    inv = inva + invb
    while len(a) != 0 or len(b) != 0:
        if len(a) == 0:
            c = np.append(c, b)
            b = np.delete(b, xrange(len(b)))
        elif len(b) == 0:
            c = np.append(c, a)
            a = np.delete(a, xrange(len(a)))
        elif a[0] > b[0]:
            c = np.append(c, b[0])
            b = np.delete(b, 0)
            inv += len(a)
        else:
            c = np.append(c, a[0])
            a = np.delete(a, 0)

    return c, inv

x = np.genfromtxt('IntegerArray.txt', dtype='int')
x, inv = merge_count_inversions(x)
print 'Number of Inversions:', inv
