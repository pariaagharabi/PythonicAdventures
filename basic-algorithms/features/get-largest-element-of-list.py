def get_largest_element_v1(list):
    max_num = list[0]

    for i in range(1, len(list)):
        if list[i] > max_num:
            max_num = list[i]
    return max_num


def get_largest_element_v2(list):
    max_num = list[0]

    for i in list:
        if max_num < i:
            max_num = i
    return max_num
