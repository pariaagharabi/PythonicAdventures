# The method finds the sum of every number in an int number. Example: input= 1984, output should be 32 (1+9+8+4).


def sum_digits(number):
    sum_num = 0
    while number > 0:
        reminder = number % 10
        number //= 10
        sum_num += reminder
    return sum_num
