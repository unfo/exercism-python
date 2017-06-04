def sum_of_multiples(upto, multis):
    _multis = []
    for n in multis:
        _multis += [multi for multi in range(n, upto, n)]

    return sum(set(_multis))
