from functools import reduce
from itertools import starmap
from operator import mul


def largest_product(txt, n):
    if len(txt) < n or n < 0:
        raise ValueError("Input length is less than n")

    if any(not c.isdigit() for c in txt):
        raise ValueError("Input must be numeric")

    if n == 0:
        return 1

    products = [reduce(mul, grp) for grp in slices(txt, n)]
    largest = reduce(max, products)

    return largest


# from series.py
def slices(data, n):
    if n == 0 or len(data) < n:
        raise ValueError('Illegal length requested')

    def partition(i): return data[i:(i+n)]

    def str_to_ints(x): return [int(y) for y in x]

    data_range = range(0, (len(data) - n) + 1)

    return [str_to_ints(partition(i)) for i in data_range]
