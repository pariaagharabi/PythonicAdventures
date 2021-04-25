def binary_search(lst, key):
    if lst is None or key is None:
        return -1

    left = 0
    right = len(lst) - 1

    while right >= left:
        mid = (left + right) // 2

        if (lst[mid] == key):
            return mid

        if (key > lst[mid]):
            left = mid + 1
        else:
            right = mid - 1

    return -1
