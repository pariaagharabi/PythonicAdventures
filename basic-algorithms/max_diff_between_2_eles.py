# Maximum difference between two elements in an array


def maximum_difference_two_elements(lst, lst_size):
    max_diff_two_eles = lst[1] - lst[0]

    for element in range(0, lst_size):
        for item in range(element+1, lst_size):
            if(lst[item] - lst[element] > max_diff_two_eles):
                max_diff_two_eles = lst[item] - lst[element]

    return max_diff_two_eles
