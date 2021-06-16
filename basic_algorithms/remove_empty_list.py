def remove_empty_list(lst):
    for item in lst:
        if item == []:
            lst.remove(item)
    return lst
