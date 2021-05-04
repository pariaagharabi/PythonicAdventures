# check if it's prime number


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return("Not prime!")

    else:
        return("Prime")


print(is_prime(-6))
