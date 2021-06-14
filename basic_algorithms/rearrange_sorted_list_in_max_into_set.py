def rearrange_sorted_list_in_max_into_set(lst):
    result = []

    for i in range(len(lst)//2):
        result.append((lst[i], lst[-i - 1]))

    if len(lst) % 2 == 1:
        result.append(lst[len(lst)//2])
    return result
