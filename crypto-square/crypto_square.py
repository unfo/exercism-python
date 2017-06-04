from math import ceil, floor, sqrt


def encode(plaintext):
    if len(plaintext) == 0:
        return ''

    text = [c.lower() for c in plaintext if c.isalnum()]
    cols = ceil(sqrt(len(text)))
    rows = partition(text, cols)

    message = []
    for col in range(0, cols):
        for row in rows:
            if len(row) > col:
                message.append(row[col])
        message.append(' ')
    return "".join(message).rstrip()


def partition(data, n):
    if n < 1:
        raise ValueError('Illegal length requested')

    def partition(i): return data[i:(i+n)]
    data_range = range(0, len(data), n)

    return [partition(i) for i in data_range]
