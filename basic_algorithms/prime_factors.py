def prime_factors(num):
    factors = list()

    for i in range(2, num):
        if num % i == 0:
            factors.append(i)
            num /= i
        else:
            i += 1

    return factors
