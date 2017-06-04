def prime_factors(n):
    factors = []
    candidate_factor = 2
    while n > 1:
        while n % candidate_factor == 0:
            factors.append(candidate_factor)
            n /= candidate_factor
        candidate_factor += 1

    if n > 1:
        factors.append(n)

    return factors
