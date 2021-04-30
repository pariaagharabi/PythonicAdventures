# The method to compute Sum(N) = 1+2+3+…+N.


def sum_number(number):

    if number < 0:
        raise ValueError(
            "Invalid number, the number should be a positive number!")

    if number > 1:
        number = number * (number + 1) // 2

    return number
