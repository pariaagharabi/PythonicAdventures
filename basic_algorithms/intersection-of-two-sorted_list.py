# ================First Solution==================


def intersect_sorted_list_v1(lst1, lst2):
    lst1 = sorted(lst1)
    lst2 = sorted(lst2)

    return (set(lst1).intersection(lst2))

# ================Second Solution==================


def intersect_sorted_list_v2(lst1, lst2):
    result = []

    for item in lst1:
        if item in lst2:
            result.append(item)

    return set(result)


# ================Third Solution==================


def intersect_sorted_list_v3(lst1, lst2):
    result = set()

    for item in lst1:
        if item in lst2:
            if(item not in result):
                result.add(item)
                yield item
