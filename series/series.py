def slices(data, n):
    if n == 0 or len(data) < n:
        raise ValueError('Illegal length requested')

    partition   = lambda i: data[i:(i+n)]
    str_to_ints = lambda x: [int(y) for y in x]
    data_range  = range(0, (len(data) - n) + 1)

    return [str_to_ints(partition(i)) for i in data_range]

