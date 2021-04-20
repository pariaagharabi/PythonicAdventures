def get_largest_element_v1(lst):
    max_num = lst[0]

    for i in range(1, len(lst)):
        if lst[i] > max_num:
            max_num = lst[i]
    return max_num


def get_largest_element_v2(lst):
    max_num = lst[0]

    for i in lst:
        if max_num < i:
            max_num = i
    return max_num
