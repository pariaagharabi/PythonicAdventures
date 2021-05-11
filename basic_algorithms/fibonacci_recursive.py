def fib_number(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fib_number(num - 1) + fib_number(num - 2)
