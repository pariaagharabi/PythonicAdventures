def binary_search(lst, key):
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
