def sieve(upto):
    if upto < 2:
        return []

    primes = [2]
    skip = set(range(2, upto+1, 2))
    n = 3   # starting from 3 allows me to inc n by 2
    while n <= upto:
        if n not in skip:
            primes.append(n)
            skip.update(range(n, upto+1, n))
        n += 2

    return primes
