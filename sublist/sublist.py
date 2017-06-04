SUBLIST = -1
SUPERLIST = 9001
EQUAL = 0
UNEQUAL = 1


def check_lists(a, b):
    if a == b:
        return EQUAL

    if sublist(a, b):
        return SUBLIST

    if superlist(a, b):
        return SUPERLIST

    return UNEQUAL


def sublist(a, b):
    if len(a) > len(b):
        return False
    lena = len(a)
    lenb = len(b)
    return any(b[n:n+lena] == a for n in range(lenb))


def superlist(a, b):
    return sublist(b, a)
