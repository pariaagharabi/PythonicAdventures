# Find missing number in ordered list


def find_missinf_number(lst):
    first_element = lst[0]
    last_element = lst[-1]

    miss_nums = []

    for item in range(first_element, last_element + 1):
        if item is not lst:
            miss_nums.append(item)

    return miss_nums
