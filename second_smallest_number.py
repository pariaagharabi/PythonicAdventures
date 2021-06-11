def second_smallest_number(lst):
    smallest = second_smallest = float("inf")

    for i in range(len(lst)):
        if lst[i] < smallest:
            second_smallest = smallest
            smallest = lst[i]
        else:
            if lst[i] < second_smallest:
                second_smallest = lst[i]
    return second_smallest
