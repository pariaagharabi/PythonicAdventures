def remove_empty_string(lst):
    for item in lst:
        if item == "":
            lst.remove(item)
    return lst
