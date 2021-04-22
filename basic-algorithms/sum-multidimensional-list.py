def sum_multidimensional_list_v1(lst):
    sum_nums = 0

    for row in range(len(lst)):
        for col in range(len(lst[row])):
            sum_nums += lst[row][col]

    return sum_nums


def sum_multidimensional_list_v2(lst):
    sum_nums = 0

    for row in lst:
        for col in row:
            sum_nums += col

    return sum_nums
