def largest_prime_factor(num):
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
    return num
