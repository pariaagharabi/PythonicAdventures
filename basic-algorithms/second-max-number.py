def second_max_number(lst):
    largest = max(lst[0], lst[1])
    second_largest = min(lst[0], lst[1])

    for num in range(2, len(lst)):
        if lst[num] > largest:
            second_largest = largest
            largest = lst[num]
        else:
            if lst[num] > second_largest:
                second_largest = lst[num]

    return second_largest
