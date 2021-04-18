def fact(num):
    if num < 0:
        raise ValueError("Number should be greater or equel zero!")

    if num == 0:
        return 1

    return num * fact(num-1)
