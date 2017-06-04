"""
Letter                           Value
a, e, i, o, u, l, n, r, s, t       1
d, g                               2
b, c, m, p                         3
f, h, v, w, y                      4
k                                  5
j, x                               8
q, z                               10
"""
POINTS = {
    'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1,
    'l': 1, 'n': 1, 'r': 1, 's': 1, 't': 1,
    'd': 2, 'g': 2,
    'b': 3, 'c': 3, 'm': 3, 'p': 3,
    'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4,
    'k': 5,
    'j': 8, 'x': 8,
    'q': 10, 'z': 10
}


def score(word):
    return sum([POINTS[c.lower()] for c in word])
