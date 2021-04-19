def binary_search_recursive(lst, key, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if lst[mid] == key:
        return mid
    if key > lst[mid]:
        return binary_search_recursive(lst, key, mid + 1, right)
    else:
        return binary_search_recursive(lst, key, left, mid - 1)


def search(lst, key):
    return binary_search_recursive(lst, key, 0, len(lst) - 1)
