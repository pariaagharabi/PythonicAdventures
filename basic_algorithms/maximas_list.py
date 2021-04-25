# Get all the maxima’s in a list. (A value is a maximum if the value before and
# after its index are smaller than it is or does not exist.)


def maxima(lst):
    maxima_list = []

    if lst[0] > lst[1]:
        maxima_list.append(lst[0])

    for i in range(1, len(lst)-1):
        if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
            maxima_list.append(lst[i])

    if lst[-1] > lst[-2]:
        maxima_list.append(lst[-1])

    return maxima_list
